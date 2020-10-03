import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PolicyTroubleshooterResource(googleapiclient.discovery.Resource):
    class IamResource(googleapiclient.discovery.Resource):
        def troubleshoot(
            self,
            *,
            body: GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponseHttpRequest: ...
    def iam(self) -> IamResource: ...

class GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponse: ...
