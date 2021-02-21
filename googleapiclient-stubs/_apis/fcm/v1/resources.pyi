import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class FirebaseCloudMessagingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MessagesResource(googleapiclient.discovery.Resource):
            def send(
                self,
                *,
                parent: str,
                body: SendMessageRequest = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
        def messages(self) -> MessagesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Message: ...
