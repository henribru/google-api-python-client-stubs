import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleAppsDriveLabelsV2ListLabelLocksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAppsDriveLabelsV2ListLabelLocksResponseHttpRequest,
                previous_response: GoogleAppsDriveLabelsV2ListLabelLocksResponse,
            ) -> GoogleAppsDriveLabelsV2ListLabelLocksResponseHttpRequest | None: ...

        @typing.type_check_only
        class PermissionsResource(googleapiclient.discovery.Resource):
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequest,
                **kwargs: typing.Any,
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseHttpRequest
            ): ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAppsDriveLabelsV2LabelPermission,
                useAdminAccess: bool | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleAppsDriveLabelsV2LabelPermissionHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                useAdminAccess: bool | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                useAdminAccess: bool | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleAppsDriveLabelsV2ListLabelPermissionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAppsDriveLabelsV2ListLabelPermissionsResponseHttpRequest,
                previous_response: GoogleAppsDriveLabelsV2ListLabelPermissionsResponse,
            ) -> (
                GoogleAppsDriveLabelsV2ListLabelPermissionsResponseHttpRequest | None
            ): ...

        @typing.type_check_only
        class RevisionsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocksResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleAppsDriveLabelsV2ListLabelLocksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleAppsDriveLabelsV2ListLabelLocksResponseHttpRequest,
                    previous_response: GoogleAppsDriveLabelsV2ListLabelLocksResponse,
                ) -> (
                    GoogleAppsDriveLabelsV2ListLabelLocksResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class PermissionsResource(googleapiclient.discovery.Resource):
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAppsDriveLabelsV2LabelPermission,
                    useAdminAccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleAppsDriveLabelsV2LabelPermissionHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    useAdminAccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    useAdminAccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleAppsDriveLabelsV2ListLabelPermissionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleAppsDriveLabelsV2ListLabelPermissionsResponseHttpRequest,
                    previous_response: GoogleAppsDriveLabelsV2ListLabelPermissionsResponse,
                ) -> (
                    GoogleAppsDriveLabelsV2ListLabelPermissionsResponseHttpRequest
                    | None
                ): ...

            def updatePermissions(
                self,
                *,
                parent: str,
                body: GoogleAppsDriveLabelsV2LabelPermission,
                useAdminAccess: bool | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleAppsDriveLabelsV2LabelPermissionHttpRequest: ...
            def locks(self) -> LocksResource: ...
            def permissions(self) -> PermissionsResource: ...

        def create(
            self,
            *,
            body: GoogleAppsDriveLabelsV2Label,
            languageCode: str | None = ...,
            useAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def delete(
            self,
            *,
            name: str,
            useAdminAccess: bool | None = ...,
            writeControl_requiredRevisionId: str | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def delta(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2DeltaUpdateLabelRequest,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseHttpRequest: ...
        def disable(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2DisableLabelRequest,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def enable(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2EnableLabelRequest,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def get(
            self,
            *,
            name: str,
            languageCode: str | None = ...,
            useAdminAccess: bool | None = ...,
            view: typing_extensions.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def list(
            self,
            *,
            customer: str | None = ...,
            languageCode: str | None = ...,
            minimumRole: typing_extensions.Literal[
                "LABEL_ROLE_UNSPECIFIED", "READER", "APPLIER", "ORGANIZER", "EDITOR"
            ]
            | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            publishedOnly: bool | None = ...,
            useAdminAccess: bool | None = ...,
            view: typing_extensions.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest,
            previous_response: GoogleAppsDriveLabelsV2ListLabelsResponse,
        ) -> GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest | None: ...
        def publish(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2PublishLabelRequest,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def updateLabelCopyMode(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequest,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def updateLabelEnabledAppSettings(
            self,
            *,
            name: str,
            body: GoogleAppsDriveLabelsV2UpdateLabelEnabledAppSettingsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def updatePermissions(
            self,
            *,
            parent: str,
            body: GoogleAppsDriveLabelsV2LabelPermission,
            useAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleAppsDriveLabelsV2LabelPermissionHttpRequest: ...
        def locks(self) -> LocksResource: ...
        def permissions(self) -> PermissionsResource: ...
        def revisions(self) -> RevisionsResource: ...

    @typing.type_check_only
    class LimitsResource(googleapiclient.discovery.Resource):
        def getLabel(
            self, *, name: str | None = ..., **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2LabelLimitsHttpRequest: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def getCapabilities(
            self, *, name: str, customer: str | None = ..., **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2UserCapabilitiesHttpRequest: ...

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
    def labels(self) -> LabelsResource: ...
    def limits(self) -> LimitsResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2DeltaUpdateLabelResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2Label: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelLimitsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2LabelLimits: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelPermissionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2LabelPermission: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelLocksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2ListLabelLocksResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2ListLabelPermissionsResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2ListLabelsResponse: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserCapabilitiesHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsDriveLabelsV2UserCapabilities: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
