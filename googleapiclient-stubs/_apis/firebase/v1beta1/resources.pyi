import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AvailableProjectsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListAvailableProjectsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAvailableProjectsResponseHttpRequest,
            previous_response: ListAvailableProjectsResponse,
        ) -> ListAvailableProjectsResponseHttpRequest | None: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AndroidAppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ShaResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ShaCertificate = ...,
                    **kwargs: typing.Any
                ) -> ShaCertificateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> ListShaCertificatesResponseHttpRequest: ...

            def create(
                self, *, parent: str, body: AndroidApp = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AndroidAppHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> AndroidAppConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                **kwargs: typing.Any
            ) -> ListAndroidAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAndroidAppsResponseHttpRequest,
                previous_response: ListAndroidAppsResponse,
            ) -> ListAndroidAppsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: AndroidApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AndroidAppHttpRequest: ...
            def remove(
                self,
                *,
                name: str,
                body: RemoveAndroidAppRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteAndroidAppRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def sha(self) -> ShaResource: ...

        @typing.type_check_only
        class AvailableLocationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAvailableLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAvailableLocationsResponseHttpRequest,
                previous_response: ListAvailableLocationsResponse,
            ) -> ListAvailableLocationsResponseHttpRequest | None: ...

        @typing.type_check_only
        class DefaultLocationResource(googleapiclient.discovery.Resource):
            def finalize(
                self,
                *,
                parent: str,
                body: FinalizeDefaultLocationRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class IosAppsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: IosApp = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> IosAppHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> IosAppConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                **kwargs: typing.Any
            ) -> ListIosAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListIosAppsResponseHttpRequest,
                previous_response: ListIosAppsResponse,
            ) -> ListIosAppsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: IosApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> IosAppHttpRequest: ...
            def remove(
                self,
                *,
                name: str,
                body: RemoveIosAppRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteIosAppRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class WebAppsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: WebApp = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> WebAppHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebAppConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                **kwargs: typing.Any
            ) -> ListWebAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListWebAppsResponseHttpRequest,
                previous_response: ListWebAppsResponse,
            ) -> ListWebAppsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: WebApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> WebAppHttpRequest: ...
            def remove(
                self,
                *,
                name: str,
                body: RemoveWebAppRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteWebAppRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def addFirebase(
            self, *, project: str, body: AddFirebaseRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addGoogleAnalytics(
            self,
            *,
            parent: str,
            body: AddGoogleAnalyticsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> FirebaseProjectHttpRequest: ...
        def getAdminSdkConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> AdminSdkConfigHttpRequest: ...
        def getAnalyticsDetails(
            self, *, name: str, **kwargs: typing.Any
        ) -> AnalyticsDetailsHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> ListFirebaseProjectsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListFirebaseProjectsResponseHttpRequest,
            previous_response: ListFirebaseProjectsResponse,
        ) -> ListFirebaseProjectsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: FirebaseProject = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> FirebaseProjectHttpRequest: ...
        def removeAnalytics(
            self,
            *,
            parent: str,
            body: RemoveAnalyticsRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def searchApps(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> SearchFirebaseAppsResponseHttpRequest: ...
        def searchApps_next(
            self,
            previous_request: SearchFirebaseAppsResponseHttpRequest,
            previous_response: SearchFirebaseAppsResponse,
        ) -> SearchFirebaseAppsResponseHttpRequest | None: ...
        def androidApps(self) -> AndroidAppsResource: ...
        def availableLocations(self) -> AvailableLocationsResource: ...
        def defaultLocation(self) -> DefaultLocationResource: ...
        def iosApps(self) -> IosAppsResource: ...
        def webApps(self) -> WebAppsResource: ...

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
    def availableProjects(self) -> AvailableProjectsResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AdminSdkConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdminSdkConfig: ...

@typing.type_check_only
class AnalyticsDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnalyticsDetails: ...

@typing.type_check_only
class AndroidAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AndroidApp: ...

@typing.type_check_only
class AndroidAppConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AndroidAppConfig: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FirebaseProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FirebaseProject: ...

@typing.type_check_only
class IosAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IosApp: ...

@typing.type_check_only
class IosAppConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IosAppConfig: ...

@typing.type_check_only
class ListAndroidAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAndroidAppsResponse: ...

@typing.type_check_only
class ListAvailableLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAvailableLocationsResponse: ...

@typing.type_check_only
class ListAvailableProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAvailableProjectsResponse: ...

@typing.type_check_only
class ListFirebaseProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListFirebaseProjectsResponse: ...

@typing.type_check_only
class ListIosAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListIosAppsResponse: ...

@typing.type_check_only
class ListShaCertificatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListShaCertificatesResponse: ...

@typing.type_check_only
class ListWebAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListWebAppsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class SearchFirebaseAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchFirebaseAppsResponse: ...

@typing.type_check_only
class ShaCertificateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShaCertificate: ...

@typing.type_check_only
class WebAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WebApp: ...

@typing.type_check_only
class WebAppConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WebAppConfig: ...
