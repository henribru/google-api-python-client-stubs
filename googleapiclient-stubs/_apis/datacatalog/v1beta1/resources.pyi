import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DataCatalogResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CatalogResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            body: GoogleCloudDatacatalogV1beta1SearchCatalogRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest,
            previous_response: GoogleCloudDatacatalogV1beta1SearchCatalogResponse,
        ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest | None: ...

    @typing.type_check_only
    class EntriesResource(googleapiclient.discovery.Resource):
        def lookup(
            self,
            *,
            linkedResource: str = ...,
            sqlResource: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDatacatalogV1beta1EntryHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EntryGroupsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntriesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TagsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDatacatalogV1beta1Tag = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1TagHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest,
                            previous_response: GoogleCloudDatacatalogV1beta1ListTagsResponse,
                        ) -> GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDatacatalogV1beta1Tag = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1TagHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1beta1Entry = ...,
                        entryId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1EntryHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1EntryHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1ListEntriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1beta1ListEntriesResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1beta1ListEntriesResponse,
                    ) -> GoogleCloudDatacatalogV1beta1ListEntriesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1Entry = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1EntryHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def tags(self) -> TagsResource: ...

                @typing.type_check_only
                class TagsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1beta1Tag = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1TagHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1beta1ListTagsResponse,
                    ) -> GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1Tag = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1TagHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1beta1EntryGroup = ...,
                    entryGroupId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ListEntryGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatacatalogV1beta1ListEntryGroupsResponseHttpRequest,
                    previous_response: GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse,
                ) -> GoogleCloudDatacatalogV1beta1ListEntryGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1beta1EntryGroup = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def entries(self) -> EntriesResource: ...
                def tags(self) -> TagsResource: ...

            @typing.type_check_only
            class TagTemplatesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FieldsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class EnumValuesResource(googleapiclient.discovery.Resource):
                        def rename(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1beta1TagTemplateField = ...,
                        tagTemplateFieldId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1TagTemplateField = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest: ...
                    def rename(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest: ...
                    def enumValues(self) -> EnumValuesResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1beta1TagTemplate = ...,
                    tagTemplateId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TagTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TagTemplateHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1beta1TagTemplate = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TagTemplateHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def fields(self) -> FieldsResource: ...

            @typing.type_check_only
            class TaxonomiesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PolicyTagsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1beta1PolicyTag = ...,
                        **kwargs: typing.Any
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
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse,
                    ) -> GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1PolicyTag = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1beta1Taxonomy = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def export(
                    self,
                    *,
                    parent: str,
                    serializedTaxonomies: bool = ...,
                    taxonomies: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest,
                    previous_response: GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse,
                ) -> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1beta1Taxonomy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def policyTags(self) -> PolicyTagsResource: ...

            def entryGroups(self) -> EntryGroupsResource: ...
            def tagTemplates(self) -> TagTemplatesResource: ...
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def catalog(self) -> CatalogResource: ...
    def entries(self) -> EntriesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1EntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1Entry: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1EntryGroup: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListEntriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1ListEntriesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListEntryGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1ListTagsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1PolicyTag: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1Tag: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TagTemplateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1TagTemplate: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1TagTemplateField: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1beta1Taxonomy: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
