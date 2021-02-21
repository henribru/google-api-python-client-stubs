import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class V1p4beta1Resource(googleapiclient.discovery.Resource):
        def analyzeIamPolicy(
            self,
            *,
            parent: str,
            analysisQuery_accessSelector_permissions: typing.Union[
                str, typing.List[str]
            ] = ...,
            analysisQuery_accessSelector_roles: typing.Union[
                str, typing.List[str]
            ] = ...,
            analysisQuery_identitySelector_identity: str = ...,
            analysisQuery_resourceSelector_fullResourceName: str = ...,
            options_analyzeServiceAccountImpersonation: bool = ...,
            options_executionTimeout: str = ...,
            options_expandGroups: bool = ...,
            options_expandResources: bool = ...,
            options_expandRoles: bool = ...,
            options_outputGroupEdges: bool = ...,
            options_outputResourceEdges: bool = ...,
            **kwargs: typing.Any
        ) -> AnalyzeIamPolicyResponseHttpRequest: ...
        def exportIamPolicyAnalysis(
            self,
            *,
            parent: str,
            body: ExportIamPolicyAnalysisRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def v1p4beta1(self) -> V1p4beta1Resource: ...

@typing.type_check_only
class AnalyzeIamPolicyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AnalyzeIamPolicyResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...
