import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccountConnector(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    oauthStartUri: str
    providerOauthConfig: ProviderOAuthConfig
    updateTime: str

@typing.type_check_only
class AppHubWorkload(typing_extensions.TypedDict, total=False):
    criticality: str
    environment: str
    workload: str

@typing.type_check_only
class ArtifactConfig(typing_extensions.TypedDict, total=False):
    googleArtifactAnalysis: GoogleArtifactAnalysis
    googleArtifactRegistry: GoogleArtifactRegistry
    uri: str

@typing.type_check_only
class BitbucketCloudConfig(typing_extensions.TypedDict, total=False):
    authorizerCredential: UserCredential
    readAuthorizerCredential: UserCredential
    webhookSecretSecretVersion: str
    workspace: str

@typing.type_check_only
class BitbucketDataCenterConfig(typing_extensions.TypedDict, total=False):
    authorizerCredential: UserCredential
    hostUri: str
    readAuthorizerCredential: UserCredential
    serverVersion: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    bitbucketCloudConfig: BitbucketCloudConfig
    bitbucketDataCenterConfig: BitbucketDataCenterConfig
    createTime: str
    cryptoKeyConfig: CryptoKeyConfig
    deleteTime: str
    disabled: bool
    etag: str
    gitProxyConfig: GitProxyConfig
    githubConfig: GitHubConfig
    githubEnterpriseConfig: GitHubEnterpriseConfig
    gitlabConfig: GitLabConfig
    gitlabEnterpriseConfig: GitLabEnterpriseConfig
    installationState: InstallationState
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    uid: str
    updateTime: str

@typing.type_check_only
class CryptoKeyConfig(typing_extensions.TypedDict, total=False):
    keyReference: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExchangeError(typing_extensions.TypedDict, total=False):
    code: str
    description: str

@typing.type_check_only
class FetchAccessTokenRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchAccessTokenResponse(typing_extensions.TypedDict, total=False):
    exchangeError: ExchangeError
    expirationTime: str
    scopes: _list[str]
    token: str

@typing.type_check_only
class FetchGitHubInstallationsResponse(typing_extensions.TypedDict, total=False):
    installations: _list[Installation]

@typing.type_check_only
class FetchGitRefsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    refNames: _list[str]

@typing.type_check_only
class FetchLinkableGitRepositoriesResponse(typing_extensions.TypedDict, total=False):
    linkableGitRepositories: _list[LinkableGitRepository]
    nextPageToken: str

@typing.type_check_only
class FetchReadTokenRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchReadTokenResponse(typing_extensions.TypedDict, total=False):
    expirationTime: str
    gitUsername: str
    token: str

@typing.type_check_only
class FetchReadWriteTokenRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchReadWriteTokenResponse(typing_extensions.TypedDict, total=False):
    expirationTime: str
    gitUsername: str
    token: str

@typing.type_check_only
class GKEWorkload(typing_extensions.TypedDict, total=False):
    cluster: str
    deployment: str

@typing.type_check_only
class GitHubConfig(typing_extensions.TypedDict, total=False):
    appInstallationId: str
    authorizerCredential: OAuthCredential
    githubApp: typing_extensions.Literal[
        "GIT_HUB_APP_UNSPECIFIED", "DEVELOPER_CONNECT", "FIREBASE"
    ]
    installationUri: str

@typing.type_check_only
class GitHubEnterpriseConfig(typing_extensions.TypedDict, total=False):
    appId: str
    appInstallationId: str
    appSlug: str
    hostUri: str
    installationUri: str
    privateKeySecretVersion: str
    serverVersion: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class GitLabConfig(typing_extensions.TypedDict, total=False):
    authorizerCredential: UserCredential
    readAuthorizerCredential: UserCredential
    webhookSecretSecretVersion: str

@typing.type_check_only
class GitLabEnterpriseConfig(typing_extensions.TypedDict, total=False):
    authorizerCredential: UserCredential
    hostUri: str
    readAuthorizerCredential: UserCredential
    serverVersion: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class GitProxyConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GitRepositoryLink(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    cloneUri: str
    createTime: str
    deleteTime: str
    etag: str
    gitProxyUri: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    uid: str
    updateTime: str
    webhookId: str

@typing.type_check_only
class GoogleArtifactAnalysis(typing_extensions.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class GoogleArtifactRegistry(typing_extensions.TypedDict, total=False):
    artifactRegistryPackage: str
    projectId: str

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class InsightsConfig(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    appHubApplication: str
    artifactConfigs: _list[ArtifactConfig]
    createTime: str
    errors: _list[Status]
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    runtimeConfigs: _list[RuntimeConfig]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COMPLETE", "ERROR"
    ]
    updateTime: str

@typing.type_check_only
class Installation(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    type: str

@typing.type_check_only
class InstallationState(typing_extensions.TypedDict, total=False):
    actionUri: str
    message: str
    stage: typing_extensions.Literal[
        "STAGE_UNSPECIFIED",
        "PENDING_CREATE_APP",
        "PENDING_USER_OAUTH",
        "PENDING_INSTALL_APP",
        "COMPLETE",
    ]

@typing.type_check_only
class LinkableGitRepository(typing_extensions.TypedDict, total=False):
    cloneUri: str

@typing.type_check_only
class ListAccountConnectorsResponse(typing_extensions.TypedDict, total=False):
    accountConnectors: _list[AccountConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGitRepositoryLinksResponse(typing_extensions.TypedDict, total=False):
    gitRepositoryLinks: _list[GitRepositoryLink]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInsightsConfigsResponse(typing_extensions.TypedDict, total=False):
    insightsConfigs: _list[InsightsConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    users: _list[User]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class OAuthCredential(typing_extensions.TypedDict, total=False):
    oauthTokenSecretVersion: str
    username: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ProcessBitbucketCloudWebhookRequest(typing_extensions.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProcessBitbucketDataCenterWebhookRequest(
    typing_extensions.TypedDict, total=False
):
    body: HttpBody

@typing.type_check_only
class ProcessGitHubEnterpriseWebhookRequest(typing_extensions.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProcessGitLabEnterpriseWebhookRequest(typing_extensions.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProcessGitLabWebhookRequest(typing_extensions.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProviderOAuthConfig(typing_extensions.TypedDict, total=False):
    scopes: _list[str]
    systemProviderId: typing_extensions.Literal[
        "SYSTEM_PROVIDER_UNSPECIFIED",
        "GITHUB",
        "GITLAB",
        "GOOGLE",
        "SENTRY",
        "ROVO",
        "NEW_RELIC",
        "DATASTAX",
        "DYNATRACE",
    ]

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    appHubWorkload: AppHubWorkload
    gkeWorkload: GKEWorkload
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "LINKED", "UNLINKED"]
    uri: str

@typing.type_check_only
class ServiceDirectoryConfig(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    lastTokenRequestTime: str
    name: str

@typing.type_check_only
class UserCredential(typing_extensions.TypedDict, total=False):
    userTokenSecretVersion: str
    username: str
