import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class PolicyTroubleshooterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class IamResource(googleapiclient.discovery.Resource):
        def troubleshoot(
            self,
            *,
            body: GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponseHttpRequest: ...
    def iam(self) -> IamResource: ...

@typing.type_check_only
class GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponse: ...
