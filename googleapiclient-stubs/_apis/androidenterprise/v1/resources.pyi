import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AndroidEnterpriseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DevicesResource(googleapiclient.discovery.Resource):
        def forceReportUpload(
            self, *, enterpriseId: str, userId: str, deviceId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, enterpriseId: str, userId: str, deviceId: str, **kwargs: typing.Any
        ) -> DeviceHttpRequest: ...
        def getState(
            self, *, enterpriseId: str, userId: str, deviceId: str, **kwargs: typing.Any
        ) -> DeviceStateHttpRequest: ...
        def list(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> DevicesListResponseHttpRequest: ...
        def setState(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            body: DeviceState = ...,
            **kwargs: typing.Any
        ) -> DeviceStateHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            body: Device = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> DeviceHttpRequest: ...

    @typing.type_check_only
    class EnterprisesResource(googleapiclient.discovery.Resource):
        def acknowledgeNotificationSet(
            self, *, notificationSetId: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def completeSignup(
            self,
            *,
            completionToken: str = ...,
            enterpriseToken: str = ...,
            **kwargs: typing.Any
        ) -> EnterpriseHttpRequest: ...
        def createWebToken(
            self,
            *,
            enterpriseId: str,
            body: AdministratorWebTokenSpec = ...,
            **kwargs: typing.Any
        ) -> AdministratorWebTokenHttpRequest: ...
        def enroll(
            self, *, token: str, body: Enterprise = ..., **kwargs: typing.Any
        ) -> EnterpriseHttpRequest: ...
        def generateSignupUrl(
            self, *, callbackUrl: str = ..., **kwargs: typing.Any
        ) -> SignupInfoHttpRequest: ...
        def get(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> EnterpriseHttpRequest: ...
        def getServiceAccount(
            self,
            *,
            enterpriseId: str,
            keyType: typing_extensions.Literal["googleCredentials", "pkcs12"] = ...,
            **kwargs: typing.Any
        ) -> ServiceAccountHttpRequest: ...
        def getStoreLayout(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> StoreLayoutHttpRequest: ...
        def list(
            self, *, domain: str, **kwargs: typing.Any
        ) -> EnterprisesListResponseHttpRequest: ...
        def pullNotificationSet(
            self,
            *,
            requestMode: typing_extensions.Literal[
                "waitForNotifications", "returnImmediately"
            ] = ...,
            **kwargs: typing.Any
        ) -> NotificationSetHttpRequest: ...
        def sendTestPushNotification(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> EnterprisesSendTestPushNotificationResponseHttpRequest: ...
        def setAccount(
            self,
            *,
            enterpriseId: str,
            body: EnterpriseAccount = ...,
            **kwargs: typing.Any
        ) -> EnterpriseAccountHttpRequest: ...
        def setStoreLayout(
            self, *, enterpriseId: str, body: StoreLayout = ..., **kwargs: typing.Any
        ) -> StoreLayoutHttpRequest: ...
        def unenroll(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class EntitlementsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            enterpriseId: str,
            userId: str,
            entitlementId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            enterpriseId: str,
            userId: str,
            entitlementId: str,
            **kwargs: typing.Any
        ) -> EntitlementHttpRequest: ...
        def list(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> EntitlementsListResponseHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            userId: str,
            entitlementId: str,
            body: Entitlement = ...,
            install: bool = ...,
            **kwargs: typing.Any
        ) -> EntitlementHttpRequest: ...

    @typing.type_check_only
    class GrouplicensesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, enterpriseId: str, groupLicenseId: str, **kwargs: typing.Any
        ) -> GroupLicenseHttpRequest: ...
        def list(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> GroupLicensesListResponseHttpRequest: ...

    @typing.type_check_only
    class GrouplicenseusersResource(googleapiclient.discovery.Resource):
        def list(
            self, *, enterpriseId: str, groupLicenseId: str, **kwargs: typing.Any
        ) -> GroupLicenseUsersListResponseHttpRequest: ...

    @typing.type_check_only
    class InstallsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            installId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            installId: str,
            **kwargs: typing.Any
        ) -> InstallHttpRequest: ...
        def list(
            self, *, enterpriseId: str, userId: str, deviceId: str, **kwargs: typing.Any
        ) -> InstallsListResponseHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            installId: str,
            body: Install = ...,
            **kwargs: typing.Any
        ) -> InstallHttpRequest: ...

    @typing.type_check_only
    class ManagedconfigurationsfordeviceResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            managedConfigurationForDeviceId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            managedConfigurationForDeviceId: str,
            **kwargs: typing.Any
        ) -> ManagedConfigurationHttpRequest: ...
        def list(
            self, *, enterpriseId: str, userId: str, deviceId: str, **kwargs: typing.Any
        ) -> ManagedConfigurationsForDeviceListResponseHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            userId: str,
            deviceId: str,
            managedConfigurationForDeviceId: str,
            body: ManagedConfiguration = ...,
            **kwargs: typing.Any
        ) -> ManagedConfigurationHttpRequest: ...

    @typing.type_check_only
    class ManagedconfigurationsforuserResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            enterpriseId: str,
            userId: str,
            managedConfigurationForUserId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            enterpriseId: str,
            userId: str,
            managedConfigurationForUserId: str,
            **kwargs: typing.Any
        ) -> ManagedConfigurationHttpRequest: ...
        def list(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> ManagedConfigurationsForUserListResponseHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            userId: str,
            managedConfigurationForUserId: str,
            body: ManagedConfiguration = ...,
            **kwargs: typing.Any
        ) -> ManagedConfigurationHttpRequest: ...

    @typing.type_check_only
    class ManagedconfigurationssettingsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, enterpriseId: str, productId: str, **kwargs: typing.Any
        ) -> ManagedConfigurationsSettingsListResponseHttpRequest: ...

    @typing.type_check_only
    class PermissionsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, permissionId: str, language: str = ..., **kwargs: typing.Any
        ) -> PermissionHttpRequest: ...

    @typing.type_check_only
    class ProductsResource(googleapiclient.discovery.Resource):
        def approve(
            self,
            *,
            enterpriseId: str,
            productId: str,
            body: ProductsApproveRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def generateApprovalUrl(
            self,
            *,
            enterpriseId: str,
            productId: str,
            languageCode: str = ...,
            **kwargs: typing.Any
        ) -> ProductsGenerateApprovalUrlResponseHttpRequest: ...
        def get(
            self,
            *,
            enterpriseId: str,
            productId: str,
            language: str = ...,
            **kwargs: typing.Any
        ) -> ProductHttpRequest: ...
        def getAppRestrictionsSchema(
            self,
            *,
            enterpriseId: str,
            productId: str,
            language: str = ...,
            **kwargs: typing.Any
        ) -> AppRestrictionsSchemaHttpRequest: ...
        def getPermissions(
            self, *, enterpriseId: str, productId: str, **kwargs: typing.Any
        ) -> ProductPermissionsHttpRequest: ...
        def list(
            self,
            *,
            enterpriseId: str,
            approved: bool = ...,
            language: str = ...,
            maxResults: int = ...,
            query: str = ...,
            token: str = ...,
            **kwargs: typing.Any
        ) -> ProductsListResponseHttpRequest: ...
        def unapprove(
            self, *, enterpriseId: str, productId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class ServiceaccountkeysResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, enterpriseId: str, keyId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            enterpriseId: str,
            body: ServiceAccountKey = ...,
            **kwargs: typing.Any
        ) -> ServiceAccountKeyHttpRequest: ...
        def list(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> ServiceAccountKeysListResponseHttpRequest: ...

    @typing.type_check_only
    class StorelayoutclustersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            enterpriseId: str,
            pageId: str,
            clusterId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            enterpriseId: str,
            pageId: str,
            clusterId: str,
            **kwargs: typing.Any
        ) -> StoreClusterHttpRequest: ...
        def insert(
            self,
            *,
            enterpriseId: str,
            pageId: str,
            body: StoreCluster = ...,
            **kwargs: typing.Any
        ) -> StoreClusterHttpRequest: ...
        def list(
            self, *, enterpriseId: str, pageId: str, **kwargs: typing.Any
        ) -> StoreLayoutClustersListResponseHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            pageId: str,
            clusterId: str,
            body: StoreCluster = ...,
            **kwargs: typing.Any
        ) -> StoreClusterHttpRequest: ...

    @typing.type_check_only
    class StorelayoutpagesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, enterpriseId: str, pageId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, enterpriseId: str, pageId: str, **kwargs: typing.Any
        ) -> StorePageHttpRequest: ...
        def insert(
            self, *, enterpriseId: str, body: StorePage = ..., **kwargs: typing.Any
        ) -> StorePageHttpRequest: ...
        def list(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> StoreLayoutPagesListResponseHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            pageId: str,
            body: StorePage = ...,
            **kwargs: typing.Any
        ) -> StorePageHttpRequest: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def generateAuthenticationToken(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> AuthenticationTokenHttpRequest: ...
        def get(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def getAvailableProductSet(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> ProductSetHttpRequest: ...
        def insert(
            self, *, enterpriseId: str, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def list(
            self, *, enterpriseId: str, email: str, **kwargs: typing.Any
        ) -> UsersListResponseHttpRequest: ...
        def revokeDeviceAccess(
            self, *, enterpriseId: str, userId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def setAvailableProductSet(
            self,
            *,
            enterpriseId: str,
            userId: str,
            body: ProductSet = ...,
            **kwargs: typing.Any
        ) -> ProductSetHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            userId: str,
            body: User = ...,
            **kwargs: typing.Any
        ) -> UserHttpRequest: ...

    @typing.type_check_only
    class WebappsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, enterpriseId: str, webAppId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, enterpriseId: str, webAppId: str, **kwargs: typing.Any
        ) -> WebAppHttpRequest: ...
        def insert(
            self, *, enterpriseId: str, body: WebApp = ..., **kwargs: typing.Any
        ) -> WebAppHttpRequest: ...
        def list(
            self, *, enterpriseId: str, **kwargs: typing.Any
        ) -> WebAppsListResponseHttpRequest: ...
        def update(
            self,
            *,
            enterpriseId: str,
            webAppId: str,
            body: WebApp = ...,
            **kwargs: typing.Any
        ) -> WebAppHttpRequest: ...

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
    def devices(self) -> DevicesResource: ...
    def enterprises(self) -> EnterprisesResource: ...
    def entitlements(self) -> EntitlementsResource: ...
    def grouplicenses(self) -> GrouplicensesResource: ...
    def grouplicenseusers(self) -> GrouplicenseusersResource: ...
    def installs(self) -> InstallsResource: ...
    def managedconfigurationsfordevice(
        self,
    ) -> ManagedconfigurationsfordeviceResource: ...
    def managedconfigurationsforuser(self) -> ManagedconfigurationsforuserResource: ...
    def managedconfigurationssettings(
        self,
    ) -> ManagedconfigurationssettingsResource: ...
    def permissions(self) -> PermissionsResource: ...
    def products(self) -> ProductsResource: ...
    def serviceaccountkeys(self) -> ServiceaccountkeysResource: ...
    def storelayoutclusters(self) -> StorelayoutclustersResource: ...
    def storelayoutpages(self) -> StorelayoutpagesResource: ...
    def users(self) -> UsersResource: ...
    def webapps(self) -> WebappsResource: ...

@typing.type_check_only
class AdministratorWebTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdministratorWebToken: ...

@typing.type_check_only
class AppRestrictionsSchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AppRestrictionsSchema: ...

@typing.type_check_only
class AuthenticationTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AuthenticationToken: ...

@typing.type_check_only
class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Device: ...

@typing.type_check_only
class DeviceStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeviceState: ...

@typing.type_check_only
class DevicesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DevicesListResponse: ...

@typing.type_check_only
class EnterpriseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Enterprise: ...

@typing.type_check_only
class EnterpriseAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EnterpriseAccount: ...

@typing.type_check_only
class EnterprisesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EnterprisesListResponse: ...

@typing.type_check_only
class EnterprisesSendTestPushNotificationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EnterprisesSendTestPushNotificationResponse: ...

@typing.type_check_only
class EntitlementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Entitlement: ...

@typing.type_check_only
class EntitlementsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EntitlementsListResponse: ...

@typing.type_check_only
class GroupLicenseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GroupLicense: ...

@typing.type_check_only
class GroupLicenseUsersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GroupLicenseUsersListResponse: ...

@typing.type_check_only
class GroupLicensesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GroupLicensesListResponse: ...

@typing.type_check_only
class InstallHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Install: ...

@typing.type_check_only
class InstallsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstallsListResponse: ...

@typing.type_check_only
class ManagedConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedConfiguration: ...

@typing.type_check_only
class ManagedConfigurationsForDeviceListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedConfigurationsForDeviceListResponse: ...

@typing.type_check_only
class ManagedConfigurationsForUserListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedConfigurationsForUserListResponse: ...

@typing.type_check_only
class ManagedConfigurationsSettingsListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedConfigurationsSettingsListResponse: ...

@typing.type_check_only
class NotificationSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NotificationSet: ...

@typing.type_check_only
class PermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Permission: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Product: ...

@typing.type_check_only
class ProductPermissionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductPermissions: ...

@typing.type_check_only
class ProductSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductSet: ...

@typing.type_check_only
class ProductsGenerateApprovalUrlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductsGenerateApprovalUrlResponse: ...

@typing.type_check_only
class ProductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductsListResponse: ...

@typing.type_check_only
class ServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceAccount: ...

@typing.type_check_only
class ServiceAccountKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceAccountKey: ...

@typing.type_check_only
class ServiceAccountKeysListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceAccountKeysListResponse: ...

@typing.type_check_only
class SignupInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SignupInfo: ...

@typing.type_check_only
class StoreClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StoreCluster: ...

@typing.type_check_only
class StoreLayoutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StoreLayout: ...

@typing.type_check_only
class StoreLayoutClustersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StoreLayoutClustersListResponse: ...

@typing.type_check_only
class StoreLayoutPagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StoreLayoutPagesListResponse: ...

@typing.type_check_only
class StorePageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StorePage: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> User: ...

@typing.type_check_only
class UsersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UsersListResponse: ...

@typing.type_check_only
class WebAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WebApp: ...

@typing.type_check_only
class WebAppsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WebAppsListResponse: ...
