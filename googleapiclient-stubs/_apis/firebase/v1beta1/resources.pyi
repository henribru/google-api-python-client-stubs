import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class FirebaseManagementResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class WebAppsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListWebAppsResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> WebAppHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebAppConfigHttpRequest: ...
            def create(
                self, *, parent: str, body: WebApp = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: WebApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> WebAppHttpRequest: ...
        class IosAppsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: IosApp = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> IosAppConfigHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> IosAppHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListIosAppsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: IosApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> IosAppHttpRequest: ...
        class DefaultLocationResource(googleapiclient.discovery.Resource):
            def finalize(
                self,
                *,
                parent: str,
                body: FinalizeDefaultLocationRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class AvailableLocationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAvailableLocationsResponseHttpRequest: ...
        class AndroidAppsResource(googleapiclient.discovery.Resource):
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
            def patch(
                self,
                *,
                name: str,
                body: AndroidApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AndroidAppHttpRequest: ...
            def create(
                self, *, parent: str, body: AndroidApp = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAndroidAppsResponseHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> AndroidAppConfigHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AndroidAppHttpRequest: ...
            def sha(self) -> ShaResource: ...
        def addFirebase(
            self, *, project: str, body: AddFirebaseRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: FirebaseProject = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> FirebaseProjectHttpRequest: ...
        def addGoogleAnalytics(
            self,
            *,
            parent: str,
            body: AddGoogleAnalyticsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def getAdminSdkConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> AdminSdkConfigHttpRequest: ...
        def getAnalyticsDetails(
            self, *, name: str, **kwargs: typing.Any
        ) -> AnalyticsDetailsHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListFirebaseProjectsResponseHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> SearchFirebaseAppsResponseHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> FirebaseProjectHttpRequest: ...
        def webApps(self) -> WebAppsResource: ...
        def iosApps(self) -> IosAppsResource: ...
        def defaultLocation(self) -> DefaultLocationResource: ...
        def availableLocations(self) -> AvailableLocationsResource: ...
        def androidApps(self) -> AndroidAppsResource: ...
    class AvailableProjectsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListAvailableProjectsResponseHttpRequest: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def availableProjects(self) -> AvailableProjectsResource: ...
    def operations(self) -> OperationsResource: ...

class AnalyticsDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AnalyticsDetails: ...

class WebAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WebApp: ...

class ListShaCertificatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListShaCertificatesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListWebAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListWebAppsResponse: ...

class AndroidAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AndroidApp: ...

class ListAvailableProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAvailableProjectsResponse: ...

class AdminSdkConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdminSdkConfig: ...

class WebAppConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WebAppConfig: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class AndroidAppConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AndroidAppConfig: ...

class IosAppConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IosAppConfig: ...

class ListFirebaseProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFirebaseProjectsResponse: ...

class ShaCertificateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShaCertificate: ...

class ListIosAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListIosAppsResponse: ...

class SearchFirebaseAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchFirebaseAppsResponse: ...

class FirebaseProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirebaseProject: ...

class ListAvailableLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAvailableLocationsResponse: ...

class ListAndroidAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAndroidAppsResponse: ...

class IosAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IosApp: ...
