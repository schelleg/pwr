# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import mmio_pb2 as mmio__pb2


class MMIOStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.write = channel.unary_unary(
                '/mmio.MMIO/write',
                request_serializer=mmio__pb2.WriteRequest.SerializeToString,
                response_deserializer=mmio__pb2.WriteReply.FromString,
                )
        self.read = channel.unary_unary(
                '/mmio.MMIO/read',
                request_serializer=mmio__pb2.ReadRequest.SerializeToString,
                response_deserializer=mmio__pb2.ReadReply.FromString,
                )


class MMIOServicer(object):
    """Missing associated documentation comment in .proto file."""

    def write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MMIOServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'write': grpc.unary_unary_rpc_method_handler(
                    servicer.write,
                    request_deserializer=mmio__pb2.WriteRequest.FromString,
                    response_serializer=mmio__pb2.WriteReply.SerializeToString,
            ),
            'read': grpc.unary_unary_rpc_method_handler(
                    servicer.read,
                    request_deserializer=mmio__pb2.ReadRequest.FromString,
                    response_serializer=mmio__pb2.ReadReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mmio.MMIO', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MMIO(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mmio.MMIO/write',
            mmio__pb2.WriteRequest.SerializeToString,
            mmio__pb2.WriteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mmio.MMIO/read',
            mmio__pb2.ReadRequest.SerializeToString,
            mmio__pb2.ReadReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
