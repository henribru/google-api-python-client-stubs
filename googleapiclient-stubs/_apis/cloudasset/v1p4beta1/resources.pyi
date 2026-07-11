import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class V1p4beta1Resource(googleapiclient.discovery.Resource):
        def analyzeIamPolicy(
            self,
            *,
            parent: str,
            analysisQuery_accessSelector_permissions: str | _list[str] | None = ...,
            analysisQuery_accessSelector_roles: str | _list[str] | None = ...,
            analysisQuery_identitySelector_identity: str | None = ...,
            analysisQuery_resourceSelector_fullResourceName: str | None = ...,
            options_analyzeServiceAccountImpersonation: bool | None = ...,
            options_executionTimeout: str | None = ...,
            options_expandGroups: bool | None = ...,
            options_expandResources: bool | None = ...,
            options_expandRoles: bool | None = ...,
            options_outputGroupEdges: bool | None = ...,
            options_outputResourceEdges: bool | None = ...,
            **kwargs: typing.Any,
        ) -> AnalyzeIamPolicyResponseHttpRequest: ...
        def exportIamPolicyAnalysis(
            self,
            *,
            parent: str,
            body: ExportIamPolicyAnalysisRequest,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def v1p4beta1(self) -> V1p4beta1Resource: ...

@typing.type_check_only
class AnalyzeIamPolicyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyzeIamPolicyResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...
