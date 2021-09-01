import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class ResourceSettingsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SettingsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "SETTING_VIEW_UNSPECIFIED",
                    "SETTING_VIEW_BASIC",
                    "SETTING_VIEW_EFFECTIVE_VALUE",
                    "SETTING_VIEW_LOCAL_VALUE",
                ] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1SettingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "SETTING_VIEW_UNSPECIFIED",
                    "SETTING_VIEW_BASIC",
                    "SETTING_VIEW_EFFECTIVE_VALUE",
                    "SETTING_VIEW_LOCAL_VALUE",
                ] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1ListSettingsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudResourcesettingsV1Setting = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1SettingHttpRequest: ...
        def settings(self) -> SettingsResource: ...
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SettingsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "SETTING_VIEW_UNSPECIFIED",
                    "SETTING_VIEW_BASIC",
                    "SETTING_VIEW_EFFECTIVE_VALUE",
                    "SETTING_VIEW_LOCAL_VALUE",
                ] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1SettingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "SETTING_VIEW_UNSPECIFIED",
                    "SETTING_VIEW_BASIC",
                    "SETTING_VIEW_EFFECTIVE_VALUE",
                    "SETTING_VIEW_LOCAL_VALUE",
                ] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1ListSettingsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudResourcesettingsV1Setting = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1SettingHttpRequest: ...
        def settings(self) -> SettingsResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SettingsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "SETTING_VIEW_UNSPECIFIED",
                    "SETTING_VIEW_BASIC",
                    "SETTING_VIEW_EFFECTIVE_VALUE",
                    "SETTING_VIEW_LOCAL_VALUE",
                ] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1SettingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "SETTING_VIEW_UNSPECIFIED",
                    "SETTING_VIEW_BASIC",
                    "SETTING_VIEW_EFFECTIVE_VALUE",
                    "SETTING_VIEW_LOCAL_VALUE",
                ] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1ListSettingsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudResourcesettingsV1Setting = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudResourcesettingsV1SettingHttpRequest: ...
        def settings(self) -> SettingsResource: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudResourcesettingsV1ListSettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudResourcesettingsV1ListSettingsResponse: ...

@typing.type_check_only
class GoogleCloudResourcesettingsV1SettingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudResourcesettingsV1Setting: ...
