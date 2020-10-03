import typing

import typing_extensions

class RealtimeData(typing_extensions.TypedDict, total=False):
    id: str
    totalsForAllResults: typing.Dict[str, typing.Any]
    profileInfo: typing.Dict[str, typing.Any]
    rows: typing.List[list]
    selfLink: str
    columnHeaders: typing.List[typing.Dict[str, typing.Any]]
    totalResults: int
    kind: str
    query: typing.Dict[str, typing.Any]

class Segment(typing_extensions.TypedDict, total=False):
    definition: str
    selfLink: str
    type: str
    kind: str
    segmentId: str
    created: str
    name: str
    id: str
    updated: str

class Upload(typing_extensions.TypedDict, total=False):
    kind: str
    status: str
    accountId: str
    uploadTime: str
    id: str
    errors: typing.List[str]
    customDataSourceId: str

class Segments(typing_extensions.TypedDict, total=False):
    nextLink: str
    username: str
    itemsPerPage: int
    kind: str
    items: typing.List[Segment]
    startIndex: int
    previousLink: str
    totalResults: int

class RemarketingAudience(typing_extensions.TypedDict, total=False):
    internalWebPropertyId: str
    webPropertyId: str
    id: str
    description: str
    audienceDefinition: typing.Dict[str, typing.Any]
    linkedAdAccounts: typing.List[LinkedForeignAccount]
    accountId: str
    updated: str
    linkedViews: typing.List[str]
    name: str
    kind: str
    audienceType: str
    stateBasedAudienceDefinition: typing.Dict[str, typing.Any]
    created: str

class Filters(typing_extensions.TypedDict, total=False):
    username: str
    startIndex: int
    totalResults: int
    kind: str
    previousLink: str
    nextLink: str
    itemsPerPage: int
    items: typing.List[Filter]

class GaData(typing_extensions.TypedDict, total=False):
    selfLink: str
    sampleSpace: str
    kind: str
    sampleSize: str
    rows: typing.List[list]
    itemsPerPage: int
    query: typing.Dict[str, typing.Any]
    previousLink: str
    containsSampledData: bool
    totalResults: int
    dataLastRefreshed: str
    id: str
    totalsForAllResults: typing.Dict[str, typing.Any]
    profileInfo: typing.Dict[str, typing.Any]
    nextLink: str
    columnHeaders: typing.List[typing.Dict[str, typing.Any]]
    dataTable: typing.Dict[str, typing.Any]

class CustomDimensions(typing_extensions.TypedDict, total=False):
    startIndex: int
    totalResults: int
    itemsPerPage: int
    kind: str
    items: typing.List[CustomDimension]
    previousLink: str
    nextLink: str
    username: str

class WebPropertySummary(typing_extensions.TypedDict, total=False):
    profiles: typing.List[ProfileSummary]
    kind: str
    starred: bool
    internalWebPropertyId: str
    id: str
    level: str
    websiteUrl: str
    name: str

class Webproperty(typing_extensions.TypedDict, total=False):
    level: str
    created: str
    websiteUrl: str
    dataRetentionResetOnNewActivity: bool
    dataRetentionTtl: str
    updated: str
    accountId: str
    industryVertical: str
    childLink: typing.Dict[str, typing.Any]
    name: str
    profileCount: int
    kind: str
    permissions: typing.Dict[str, typing.Any]
    defaultProfileId: str
    id: str
    parentLink: typing.Dict[str, typing.Any]
    internalWebPropertyId: str
    starred: bool
    selfLink: str

class IncludeConditions(typing_extensions.TypedDict, total=False):
    membershipDurationDays: int
    daysToLookBack: int
    segment: str
    isSmartList: bool
    kind: str

class AccountTicket(typing_extensions.TypedDict, total=False):
    redirectUri: str
    id: str
    kind: str
    profile: Profile
    webproperty: Webproperty
    account: Account

class ProfileFilterLinks(typing_extensions.TypedDict, total=False):
    nextLink: str
    kind: str
    startIndex: int
    previousLink: str
    items: typing.List[ProfileFilterLink]
    itemsPerPage: int
    username: str
    totalResults: int

class Accounts(typing_extensions.TypedDict, total=False):
    username: str
    itemsPerPage: int
    totalResults: int
    startIndex: int
    nextLink: str
    previousLink: str
    kind: str
    items: typing.List[Account]

class RemarketingAudiences(typing_extensions.TypedDict, total=False):
    startIndex: int
    username: str
    itemsPerPage: int
    kind: str
    totalResults: int
    items: typing.List[RemarketingAudience]
    previousLink: str
    nextLink: str

class CustomMetrics(typing_extensions.TypedDict, total=False):
    itemsPerPage: int
    nextLink: str
    previousLink: str
    username: str
    items: typing.List[CustomMetric]
    kind: str
    startIndex: int
    totalResults: int

class EntityAdWordsLinks(typing_extensions.TypedDict, total=False):
    kind: str
    startIndex: int
    items: typing.List[EntityAdWordsLink]
    itemsPerPage: int
    nextLink: str
    previousLink: str
    totalResults: int

class UnsampledReports(typing_extensions.TypedDict, total=False):
    totalResults: int
    startIndex: int
    itemsPerPage: int
    kind: str
    previousLink: str
    nextLink: str
    username: str
    items: typing.List[UnsampledReport]

class ProfileFilterLink(typing_extensions.TypedDict, total=False):
    selfLink: str
    profileRef: ProfileRef
    filterRef: FilterRef
    kind: str
    id: str
    rank: int

class Filter(typing_extensions.TypedDict, total=False):
    accountId: str
    lowercaseDetails: typing.Dict[str, typing.Any]
    advancedDetails: typing.Dict[str, typing.Any]
    parentLink: typing.Dict[str, typing.Any]
    uppercaseDetails: typing.Dict[str, typing.Any]
    searchAndReplaceDetails: typing.Dict[str, typing.Any]
    type: str
    id: str
    name: str
    excludeDetails: FilterExpression
    selfLink: str
    updated: str
    kind: str
    created: str
    includeDetails: FilterExpression

class CustomDataSource(typing_extensions.TypedDict, total=False):
    description: str
    uploadType: str
    name: str
    accountId: str
    webPropertyId: str
    id: str
    updated: str
    created: str
    profilesLinked: typing.List[str]
    type: str
    schema: typing.List[str]
    selfLink: str
    parentLink: typing.Dict[str, typing.Any]
    childLink: typing.Dict[str, typing.Any]
    importBehavior: str
    kind: str

class UserRef(typing_extensions.TypedDict, total=False):
    kind: str
    email: str
    id: str

class CustomMetric(typing_extensions.TypedDict, total=False):
    created: str
    accountId: str
    max_value: str
    type: str
    scope: str
    name: str
    selfLink: str
    kind: str
    index: int
    min_value: str
    id: str
    updated: str
    webPropertyId: str
    active: bool
    parentLink: typing.Dict[str, typing.Any]

class Goal(typing_extensions.TypedDict, total=False):
    type: str
    parentLink: typing.Dict[str, typing.Any]
    id: str
    updated: str
    internalWebPropertyId: str
    profileId: str
    value: float
    visitNumPagesDetails: typing.Dict[str, typing.Any]
    active: bool
    selfLink: str
    name: str
    urlDestinationDetails: typing.Dict[str, typing.Any]
    visitTimeOnSiteDetails: typing.Dict[str, typing.Any]
    created: str
    webPropertyId: str
    accountId: str
    kind: str
    eventDetails: typing.Dict[str, typing.Any]

class CustomDataSources(typing_extensions.TypedDict, total=False):
    itemsPerPage: int
    startIndex: int
    items: typing.List[CustomDataSource]
    nextLink: str
    totalResults: int
    username: str
    previousLink: str
    kind: str

class Column(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    kind: str
    id: str

class Profile(typing_extensions.TypedDict, total=False):
    id: str
    webPropertyId: str
    starred: bool
    updated: str
    type: str
    botFilteringEnabled: bool
    selfLink: str
    kind: str
    name: str
    parentLink: typing.Dict[str, typing.Any]
    defaultPage: str
    siteSearchQueryParameters: str
    childLink: typing.Dict[str, typing.Any]
    internalWebPropertyId: str
    stripSiteSearchQueryParameters: bool
    created: str
    siteSearchCategoryParameters: str
    enhancedECommerceTracking: bool
    websiteUrl: str
    timezone: str
    permissions: typing.Dict[str, typing.Any]
    currency: str
    accountId: str
    stripSiteSearchCategoryParameters: bool
    excludeQueryParameters: str
    eCommerceTracking: bool

class Experiment(typing_extensions.TypedDict, total=False):
    equalWeighting: bool
    webPropertyId: str
    endTime: str
    trafficCoverage: float
    servingFramework: str
    updated: str
    selfLink: str
    winnerConfidenceLevel: float
    name: str
    editableInGaUi: bool
    startTime: str
    optimizationType: str
    minimumExperimentLengthInDays: int
    description: str
    objectiveMetric: str
    rewriteVariationUrlsAsOriginal: bool
    snippet: str
    kind: str
    parentLink: typing.Dict[str, typing.Any]
    internalWebPropertyId: str
    winnerFound: bool
    reasonExperimentEnded: str
    accountId: str
    id: str
    created: str
    variations: typing.List[typing.Dict[str, typing.Any]]
    profileId: str
    status: str

class AccountTreeRequest(typing_extensions.TypedDict, total=False):
    websiteUrl: str
    accountName: str
    profileName: str
    kind: str
    timezone: str
    webpropertyName: str

class CustomDimension(typing_extensions.TypedDict, total=False):
    id: str
    updated: str
    webPropertyId: str
    accountId: str
    active: bool
    selfLink: str
    scope: str
    created: str
    parentLink: typing.Dict[str, typing.Any]
    index: int
    kind: str
    name: str

class AnalyticsDataimportDeleteUploadDataRequest(
    typing_extensions.TypedDict, total=False
):
    customDataImportUids: typing.List[str]

class FilterRef(typing_extensions.TypedDict, total=False):
    kind: str
    href: str
    accountId: str
    name: str
    id: str

UnsampledReport = typing_extensions.TypedDict(
    "UnsampledReport",
    {
        "downloadType": str,
        "status": str,
        "updated": str,
        "profileId": str,
        "title": str,
        "filters": str,
        "cloudStorageDownloadDetails": typing.Dict[str, typing.Any],
        "end-date": str,
        "start-date": str,
        "selfLink": str,
        "segment": str,
        "kind": str,
        "id": str,
        "created": str,
        "accountId": str,
        "dimensions": str,
        "webPropertyId": str,
        "metrics": str,
        "driveDownloadDetails": typing.Dict[str, typing.Any],
    },
    total=False,
)

class AdWordsAccount(typing_extensions.TypedDict, total=False):
    autoTaggingEnabled: bool
    customerId: str
    kind: str

class AccountTreeResponse(typing_extensions.TypedDict, total=False):
    account: Account
    kind: str
    profile: Profile
    webproperty: Webproperty

class HashClientIdRequest(typing_extensions.TypedDict, total=False):
    kind: str
    webPropertyId: str
    clientId: str

class Experiments(typing_extensions.TypedDict, total=False):
    username: str
    nextLink: str
    items: typing.List[Experiment]
    kind: str
    startIndex: int
    itemsPerPage: int
    totalResults: int
    previousLink: str

class EntityAdWordsLink(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    adWordsAccounts: typing.List[AdWordsAccount]
    id: str
    entity: typing.Dict[str, typing.Any]
    selfLink: str
    profileIds: typing.List[str]

class AccountSummary(typing_extensions.TypedDict, total=False):
    id: str
    starred: bool
    name: str
    webProperties: typing.List[WebPropertySummary]
    kind: str

class EntityUserLink(typing_extensions.TypedDict, total=False):
    id: str
    entity: typing.Dict[str, typing.Any]
    permissions: typing.Dict[str, typing.Any]
    kind: str
    userRef: UserRef
    selfLink: str

class ProfileRef(typing_extensions.TypedDict, total=False):
    webPropertyId: str
    name: str
    href: str
    kind: str
    id: str
    internalWebPropertyId: str
    accountId: str

class Goals(typing_extensions.TypedDict, total=False):
    kind: str
    nextLink: str
    username: str
    items: typing.List[Goal]
    itemsPerPage: int
    totalResults: int
    startIndex: int
    previousLink: str

class HashClientIdResponse(typing_extensions.TypedDict, total=False):
    hashedClientId: str
    kind: str
    clientId: str
    webPropertyId: str

class AccountRef(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    href: str
    kind: str

class EntityUserLinks(typing_extensions.TypedDict, total=False):
    itemsPerPage: int
    totalResults: int
    startIndex: int
    kind: str
    previousLink: str
    items: typing.List[EntityUserLink]
    nextLink: str

class WebPropertyRef(typing_extensions.TypedDict, total=False):
    kind: str
    href: str
    name: str
    internalWebPropertyId: str
    accountId: str
    id: str

class Webproperties(typing_extensions.TypedDict, total=False):
    previousLink: str
    items: typing.List[Webproperty]
    nextLink: str
    totalResults: int
    startIndex: int
    itemsPerPage: int
    kind: str
    username: str

class UserDeletionRequest(typing_extensions.TypedDict, total=False):
    propertyId: str
    id: typing.Dict[str, typing.Any]
    webPropertyId: str
    kind: str
    firebaseProjectId: str
    deletionRequestTime: str

class Profiles(typing_extensions.TypedDict, total=False):
    itemsPerPage: int
    username: str
    nextLink: str
    startIndex: int
    kind: str
    previousLink: str
    totalResults: int
    items: typing.List[Profile]

class LinkedForeignAccount(typing_extensions.TypedDict, total=False):
    type: str
    id: str
    webPropertyId: str
    status: str
    internalWebPropertyId: str
    linkedAccountId: str
    kind: str
    eligibleForSearch: bool
    remarketingAudienceId: str
    accountId: str

class Account(typing_extensions.TypedDict, total=False):
    id: str
    updated: str
    created: str
    kind: str
    selfLink: str
    starred: bool
    name: str
    permissions: typing.Dict[str, typing.Any]
    childLink: typing.Dict[str, typing.Any]

class McfData(typing_extensions.TypedDict, total=False):
    sampleSpace: str
    totalsForAllResults: typing.Dict[str, typing.Any]
    profileInfo: typing.Dict[str, typing.Any]
    rows: typing.List[list]
    itemsPerPage: int
    totalResults: int
    nextLink: str
    containsSampledData: bool
    columnHeaders: typing.List[typing.Dict[str, typing.Any]]
    sampleSize: str
    selfLink: str
    previousLink: str
    id: str
    kind: str
    query: typing.Dict[str, typing.Any]

class Uploads(typing_extensions.TypedDict, total=False):
    itemsPerPage: int
    totalResults: int
    items: typing.List[Upload]
    kind: str
    startIndex: int
    nextLink: str
    previousLink: str

class Columns(typing_extensions.TypedDict, total=False):
    totalResults: int
    kind: str
    etag: str
    items: typing.List[Column]
    attributeNames: typing.List[str]

class AccountSummaries(typing_extensions.TypedDict, total=False):
    items: typing.List[AccountSummary]
    previousLink: str
    totalResults: int
    startIndex: int
    nextLink: str
    username: str
    itemsPerPage: int
    kind: str

class ProfileSummary(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    id: str
    starred: bool
    type: str

class FilterExpression(typing_extensions.TypedDict, total=False):
    expressionValue: str
    kind: str
    caseSensitive: bool
    fieldIndex: int
    field: str
    matchType: str
