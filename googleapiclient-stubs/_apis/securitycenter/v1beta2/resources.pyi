import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> EventThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class RapidVulnerabilityDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...

        @typing.type_check_only
        class VirtualMachineThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> WebSecurityScannerSettingsHttpRequest: ...

        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getRapidVulnerabilityDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...
        def getSecurityCenterSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityCenterSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getVirtualMachineThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def updateContainerThreatDetectionSettings(
            self,
            *,
            name: str,
            body: ContainerThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def updateRapidVulnerabilityDetectionSettings(
            self,
            *,
            name: str,
            body: RapidVulnerabilityDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def updateVirtualMachineThreatDetectionSettings(
            self,
            *,
            name: str,
            body: VirtualMachineThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def rapidVulnerabilityDetectionSettings(
            self,
        ) -> RapidVulnerabilityDetectionSettingsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def virtualMachineThreatDetectionSettings(
            self,
        ) -> VirtualMachineThreatDetectionSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> EventThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class RapidVulnerabilityDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...

        @typing.type_check_only
        class VirtualMachineThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> WebSecurityScannerSettingsHttpRequest: ...

        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getRapidVulnerabilityDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...
        def getSecurityCenterSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityCenterSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getSubscription(
            self, *, name: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def getVirtualMachineThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def updateContainerThreatDetectionSettings(
            self,
            *,
            name: str,
            body: ContainerThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def updateRapidVulnerabilityDetectionSettings(
            self,
            *,
            name: str,
            body: RapidVulnerabilityDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def updateVirtualMachineThreatDetectionSettings(
            self,
            *,
            name: str,
            body: VirtualMachineThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def rapidVulnerabilityDetectionSettings(
            self,
        ) -> RapidVulnerabilityDetectionSettingsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def virtualMachineThreatDetectionSettings(
            self,
        ) -> VirtualMachineThreatDetectionSettingsResource: ...
        def webSecurityScannerSettings(self) -> WebSecurityScannerSettingsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContainerThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> ContainerThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
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
                        self,
                        *,
                        name: str,
                        showEligibleModulesOnly: bool = ...,
                        **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> ContainerThreatDetectionSettingsHttpRequest: ...
                def containerThreatDetectionSettings(
                    self,
                ) -> ContainerThreatDetectionSettingsResource: ...

            def clusters(self) -> ClustersResource: ...

        @typing.type_check_only
        class RapidVulnerabilityDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self, *, name: str, **kwargs: typing.Any
            ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...

        @typing.type_check_only
        class VirtualMachineThreatDetectionSettingsResource(
            googleapiclient.discovery.Resource
        ):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...

        @typing.type_check_only
        class WebSecurityScannerSettingsResource(googleapiclient.discovery.Resource):
            def calculate(
                self,
                *,
                name: str,
                showEligibleModulesOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> WebSecurityScannerSettingsHttpRequest: ...

        def getContainerThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def getEventThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def getRapidVulnerabilityDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...
        def getSecurityCenterSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityCenterSettingsHttpRequest: ...
        def getSecurityHealthAnalyticsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def getVirtualMachineThreatDetectionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...
        def getWebSecurityScannerSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def updateContainerThreatDetectionSettings(
            self,
            *,
            name: str,
            body: ContainerThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> ContainerThreatDetectionSettingsHttpRequest: ...
        def updateEventThreatDetectionSettings(
            self,
            *,
            name: str,
            body: EventThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> EventThreatDetectionSettingsHttpRequest: ...
        def updateRapidVulnerabilityDetectionSettings(
            self,
            *,
            name: str,
            body: RapidVulnerabilityDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> RapidVulnerabilityDetectionSettingsHttpRequest: ...
        def updateSecurityHealthAnalyticsSettings(
            self,
            *,
            name: str,
            body: SecurityHealthAnalyticsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SecurityHealthAnalyticsSettingsHttpRequest: ...
        def updateVirtualMachineThreatDetectionSettings(
            self,
            *,
            name: str,
            body: VirtualMachineThreatDetectionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> VirtualMachineThreatDetectionSettingsHttpRequest: ...
        def updateWebSecurityScannerSettings(
            self,
            *,
            name: str,
            body: WebSecurityScannerSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> WebSecurityScannerSettingsHttpRequest: ...
        def containerThreatDetectionSettings(
            self,
        ) -> ContainerThreatDetectionSettingsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def locations(self) -> LocationsResource: ...
        def rapidVulnerabilityDetectionSettings(
            self,
        ) -> RapidVulnerabilityDetectionSettingsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def virtualMachineThreatDetectionSettings(
            self,
        ) -> VirtualMachineThreatDetectionSettingsResource: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ContainerThreatDetectionSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ContainerThreatDetectionSettings: ...

@typing.type_check_only
class EventThreatDetectionSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventThreatDetectionSettings: ...

@typing.type_check_only
class RapidVulnerabilityDetectionSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RapidVulnerabilityDetectionSettings: ...

@typing.type_check_only
class SecurityCenterSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SecurityCenterSettings: ...

@typing.type_check_only
class SecurityHealthAnalyticsSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SecurityHealthAnalyticsSettings: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subscription: ...

@typing.type_check_only
class VirtualMachineThreatDetectionSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VirtualMachineThreatDetectionSettings: ...

@typing.type_check_only
class WebSecurityScannerSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WebSecurityScannerSettings: ...
