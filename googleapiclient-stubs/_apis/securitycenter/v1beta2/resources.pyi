import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SecurityCommandCenterResource(googleapiclient.discovery.Resource):
    class FoldersResource(googleapiclient.discovery.Resource):
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> EventThreatDetectionSettingsHttpRequest: ...
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebSecurityScannerSettingsHttpRequest: ...
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...
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
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> EventThreatDetectionSettingsHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class ClustersResource(googleapiclient.discovery.Resource):
                class ContainerThreatDetectionSettingsResource(
                    googleapiclient.discovery.Resource
                ):
                    def calculate(
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
                def getContainerThreatDetectionSettings(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ContainerThreatDetectionSettingsHttpRequest: ...
                def containerThreatDetectionSettings(
                    self,
                ) -> ContainerThreatDetectionSettingsResource: ...
            def clusters(self) -> ClustersResource: ...
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebSecurityScannerSettingsHttpRequest: ...
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
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
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def locations(self) -> LocationsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> WebSecurityScannerSettingsHttpRequest: ...
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> EventThreatDetectionSettingsHttpRequest: ...
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getSubscription(
            self, *, name: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def updateContainerThreatDetectionSettings(
            self,
            *,
            name: str,
            body: ContainerThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getSecurityCenterSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityCenterSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
    def folders(self) -> FoldersResource: ...
    def projects(self) -> ProjectsResource: ...
    def organizations(self) -> OrganizationsResource: ...

class SecurityHealthAnalyticsSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityHealthAnalyticsSettings: ...

class ContainerThreatDetectionSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ContainerThreatDetectionSettings: ...

class SecurityCenterSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityCenterSettings: ...

class WebSecurityScannerSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WebSecurityScannerSettings: ...

class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subscription: ...

class EventThreatDetectionSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EventThreatDetectionSettings: ...
