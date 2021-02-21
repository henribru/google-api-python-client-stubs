import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class RemoteBuildExecutionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ActionResultsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            instanceName: str,
            hash: str,
            sizeBytes: str,
            inlineOutputFiles: typing.Union[str, typing.List[str]] = ...,
            inlineStderr: bool = ...,
            inlineStdout: bool = ...,
            **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2ActionResultHttpRequest: ...
        def update(
            self,
            *,
            instanceName: str,
            hash: str,
            sizeBytes: str,
            body: BuildBazelRemoteExecutionV2ActionResult = ...,
            resultsCachePolicy_priority: int = ...,
            **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2ActionResultHttpRequest: ...
    @typing.type_check_only
    class ActionsResource(googleapiclient.discovery.Resource):
        def execute(
            self,
            *,
            instanceName: str,
            body: BuildBazelRemoteExecutionV2ExecuteRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
    @typing.type_check_only
    class BlobsResource(googleapiclient.discovery.Resource):
        def batchRead(
            self,
            *,
            instanceName: str,
            body: BuildBazelRemoteExecutionV2BatchReadBlobsRequest = ...,
            **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2BatchReadBlobsResponseHttpRequest: ...
        def batchUpdate(
            self,
            *,
            instanceName: str,
            body: BuildBazelRemoteExecutionV2BatchUpdateBlobsRequest = ...,
            **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2BatchUpdateBlobsResponseHttpRequest: ...
        def findMissing(
            self,
            *,
            instanceName: str,
            body: BuildBazelRemoteExecutionV2FindMissingBlobsRequest = ...,
            **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2FindMissingBlobsResponseHttpRequest: ...
        def getTree(
            self,
            *,
            instanceName: str,
            hash: str,
            sizeBytes: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2GetTreeResponseHttpRequest: ...
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def waitExecution(
            self,
            *,
            name: str,
            body: BuildBazelRemoteExecutionV2WaitExecutionRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
    @typing.type_check_only
    class V2Resource(googleapiclient.discovery.Resource):
        def getCapabilities(
            self, *, instanceName: str, **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2ServerCapabilitiesHttpRequest: ...
    def actionResults(self) -> ActionResultsResource: ...
    def actions(self) -> ActionsResource: ...
    def blobs(self) -> BlobsResource: ...
    def operations(self) -> OperationsResource: ...
    def v2(self) -> V2Resource: ...

@typing.type_check_only
class BuildBazelRemoteExecutionV2ActionResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BuildBazelRemoteExecutionV2ActionResult: ...

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchReadBlobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BuildBazelRemoteExecutionV2BatchReadBlobsResponse: ...

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchUpdateBlobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BuildBazelRemoteExecutionV2BatchUpdateBlobsResponse: ...

@typing.type_check_only
class BuildBazelRemoteExecutionV2FindMissingBlobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BuildBazelRemoteExecutionV2FindMissingBlobsResponse: ...

@typing.type_check_only
class BuildBazelRemoteExecutionV2GetTreeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BuildBazelRemoteExecutionV2GetTreeResponse: ...

@typing.type_check_only
class BuildBazelRemoteExecutionV2ServerCapabilitiesHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BuildBazelRemoteExecutionV2ServerCapabilities: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...
