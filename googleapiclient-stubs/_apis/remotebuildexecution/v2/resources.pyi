import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class RemoteBuildExecutionResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def waitExecution(
            self,
            *,
            name: str,
            body: BuildBazelRemoteExecutionV2WaitExecutionRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
    class ActionsResource(googleapiclient.discovery.Resource):
        def execute(
            self,
            *,
            instanceName: str,
            body: BuildBazelRemoteExecutionV2ExecuteRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
    class ActionResultsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            instanceName: str,
            hash: str,
            sizeBytes: str,
            inlineStdout: bool = ...,
            inlineStderr: bool = ...,
            inlineOutputFiles: typing.Union[str, typing.List[str]] = ...,
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
    class BlobsResource(googleapiclient.discovery.Resource):
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
        def batchRead(
            self,
            *,
            instanceName: str,
            body: BuildBazelRemoteExecutionV2BatchReadBlobsRequest = ...,
            **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2BatchReadBlobsResponseHttpRequest: ...
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
    class V2Resource(googleapiclient.discovery.Resource):
        def getCapabilities(
            self, *, instanceName: str, **kwargs: typing.Any
        ) -> BuildBazelRemoteExecutionV2ServerCapabilitiesHttpRequest: ...
    def operations(self) -> OperationsResource: ...
    def actions(self) -> ActionsResource: ...
    def actionResults(self) -> ActionResultsResource: ...
    def blobs(self) -> BlobsResource: ...
    def v2(self) -> V2Resource: ...

class BuildBazelRemoteExecutionV2ServerCapabilitiesHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BuildBazelRemoteExecutionV2ServerCapabilities: ...

class BuildBazelRemoteExecutionV2BatchReadBlobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BuildBazelRemoteExecutionV2BatchReadBlobsResponse: ...

class BuildBazelRemoteExecutionV2ActionResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BuildBazelRemoteExecutionV2ActionResult: ...

class BuildBazelRemoteExecutionV2FindMissingBlobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BuildBazelRemoteExecutionV2FindMissingBlobsResponse: ...

class BuildBazelRemoteExecutionV2BatchUpdateBlobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BuildBazelRemoteExecutionV2BatchUpdateBlobsResponse: ...

class BuildBazelRemoteExecutionV2GetTreeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BuildBazelRemoteExecutionV2GetTreeResponse: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...
