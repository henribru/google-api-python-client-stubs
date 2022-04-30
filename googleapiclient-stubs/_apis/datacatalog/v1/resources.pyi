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
            body: GoogleCloudDatacatalogV1SearchCatalogRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest,
            previous_response: GoogleCloudDatacatalogV1SearchCatalogResponse,
        ) -> GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest | None: ...

    @typing.type_check_only
    class EntriesResource(googleapiclient.discovery.Resource):
        def lookup(
            self,
            *,
            fullyQualifiedName: str = ...,
            linkedResource: str = ...,
            sqlResource: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDatacatalogV1EntryHttpRequest: ...

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
                            body: GoogleCloudDatacatalogV1Tag = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1TagHttpRequest: ...
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
                        ) -> GoogleCloudDatacatalogV1ListTagsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDatacatalogV1ListTagsResponseHttpRequest,
                            previous_response: GoogleCloudDatacatalogV1ListTagsResponse,
                        ) -> GoogleCloudDatacatalogV1ListTagsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDatacatalogV1Tag = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1TagHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1Entry = ...,
                        entryId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1EntryHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1EntryHttpRequest: ...
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
                    ) -> GoogleCloudDatacatalogV1ListEntriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1ListEntriesResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1ListEntriesResponse,
                    ) -> GoogleCloudDatacatalogV1ListEntriesResponseHttpRequest | None: ...
                    def modifyEntryContacts(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1ModifyEntryContactsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1ContactsHttpRequest: ...
                    def modifyEntryOverview(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1ModifyEntryOverviewRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1EntryOverviewHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1Entry = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1EntryHttpRequest: ...
                    def star(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1StarEntryRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1StarEntryResponseHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def unstar(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1UnstarEntryRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1UnstarEntryResponseHttpRequest: ...
                    def tags(self) -> TagsResource: ...

                @typing.type_check_only
                class TagsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1Tag = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1TagHttpRequest: ...
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
                    ) -> GoogleCloudDatacatalogV1ListTagsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1ListTagsResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1ListTagsResponse,
                    ) -> GoogleCloudDatacatalogV1ListTagsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1Tag = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1TagHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1EntryGroup = ...,
                    entryGroupId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1EntryGroupHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1EntryGroupHttpRequest: ...
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
                ) -> GoogleCloudDatacatalogV1ListEntryGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatacatalogV1ListEntryGroupsResponseHttpRequest,
                    previous_response: GoogleCloudDatacatalogV1ListEntryGroupsResponse,
                ) -> GoogleCloudDatacatalogV1ListEntryGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1EntryGroup = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1EntryGroupHttpRequest: ...
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
                            body: GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1TagTemplateFieldHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1TagTemplateField = ...,
                        tagTemplateFieldId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1TagTemplateFieldHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1TagTemplateField = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1TagTemplateFieldHttpRequest: ...
                    def rename(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1RenameTagTemplateFieldRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1TagTemplateFieldHttpRequest: ...
                    def enumValues(self) -> EnumValuesResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1TagTemplate = ...,
                    tagTemplateId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TagTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TagTemplateHttpRequest: ...
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
                    body: GoogleCloudDatacatalogV1TagTemplate = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TagTemplateHttpRequest: ...
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
                        body: GoogleCloudDatacatalogV1PolicyTag = ...,
                        **kwargs: typing.Any
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
                    ) -> GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogV1ListPolicyTagsResponse,
                    ) -> GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1PolicyTag = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1PolicyTagHttpRequest: ...
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
                    body: GoogleCloudDatacatalogV1Taxonomy = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
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
                ) -> GoogleCloudDatacatalogV1ExportTaxonomiesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
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
                    body: GoogleCloudDatacatalogV1ImportTaxonomiesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1ImportTaxonomiesResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest,
                    previous_response: GoogleCloudDatacatalogV1ListTaxonomiesResponse,
                ) -> GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1Taxonomy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
                def replace(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1ReplaceTaxonomyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1TaxonomyHttpRequest: ...
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
class GoogleCloudDatacatalogV1ContactsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1Contacts: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1EntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1Entry: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1EntryGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1EntryGroup: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1EntryOverviewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1EntryOverview: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ExportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1ExportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1ImportTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1ListEntriesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntryGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1ListEntryGroupsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListPolicyTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1ListPolicyTagsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1ListTagsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1ListTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PolicyTagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1PolicyTag: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1SearchCatalogResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1StarEntryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1StarEntryResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1Tag: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1TagTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1TagTemplate: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1TagTemplateFieldHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1TagTemplateField: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1TaxonomyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1Taxonomy: ...

@typing.type_check_only
class GoogleCloudDatacatalogV1UnstarEntryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatacatalogV1UnstarEntryResponse: ...

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
