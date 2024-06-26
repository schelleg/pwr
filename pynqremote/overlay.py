from .file_transfer import FileClient
from pathlib import Path
import struct
import numpy as np
from .client import Client
import os

PORT = "50051"

def parse_bit_header(bit_data):
    """The method to parse the header of a bitstream.

    The returned dictionary has the following keys:
    "design": str, the Vivado project name that generated the bitstream;
    "version": str, the Vivado tool version that generated the bitstream;
    "part": str, the Xilinx part name that the bitstream targets;
    "date": str, the date the bitstream was compiled on;
    "time": str, the time the bitstream finished compilation;
    "length": int, total length of the bitstream (in bytes);
    "data": binary, binary data in .bit file format

    Returns
    -------
    Dict
        A dictionary containing the header information.

    Note
    ----
    Implemented based on: https://blog.aeste.my/?p=2892

    """
    finished = False
    offset = 0
    contents = bit_data
    bit_dict = {}

    # Strip the (2+n)-byte first field (2-bit length, n-bit data)
    length = struct.unpack(">h", contents[offset : offset + 2])[0]
    offset += 2 + length

    # Strip a two-byte unknown field (usually 1)
    offset += 2

    # Strip the remaining headers. 0x65 signals the bit data field
    while not finished:
        desc = contents[offset]
        offset += 1

        if desc != 0x65:
            length = struct.unpack(">h", contents[offset : offset + 2])[0]
            offset += 2
            fmt = ">{}s".format(length)
            data = struct.unpack(fmt, contents[offset : offset + length])[0]
            data = data.decode("ascii")[:-1]
            offset += length

        if desc == 0x61:
            s = data.split(";")
            bit_dict["design"] = s[0]
            bit_dict["version"] = s[-1]
        elif desc == 0x62:
            bit_dict["part"] = data
        elif desc == 0x63:
            bit_dict["date"] = data
        elif desc == 0x64:
            bit_dict["time"] = data
        elif desc == 0x65:
            finished = True
            length = struct.unpack(">i", contents[offset : offset + 4])[0]
            offset += 4
            # Expected length values can be verified in the chip TRM
            bit_dict["length"] = str(length)
            if length + offset != len(contents):
                raise RuntimeError("Invalid length found")
            bit_dict["data"] = contents[offset : offset + length]
        else:
            raise RuntimeError("Unknown field: {}".format(hex(desc)))
    return bit_dict

def bit2bin(bit_data):
    """Convert an in-memory .bit file to .bin data for fpga_manager"""
    bit_dict = parse_bit_header(bit_data)
    bit_buffer = np.frombuffer(bit_dict["data"], "i4")
    bin_buffer = bit_buffer.byteswap()
    return bytes(bin_buffer)

def make_bin_file(bitfile):
    bitfile_path = Path(bitfile)
    bin_data = bit2bin(bitfile_path.read_bytes())
    binfile_name = Path(bitfile).stem + ".bin"
    bin_path = Path('./') / binfile_name
    bin_path.write_bytes(bin_data)
    return binfile_name

class Overlay:
    def __init__(self, bitstream, address, download=True) -> None:
       #self.bitstream = os.path.abspath(bitstream)
       self.bitstream = bitstream
       self.channel = Client(address, PORT).channel
       if download:
           self.upload()

    def upload(self):
        bin_path = make_bin_file(self.bitstream)
        file_client = FileClient(self.channel)
        file_client.upload(bin_path)
       
    def MMIO():
        pass