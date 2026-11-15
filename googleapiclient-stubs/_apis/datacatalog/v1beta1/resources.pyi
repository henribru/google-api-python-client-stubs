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
            body: GoogleCloudDatacatalogV1beta1SearchCatalogRequest,
            **kwargs: typing.Any,
        ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest,
            previous_response: GoogleCloudDatacatalogV1beta1SearchCatalogResponse,
        ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class TaxonomiesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PolicyTagsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1beta1PolicyTag,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest: ...
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
                    ) -> (
                        GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse,
                    ) -> (
                        GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1PolicyTag,
                        updateMask: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest: ...
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
                    body: GoogleCloudDatacatalogV1beta1Taxonomy,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
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
                ) -> (
                    GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponseHttpRequest
                ): ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
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
                    body: GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponseHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest,
                    previous_response: GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse,
                ) -> (
                    GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1beta1Taxonomy,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1beta1PolicyTag: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogV1beta1Taxonomy: ...

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
