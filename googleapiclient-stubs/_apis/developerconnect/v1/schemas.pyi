import typing

_list = list

@typing.type_check_only
class AccountConnector(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    customOauthConfig: CustomOAuthConfig
    etag: str
    labels: dict[str, typing.Any]
    name: str
    oauthStartUri: str
    providerOauthConfig: ProviderOAuthConfig
    proxyConfig: ProxyConfig
    uid: str
    updateTime: str

@typing.type_check_only
class AppHubService(typing.TypedDict, total=False):
    apphubService: str
    criticality: str
    environment: str

@typing.type_check_only
class AppHubWorkload(typing.TypedDict, total=False):
    criticality: str
    environment: str
    workload: str

@typing.type_check_only
class ArtifactConfig(typing.TypedDict, total=False):
    googleArtifactAnalysis: GoogleArtifactAnalysis
    googleArtifactRegistry: GoogleArtifactRegistry
    uri: str

@typing.type_check_only
class ArtifactDeployment(typing.TypedDict, total=False):
    artifactAlias: str
    artifactReference: str
    containerStatusSummary: str
    deployTime: str
    id: str
    sourceCodeUris: _list[str]
    sourceCommitUris: _list[str]
    undeployTime: str

@typing.type_check_only
class BasicAuthentication(typing.TypedDict, total=False):
    passwordSecretVersion: str
    username: str

@typing.type_check_only
class BearerTokenAuthentication(typing.TypedDict, total=False):
    tokenSecretVersion: str

@typing.type_check_only
class BitbucketCloudConfig(typing.TypedDict, total=False):
    authorizerCredential: UserCredential
    readAuthorizerCredential: UserCredential
    webhookSecretSecretVersion: str
    workspace: str

@typing.type_check_only
class BitbucketDataCenterConfig(typing.TypedDict, total=False):
    authorizerCredential: UserCredential
    hostUri: str
    readAuthorizerCredential: UserCredential
    serverVersion: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Connection(typing.TypedDict, total=False):
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
    httpConfig: GenericHTTPEndpointConfig
    installationState: InstallationState
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    secureSourceManagerInstanceConfig: SecureSourceManagerInstanceConfig
    uid: str
    updateTime: str

@typing.type_check_only
class CryptoKeyConfig(typing.TypedDict, total=False):
    keyReference: str

@typing.type_check_only
class CustomOAuthConfig(typing.TypedDict, total=False):
    authUri: str
    clientId: str
    clientSecret: str
    hostUri: str
    pkceDisabled: bool
    scmProvider: typing.Literal[
        "SCM_PROVIDER_UNKNOWN",
        "GITHUB_ENTERPRISE",
        "GITLAB_ENTERPRISE",
        "BITBUCKET_DATA_CENTER",
    ]
    scopes: _list[str]
    serverVersion: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str
    tokenUri: str

@typing.type_check_only
class DeploymentEvent(typing.TypedDict, total=False):
    artifactDeployments: _list[ArtifactDeployment]
    createTime: str
    deployTime: str
    name: str
    runtimeConfig: RuntimeConfig
    runtimeDeploymentUri: str
    state: typing.Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_INACTIVE"]
    undeployTime: str
    updateTime: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExchangeError(typing.TypedDict, total=False):
    code: str
    description: str

@typing.type_check_only
class FetchAccessTokenRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchAccessTokenResponse(typing.TypedDict, total=False):
    exchangeError: ExchangeError
    expirationTime: str
    scopes: _list[str]
    token: str

@typing.type_check_only
class FetchGitHubInstallationsResponse(typing.TypedDict, total=False):
    installations: _list[Installation]

@typing.type_check_only
class FetchGitRefsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    refNames: _list[str]

@typing.type_check_only
class FetchLinkableGitRepositoriesResponse(typing.TypedDict, total=False):
    linkableGitRepositories: _list[LinkableGitRepository]
    nextPageToken: str

@typing.type_check_only
class FetchReadTokenRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchReadTokenResponse(typing.TypedDict, total=False):
    expirationTime: str
    gitUsername: str
    token: str

@typing.type_check_only
class FetchReadWriteTokenRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchReadWriteTokenResponse(typing.TypedDict, total=False):
    expirationTime: str
    gitUsername: str
    token: str

@typing.type_check_only
class FetchUserRepositoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userRepos: _list[UserRepository]

@typing.type_check_only
class FinishOAuthResponse(typing.TypedDict, total=False):
    exchangeError: ExchangeError

@typing.type_check_only
class GKEWorkload(typing.TypedDict, total=False):
    cluster: str
    deployment: str

@typing.type_check_only
class GenericHTTPEndpointConfig(typing.TypedDict, total=False):
    basicAuthentication: BasicAuthentication
    bearerTokenAuthentication: BearerTokenAuthentication
    hostUri: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str

@typing.type_check_only
class GitHubConfig(typing.TypedDict, total=False):
    appInstallationId: str
    authorizerCredential: OAuthCredential
    githubApp: typing.Literal[
        "GIT_HUB_APP_UNSPECIFIED",
        "DEVELOPER_CONNECT",
        "FIREBASE",
        "GEMINI_CODE_ASSIST",
        "DATAFORM",
    ]
    installationUri: str

@typing.type_check_only
class GitHubEnterpriseConfig(typing.TypedDict, total=False):
    appId: str
    appInstallationId: str
    appSlug: str
    hostUri: str
    installationUri: str
    organization: str
    privateKeySecretVersion: str
    serverVersion: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class GitLabConfig(typing.TypedDict, total=False):
    authorizerCredential: UserCredential
    readAuthorizerCredential: UserCredential
    webhookSecretSecretVersion: str

@typing.type_check_only
class GitLabEnterpriseConfig(typing.TypedDict, total=False):
    authorizerCredential: UserCredential
    hostUri: str
    readAuthorizerCredential: UserCredential
    serverVersion: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCaCertificate: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class GitProxyConfig(typing.TypedDict, total=False):
    enabled: bool
    httpProxyBaseUri: str

@typing.type_check_only
class GitRepositoryLink(typing.TypedDict, total=False):
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
class GoogleArtifactAnalysis(typing.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class GoogleArtifactRegistry(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    projectId: str

@typing.type_check_only
class GoogleCloudRun(typing.TypedDict, total=False):
    serviceUri: str

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class InsightsConfig(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    appHubApplication: str
    artifactConfigs: _list[ArtifactConfig]
    createTime: str
    errors: _list[Status]
    labels: dict[str, typing.Any]
    name: str
    projects: Projects
    reconciling: bool
    runtimeConfigs: _list[RuntimeConfig]
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "COMPLETE", "ERROR"]
    updateTime: str

@typing.type_check_only
class Installation(typing.TypedDict, total=False):
    id: str
    name: str
    type: str

@typing.type_check_only
class InstallationState(typing.TypedDict, total=False):
    actionUri: str
    message: str
    stage: typing.Literal[
        "STAGE_UNSPECIFIED",
        "PENDING_CREATE_APP",
        "PENDING_USER_OAUTH",
        "PENDING_INSTALL_APP",
        "COMPLETE",
    ]

@typing.type_check_only
class LinkableGitRepository(typing.TypedDict, total=False):
    cloneUri: str

@typing.type_check_only
class ListAccountConnectorsResponse(typing.TypedDict, total=False):
    accountConnectors: _list[AccountConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDeploymentEventsResponse(typing.TypedDict, total=False):
    deploymentEvents: _list[DeploymentEvent]
    nextPageToken: str

@typing.type_check_only
class ListGitRepositoryLinksResponse(typing.TypedDict, total=False):
    gitRepositoryLinks: _list[GitRepositoryLink]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInsightsConfigsResponse(typing.TypedDict, total=False):
    insightsConfigs: _list[InsightsConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListUsersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    users: _list[User]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class OAuthCredential(typing.TypedDict, total=False):
    oauthTokenSecretVersion: str
    username: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ProcessBitbucketCloudWebhookRequest(typing.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProcessBitbucketDataCenterWebhookRequest(typing.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProcessGitHubEnterpriseWebhookRequest(typing.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProcessGitLabEnterpriseWebhookRequest(typing.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class ProcessGitLabWebhookRequest(typing.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class Projects(typing.TypedDict, total=False):
    projectIds: _list[str]

@typing.type_check_only
class ProviderOAuthConfig(typing.TypedDict, total=False):
    scopes: _list[str]
    systemProviderId: typing.Literal[
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
class ProxyConfig(typing.TypedDict, total=False):
    enabled: bool
    httpProxyBaseUri: str

@typing.type_check_only
class RuntimeConfig(typing.TypedDict, total=False):
    appHubService: AppHubService
    appHubWorkload: AppHubWorkload
    gkeWorkload: GKEWorkload
    googleCloudRun: GoogleCloudRun
    state: typing.Literal["STATE_UNSPECIFIED", "LINKED", "UNLINKED"]
    uri: str

@typing.type_check_only
class SecureSourceManagerInstanceConfig(typing.TypedDict, total=False):
    instance: str

@typing.type_check_only
class ServiceDirectoryConfig(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class StartOAuthResponse(typing.TypedDict, total=False):
    authUri: str
    clientId: str
    codeChallenge: str
    codeChallengeMethod: str
    scopes: _list[str]
    systemProviderId: typing.Literal[
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
    ticket: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class User(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    lastTokenRequestTime: str
    name: str

@typing.type_check_only
class UserCredential(typing.TypedDict, total=False):
    userTokenSecretVersion: str
    username: str

@typing.type_check_only
class UserRepository(typing.TypedDict, total=False):
    cloneUri: str
    displayName: str
    gitProxyUri: str
