import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class FirebaseCloudMessagingResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
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

class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Message: ...
