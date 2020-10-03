import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudDebuggerResource(googleapiclient.discovery.Resource):
    class DebuggerResource(googleapiclient.discovery.Resource):
        class DebuggeesResource(googleapiclient.discovery.Resource):
            class BreakpointsResource(googleapiclient.discovery.Resource):
                def set(
                    self,
                    *,
                    debuggeeId: str,
                    body: Breakpoint = ...,
                    clientVersion: str = ...,
                    canaryOption: typing_extensions.Literal[
                        "CANARY_OPTION_UNSPECIFIED",
                        "CANARY_OPTION_TRY_ENABLE",
                        "CANARY_OPTION_TRY_DISABLE",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> SetBreakpointResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    debuggeeId: str,
                    clientVersion: str = ...,
                    includeInactive: bool = ...,
                    stripResults: bool = ...,
                    includeAllUsers: bool = ...,
                    waitToken: str = ...,
                    action_value: typing_extensions.Literal["CAPTURE", "LOG"] = ...,
                    **kwargs: typing.Any
                ) -> ListBreakpointsResponseHttpRequest: ...
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
                project: str = ...,
                clientVersion: str = ...,
                includeInactive: bool = ...,
                **kwargs: typing.Any
            ) -> ListDebuggeesResponseHttpRequest: ...
            def breakpoints(self) -> BreakpointsResource: ...
        def debuggees(self) -> DebuggeesResource: ...
    class ControllerResource(googleapiclient.discovery.Resource):
        class DebuggeesResource(googleapiclient.discovery.Resource):
            class BreakpointsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    debuggeeId: str,
                    waitToken: str = ...,
                    agentId: str = ...,
                    successOnTimeout: bool = ...,
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
    def debugger(self) -> DebuggerResource: ...
    def controller(self) -> ControllerResource: ...

class ListBreakpointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBreakpointsResponse: ...

class ListDebuggeesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDebuggeesResponse: ...

class RegisterDebuggeeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegisterDebuggeeResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListActiveBreakpointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListActiveBreakpointsResponse: ...

class GetBreakpointResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetBreakpointResponse: ...

class SetBreakpointResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SetBreakpointResponse: ...

class UpdateActiveBreakpointResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UpdateActiveBreakpointResponse: ...
