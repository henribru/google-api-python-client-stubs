import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DriveLabelsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LabelsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocksResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAppsDriveLabelsV2betaListLabelLocksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAppsDriveLabelsV2betaListLabelLocksResponseHttpRequest,
                previous_response: GoogleAppsDriveLabelsV2betaListLabelLocksResponse,
            ) -> GoogleAppsDriveLabelsV2betaListLabelLocksResponseHttpRequest | None: ...

        @typing.type_check_only
        class PermissionsResource(googleapiclient.discovery.Resource):
            def batchDelete(
                self,
                *,
                labelsId: str,
                body: GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAppsDriveLabelsV2betaLabelPermission = ...,
                useAdminAccess: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleAppsDriveLabelsV2betaLabelPermissionHttpRequest: ...
            def delete(
                self, *, name: str, useAdminAccess: bool = ..., **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                useAdminAccess: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleAppsDriveLabelsV2betaListLabelPermissionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAppsDriveLabelsV2betaListLabelPermissionsResponseHttpRequest,
                previous_response: GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse,
            ) -> GoogleAppsDriveLabelsV2betaListLabelPermissionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                parent: str,
                body: GoogleAppsDriveLabelsV2betaLabelPermission = ...,
                useAdminAccess: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleAppsDriveLabelsV2betaLabelPermissionHttpRequest: ...

        @typing.type_check_only
        class RevisionsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocksResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAppsDriveLabelsV2betaListLabelLocksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleAppsDriveLabelsV2betaListLabelLocksResponseHttpRequest,
                    previous_response: GoogleAppsDriveLabelsV2betaListLabelLocksResponse,
                ) -> GoogleAppsDriveLabelsV2betaListLabelLocksResponseHttpRequest | None: ...

            @typing.type_check_only
            class PermissionsResource(googleapiclient.discovery.Resource):
                def batchDelete(
                    self,
                    *,
                    labelsId: str,
                    revisionsId: str,
                    body: GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAppsDriveLabelsV2betaLabelPermission = ...,
                    useAdminAccess: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleAppsDriveLabelsV2betaLabelPermissionHttpRequest: ...
                def delete(
                    self, *, name: str, useAdminAccess: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    useAdminAccess: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleAppsDriveLabelsV2betaListLabelPermissionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleAppsDriveLabelsV2betaListLabelPermissionsResponseHttpRequest,
                    previous_response: GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse,
                ) -> GoogleAppsDriveLabelsV2betaListLabelPermissionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    parent: str,
                    body: GoogleAppsDriveLabelsV2betaLabelPermission = ...,
                    useAdminAccess: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleAppsDriveLabelsV2betaLabelPermissionHttpRequest: ...

            def locks(self) -> LocksResource: ...
            def permissions(self) -> PermissionsResource: ...

        def create(
            self,
            *,
            body: GoogleAppsDriveLabelsV2betaLabel = ...,
            languageCode: str = ...,
            useAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaLabelHttpRequest: ...
        def delete(
            self,
            *,
            name: str,
            useAdminAccess: bool = ...,
            writeControl_requiredRevisionId: str = ...,
            **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def delta(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseHttpRequest: ...
        def disable(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2betaDisableLabelRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaLabelHttpRequest: ...
        def enable(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2betaEnableLabelRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaLabelHttpRequest: ...
        def get(
            self,
            *,
            name: str,
            languageCode: str = ...,
            useAdminAccess: bool = ...,
            view: typing_extensions.Literal[
                "LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaLabelHttpRequest: ...
        def list(
            self,
            *,
            languageCode: str = ...,
            minimumRole: typing_extensions.Literal[
                "LABEL_ROLE_UNSPECIFIED", "READER", "APPLIER", "ORGANIZER", "EDITOR"
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            publishedOnly: bool = ...,
            useAdminAccess: bool = ...,
            view: typing_extensions.Literal[
                "LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaListLabelsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAppsDriveLabelsV2betaListLabelsResponseHttpRequest,
            previous_response: GoogleAppsDriveLabelsV2betaListLabelsResponse,
        ) -> GoogleAppsDriveLabelsV2betaListLabelsResponseHttpRequest | None: ...
        def publish(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2betaPublishLabelRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaLabelHttpRequest: ...
        def updateLabelCopyMode(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaLabelHttpRequest: ...
        def locks(self) -> LocksResource: ...
        def permissions(self) -> PermissionsResource: ...
        def revisions(self) -> RevisionsResource: ...

    @typing.type_check_only
    class LimitsResource(googleapiclient.discovery.Resource):
        def getLabel(
            self, *, name: str = ..., **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaLabelLimitsHttpRequest: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def getCapabilities(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2betaUserCapabilitiesHttpRequest: ...

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
    def labels(self) -> LabelsResource: ...
    def limits(self) -> LimitsResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaLabel: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelLimitsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaLabelLimits: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelPermissionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaLabelPermission: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaListLabelLocksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaListLabelLocksResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaListLabelPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaListLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaListLabelsResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaUserCapabilitiesHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2betaUserCapabilities: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
