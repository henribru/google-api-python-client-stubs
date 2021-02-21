import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class ServiceConsumerManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TenancyUnitsResource(googleapiclient.discovery.Resource):
            def addProject(
                self,
                *,
                parent: str,
                body: AddTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def applyProjectConfig(
                self,
                *,
                name: str,
                body: ApplyTenantProjectConfigRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def attachProject(
                self,
                *,
                name: str,
                body: AttachTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CreateTenancyUnitRequest = ...,
                **kwargs: typing.Any
            ) -> TenancyUnitHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def deleteProject(
                self,
                *,
                name: str,
                body: DeleteTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTenancyUnitsResponseHttpRequest: ...
            def removeProject(
                self,
                *,
                name: str,
                body: RemoveTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def undeleteProject(
                self,
                *,
                name: str,
                body: UndeleteTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def search(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchTenancyUnitsResponseHttpRequest: ...
        def tenancyUnits(self) -> TenancyUnitsResource: ...
    def operations(self) -> OperationsResource: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

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
class ListTenancyUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTenancyUnitsResponse: ...

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
class SearchTenancyUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchTenancyUnitsResponse: ...

@typing.type_check_only
class TenancyUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TenancyUnit: ...
