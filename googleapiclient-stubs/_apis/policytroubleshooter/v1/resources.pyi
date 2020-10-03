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
            body: GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseHttpRequest: ...
    def iam(self) -> IamResource: ...

class GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponse: ...
