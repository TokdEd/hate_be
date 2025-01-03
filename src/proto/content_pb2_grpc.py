# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import content_pb2 as content__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in content_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ContentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterUser = channel.unary_unary(
                '/content.ContentService/RegisterUser',
                request_serializer=content__pb2.RegisterRequest.SerializeToString,
                response_deserializer=content__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.CreateSubmission = channel.unary_unary(
                '/content.ContentService/CreateSubmission',
                request_serializer=content__pb2.SubmissionRequest.SerializeToString,
                response_deserializer=content__pb2.Submission.FromString,
                _registered_method=True)
        self.ReviewSubmission = channel.unary_unary(
                '/content.ContentService/ReviewSubmission',
                request_serializer=content__pb2.ReviewRequest.SerializeToString,
                response_deserializer=content__pb2.Submission.FromString,
                _registered_method=True)


class ContentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSubmission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReviewSubmission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=content__pb2.RegisterRequest.FromString,
                    response_serializer=content__pb2.RegisterResponse.SerializeToString,
            ),
            'CreateSubmission': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSubmission,
                    request_deserializer=content__pb2.SubmissionRequest.FromString,
                    response_serializer=content__pb2.Submission.SerializeToString,
            ),
            'ReviewSubmission': grpc.unary_unary_rpc_method_handler(
                    servicer.ReviewSubmission,
                    request_deserializer=content__pb2.ReviewRequest.FromString,
                    response_serializer=content__pb2.Submission.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'content.ContentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('content.ContentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ContentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/content.ContentService/RegisterUser',
            content__pb2.RegisterRequest.SerializeToString,
            content__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateSubmission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/content.ContentService/CreateSubmission',
            content__pb2.SubmissionRequest.SerializeToString,
            content__pb2.Submission.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReviewSubmission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/content.ContentService/ReviewSubmission',
            content__pb2.ReviewRequest.SerializeToString,
            content__pb2.Submission.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
