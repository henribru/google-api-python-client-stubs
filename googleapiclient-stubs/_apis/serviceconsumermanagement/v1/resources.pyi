import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ServiceConsumerManagementResource(googleapiclient.discovery.Resource):
    class ServicesResource(googleapiclient.discovery.Resource):
        class TenancyUnitsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTenancyUnitsResponseHttpRequest: ...
            def attachProject(
                self,
                *,
                name: str,
                body: AttachTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def applyProjectConfig(
                self,
                *,
                name: str,
                body: ApplyTenantProjectConfigRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def undeleteProject(
                self,
                *,
                name: str,
                body: UndeleteTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def addProject(
                self,
                *,
                parent: str,
                body: AddTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def removeProject(
                self,
                *,
                name: str,
                body: RemoveTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def deleteProject(
                self,
                *,
                name: str,
                body: DeleteTenantProjectRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CreateTenancyUnitRequest = ...,
                **kwargs: typing.Any
            ) -> TenancyUnitHttpRequest: ...
        def search(
            self,
            *,
            parent: str,
            pageToken: str = ...,
            query: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> SearchTenancyUnitsResponseHttpRequest: ...
        def tenancyUnits(self) -> TenancyUnitsResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            pageSize: int = ...,
            filter: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    def services(self) -> ServicesResource: ...
    def operations(self) -> OperationsResource: ...

class TenancyUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TenancyUnit: ...

class ListTenancyUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTenancyUnitsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class SearchTenancyUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchTenancyUnitsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...
