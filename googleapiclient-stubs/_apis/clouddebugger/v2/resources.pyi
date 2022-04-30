import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudDebuggerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ControllerResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DebuggeesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BreakpointsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    debuggeeId: str,
                    agentId: str = ...,
                    successOnTimeout: bool = ...,
                    waitToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListActiveBreakpointsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    debuggeeId: str,
                    id: str,
                    body: UpdateActiveBreakpointRequest = ...,
                    **kwargs: typing.Any
                ) -> UpdateActiveBreakpointResponseHttpRequest: ...

            def register(
                self, *, body: RegisterDebuggeeRequest = ..., **kwargs: typing.Any
            ) -> RegisterDebuggeeResponseHttpRequest: ...
            def breakpoints(self) -> BreakpointsResource: ...

        def debuggees(self) -> DebuggeesResource: ...

    @typing.type_check_only
    class DebuggerResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DebuggeesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BreakpointsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    debuggeeId: str,
                    breakpointId: str,
                    clientVersion: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    debuggeeId: str,
                    breakpointId: str,
                    clientVersion: str = ...,
                    **kwargs: typing.Any
                ) -> GetBreakpointResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    debuggeeId: str,
                    action_value: typing_extensions.Literal["CAPTURE", "LOG"] = ...,
                    clientVersion: str = ...,
                    includeAllUsers: bool = ...,
                    includeInactive: bool = ...,
                    stripResults: bool = ...,
                    waitToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBreakpointsResponseHttpRequest: ...
                def set(
                    self,
                    *,
                    debuggeeId: str,
                    body: Breakpoint = ...,
                    canaryOption: typing_extensions.Literal[
                        "CANARY_OPTION_UNSPECIFIED",
                        "CANARY_OPTION_TRY_ENABLE",
                        "CANARY_OPTION_TRY_DISABLE",
                    ] = ...,
                    clientVersion: str = ...,
                    **kwargs: typing.Any
                ) -> SetBreakpointResponseHttpRequest: ...

            def list(
                self,
                *,
                clientVersion: str = ...,
                includeInactive: bool = ...,
                project: str = ...,
                **kwargs: typing.Any
            ) -> ListDebuggeesResponseHttpRequest: ...
            def breakpoints(self) -> BreakpointsResource: ...

        def debuggees(self) -> DebuggeesResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def controller(self) -> ControllerResource: ...
    def debugger(self) -> DebuggerResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetBreakpointResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetBreakpointResponse: ...

@typing.type_check_only
class ListActiveBreakpointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListActiveBreakpointsResponse: ...

@typing.type_check_only
class ListBreakpointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBreakpointsResponse: ...

@typing.type_check_only
class ListDebuggeesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDebuggeesResponse: ...

@typing.type_check_only
class RegisterDebuggeeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegisterDebuggeeResponse: ...

@typing.type_check_only
class SetBreakpointResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SetBreakpointResponse: ...

@typing.type_check_only
class UpdateActiveBreakpointResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UpdateActiveBreakpointResponse: ...
