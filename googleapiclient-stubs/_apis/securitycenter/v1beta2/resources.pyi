import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SecurityCommandCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> EventThreatDetectionSettingsHttpRequest: ...
        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        @typing.type_check_only
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebSecurityScannerSettingsHttpRequest: ...
        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def updateContainerThreatDetectionSettings(
            self,
            *,
            name: str,
            body: ContainerThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> EventThreatDetectionSettingsHttpRequest: ...
        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        @typing.type_check_only
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebSecurityScannerSettingsHttpRequest: ...
        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getSecurityCenterSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityCenterSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getSubscription(
            self, *, name: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def updateContainerThreatDetectionSettings(
            self,
            *,
            name: str,
            body: ContainerThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> EventThreatDetectionSettingsHttpRequest: ...
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ContainerThreatDetectionSettingsResource(
                    googleapiclient.discovery.Resource
                ):
                    def calculate(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ContainerThreatDetectionSettingsHttpRequest: ...
                def getContainerThreatDetectionSettings(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ContainerThreatDetectionSettingsHttpRequest: ...
                def updateContainerThreatDetectionSettings(
                    self,
                    *,
                    name: str,
                    body: ContainerThreatDetectionSettings = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ContainerThreatDetectionSettingsHttpRequest: ...
                def containerThreatDetectionSettings(
                    self,
                ) -> ContainerThreatDetectionSettingsResource: ...
            def clusters(self) -> ClustersResource: ...
        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        @typing.type_check_only
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebSecurityScannerSettingsHttpRequest: ...
        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def updateContainerThreatDetectionSettings(
            self,
            *,
            name: str,
            body: ContainerThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def locations(self) -> LocationsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...
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
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ContainerThreatDetectionSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ContainerThreatDetectionSettings: ...

@typing.type_check_only
class EventThreatDetectionSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EventThreatDetectionSettings: ...

@typing.type_check_only
class SecurityCenterSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityCenterSettings: ...

@typing.type_check_only
class SecurityHealthAnalyticsSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityHealthAnalyticsSettings: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Subscription: ...

@typing.type_check_only
class WebSecurityScannerSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WebSecurityScannerSettings: ...
