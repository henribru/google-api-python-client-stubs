import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    childLink: dict[str, typing.Any]
    created: str
    id: str
    kind: str
    name: str
    permissions: dict[str, typing.Any]
    selfLink: str
    starred: bool
    updated: str

@typing.type_check_only
class AccountRef(typing_extensions.TypedDict, total=False):
    href: str
    id: str
    kind: str
    name: str

@typing.type_check_only
class AccountSummaries(typing_extensions.TypedDict, total=False):
    items: _list[AccountSummary]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class AccountSummary(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str
    starred: bool
    webProperties: _list[WebPropertySummary]

@typing.type_check_only
class AccountTicket(typing_extensions.TypedDict, total=False):
    account: Account
    id: str
    kind: str
    profile: Profile
    redirectUri: str
    webproperty: Webproperty

@typing.type_check_only
class AccountTreeRequest(typing_extensions.TypedDict, total=False):
    accountName: str
    kind: str
    profileName: str
    timezone: str
    webpropertyName: str
    websiteUrl: str

@typing.type_check_only
class AccountTreeResponse(typing_extensions.TypedDict, total=False):
    account: Account
    kind: str
    profile: Profile
    webproperty: Webproperty

@typing.type_check_only
class Accounts(typing_extensions.TypedDict, total=False):
    items: _list[Account]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class AdWordsAccount(typing_extensions.TypedDict, total=False):
    autoTaggingEnabled: bool
    customerId: str
    kind: str

@typing.type_check_only
class AnalyticsDataimportDeleteUploadDataRequest(
    typing_extensions.TypedDict, total=False
):
    customDataImportUids: _list[str]

@typing.type_check_only
class Column(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    id: str
    kind: str

@typing.type_check_only
class Columns(typing_extensions.TypedDict, total=False):
    attributeNames: _list[str]
    etag: str
    items: _list[Column]
    kind: str
    totalResults: int

@typing.type_check_only
class CustomDataSource(typing_extensions.TypedDict, total=False):
    accountId: str
    childLink: dict[str, typing.Any]
    created: str
    description: str
    id: str
    importBehavior: str
    kind: str
    name: str
    parentLink: dict[str, typing.Any]
    profilesLinked: _list[str]
    schema: _list[str]
    selfLink: str
    type: str
    updated: str
    uploadType: str
    webPropertyId: str

@typing.type_check_only
class CustomDataSources(typing_extensions.TypedDict, total=False):
    items: _list[CustomDataSource]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class CustomDimension(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    created: str
    id: str
    index: int
    kind: str
    name: str
    parentLink: dict[str, typing.Any]
    scope: str
    selfLink: str
    updated: str
    webPropertyId: str

@typing.type_check_only
class CustomDimensions(typing_extensions.TypedDict, total=False):
    items: _list[CustomDimension]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class CustomMetric(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    created: str
    id: str
    index: int
    kind: str
    max_value: str
    min_value: str
    name: str
    parentLink: dict[str, typing.Any]
    scope: str
    selfLink: str
    type: str
    updated: str
    webPropertyId: str

@typing.type_check_only
class CustomMetrics(typing_extensions.TypedDict, total=False):
    items: _list[CustomMetric]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class EntityAdWordsLink(typing_extensions.TypedDict, total=False):
    adWordsAccounts: _list[AdWordsAccount]
    entity: dict[str, typing.Any]
    id: str
    kind: str
    name: str
    profileIds: _list[str]
    selfLink: str

@typing.type_check_only
class EntityAdWordsLinks(typing_extensions.TypedDict, total=False):
    items: _list[EntityAdWordsLink]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int

@typing.type_check_only
class EntityUserLink(typing_extensions.TypedDict, total=False):
    entity: dict[str, typing.Any]
    id: str
    kind: str
    permissions: dict[str, typing.Any]
    selfLink: str
    userRef: UserRef

@typing.type_check_only
class EntityUserLinks(typing_extensions.TypedDict, total=False):
    items: _list[EntityUserLink]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int

@typing.type_check_only
class Experiment(typing_extensions.TypedDict, total=False):
    accountId: str
    created: str
    description: str
    editableInGaUi: bool
    endTime: str
    equalWeighting: bool
    id: str
    internalWebPropertyId: str
    kind: str
    minimumExperimentLengthInDays: int
    name: str
    objectiveMetric: str
    optimizationType: str
    parentLink: dict[str, typing.Any]
    profileId: str
    reasonExperimentEnded: str
    rewriteVariationUrlsAsOriginal: bool
    selfLink: str
    servingFramework: str
    snippet: str
    startTime: str
    status: str
    trafficCoverage: float
    updated: str
    variations: _list[dict[str, typing.Any]]
    webPropertyId: str
    winnerConfidenceLevel: float
    winnerFound: bool

@typing.type_check_only
class Experiments(typing_extensions.TypedDict, total=False):
    items: _list[Experiment]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    accountId: str
    advancedDetails: dict[str, typing.Any]
    created: str
    excludeDetails: FilterExpression
    id: str
    includeDetails: FilterExpression
    kind: str
    lowercaseDetails: dict[str, typing.Any]
    name: str
    parentLink: dict[str, typing.Any]
    searchAndReplaceDetails: dict[str, typing.Any]
    selfLink: str
    type: str
    updated: str
    uppercaseDetails: dict[str, typing.Any]

@typing.type_check_only
class FilterExpression(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    expressionValue: str
    field: str
    fieldIndex: int
    kind: str
    matchType: str

@typing.type_check_only
class FilterRef(typing_extensions.TypedDict, total=False):
    accountId: str
    href: str
    id: str
    kind: str
    name: str

@typing.type_check_only
class Filters(typing_extensions.TypedDict, total=False):
    items: _list[Filter]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class GaData(typing_extensions.TypedDict, total=False):
    columnHeaders: _list[dict[str, typing.Any]]
    containsSampledData: bool
    dataLastRefreshed: str
    dataTable: dict[str, typing.Any]
    id: str
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    profileInfo: dict[str, typing.Any]
    query: dict[str, typing.Any]
    rows: _list[list]
    sampleSize: str
    sampleSpace: str
    selfLink: str
    totalResults: int
    totalsForAllResults: dict[str, typing.Any]

@typing.type_check_only
class Goal(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    created: str
    eventDetails: dict[str, typing.Any]
    id: str
    internalWebPropertyId: str
    kind: str
    name: str
    parentLink: dict[str, typing.Any]
    profileId: str
    selfLink: str
    type: str
    updated: str
    urlDestinationDetails: dict[str, typing.Any]
    value: float
    visitNumPagesDetails: dict[str, typing.Any]
    visitTimeOnSiteDetails: dict[str, typing.Any]
    webPropertyId: str

@typing.type_check_only
class Goals(typing_extensions.TypedDict, total=False):
    items: _list[Goal]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class HashClientIdRequest(typing_extensions.TypedDict, total=False):
    clientId: str
    kind: str
    webPropertyId: str

@typing.type_check_only
class HashClientIdResponse(typing_extensions.TypedDict, total=False):
    clientId: str
    hashedClientId: str
    kind: str
    webPropertyId: str

@typing.type_check_only
class IncludeConditions(typing_extensions.TypedDict, total=False):
    daysToLookBack: int
    isSmartList: bool
    kind: str
    membershipDurationDays: int
    segment: str

@typing.type_check_only
class LinkedForeignAccount(typing_extensions.TypedDict, total=False):
    accountId: str
    eligibleForSearch: bool
    id: str
    internalWebPropertyId: str
    kind: str
    linkedAccountId: str
    remarketingAudienceId: str
    status: str
    type: str
    webPropertyId: str

@typing.type_check_only
class McfData(typing_extensions.TypedDict, total=False):
    columnHeaders: _list[dict[str, typing.Any]]
    containsSampledData: bool
    id: str
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    profileInfo: dict[str, typing.Any]
    query: dict[str, typing.Any]
    rows: _list[list]
    sampleSize: str
    sampleSpace: str
    selfLink: str
    totalResults: int
    totalsForAllResults: dict[str, typing.Any]

@typing.type_check_only
class Profile(typing_extensions.TypedDict, total=False):
    accountId: str
    botFilteringEnabled: bool
    childLink: dict[str, typing.Any]
    created: str
    currency: str
    defaultPage: str
    eCommerceTracking: bool
    enhancedECommerceTracking: bool
    excludeQueryParameters: str
    id: str
    internalWebPropertyId: str
    kind: str
    name: str
    parentLink: dict[str, typing.Any]
    permissions: dict[str, typing.Any]
    selfLink: str
    siteSearchCategoryParameters: str
    siteSearchQueryParameters: str
    starred: bool
    stripSiteSearchCategoryParameters: bool
    stripSiteSearchQueryParameters: bool
    timezone: str
    type: str
    updated: str
    webPropertyId: str
    websiteUrl: str

@typing.type_check_only
class ProfileFilterLink(typing_extensions.TypedDict, total=False):
    filterRef: FilterRef
    id: str
    kind: str
    profileRef: ProfileRef
    rank: int
    selfLink: str

@typing.type_check_only
class ProfileFilterLinks(typing_extensions.TypedDict, total=False):
    items: _list[ProfileFilterLink]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class ProfileRef(typing_extensions.TypedDict, total=False):
    accountId: str
    href: str
    id: str
    internalWebPropertyId: str
    kind: str
    name: str
    webPropertyId: str

@typing.type_check_only
class ProfileSummary(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str
    starred: bool
    type: str

@typing.type_check_only
class Profiles(typing_extensions.TypedDict, total=False):
    items: _list[Profile]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class RealtimeData(typing_extensions.TypedDict, total=False):
    columnHeaders: _list[dict[str, typing.Any]]
    id: str
    kind: str
    profileInfo: dict[str, typing.Any]
    query: dict[str, typing.Any]
    rows: _list[list]
    selfLink: str
    totalResults: int
    totalsForAllResults: dict[str, typing.Any]

@typing.type_check_only
class RemarketingAudience(typing_extensions.TypedDict, total=False):
    accountId: str
    audienceDefinition: dict[str, typing.Any]
    audienceType: str
    created: str
    description: str
    id: str
    internalWebPropertyId: str
    kind: str
    linkedAdAccounts: _list[LinkedForeignAccount]
    linkedViews: _list[str]
    name: str
    stateBasedAudienceDefinition: dict[str, typing.Any]
    updated: str
    webPropertyId: str

@typing.type_check_only
class RemarketingAudiences(typing_extensions.TypedDict, total=False):
    items: _list[RemarketingAudience]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class Segment(typing_extensions.TypedDict, total=False):
    created: str
    definition: str
    id: str
    kind: str
    name: str
    segmentId: str
    selfLink: str
    type: str
    updated: str

@typing.type_check_only
class Segments(typing_extensions.TypedDict, total=False):
    items: _list[Segment]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

AlternativeUnsampledReport = typing_extensions.TypedDict(
    "AlternativeUnsampledReport",
    {
        "accountId": str,
        "cloudStorageDownloadDetails": dict[str, typing.Any],
        "created": str,
        "dimensions": str,
        "downloadType": str,
        "driveDownloadDetails": dict[str, typing.Any],
        "end-date": str,
        "filters": str,
        "id": str,
        "kind": str,
        "metrics": str,
        "profileId": str,
        "segment": str,
        "selfLink": str,
        "start-date": str,
        "status": str,
        "title": str,
        "updated": str,
        "webPropertyId": str,
    },
    total=False,
)

@typing.type_check_only
class UnsampledReport(AlternativeUnsampledReport): ...

@typing.type_check_only
class UnsampledReports(typing_extensions.TypedDict, total=False):
    items: _list[UnsampledReport]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class Upload(typing_extensions.TypedDict, total=False):
    accountId: str
    customDataSourceId: str
    errors: _list[str]
    id: str
    kind: str
    status: str
    uploadTime: str

@typing.type_check_only
class Uploads(typing_extensions.TypedDict, total=False):
    items: _list[Upload]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int

@typing.type_check_only
class UserDeletionRequest(typing_extensions.TypedDict, total=False):
    deletionRequestTime: str
    firebaseProjectId: str
    id: dict[str, typing.Any]
    kind: str
    propertyId: str
    webPropertyId: str

@typing.type_check_only
class UserRef(typing_extensions.TypedDict, total=False):
    email: str
    id: str
    kind: str

@typing.type_check_only
class WebPropertyRef(typing_extensions.TypedDict, total=False):
    accountId: str
    href: str
    id: str
    internalWebPropertyId: str
    kind: str
    name: str

@typing.type_check_only
class WebPropertySummary(typing_extensions.TypedDict, total=False):
    id: str
    internalWebPropertyId: str
    kind: str
    level: str
    name: str
    profiles: _list[ProfileSummary]
    starred: bool
    websiteUrl: str

@typing.type_check_only
class Webproperties(typing_extensions.TypedDict, total=False):
    items: _list[Webproperty]
    itemsPerPage: int
    kind: str
    nextLink: str
    previousLink: str
    startIndex: int
    totalResults: int
    username: str

@typing.type_check_only
class Webproperty(typing_extensions.TypedDict, total=False):
    accountId: str
    childLink: dict[str, typing.Any]
    created: str
    dataRetentionResetOnNewActivity: bool
    dataRetentionTtl: str
    defaultProfileId: str
    id: str
    industryVertical: str
    internalWebPropertyId: str
    kind: str
    level: str
    name: str
    parentLink: dict[str, typing.Any]
    permissions: dict[str, typing.Any]
    profileCount: int
    selfLink: str
    starred: bool
    updated: str
    websiteUrl: str
