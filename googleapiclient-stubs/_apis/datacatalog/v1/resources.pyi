import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DataCatalogResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CatalogResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            body: GoogleCloudDatacatalogV1SearchCatalogRequest,
            **kwargs: typing.Any,
        ) -> GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest,
            previous_response: GoogleCloudDatacatalogV1SearchCatalogResponse,
        ) -> GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest | None: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            def retrieveConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDatacatalogV1OrganizationConfigHttpRequest: ...
            def retrieveEffectiveConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDatacatalogV1MigrationConfigHttpRequest: ...
            def setConfig(
                self,
                *,
                name: str,
                body: GoogleCloudDatacatalogV1SetConfigRequest,
                **kwargs: typing.Any,
            ) -> GoogleCloudDatacatalogV1MigrationConfigHttpRequest: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class TaxonomiesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PolicyTagsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1PolicyTag,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogV1PolicyTagHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1PolicyTagHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1ListPolicyTagsResponse,
                    ) -> (
                        GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1PolicyTag,
                        updateMask: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogV1PolicyTagHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1Taxonomy,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def export(
                    self,
                    *,
                    parent: str,
                    serializedTaxonomies: bool | None = ...,
                    taxonomies: str | _list[str] | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1ExportTaxonomiesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1ImportTaxonomiesRequest,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1ImportTaxonomiesResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest,
                    previous_response: GoogleCloudDatacatalogV1ListTaxonomiesResponse,
                ) -> (
                    GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1Taxonomy,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
                def replace(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1ReplaceTaxonomyRequest,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def policyTags(self) -> PolicyTagsResource: ...

            def retrieveEffectiveConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDatacatalogV1MigrationConfigHttpRequest: ...
            def setConfig(
                self,
                *,
                name: str,
                body: GoogleCloudDatacatalogV1SetConfigRequest,
                **kwargs: typing.Any,
            ) -> GoogleCloudDatacatalogV1MigrationConfigHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def taxonomies(self) -> TaxonomiesResource: ...

        def locations(self) -> LocationsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def catalog(self) -> CatalogResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ExportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1ExportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1ImportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1ListPolicyTagsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1ListTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1MigrationConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1MigrationConfig: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1OrganizationConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1OrganizationConfig: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PolicyTagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1PolicyTag: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1SearchCatalogResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1TaxonomyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1Taxonomy: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
