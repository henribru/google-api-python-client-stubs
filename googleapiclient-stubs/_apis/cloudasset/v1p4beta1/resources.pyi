import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudAssetResource(googleapiclient.discovery.Resource):
    class V1p4beta1Resource(googleapiclient.discovery.Resource):
        def exportIamPolicyAnalysis(
            self,
            *,
            parent: str,
            body: ExportIamPolicyAnalysisRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def analyzeIamPolicy(
            self,
            *,
            parent: str,
            options_analyzeServiceAccountImpersonation: bool = ...,
            analysisQuery_identitySelector_identity: str = ...,
            analysisQuery_resourceSelector_fullResourceName: str = ...,
            options_executionTimeout: str = ...,
            options_expandResources: bool = ...,
            options_expandGroups: bool = ...,
            options_expandRoles: bool = ...,
            analysisQuery_accessSelector_permissions: typing.Union[
                str, typing.List[str]
            ] = ...,
            options_outputResourceEdges: bool = ...,
            options_outputGroupEdges: bool = ...,
            analysisQuery_accessSelector_roles: typing.Union[
                str, typing.List[str]
            ] = ...,
            **kwargs: typing.Any
        ) -> AnalyzeIamPolicyResponseHttpRequest: ...
    def v1p4beta1(self) -> V1p4beta1Resource: ...

class AnalyzeIamPolicyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AnalyzeIamPolicyResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...
