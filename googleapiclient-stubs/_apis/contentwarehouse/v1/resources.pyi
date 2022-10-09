import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ContentwarehouseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DocumentSchemasResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContentwarehouseV1DocumentSchema = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1DocumentSchemaHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1DocumentSchemaHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1ListDocumentSchemasResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContentwarehouseV1ListDocumentSchemasResponseHttpRequest,
                    previous_response: GoogleCloudContentwarehouseV1ListDocumentSchemasResponse,
                ) -> GoogleCloudContentwarehouseV1ListDocumentSchemasResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContentwarehouseV1UpdateDocumentSchemaRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1DocumentSchemaHttpRequest: ...

            @typing.type_check_only
            class DocumentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DocumentLinksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContentwarehouseV1CreateDocumentLinkRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudContentwarehouseV1DocumentLinkHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContentwarehouseV1DeleteDocumentLinkRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...

                @typing.type_check_only
                class ReferenceIdResource(googleapiclient.discovery.Resource):
                    def delete(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContentwarehouseV1DeleteDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContentwarehouseV1GetDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudContentwarehouseV1DocumentHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContentwarehouseV1UpdateDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudContentwarehouseV1UpdateDocumentResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContentwarehouseV1CreateDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1CreateDocumentResponseHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContentwarehouseV1DeleteDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def fetchAcl(
                    self,
                    *,
                    resource: str,
                    body: GoogleCloudContentwarehouseV1FetchAclRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1FetchAclResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContentwarehouseV1GetDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1DocumentHttpRequest: ...
                def linkedSources(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContentwarehouseV1ListLinkedSourcesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1ListLinkedSourcesResponseHttpRequest: ...
                def linkedSources_next(
                    self,
                    previous_request: GoogleCloudContentwarehouseV1ListLinkedSourcesResponseHttpRequest,
                    previous_response: GoogleCloudContentwarehouseV1ListLinkedSourcesResponse,
                ) -> GoogleCloudContentwarehouseV1ListLinkedSourcesResponseHttpRequest | None: ...
                def linkedTargets(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContentwarehouseV1ListLinkedTargetsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1ListLinkedTargetsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContentwarehouseV1UpdateDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1UpdateDocumentResponseHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContentwarehouseV1SearchDocumentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1SearchDocumentsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GoogleCloudContentwarehouseV1SearchDocumentsResponseHttpRequest,
                    previous_response: GoogleCloudContentwarehouseV1SearchDocumentsResponse,
                ) -> GoogleCloudContentwarehouseV1SearchDocumentsResponseHttpRequest | None: ...
                def setAcl(
                    self,
                    *,
                    resource: str,
                    body: GoogleCloudContentwarehouseV1SetAclRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1SetAclResponseHttpRequest: ...
                def documentLinks(self) -> DocumentLinksResource: ...
                def referenceId(self) -> ReferenceIdResource: ...

            @typing.type_check_only
            class RuleSetsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContentwarehouseV1RuleSet = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1RuleSetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1RuleSetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1ListRuleSetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContentwarehouseV1ListRuleSetsResponseHttpRequest,
                    previous_response: GoogleCloudContentwarehouseV1ListRuleSetsResponse,
                ) -> GoogleCloudContentwarehouseV1ListRuleSetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContentwarehouseV1UpdateRuleSetRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1RuleSetHttpRequest: ...

            @typing.type_check_only
            class SynonymSetsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContentwarehouseV1SynonymSet = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1SynonymSetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1SynonymSetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1ListSynonymSetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContentwarehouseV1ListSynonymSetsResponseHttpRequest,
                    previous_response: GoogleCloudContentwarehouseV1ListSynonymSetsResponse,
                ) -> GoogleCloudContentwarehouseV1ListSynonymSetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContentwarehouseV1SynonymSet = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContentwarehouseV1SynonymSetHttpRequest: ...

            def initialize(
                self,
                *,
                location: str,
                body: GoogleCloudContentwarehouseV1InitializeProjectRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def documentSchemas(self) -> DocumentSchemasResource: ...
            def documents(self) -> DocumentsResource: ...
            def ruleSets(self) -> RuleSetsResource: ...
            def synonymSets(self) -> SynonymSetsResource: ...

        def fetchAcl(
            self,
            *,
            resource: str,
            body: GoogleCloudContentwarehouseV1FetchAclRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudContentwarehouseV1FetchAclResponseHttpRequest: ...
        def setAcl(
            self,
            *,
            resource: str,
            body: GoogleCloudContentwarehouseV1SetAclRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudContentwarehouseV1SetAclResponseHttpRequest: ...
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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1CreateDocumentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1CreateDocumentResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1DocumentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1Document: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1DocumentLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1DocumentLink: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1DocumentSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1DocumentSchema: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1FetchAclResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1FetchAclResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListDocumentSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1ListDocumentSchemasResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListLinkedSourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1ListLinkedSourcesResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListLinkedTargetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1ListLinkedTargetsResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListRuleSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1ListRuleSetsResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListSynonymSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1ListSynonymSetsResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1RuleSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1RuleSet: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1SearchDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1SearchDocumentsResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1SetAclResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1SetAclResponse: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1SynonymSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1SynonymSet: ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1UpdateDocumentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContentwarehouseV1UpdateDocumentResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
