import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AppengineResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, appsId: str, locationsId: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
        @typing.type_check_only
        class ModulesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InstancesResource(googleapiclient.discovery.Resource):
                    def debug(
                        self,
                        *,
                        appsId: str,
                        modulesId: str,
                        versionsId: str,
                        instancesId: str,
                        body: DebugInstanceRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        appsId: str,
                        modulesId: str,
                        versionsId: str,
                        instancesId: str,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        appsId: str,
                        modulesId: str,
                        versionsId: str,
                        instancesId: str,
                        **kwargs: typing.Any
                    ) -> InstanceHttpRequest: ...
                    def list(
                        self,
                        *,
                        appsId: str,
                        modulesId: str,
                        versionsId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListInstancesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    appsId: str,
                    modulesId: str,
                    body: Version = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    appsId: str,
                    modulesId: str,
                    versionsId: str,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    appsId: str,
                    modulesId: str,
                    versionsId: str,
                    view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                    **kwargs: typing.Any
                ) -> VersionHttpRequest: ...
                def list(
                    self,
                    *,
                    appsId: str,
                    modulesId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                    **kwargs: typing.Any
                ) -> ListVersionsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    appsId: str,
                    modulesId: str,
                    versionsId: str,
                    body: Version = ...,
                    mask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def instances(self) -> InstancesResource: ...
            def delete(
                self, *, appsId: str, modulesId: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, appsId: str, modulesId: str, **kwargs: typing.Any
            ) -> ModuleHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListModulesResponseHttpRequest: ...
            def patch(
                self,
                *,
                appsId: str,
                modulesId: str,
                body: Module = ...,
                mask: str = ...,
                migrateTraffic: bool = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def versions(self) -> VersionsResource: ...
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, appsId: str, operationsId: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
        def create(
            self, *, body: Application = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, appsId: str, ensureResourcesExist: bool = ..., **kwargs: typing.Any
        ) -> ApplicationHttpRequest: ...
        def patch(
            self,
            *,
            appsId: str,
            body: Application = ...,
            mask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def locations(self) -> LocationsResource: ...
        def modules(self) -> ModulesResource: ...
        def operations(self) -> OperationsResource: ...
    def apps(self) -> AppsResource: ...

@typing.type_check_only
class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Application: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Instance: ...

@typing.type_check_only
class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListInstancesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListModulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListModulesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListVersionsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class ModuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Module: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Version: ...
