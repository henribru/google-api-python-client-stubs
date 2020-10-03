import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DataCatalogResource(googleapiclient.discovery.Resource):
    class EntriesResource(googleapiclient.discovery.Resource):
        def lookup(
            self,
            *,
            sqlResource: str = ...,
            linkedResource: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDatacatalogV1beta1EntryHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class TaxonomiesResource(googleapiclient.discovery.Resource):
                class PolicyTagsResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1PolicyTag = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest: ...
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
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
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
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def export(
                    self,
                    *,
                    parent: str,
                    serializedTaxonomies: bool = ...,
                    taxonomies: typing.Union[str, typing.List[str]] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogV1beta1Taxonomy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def policyTags(self) -> PolicyTagsResource: ...
            class TagTemplatesResource(googleapiclient.discovery.Resource):
                class FieldsResource(googleapiclient.discovery.Resource):
                    class EnumValuesResource(googleapiclient.discovery.Resource):
                        def rename(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest: ...
                    def rename(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldRequest = ...,
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
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1beta1TagTemplateField = ...,
                        tagTemplateFieldId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest: ...
                    def enumValues(self) -> EnumValuesResource: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
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
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TagTemplateHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1beta1TagTemplate = ...,
                    tagTemplateId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1TagTemplateHttpRequest: ...
                def fields(self) -> FieldsResource: ...
            class EntryGroupsResource(googleapiclient.discovery.Resource):
                class TagsResource(googleapiclient.discovery.Resource):
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
                        body: GoogleCloudDatacatalogV1beta1Tag = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1TagHttpRequest: ...
                class EntriesResource(googleapiclient.discovery.Resource):
                    class TagsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDatacatalogV1beta1Tag = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1TagHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDatacatalogV1beta1Tag = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogV1beta1TagHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogV1beta1Entry = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1EntryHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        readMask: str = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1ListEntriesResponseHttpRequest: ...
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
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogV1beta1Entry = ...,
                        entryId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogV1beta1EntryHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def tags(self) -> TagsResource: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1ListEntryGroupsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogV1beta1EntryGroup = ...,
                    entryGroupId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
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
                    body: GoogleCloudDatacatalogV1beta1EntryGroup = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest: ...
                def tags(self) -> TagsResource: ...
                def entries(self) -> EntriesResource: ...
            def taxonomies(self) -> TaxonomiesResource: ...
            def tagTemplates(self) -> TagTemplatesResource: ...
            def entryGroups(self) -> EntryGroupsResource: ...
        def locations(self) -> LocationsResource: ...
    class CatalogResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            body: GoogleCloudDatacatalogV1beta1SearchCatalogRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest: ...
    def entries(self) -> EntriesResource: ...
    def projects(self) -> ProjectsResource: ...
    def catalog(self) -> CatalogResource: ...

class GoogleCloudDatacatalogV1beta1SearchCatalogResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1SearchCatalogResponse: ...

class GoogleCloudDatacatalogV1beta1ListTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1ListTagsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse: ...

class GoogleCloudDatacatalogV1beta1TagTemplateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1TagTemplate: ...

class GoogleCloudDatacatalogV1beta1ListEntryGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse: ...

class GoogleCloudDatacatalogV1beta1EntryGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1EntryGroup: ...

class GoogleCloudDatacatalogV1beta1EntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1Entry: ...

class GoogleCloudDatacatalogV1beta1PolicyTagHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1PolicyTag: ...

class GoogleCloudDatacatalogV1beta1ListTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse: ...

class GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse: ...

class GoogleCloudDatacatalogV1beta1TaxonomyHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1Taxonomy: ...

class GoogleCloudDatacatalogV1beta1ListEntriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1ListEntriesResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class GoogleCloudDatacatalogV1beta1ListPolicyTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse: ...

class GoogleCloudDatacatalogV1beta1TagTemplateFieldHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1TagTemplateField: ...

class GoogleCloudDatacatalogV1beta1TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDatacatalogV1beta1Tag: ...
