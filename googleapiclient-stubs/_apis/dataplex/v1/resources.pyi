import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudDataplexResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EncryptionConfigsResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def listOperations(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def listOperations_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            def encryptionConfigs(self) -> EncryptionConfigsResource: ...
            def operations(self) -> OperationsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AspectTypesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1AspectType = ...,
                    aspectTypeId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1AspectTypeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1ListAspectTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListAspectTypesResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListAspectTypesResponse,
                ) -> GoogleCloudDataplexV1ListAspectTypesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1AspectType = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class DataAttributeBindingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1DataAttributeBinding = ...,
                    dataAttributeBindingId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1DataAttributeBindingHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDataplexV1ListDataAttributeBindingsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListDataAttributeBindingsResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListDataAttributeBindingsResponse,
                ) -> (
                    GoogleCloudDataplexV1ListDataAttributeBindingsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1DataAttributeBinding = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class DataScansResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class JobsResource(googleapiclient.discovery.Resource):
                    def generateDataQualityRules(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1GenerateDataQualityRulesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDataplexV1GenerateDataQualityRulesResponseHttpRequest
                    ): ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "DATA_SCAN_JOB_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1DataScanJobHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListDataScanJobsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListDataScanJobsResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListDataScanJobsResponse,
                    ) -> (
                        GoogleCloudDataplexV1ListDataScanJobsResponseHttpRequest | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1DataScan = ...,
                    dataScanId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def generateDataQualityRules(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1GenerateDataQualityRulesRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDataplexV1GenerateDataQualityRulesResponseHttpRequest
                ): ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "DATA_SCAN_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1DataScanHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1ListDataScansResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListDataScansResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListDataScansResponse,
                ) -> GoogleCloudDataplexV1ListDataScansResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1DataScan = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def run(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1RunDataScanRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1RunDataScanResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def jobs(self) -> JobsResource: ...

            @typing.type_check_only
            class DataTaxonomiesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AttributesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1DataAttribute = ...,
                        dataAttributeId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1DataAttributeHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListDataAttributesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListDataAttributesResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListDataAttributesResponse,
                    ) -> (
                        GoogleCloudDataplexV1ListDataAttributesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1DataAttribute = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1DataTaxonomy = ...,
                    dataTaxonomyId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1DataTaxonomyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1ListDataTaxonomiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListDataTaxonomiesResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListDataTaxonomiesResponse,
                ) -> (
                    GoogleCloudDataplexV1ListDataTaxonomiesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1DataTaxonomy = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def attributes(self) -> AttributesResource: ...

            @typing.type_check_only
            class EntryGroupsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntriesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Entry = ...,
                        entryId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1EntryHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1EntryHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        aspectTypes: str | _list[str] = ...,
                        paths: str | _list[str] = ...,
                        view: typing_extensions.Literal[
                            "ENTRY_VIEW_UNSPECIFIED", "BASIC", "FULL", "CUSTOM", "ALL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1EntryHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListEntriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListEntriesResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListEntriesResponse,
                    ) -> GoogleCloudDataplexV1ListEntriesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Entry = ...,
                        allowMissing: bool = ...,
                        aspectKeys: str | _list[str] = ...,
                        deleteMissingAspects: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1EntryHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1EntryGroup = ...,
                    entryGroupId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1EntryGroupHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1ListEntryGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListEntryGroupsResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListEntryGroupsResponse,
                ) -> GoogleCloudDataplexV1ListEntryGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1EntryGroup = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def entries(self) -> EntriesResource: ...

            @typing.type_check_only
            class EntryLinkTypesResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class EntryTypesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1EntryType = ...,
                    entryTypeId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1EntryTypeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1ListEntryTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListEntryTypesResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListEntryTypesResponse,
                ) -> GoogleCloudDataplexV1ListEntryTypesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1EntryType = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class GlossariesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CategoriesResource(googleapiclient.discovery.Resource):
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                @typing.type_check_only
                class TermsResource(googleapiclient.discovery.Resource):
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def categories(self) -> CategoriesResource: ...
                def terms(self) -> TermsResource: ...

            @typing.type_check_only
            class GovernanceRulesResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class LakesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ActionsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListActionsResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListActionsResponse,
                    ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest | None: ...

                @typing.type_check_only
                class ContentResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "CONTENT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListContentResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListContentResponse,
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                @typing.type_check_only
                class ContentitemsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "CONTENT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListContentResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListContentResponse,
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                @typing.type_check_only
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1ListSessionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListSessionsResponse,
                        ) -> (
                            GoogleCloudDataplexV1ListSessionsResponseHttpRequest | None
                        ): ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Environment = ...,
                        environmentId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1EnvironmentHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListEnvironmentsResponse,
                    ) -> (
                        GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Environment = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def sessions(self) -> SessionsResource: ...

                @typing.type_check_only
                class TasksResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class JobsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDataplexV1CancelJobRequest = ...,
                            **kwargs: typing.Any,
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1JobHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1ListJobsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListJobsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListJobsResponse,
                        ) -> (
                            GoogleCloudDataplexV1ListJobsResponseHttpRequest | None
                        ): ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Task = ...,
                        taskId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1TaskHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListTasksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListTasksResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListTasksResponse,
                    ) -> GoogleCloudDataplexV1ListTasksResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Task = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def run(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1RunTaskRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1RunTaskResponseHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def jobs(self) -> JobsResource: ...

                @typing.type_check_only
                class ZonesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ActionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListActionsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListActionsResponse,
                        ) -> (
                            GoogleCloudDataplexV1ListActionsResponseHttpRequest | None
                        ): ...

                    @typing.type_check_only
                    class AssetsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class ActionsResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDataplexV1ListActionsResponseHttpRequest
                            ): ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDataplexV1ListActionsResponseHttpRequest,
                                previous_response: GoogleCloudDataplexV1ListActionsResponse,
                            ) -> (
                                GoogleCloudDataplexV1ListActionsResponseHttpRequest
                                | None
                            ): ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDataplexV1Asset = ...,
                            assetId: str = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1AssetHttpRequest: ...
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1ListAssetsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListAssetsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListAssetsResponse,
                        ) -> (
                            GoogleCloudDataplexV1ListAssetsResponseHttpRequest | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDataplexV1Asset = ...,
                            updateMask: str = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1SetIamPolicyRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                        def actions(self) -> ActionsResource: ...

                    @typing.type_check_only
                    class EntitiesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class PartitionsResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDataplexV1Partition = ...,
                                validateOnly: bool = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDataplexV1PartitionHttpRequest: ...
                            def delete(
                                self,
                                *,
                                name: str,
                                etag: str = ...,
                                **kwargs: typing.Any,
                            ) -> EmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDataplexV1PartitionHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDataplexV1ListPartitionsResponseHttpRequest
                            ): ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDataplexV1ListPartitionsResponseHttpRequest,
                                previous_response: GoogleCloudDataplexV1ListPartitionsResponse,
                            ) -> (
                                GoogleCloudDataplexV1ListPartitionsResponseHttpRequest
                                | None
                            ): ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDataplexV1Entity = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1EntityHttpRequest: ...
                        def delete(
                            self, *, name: str, etag: str = ..., **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "ENTITY_VIEW_UNSPECIFIED", "BASIC", "SCHEMA", "FULL"
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1EntityHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "ENTITY_VIEW_UNSPECIFIED", "TABLES", "FILESETS"
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1ListEntitiesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListEntitiesResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListEntitiesResponse,
                        ) -> (
                            GoogleCloudDataplexV1ListEntitiesResponseHttpRequest | None
                        ): ...
                        def update(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDataplexV1Entity = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDataplexV1EntityHttpRequest: ...
                        def partitions(self) -> PartitionsResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Zone = ...,
                        validateOnly: bool = ...,
                        zoneId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ZoneHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDataplexV1ListZonesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListZonesResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListZonesResponse,
                    ) -> GoogleCloudDataplexV1ListZonesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Zone = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def actions(self) -> ActionsResource: ...
                    def assets(self) -> AssetsResource: ...
                    def entities(self) -> EntitiesResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1Lake = ...,
                    lakeId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1LakeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1ListLakesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListLakesResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListLakesResponse,
                ) -> GoogleCloudDataplexV1ListLakesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1Lake = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def actions(self) -> ActionsResource: ...
                def content(self) -> ContentResource: ...
                def contentitems(self) -> ContentitemsResource: ...
                def environments(self) -> EnvironmentsResource: ...
                def tasks(self) -> TasksResource: ...
                def zones(self) -> ZonesResource: ...

            @typing.type_check_only
            class MetadataJobsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1CancelMetadataJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1MetadataJob = ...,
                    metadataJobId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1MetadataJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDataplexV1ListMetadataJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListMetadataJobsResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListMetadataJobsResponse,
                ) -> (
                    GoogleCloudDataplexV1ListMetadataJobsResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def lookupEntry(
                self,
                *,
                name: str,
                aspectTypes: str | _list[str] = ...,
                entry: str = ...,
                paths: str | _list[str] = ...,
                view: typing_extensions.Literal[
                    "ENTRY_VIEW_UNSPECIFIED", "BASIC", "FULL", "CUSTOM", "ALL"
                ] = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDataplexV1EntryHttpRequest: ...
            def searchEntries(
                self,
                *,
                name: str,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                scope: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDataplexV1SearchEntriesResponseHttpRequest: ...
            def searchEntries_next(
                self,
                previous_request: GoogleCloudDataplexV1SearchEntriesResponseHttpRequest,
                previous_response: GoogleCloudDataplexV1SearchEntriesResponse,
            ) -> GoogleCloudDataplexV1SearchEntriesResponseHttpRequest | None: ...
            def aspectTypes(self) -> AspectTypesResource: ...
            def dataAttributeBindings(self) -> DataAttributeBindingsResource: ...
            def dataScans(self) -> DataScansResource: ...
            def dataTaxonomies(self) -> DataTaxonomiesResource: ...
            def entryGroups(self) -> EntryGroupsResource: ...
            def entryLinkTypes(self) -> EntryLinkTypesResource: ...
            def entryTypes(self) -> EntryTypesResource: ...
            def glossaries(self) -> GlossariesResource: ...
            def governanceRules(self) -> GovernanceRulesResource: ...
            def lakes(self) -> LakesResource: ...
            def metadataJobs(self) -> MetadataJobsResource: ...
            def operations(self) -> OperationsResource: ...

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
class GoogleCloudDataplexV1AspectTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1AspectType: ...

@typing.type_check_only
class GoogleCloudDataplexV1AssetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Asset: ...

@typing.type_check_only
class GoogleCloudDataplexV1ContentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Content: ...

@typing.type_check_only
class GoogleCloudDataplexV1DataAttributeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1DataAttribute: ...

@typing.type_check_only
class GoogleCloudDataplexV1DataAttributeBindingHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1DataAttributeBinding: ...

@typing.type_check_only
class GoogleCloudDataplexV1DataScanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1DataScan: ...

@typing.type_check_only
class GoogleCloudDataplexV1DataScanJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1DataScanJob: ...

@typing.type_check_only
class GoogleCloudDataplexV1DataTaxonomyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1DataTaxonomy: ...

@typing.type_check_only
class GoogleCloudDataplexV1EntityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Entity: ...

@typing.type_check_only
class GoogleCloudDataplexV1EntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Entry: ...

@typing.type_check_only
class GoogleCloudDataplexV1EntryGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1EntryGroup: ...

@typing.type_check_only
class GoogleCloudDataplexV1EntryTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1EntryType: ...

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Environment: ...

@typing.type_check_only
class GoogleCloudDataplexV1GenerateDataQualityRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1GenerateDataQualityRulesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Job: ...

@typing.type_check_only
class GoogleCloudDataplexV1LakeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Lake: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListActionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListActionsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListAspectTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListAspectTypesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListAssetsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListContentResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListDataAttributeBindingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListDataAttributeBindingsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListDataAttributesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListDataAttributesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListDataScanJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListDataScanJobsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListDataScansResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListDataScansResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListDataTaxonomiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListDataTaxonomiesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListEntitiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListEntitiesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListEntriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListEntriesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListEntryGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListEntryGroupsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListEntryTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListEntryTypesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListEnvironmentsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListJobsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListLakesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListLakesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListMetadataJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListMetadataJobsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListPartitionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListPartitionsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListSessionsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListTasksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListTasksResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListZonesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1ListZonesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1MetadataJob: ...

@typing.type_check_only
class GoogleCloudDataplexV1PartitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Partition: ...

@typing.type_check_only
class GoogleCloudDataplexV1RunDataScanResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1RunDataScanResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1RunTaskResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1RunTaskResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1SearchEntriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1SearchEntriesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Task: ...

@typing.type_check_only
class GoogleCloudDataplexV1ZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDataplexV1Zone: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...
