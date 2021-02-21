import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class TagManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContainersResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Environment = ..., **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def delete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self, *, path: str, **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def list(
                    self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                ) -> ListEnvironmentsResponseHttpRequest: ...
                def reauthorize(
                    self, *, path: str, body: Environment = ..., **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def update(
                    self,
                    *,
                    path: str,
                    body: Environment = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
            @typing.type_check_only
            class Version_headersResource(googleapiclient.discovery.Resource):
                def latest(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> ContainerVersionHeaderHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    includeDeleted: bool = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListContainerVersionsResponseHttpRequest: ...
            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    path: str,
                    containerVersionId: str = ...,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def live(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def publish(
                    self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                ) -> PublishContainerVersionResponseHttpRequest: ...
                def set_latest(
                    self, *, path: str, **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def undelete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def update(
                    self,
                    *,
                    path: str,
                    body: ContainerVersion = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
            @typing.type_check_only
            class WorkspacesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class Built_in_variablesResource(googleapiclient.discovery.Resource):
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
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListEnabledBuiltInVariablesResponseHttpRequest: ...
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
                @typing.type_check_only
                class FoldersResource(googleapiclient.discovery.Resource):
                    def create(
                        self, *, parent: str, body: Folder = ..., **kwargs: typing.Any
                    ) -> FolderHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def entities(
                        self, *, path: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> FolderEntitiesHttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> FolderHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListFoldersResponseHttpRequest: ...
                    def move_entities_to_folder(
                        self,
                        *,
                        path: str,
                        body: Folder = ...,
                        tagId: typing.Union[str, typing.List[str]] = ...,
                        triggerId: typing.Union[str, typing.List[str]] = ...,
                        variableId: typing.Union[str, typing.List[str]] = ...,
                        **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertFolderResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Folder = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> FolderHttpRequest: ...
                @typing.type_check_only
                class TagsResource(googleapiclient.discovery.Resource):
                    def create(
                        self, *, parent: str, body: Tag = ..., **kwargs: typing.Any
                    ) -> TagHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> TagHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListTagsResponseHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertTagResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Tag = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> TagHttpRequest: ...
                @typing.type_check_only
                class TemplatesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CustomTemplate = ...,
                        **kwargs: typing.Any
                    ) -> CustomTemplateHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> CustomTemplateHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListTemplatesResponseHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertTemplateResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: CustomTemplate = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> CustomTemplateHttpRequest: ...
                @typing.type_check_only
                class TriggersResource(googleapiclient.discovery.Resource):
                    def create(
                        self, *, parent: str, body: Trigger = ..., **kwargs: typing.Any
                    ) -> TriggerHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> TriggerHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListTriggersResponseHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertTriggerResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Trigger = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> TriggerHttpRequest: ...
                @typing.type_check_only
                class VariablesResource(googleapiclient.discovery.Resource):
                    def create(
                        self, *, parent: str, body: Variable = ..., **kwargs: typing.Any
                    ) -> VariableHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> VariableHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListVariablesResponseHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertVariableResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Variable = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> VariableHttpRequest: ...
                @typing.type_check_only
                class ZonesResource(googleapiclient.discovery.Resource):
                    def create(
                        self, *, parent: str, body: Zone = ..., **kwargs: typing.Any
                    ) -> ZoneHttpRequest: ...
                    def delete(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self, *, path: str, **kwargs: typing.Any
                    ) -> ZoneHttpRequest: ...
                    def list(
                        self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                    ) -> ListZonesResponseHttpRequest: ...
                    def revert(
                        self, *, path: str, fingerprint: str = ..., **kwargs: typing.Any
                    ) -> RevertZoneResponseHttpRequest: ...
                    def update(
                        self,
                        *,
                        path: str,
                        body: Zone = ...,
                        fingerprint: str = ...,
                        **kwargs: typing.Any
                    ) -> ZoneHttpRequest: ...
                def create(
                    self, *, parent: str, body: Workspace = ..., **kwargs: typing.Any
                ) -> WorkspaceHttpRequest: ...
                def create_version(
                    self,
                    *,
                    path: str,
                    body: CreateContainerVersionRequestVersionOptions = ...,
                    **kwargs: typing.Any
                ) -> CreateContainerVersionResponseHttpRequest: ...
                def delete(
                    self, *, path: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self, *, path: str, **kwargs: typing.Any
                ) -> WorkspaceHttpRequest: ...
                def getStatus(
                    self, *, path: str, **kwargs: typing.Any
                ) -> GetWorkspaceStatusResponseHttpRequest: ...
                def list(
                    self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                ) -> ListWorkspacesResponseHttpRequest: ...
                def quick_preview(
                    self, *, path: str, **kwargs: typing.Any
                ) -> QuickPreviewResponseHttpRequest: ...
                def resolve_conflict(
                    self,
                    *,
                    path: str,
                    body: Entity = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def sync(
                    self, *, path: str, **kwargs: typing.Any
                ) -> SyncWorkspaceResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    path: str,
                    body: Workspace = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> WorkspaceHttpRequest: ...
                def built_in_variables(self) -> Built_in_variablesResource: ...
                def folders(self) -> FoldersResource: ...
                def tags(self) -> TagsResource: ...
                def templates(self) -> TemplatesResource: ...
                def triggers(self) -> TriggersResource: ...
                def variables(self) -> VariablesResource: ...
                def zones(self) -> ZonesResource: ...
            def create(
                self, *, parent: str, body: Container = ..., **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def delete(
                self, *, path: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, path: str, **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def list(
                self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
            ) -> ListContainersResponseHttpRequest: ...
            def update(
                self,
                *,
                path: str,
                body: Container = ...,
                fingerprint: str = ...,
                **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def environments(self) -> EnvironmentsResource: ...
            def version_headers(self) -> Version_headersResource: ...
            def versions(self) -> VersionsResource: ...
            def workspaces(self) -> WorkspacesResource: ...
        @typing.type_check_only
        class User_permissionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: UserPermission = ..., **kwargs: typing.Any
            ) -> UserPermissionHttpRequest: ...
            def delete(
                self, *, path: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, path: str, **kwargs: typing.Any
            ) -> UserPermissionHttpRequest: ...
            def list(
                self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
            ) -> ListUserPermissionsResponseHttpRequest: ...
            def update(
                self, *, path: str, body: UserPermission = ..., **kwargs: typing.Any
            ) -> UserPermissionHttpRequest: ...
        def get(self, *, path: str, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def list(
            self, *, pageToken: str = ..., **kwargs: typing.Any
        ) -> ListAccountsResponseHttpRequest: ...
        def update(
            self,
            *,
            path: str,
            body: Account = ...,
            fingerprint: str = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def containers(self) -> ContainersResource: ...
        def user_permissions(self) -> User_permissionsResource: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class ContainerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Container: ...

@typing.type_check_only
class ContainerVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ContainerVersion: ...

@typing.type_check_only
class ContainerVersionHeaderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ContainerVersionHeader: ...

@typing.type_check_only
class CreateBuiltInVariableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CreateBuiltInVariableResponse: ...

@typing.type_check_only
class CreateContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CreateContainerVersionResponse: ...

@typing.type_check_only
class CustomTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CustomTemplate: ...

@typing.type_check_only
class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Environment: ...

@typing.type_check_only
class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Folder: ...

@typing.type_check_only
class FolderEntitiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> FolderEntities: ...

@typing.type_check_only
class GetWorkspaceStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetWorkspaceStatusResponse: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListContainerVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListContainerVersionsResponse: ...

@typing.type_check_only
class ListContainersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListContainersResponse: ...

@typing.type_check_only
class ListEnabledBuiltInVariablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListEnabledBuiltInVariablesResponse: ...

@typing.type_check_only
class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListEnvironmentsResponse: ...

@typing.type_check_only
class ListFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListFoldersResponse: ...

@typing.type_check_only
class ListTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTagsResponse: ...

@typing.type_check_only
class ListTemplatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTemplatesResponse: ...

@typing.type_check_only
class ListTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTriggersResponse: ...

@typing.type_check_only
class ListUserPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListUserPermissionsResponse: ...

@typing.type_check_only
class ListVariablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListVariablesResponse: ...

@typing.type_check_only
class ListWorkspacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListWorkspacesResponse: ...

@typing.type_check_only
class ListZonesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListZonesResponse: ...

@typing.type_check_only
class PublishContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PublishContainerVersionResponse: ...

@typing.type_check_only
class QuickPreviewResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> QuickPreviewResponse: ...

@typing.type_check_only
class RevertBuiltInVariableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RevertBuiltInVariableResponse: ...

@typing.type_check_only
class RevertFolderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RevertFolderResponse: ...

@typing.type_check_only
class RevertTagResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RevertTagResponse: ...

@typing.type_check_only
class RevertTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RevertTemplateResponse: ...

@typing.type_check_only
class RevertTriggerResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RevertTriggerResponse: ...

@typing.type_check_only
class RevertVariableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RevertVariableResponse: ...

@typing.type_check_only
class RevertZoneResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RevertZoneResponse: ...

@typing.type_check_only
class SyncWorkspaceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SyncWorkspaceResponse: ...

@typing.type_check_only
class TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Tag: ...

@typing.type_check_only
class TriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Trigger: ...

@typing.type_check_only
class UserPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UserPermission: ...

@typing.type_check_only
class VariableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Variable: ...

@typing.type_check_only
class WorkspaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Workspace: ...

@typing.type_check_only
class ZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Zone: ...
