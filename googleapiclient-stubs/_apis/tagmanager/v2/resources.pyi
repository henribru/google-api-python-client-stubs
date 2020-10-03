import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class TagManagerResource(googleapiclient.discovery.Resource):
    class AccountsResource(googleapiclient.discovery.Resource):
        class User_permissionsResource(googleapiclient.discovery.Resource):
            def update(
                self, *, path: str, body: UserPermission = ..., **kwargs: typing.Any
            ) -> UserPermissionHttpRequest: ...
            def get(
                self, *, path: str, **kwargs: typing.Any
            ) -> UserPermissionHttpRequest: ...
            def delete(
                self, *, path: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
            ) -> ListUserPermissionsResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: UserPermission = ..., **kwargs: typing.Any
            ) -> UserPermissionHttpRequest: ...
        class ContainersResource(googleapiclient.discovery.Resource):
            class Version_headersResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    includeDeleted: bool = ...,
                    **kwargs: typing.Any
                ) -> ListContainerVersionsResponseHttpRequest: ...
                def latest(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> ContainerVersionHeaderHttpRequest: ...
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                def update(
                    self,
                    *,
                    path: str,
                    body: Environment = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def reauthorize(
                    self, *, path: str, body: Environment = ..., **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def create(
                    self, *, parent: str, body: Environment = ..., **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def get(
                    self, *, path: str, **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def delete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def list(
                    self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                ) -> ListEnvironmentsResponseHttpRequest: ...
            class WorkspacesResource(googleapiclient.discovery.Resource):
                class FoldersResource(googleapiclient.discovery.Resource):
                    def update(
                        self,
                        *,
                        path: str,
                        body: Folder = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> FolderHttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> FolderHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def create(
                        self, *, parent: str, body: Folder = ..., **kwargs: typing.Any
                    ) -> FolderHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertFolderResponseHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListFoldersResponseHttpRequest: ...
                    def move_entities_to_folder(
                        self,
                        *,
                        path: str,
                        body: Folder = ...,
                        variableId: typing.Union[str, typing.List[str]] = ...,
                        triggerId: typing.Union[str, typing.List[str]] = ...,
                        tagId: typing.Union[str, typing.List[str]] = ...,
                        **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def entities(
                        self, *, path: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> FolderEntitiesHttpRequest: ...
                class TriggersResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListTriggersResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Trigger = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> TriggerHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertTriggerResponseHttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> TriggerHttpRequest: ...
                    def create(
                        self, *, parent: str, body: Trigger = ..., **kwargs: typing.Any
                    ) -> TriggerHttpRequest: ...
                class TagsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertTagResponseHttpRequest: ...
                    def create(
                        self, *, parent: str, body: Tag = ..., **kwargs: typing.Any
                    ) -> TagHttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> TagHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Tag = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> TagHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListTagsResponseHttpRequest: ...
                class ZonesResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertZoneResponseHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListZonesResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Zone = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> ZoneHttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> ZoneHttpRequest: ...
                    def create(
                        self, *, parent: str, body: Zone = ..., **kwargs: typing.Any
                    ) -> ZoneHttpRequest: ...
                class TemplatesResource(googleapiclient.discovery.Resource):
                    def update(
                        self,
                        *,
                        path: str,
                        body: CustomTemplate = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> CustomTemplateHttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> CustomTemplateHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListTemplatesResponseHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertTemplateResponseHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CustomTemplate = ...,
                        **kwargs: typing.Any
                    ) -> CustomTemplateHttpRequest: ...
                class Built_in_variablesResource(googleapiclient.discovery.Resource):
                    def revert(
                        self,
                        *,
                        path: str,
                        type: typing_extensions.Literal[
                            "builtInVariableTypeUnspecified",
                            "pageUrl",
                            "pageHostname",
                            "pagePath",
                            "referrer",
                            "event",
                            "clickElement",
                            "clickClasses",
                            "clickId",
                            "clickTarget",
                            "clickUrl",
                            "clickText",
                            "firstPartyServingUrl",
                            "formElement",
                            "formClasses",
                            "formId",
                            "formTarget",
                            "formUrl",
                            "formText",
                            "errorMessage",
                            "errorUrl",
                            "errorLine",
                            "newHistoryUrl",
                            "oldHistoryUrl",
                            "newHistoryFragment",
                            "oldHistoryFragment",
                            "newHistoryState",
                            "oldHistoryState",
                            "historySource",
                            "containerVersion",
                            "debugMode",
                            "randomNumber",
                            "containerId",
                            "appId",
                            "appName",
                            "appVersionCode",
                            "appVersionName",
                            "language",
                            "osVersion",
                            "platform",
                            "sdkVersion",
                            "deviceName",
                            "resolution",
                            "advertiserId",
                            "advertisingTrackingEnabled",
                            "htmlId",
                            "environmentName",
                            "ampBrowserLanguage",
                            "ampCanonicalPath",
                            "ampCanonicalUrl",
                            "ampCanonicalHost",
                            "ampReferrer",
                            "ampTitle",
                            "ampClientId",
                            "ampClientTimezone",
                            "ampClientTimestamp",
                            "ampClientScreenWidth",
                            "ampClientScreenHeight",
                            "ampClientScrollX",
                            "ampClientScrollY",
                            "ampClientMaxScrollX",
                            "ampClientMaxScrollY",
                            "ampTotalEngagedTime",
                            "ampPageViewId",
                            "ampPageLoadTime",
                            "ampPageDownloadTime",
                            "ampGtmEvent",
                            "eventName",
                            "firebaseEventParameterCampaign",
                            "firebaseEventParameterCampaignAclid",
                            "firebaseEventParameterCampaignAnid",
                            "firebaseEventParameterCampaignClickTimestamp",
                            "firebaseEventParameterCampaignContent",
                            "firebaseEventParameterCampaignCp1",
                            "firebaseEventParameterCampaignGclid",
                            "firebaseEventParameterCampaignSource",
                            "firebaseEventParameterCampaignTerm",
                            "firebaseEventParameterCurrency",
                            "firebaseEventParameterDynamicLinkAcceptTime",
                            "firebaseEventParameterDynamicLinkLinkid",
                            "firebaseEventParameterNotificationMessageDeviceTime",
                            "firebaseEventParameterNotificationMessageId",
                            "firebaseEventParameterNotificationMessageName",
                            "firebaseEventParameterNotificationMessageTime",
                            "firebaseEventParameterNotificationTopic",
                            "firebaseEventParameterPreviousAppVersion",
                            "firebaseEventParameterPreviousOsVersion",
                            "firebaseEventParameterPrice",
                            "firebaseEventParameterProductId",
                            "firebaseEventParameterQuantity",
                            "firebaseEventParameterValue",
                            "videoProvider",
                            "videoUrl",
                            "videoTitle",
                            "videoDuration",
                            "videoPercent",
                            "videoVisible",
                            "videoStatus",
                            "videoCurrentTime",
                            "scrollDepthThreshold",
                            "scrollDepthUnits",
                            "scrollDepthDirection",
                            "elementVisibilityRatio",
                            "elementVisibilityTime",
                            "elementVisibilityFirstTime",
                            "elementVisibilityRecentTime",
                            "requestPath",
                            "requestMethod",
                            "clientName",
                            "queryString",
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> RevertBuiltInVariableResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        type: typing.Union[
                            typing_extensions.Literal[
                                "builtInVariableTypeUnspecified",
                                "pageUrl",
                                "pageHostname",
                                "pagePath",
                                "referrer",
                                "event",
                                "clickElement",
                                "clickClasses",
                                "clickId",
                                "clickTarget",
                                "clickUrl",
                                "clickText",
                                "firstPartyServingUrl",
                                "formElement",
                                "formClasses",
                                "formId",
                                "formTarget",
                                "formUrl",
                                "formText",
                                "errorMessage",
                                "errorUrl",
                                "errorLine",
                                "newHistoryUrl",
                                "oldHistoryUrl",
                                "newHistoryFragment",
                                "oldHistoryFragment",
                                "newHistoryState",
                                "oldHistoryState",
                                "historySource",
                                "containerVersion",
                                "debugMode",
                                "randomNumber",
                                "containerId",
                                "appId",
                                "appName",
                                "appVersionCode",
                                "appVersionName",
                                "language",
                                "osVersion",
                                "platform",
                                "sdkVersion",
                                "deviceName",
                                "resolution",
                                "advertiserId",
                                "advertisingTrackingEnabled",
                                "htmlId",
                                "environmentName",
                                "ampBrowserLanguage",
                                "ampCanonicalPath",
                                "ampCanonicalUrl",
                                "ampCanonicalHost",
                                "ampReferrer",
                                "ampTitle",
                                "ampClientId",
                                "ampClientTimezone",
                                "ampClientTimestamp",
                                "ampClientScreenWidth",
                                "ampClientScreenHeight",
                                "ampClientScrollX",
                                "ampClientScrollY",
                                "ampClientMaxScrollX",
                                "ampClientMaxScrollY",
                                "ampTotalEngagedTime",
                                "ampPageViewId",
                                "ampPageLoadTime",
                                "ampPageDownloadTime",
                                "ampGtmEvent",
                                "eventName",
                                "firebaseEventParameterCampaign",
                                "firebaseEventParameterCampaignAclid",
                                "firebaseEventParameterCampaignAnid",
                                "firebaseEventParameterCampaignClickTimestamp",
                                "firebaseEventParameterCampaignContent",
                                "firebaseEventParameterCampaignCp1",
                                "firebaseEventParameterCampaignGclid",
                                "firebaseEventParameterCampaignSource",
                                "firebaseEventParameterCampaignTerm",
                                "firebaseEventParameterCurrency",
                                "firebaseEventParameterDynamicLinkAcceptTime",
                                "firebaseEventParameterDynamicLinkLinkid",
                                "firebaseEventParameterNotificationMessageDeviceTime",
                                "firebaseEventParameterNotificationMessageId",
                                "firebaseEventParameterNotificationMessageName",
                                "firebaseEventParameterNotificationMessageTime",
                                "firebaseEventParameterNotificationTopic",
                                "firebaseEventParameterPreviousAppVersion",
                                "firebaseEventParameterPreviousOsVersion",
                                "firebaseEventParameterPrice",
                                "firebaseEventParameterProductId",
                                "firebaseEventParameterQuantity",
                                "firebaseEventParameterValue",
                                "videoProvider",
                                "videoUrl",
                                "videoTitle",
                                "videoDuration",
                                "videoPercent",
                                "videoVisible",
                                "videoStatus",
                                "videoCurrentTime",
                                "scrollDepthThreshold",
                                "scrollDepthUnits",
                                "scrollDepthDirection",
                                "elementVisibilityRatio",
                                "elementVisibilityTime",
                                "elementVisibilityFirstTime",
                                "elementVisibilityRecentTime",
                                "requestPath",
                                "requestMethod",
                                "clientName",
                                "queryString",
                            ],
                            typing.List[
                                typing_extensions.Literal[
                                    "builtInVariableTypeUnspecified",
                                    "pageUrl",
                                    "pageHostname",
                                    "pagePath",
                                    "referrer",
                                    "event",
                                    "clickElement",
                                    "clickClasses",
                                    "clickId",
                                    "clickTarget",
                                    "clickUrl",
                                    "clickText",
                                    "firstPartyServingUrl",
                                    "formElement",
                                    "formClasses",
                                    "formId",
                                    "formTarget",
                                    "formUrl",
                                    "formText",
                                    "errorMessage",
                                    "errorUrl",
                                    "errorLine",
                                    "newHistoryUrl",
                                    "oldHistoryUrl",
                                    "newHistoryFragment",
                                    "oldHistoryFragment",
                                    "newHistoryState",
                                    "oldHistoryState",
                                    "historySource",
                                    "containerVersion",
                                    "debugMode",
                                    "randomNumber",
                                    "containerId",
                                    "appId",
                                    "appName",
                                    "appVersionCode",
                                    "appVersionName",
                                    "language",
                                    "osVersion",
                                    "platform",
                                    "sdkVersion",
                                    "deviceName",
                                    "resolution",
                                    "advertiserId",
                                    "advertisingTrackingEnabled",
                                    "htmlId",
                                    "environmentName",
                                    "ampBrowserLanguage",
                                    "ampCanonicalPath",
                                    "ampCanonicalUrl",
                                    "ampCanonicalHost",
                                    "ampReferrer",
                                    "ampTitle",
                                    "ampClientId",
                                    "ampClientTimezone",
                                    "ampClientTimestamp",
                                    "ampClientScreenWidth",
                                    "ampClientScreenHeight",
                                    "ampClientScrollX",
                                    "ampClientScrollY",
                                    "ampClientMaxScrollX",
                                    "ampClientMaxScrollY",
                                    "ampTotalEngagedTime",
                                    "ampPageViewId",
                                    "ampPageLoadTime",
                                    "ampPageDownloadTime",
                                    "ampGtmEvent",
                                    "eventName",
                                    "firebaseEventParameterCampaign",
                                    "firebaseEventParameterCampaignAclid",
                                    "firebaseEventParameterCampaignAnid",
                                    "firebaseEventParameterCampaignClickTimestamp",
                                    "firebaseEventParameterCampaignContent",
                                    "firebaseEventParameterCampaignCp1",
                                    "firebaseEventParameterCampaignGclid",
                                    "firebaseEventParameterCampaignSource",
                                    "firebaseEventParameterCampaignTerm",
                                    "firebaseEventParameterCurrency",
                                    "firebaseEventParameterDynamicLinkAcceptTime",
                                    "firebaseEventParameterDynamicLinkLinkid",
                                    "firebaseEventParameterNotificationMessageDeviceTime",
                                    "firebaseEventParameterNotificationMessageId",
                                    "firebaseEventParameterNotificationMessageName",
                                    "firebaseEventParameterNotificationMessageTime",
                                    "firebaseEventParameterNotificationTopic",
                                    "firebaseEventParameterPreviousAppVersion",
                                    "firebaseEventParameterPreviousOsVersion",
                                    "firebaseEventParameterPrice",
                                    "firebaseEventParameterProductId",
                                    "firebaseEventParameterQuantity",
                                    "firebaseEventParameterValue",
                                    "videoProvider",
                                    "videoUrl",
                                    "videoTitle",
                                    "videoDuration",
                                    "videoPercent",
                                    "videoVisible",
                                    "videoStatus",
                                    "videoCurrentTime",
                                    "scrollDepthThreshold",
                                    "scrollDepthUnits",
                                    "scrollDepthDirection",
                                    "elementVisibilityRatio",
                                    "elementVisibilityTime",
                                    "elementVisibilityFirstTime",
                                    "elementVisibilityRecentTime",
                                    "requestPath",
                                    "requestMethod",
                                    "clientName",
                                    "queryString",
                                ]
                            ],
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> CreateBuiltInVariableResponseHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListEnabledBuiltInVariablesResponseHttpRequest: ...
                    def delete(
                        self,
                        *,
                        path: str,
                        type: typing.Union[
                            typing_extensions.Literal[
                                "builtInVariableTypeUnspecified",
                                "pageUrl",
                                "pageHostname",
                                "pagePath",
                                "referrer",
                                "event",
                                "clickElement",
                                "clickClasses",
                                "clickId",
                                "clickTarget",
                                "clickUrl",
                                "clickText",
                                "firstPartyServingUrl",
                                "formElement",
                                "formClasses",
                                "formId",
                                "formTarget",
                                "formUrl",
                                "formText",
                                "errorMessage",
                                "errorUrl",
                                "errorLine",
                                "newHistoryUrl",
                                "oldHistoryUrl",
                                "newHistoryFragment",
                                "oldHistoryFragment",
                                "newHistoryState",
                                "oldHistoryState",
                                "historySource",
                                "containerVersion",
                                "debugMode",
                                "randomNumber",
                                "containerId",
                                "appId",
                                "appName",
                                "appVersionCode",
                                "appVersionName",
                                "language",
                                "osVersion",
                                "platform",
                                "sdkVersion",
                                "deviceName",
                                "resolution",
                                "advertiserId",
                                "advertisingTrackingEnabled",
                                "htmlId",
                                "environmentName",
                                "ampBrowserLanguage",
                                "ampCanonicalPath",
                                "ampCanonicalUrl",
                                "ampCanonicalHost",
                                "ampReferrer",
                                "ampTitle",
                                "ampClientId",
                                "ampClientTimezone",
                                "ampClientTimestamp",
                                "ampClientScreenWidth",
                                "ampClientScreenHeight",
                                "ampClientScrollX",
                                "ampClientScrollY",
                                "ampClientMaxScrollX",
                                "ampClientMaxScrollY",
                                "ampTotalEngagedTime",
                                "ampPageViewId",
                                "ampPageLoadTime",
                                "ampPageDownloadTime",
                                "ampGtmEvent",
                                "eventName",
                                "firebaseEventParameterCampaign",
                                "firebaseEventParameterCampaignAclid",
                                "firebaseEventParameterCampaignAnid",
                                "firebaseEventParameterCampaignClickTimestamp",
                                "firebaseEventParameterCampaignContent",
                                "firebaseEventParameterCampaignCp1",
                                "firebaseEventParameterCampaignGclid",
                                "firebaseEventParameterCampaignSource",
                                "firebaseEventParameterCampaignTerm",
                                "firebaseEventParameterCurrency",
                                "firebaseEventParameterDynamicLinkAcceptTime",
                                "firebaseEventParameterDynamicLinkLinkid",
                                "firebaseEventParameterNotificationMessageDeviceTime",
                                "firebaseEventParameterNotificationMessageId",
                                "firebaseEventParameterNotificationMessageName",
                                "firebaseEventParameterNotificationMessageTime",
                                "firebaseEventParameterNotificationTopic",
                                "firebaseEventParameterPreviousAppVersion",
                                "firebaseEventParameterPreviousOsVersion",
                                "firebaseEventParameterPrice",
                                "firebaseEventParameterProductId",
                                "firebaseEventParameterQuantity",
                                "firebaseEventParameterValue",
                                "videoProvider",
                                "videoUrl",
                                "videoTitle",
                                "videoDuration",
                                "videoPercent",
                                "videoVisible",
                                "videoStatus",
                                "videoCurrentTime",
                                "scrollDepthThreshold",
                                "scrollDepthUnits",
                                "scrollDepthDirection",
                                "elementVisibilityRatio",
                                "elementVisibilityTime",
                                "elementVisibilityFirstTime",
                                "elementVisibilityRecentTime",
                                "requestPath",
                                "requestMethod",
                                "clientName",
                                "queryString",
                            ],
                            typing.List[
                                typing_extensions.Literal[
                                    "builtInVariableTypeUnspecified",
                                    "pageUrl",
                                    "pageHostname",
                                    "pagePath",
                                    "referrer",
                                    "event",
                                    "clickElement",
                                    "clickClasses",
                                    "clickId",
                                    "clickTarget",
                                    "clickUrl",
                                    "clickText",
                                    "firstPartyServingUrl",
                                    "formElement",
                                    "formClasses",
                                    "formId",
                                    "formTarget",
                                    "formUrl",
                                    "formText",
                                    "errorMessage",
                                    "errorUrl",
                                    "errorLine",
                                    "newHistoryUrl",
                                    "oldHistoryUrl",
                                    "newHistoryFragment",
                                    "oldHistoryFragment",
                                    "newHistoryState",
                                    "oldHistoryState",
                                    "historySource",
                                    "containerVersion",
                                    "debugMode",
                                    "randomNumber",
                                    "containerId",
                                    "appId",
                                    "appName",
                                    "appVersionCode",
                                    "appVersionName",
                                    "language",
                                    "osVersion",
                                    "platform",
                                    "sdkVersion",
                                    "deviceName",
                                    "resolution",
                                    "advertiserId",
                                    "advertisingTrackingEnabled",
                                    "htmlId",
                                    "environmentName",
                                    "ampBrowserLanguage",
                                    "ampCanonicalPath",
                                    "ampCanonicalUrl",
                                    "ampCanonicalHost",
                                    "ampReferrer",
                                    "ampTitle",
                                    "ampClientId",
                                    "ampClientTimezone",
                                    "ampClientTimestamp",
                                    "ampClientScreenWidth",
                                    "ampClientScreenHeight",
                                    "ampClientScrollX",
                                    "ampClientScrollY",
                                    "ampClientMaxScrollX",
                                    "ampClientMaxScrollY",
                                    "ampTotalEngagedTime",
                                    "ampPageViewId",
                                    "ampPageLoadTime",
                                    "ampPageDownloadTime",
                                    "ampGtmEvent",
                                    "eventName",
                                    "firebaseEventParameterCampaign",
                                    "firebaseEventParameterCampaignAclid",
                                    "firebaseEventParameterCampaignAnid",
                                    "firebaseEventParameterCampaignClickTimestamp",
                                    "firebaseEventParameterCampaignContent",
                                    "firebaseEventParameterCampaignCp1",
                                    "firebaseEventParameterCampaignGclid",
                                    "firebaseEventParameterCampaignSource",
                                    "firebaseEventParameterCampaignTerm",
                                    "firebaseEventParameterCurrency",
                                    "firebaseEventParameterDynamicLinkAcceptTime",
                                    "firebaseEventParameterDynamicLinkLinkid",
                                    "firebaseEventParameterNotificationMessageDeviceTime",
                                    "firebaseEventParameterNotificationMessageId",
                                    "firebaseEventParameterNotificationMessageName",
                                    "firebaseEventParameterNotificationMessageTime",
                                    "firebaseEventParameterNotificationTopic",
                                    "firebaseEventParameterPreviousAppVersion",
                                    "firebaseEventParameterPreviousOsVersion",
                                    "firebaseEventParameterPrice",
                                    "firebaseEventParameterProductId",
                                    "firebaseEventParameterQuantity",
                                    "firebaseEventParameterValue",
                                    "videoProvider",
                                    "videoUrl",
                                    "videoTitle",
                                    "videoDuration",
                                    "videoPercent",
                                    "videoVisible",
                                    "videoStatus",
                                    "videoCurrentTime",
                                    "scrollDepthThreshold",
                                    "scrollDepthUnits",
                                    "scrollDepthDirection",
                                    "elementVisibilityRatio",
                                    "elementVisibilityTime",
                                    "elementVisibilityFirstTime",
                                    "elementVisibilityRecentTime",
                                    "requestPath",
                                    "requestMethod",
                                    "clientName",
                                    "queryString",
                                ]
                            ],
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                class VariablesResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListVariablesResponseHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertVariableResponseHttpRequest: ...
                    def create(
                        self, *, parent: str, body: Variable = ..., **kwargs: typing.Any
                    ) -> VariableHttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> VariableHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Variable = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> VariableHttpRequest: ...
                def getStatus(
                    self, *, path: str, **kwargs: typing.Any
                ) -> GetWorkspaceStatusResponseHttpRequest: ...
                def quick_preview(
                    self, *, path: str, **kwargs: typing.Any
                ) -> QuickPreviewResponseHttpRequest: ...
                def delete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def resolve_conflict(
                    self,
                    *,
                    path: str,
                    body: Entity = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def create(
                    self, *, parent: str, body: Workspace = ..., **kwargs: typing.Any
                ) -> WorkspaceHttpRequest: ...
                def update(
                    self,
                    *,
                    path: str,
                    body: Workspace = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> WorkspaceHttpRequest: ...
                def create_version(
                    self,
                    *,
                    path: str,
                    body: CreateContainerVersionRequestVersionOptions = ...,
                    **kwargs: typing.Any
                ) -> CreateContainerVersionResponseHttpRequest: ...
                def sync(
                    self, *, path: str, **kwargs: typing.Any
                ) -> SyncWorkspaceResponseHttpRequest: ...
                def list(
                    self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                ) -> ListWorkspacesResponseHttpRequest: ...
                def get(
                    self, *, path: str, **kwargs: typing.Any
                ) -> WorkspaceHttpRequest: ...
                def folders(self) -> FoldersResource: ...
                def triggers(self) -> TriggersResource: ...
                def tags(self) -> TagsResource: ...
                def zones(self) -> ZonesResource: ...
                def templates(self) -> TemplatesResource: ...
                def built_in_variables(self) -> Built_in_variablesResource: ...
                def variables(self) -> VariablesResource: ...
            class VersionsResource(googleapiclient.discovery.Resource):
                def publish(
                    self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                ) -> PublishContainerVersionResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    path: str,
                    containerVersionId: str = ...,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def undelete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def delete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def set_latest(
                    self, *, path: str, **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def live(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def update(
                    self,
                    *,
                    path: str,
                    body: ContainerVersion = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
            def create(
                self, *, parent: str, body: Container = ..., **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def update(
                self,
                *,
                path: str,
                body: Container = ...,
                fingerprint: str = ...,
                **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def list(
                self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
            ) -> ListContainersResponseHttpRequest: ...
            def get(
                self, *, path: str, **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def delete(
                self, *, path: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def version_headers(self) -> Version_headersResource: ...
            def environments(self) -> EnvironmentsResource: ...
            def workspaces(self) -> WorkspacesResource: ...
            def versions(self) -> VersionsResource: ...
        def list(
            self, *, pageToken: str = ..., **kwargs: typing.Any
        ) -> ListAccountsResponseHttpRequest: ...
        def get(self, *, path: str, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def update(
            self,
            *,
            path: str,
            body: Account = ...,
            fingerprint: str = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def user_permissions(self) -> User_permissionsResource: ...
        def containers(self) -> ContainersResource: ...
    def accounts(self) -> AccountsResource: ...

class TriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Trigger: ...

class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListEnvironmentsResponse: ...

class RevertFolderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevertFolderResponse: ...

class RevertTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevertTemplateResponse: ...

class ListTemplatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTemplatesResponse: ...

class UserPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserPermission: ...

class ListZonesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListZonesResponse: ...

class RevertTriggerResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevertTriggerResponse: ...

class ZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Zone: ...

class VariableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Variable: ...

class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Environment: ...

class ListVariablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVariablesResponse: ...

class ListWorkspacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListWorkspacesResponse: ...

class QuickPreviewResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QuickPreviewResponse: ...

class ListTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTriggersResponse: ...

class ListContainerVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListContainerVersionsResponse: ...

class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Folder: ...

class ListTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTagsResponse: ...

class WorkspaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Workspace: ...

class CreateContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateContainerVersionResponse: ...

class RevertBuiltInVariableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevertBuiltInVariableResponse: ...

class RevertTagResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevertTagResponse: ...

class ListFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFoldersResponse: ...

class ContainerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Container: ...

class ListUserPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUserPermissionsResponse: ...

class RevertZoneResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevertZoneResponse: ...

class CustomTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomTemplate: ...

class RevertVariableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevertVariableResponse: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class SyncWorkspaceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SyncWorkspaceResponse: ...

class FolderEntitiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FolderEntities: ...

class PublishContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublishContainerVersionResponse: ...

class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAccountsResponse: ...

class TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Tag: ...

class CreateBuiltInVariableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateBuiltInVariableResponse: ...

class ContainerVersionHeaderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ContainerVersionHeader: ...

class ListContainersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListContainersResponse: ...

class ContainerVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ContainerVersion: ...

class GetWorkspaceStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetWorkspaceStatusResponse: ...

class ListEnabledBuiltInVariablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListEnabledBuiltInVariablesResponse: ...
