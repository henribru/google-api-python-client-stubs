import typing

import typing_extensions

_list = list

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    title: str
    url: str

@typing.type_check_only
class AuditLoggingSettings(typing_extensions.TypedDict, total=False):
    logAdminReadActions: bool
    logDataReadActions: bool
    logDataWriteActions: bool
    project: str

@typing.type_check_only
class BackgroundColoredText(typing_extensions.TypedDict, total=False):
    backgroundColor: typing_extensions.Literal[
        "UNKNOWN_COLOR", "WHITE", "YELLOW", "ORANGE", "GREEN", "BLUE", "GREY"
    ]
    text: str

@typing.type_check_only
class BooleanOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class BooleanPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: BooleanOperatorOptions

@typing.type_check_only
class CheckAccessResponse(typing_extensions.TypedDict, total=False):
    hasAccess: bool

@typing.type_check_only
class CompositeFilter(typing_extensions.TypedDict, total=False):
    logicOperator: typing_extensions.Literal["AND", "OR", "NOT"]
    subFilters: _list[Filter]

@typing.type_check_only
class Content(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    description: SafeHtmlProto
    subtitle: BackgroundColoredText
    title: BackgroundColoredText

@typing.type_check_only
class Context(typing_extensions.TypedDict, total=False):
    app: _list[typing_extensions.Literal["UNKNOWN_APP", "TOPAZ", "MOMA"]]
    dayOfWeek: _list[int]
    endDateSec: str
    endDayOffsetSec: str
    locale: _list[str]
    location: _list[str]
    query: _list[str]
    startDateSec: str
    startDayOffsetSec: str
    surface: _list[
        typing_extensions.Literal[
            "UNKNOWN_SURFACE", "DESKTOP", "ANDROID", "IOS", "MOBILE", "ANY"
        ]
    ]
    type: _list[
        typing_extensions.Literal[
            "UNKNOWN_CARD_TYPE", "HOMEPAGE_CARD", "ANSWER_CARD", "RHS_CARD"
        ]
    ]

@typing.type_check_only
class ContextAttribute(typing_extensions.TypedDict, total=False):
    name: str
    values: _list[str]

@typing.type_check_only
class CustomerIndexStats(typing_extensions.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class CustomerQueryStats(typing_extensions.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class CustomerSearchApplicationStats(typing_extensions.TypedDict, total=False):
    count: str
    date: Date

@typing.type_check_only
class CustomerSessionStats(typing_extensions.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class CustomerSettings(typing_extensions.TypedDict, total=False):
    auditLoggingSettings: AuditLoggingSettings
    vpcSettings: VPCSettings

@typing.type_check_only
class CustomerUserStats(typing_extensions.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    disableModifications: bool
    disableServing: bool
    displayName: str
    indexingServiceAccounts: _list[str]
    itemsVisibility: _list[GSuitePrincipal]
    name: str
    operationIds: _list[str]
    returnThumbnailUrls: bool
    shortName: str

@typing.type_check_only
class DataSourceIndexStats(typing_extensions.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class DataSourceRestriction(typing_extensions.TypedDict, total=False):
    filterOptions: _list[FilterOptions]
    source: Source

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class DatePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DateOperatorOptions

@typing.type_check_only
class DateValues(typing_extensions.TypedDict, total=False):
    values: _list[Date]

@typing.type_check_only
class DebugOptions(typing_extensions.TypedDict, total=False):
    enableDebugging: bool

@typing.type_check_only
class DebugResponse(typing_extensions.TypedDict, total=False):
    gsrRequest: str
    gsrResponse: str
    searchResponse: SearchResponse

@typing.type_check_only
class DeleteQueueItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class DisplayedProperty(typing_extensions.TypedDict, total=False):
    propertyName: str

@typing.type_check_only
class DoubleOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class DoublePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DoubleOperatorOptions

@typing.type_check_only
class DoubleValues(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class DriveFollowUpRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED", "FOLLOWUP_SUGGESTIONS", "FOLLOWUP_ACTION_ITEMS"
    ]

@typing.type_check_only
class DriveLocationRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "TRASHED", "STARRED"]

@typing.type_check_only
class DriveMimeTypeRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "PDF",
        "DOCUMENT",
        "PRESENTATION",
        "SPREADSHEET",
        "FORM",
        "DRAWING",
        "SCRIPT",
        "MAP",
        "IMAGE",
        "AUDIO",
        "VIDEO",
        "FOLDER",
        "ARCHIVE",
        "SITE",
    ]

@typing.type_check_only
class DriveTimeSpanRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "TODAY",
        "YESTERDAY",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
    ]

@typing.type_check_only
class EmailAddress(typing_extensions.TypedDict, total=False):
    customType: str
    emailAddress: str
    emailUrl: str
    primary: bool
    type: str

@typing.type_check_only
class EnterpriseTopazFrontendTeamsLink(typing_extensions.TypedDict, total=False):
    type: str
    url: SafeUrlProto

@typing.type_check_only
class EnterpriseTopazFrontendTeamsPersonCorePhoneNumber(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str
    phoneUrl: SafeUrlProto
    type: typing_extensions.Literal["UNKNOWN", "MOBILE", "OFFICE", "OTHER"]

@typing.type_check_only
class EnterpriseTopazSidekickAgendaEntry(typing_extensions.TypedDict, total=False):
    agendaItemUrl: str
    chronology: typing_extensions.Literal[
        "STALE", "ALL_DAY", "PAST", "RECENTLY_PAST", "PRESENT", "NEAR_FUTURE", "FUTURE"
    ]
    creator: EnterpriseTopazSidekickPerson
    currentUserAttendingStatus: typing_extensions.Literal[
        "AWAITING", "YES", "NO", "MAYBE"
    ]
    description: str
    document: _list[EnterpriseTopazSidekickCommonDocument]
    endDate: str
    endTime: str
    endTimeMs: str
    eventId: str
    guestsCanInviteOthers: bool
    guestsCanModify: bool
    guestsCanSeeGuests: bool
    hangoutId: str
    hangoutUrl: str
    invitee: _list[EnterpriseTopazSidekickPerson]
    isAllDay: bool
    lastModificationTimeMs: str
    location: str
    notifyToUser: bool
    otherAttendeesExcluded: bool
    requesterIsOwner: bool
    showFullEventDetailsToUse: bool
    startDate: str
    startTime: str
    startTimeMs: str
    timeZone: str
    title: str

@typing.type_check_only
class EnterpriseTopazSidekickAgendaGroupCardProto(
    typing_extensions.TypedDict, total=False
):
    agendaItem: _list[EnterpriseTopazSidekickAgendaItem]
    context: EnterpriseTopazSidekickAgendaGroupCardProtoContext
    currentAgendaItem: EnterpriseTopazSidekickAgendaItem

@typing.type_check_only
class EnterpriseTopazSidekickAgendaGroupCardProtoContext(
    typing_extensions.TypedDict, total=False
):
    context: str
    date: str
    eventsRestrict: typing_extensions.Literal["NONE", "NEXT_MEETING"]

@typing.type_check_only
class EnterpriseTopazSidekickAgendaItem(typing_extensions.TypedDict, total=False):
    conflictedGroup: EnterpriseTopazSidekickConflictingEventsCardProto
    gapBefore: EnterpriseTopazSidekickGap
    meeting: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickAnswerAnswerList(typing_extensions.TypedDict, total=False):
    labeledAnswer: _list[EnterpriseTopazSidekickAnswerAnswerListLabeledAnswer]
    type: typing_extensions.Literal[
        "UNKNOWN",
        "PERSON_ADDRESS",
        "PERSON_BIRTHDAY",
        "PERSON_DEPARTMENT",
        "PERSON_DESK_LOCATION",
        "PERSON_EMAIL",
        "PERSON_JOB_TITLE",
        "PERSON_PHONE",
    ]

@typing.type_check_only
class EnterpriseTopazSidekickAnswerAnswerListLabeledAnswer(
    typing_extensions.TypedDict, total=False
):
    answer: str
    label: str

@typing.type_check_only
class EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCard(
    typing_extensions.TypedDict, total=False
):
    suggestedQueryCategory: _list[EnterpriseTopazSidekickAnswerSuggestedQueryCategory]

@typing.type_check_only
class EnterpriseTopazSidekickAnswerSuggestedQueryCategory(
    typing_extensions.TypedDict, total=False
):
    category: typing_extensions.Literal["UNKNOWN", "CALENDAR", "DOCUMENT", "PEOPLE"]
    isEnabled: bool
    query: _list[str]

@typing.type_check_only
class EnterpriseTopazSidekickAssistCardProto(typing_extensions.TypedDict, total=False):
    agendaGroupCardProto: EnterpriseTopazSidekickAgendaGroupCardProto
    cardMetadata: EnterpriseTopazSidekickCardMetadata
    cardType: typing_extensions.Literal[
        "UNKNOWN_TYPE",
        "AGENDA",
        "CHANGELISTS",
        "CONFLICTING_MEETINGS",
        "CREATE_NOTES_FOR_MEETING",
        "CREATE_NOTES_FOR_MEETING_REQUEST",
        "CUSTOMER_NEWS",
        "FIND_MEETING_TIME",
        "NEXT_MEETING",
        "PERSONALIZED_DOCS",
        "TRENDING_DOCS",
        "UPCOMING_TRIP",
        "SUMMARY",
        "MEETINGS",
        "HOMEPAGE",
        "SHARE_MEETING_DOCS",
        "DISCOVER_PEOPLE",
        "HOMEPAGE_V3",
        "AGENDA_GROUP",
        "WORK_IN_PROGRESS",
        "GET_AND_KEEP_AHEAD",
        "GENERIC_ANSWER_CARD",
        "THIRD_PARTY_ANSWER_CARD",
        "DOMAIN_TRENDING_DOCS",
        "TEAM_TRENDING_DOCS",
        "DOCUMENT_LIST_ANSWER_CARD",
        "SUGGESTED_QUERY_ANSWER_CARD",
        "PERSON_ANSWER_CARD",
        "RELATED_PEOPLE_ANSWER_CARD",
        "PERSON_KNOWLEDGE_CARD",
        "PEOPLE_SEARCH_PROMOTION_CARD",
    ]
    conflictingMeetingsCard: EnterpriseTopazSidekickConflictingEventsCardProto
    documentListCard: EnterpriseTopazSidekickDocumentPerCategoryList
    documentsWithMentions: EnterpriseTopazSidekickDocumentPerCategoryList
    findMeetingTimeCard: EnterpriseTopazSidekickFindMeetingTimeCardProto
    genericAnswerCard: EnterpriseTopazSidekickGenericAnswerCard
    getAndKeepAheadCard: EnterpriseTopazSidekickGetAndKeepAheadCardProto
    meeting: EnterpriseTopazSidekickAgendaEntry
    meetingNotesCard: EnterpriseTopazSidekickMeetingNotesCardProto
    meetingNotesCardRequest: EnterpriseTopazSidekickMeetingNotesCardRequest
    peopleDisambiguationCard: EnterpriseTopazSidekickPeopleDisambiguationCard
    peoplePromotionCard: PeoplePromotionCard
    personAnswerCard: EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard
    personProfileCard: EnterpriseTopazSidekickPersonProfileCard
    personalizedDocsCard: EnterpriseTopazSidekickPersonalizedDocsCardProto
    relatedPeopleAnswerCard: EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard
    shareMeetingDocsCard: EnterpriseTopazSidekickShareMeetingDocsCardProto
    sharedDocuments: EnterpriseTopazSidekickDocumentPerCategoryList
    suggestedQueryAnswerCard: EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCard
    thirdPartyAnswerCard: ThirdPartyGenericCard
    workInProgressCardProto: EnterpriseTopazSidekickRecentDocumentsCardProto

@typing.type_check_only
class EnterpriseTopazSidekickCardMetadata(typing_extensions.TypedDict, total=False):
    cardCategory: typing_extensions.Literal[
        "DEFAULT", "ANSWER", "KNOWLEDGE", "HOMEPAGE"
    ]
    cardId: str
    chronology: typing_extensions.Literal[
        "UNKNOWN", "PAST", "RECENTLY_PAST", "PRESENT", "NEAR_FUTURE", "FUTURE"
    ]
    debugInfo: str
    nlpMetadata: EnterpriseTopazSidekickNlpMetadata
    rankingParams: EnterpriseTopazSidekickRankingParams
    renderMode: typing_extensions.Literal["UNKNOWN_RENDER", "COLLAPSED", "EXPANDED"]

@typing.type_check_only
class EnterpriseTopazSidekickCommonDebugInfo(typing_extensions.TypedDict, total=False):
    message: str

@typing.type_check_only
class EnterpriseTopazSidekickCommonDocument(typing_extensions.TypedDict, total=False):
    accessType: typing_extensions.Literal["UNKNOWN_ACCESS", "ALLOWED", "NOT_ALLOWED"]
    debugInfo: EnterpriseTopazSidekickCommonDebugInfo
    documentId: str
    driveDocumentMetadata: EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata
    genericUrl: str
    justification: EnterpriseTopazSidekickCommonDocumentJustification
    mimeType: str
    provenance: typing_extensions.Literal[
        "UNKNOWN_PROVENANCE",
        "CALENDAR_DESCRIPTION",
        "CALENDAR_ATTACHMENT",
        "MINED",
        "CALENDAR_ASSIST_ATTACHMENT",
    ]
    reason: typing_extensions.Literal[
        "UNKNOWN",
        "TRENDING_IN_COLLABORATORS",
        "TRENDING_IN_DOMAIN",
        "FREQUENTLY_VIEWED",
        "FREQUENTLY_EDITED",
        "NEW_UPDATES",
        "NEW_COMMENTS",
        "EVENT_DESCRIPTION",
        "EVENT_ATTACHMENT",
        "EVENT_METADATA_ATTACHMENT",
        "MINED_DOCUMENT",
        "NEW_MENTIONS",
        "NEW_SHARES",
    ]
    snippet: str
    thumbnailUrl: str
    title: str
    type: typing_extensions.Literal[
        "UNKNOWN",
        "DOCUMENT",
        "PRESENTATION",
        "SPREADSHEET",
        "PDF",
        "IMAGE",
        "BINARY_BLOB",
        "FUSION_TABLE",
        "FOLDER",
        "DRAWING",
        "VIDEO",
        "FORM",
        "LINK_URL",
        "LINK_GO",
        "LINK_GOO_GL",
        "LINK_BIT_LY",
        "LINK_GMAIL",
        "LINK_MAILTO",
        "VIDEO_YOUTUBE",
        "VIDEO_LIVE",
        "GROUPS",
        "NEWS",
        "SITES",
        "HANGOUT",
        "AUDIO",
        "MS_WORD",
        "MS_POWERPOINT",
        "MS_EXCEL",
        "MS_OUTLOOK",
    ]
    url: str

@typing.type_check_only
class EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    documentId: str
    isPrivate: bool
    lastCommentTimeMs: str
    lastEditTimeMs: str
    lastModificationTimeMillis: str
    lastUpdatedTimeMs: str
    lastViewTimeMs: str
    owner: EnterpriseTopazSidekickCommonPerson
    scope: typing_extensions.Literal[
        "UNKNOWN_DOCUMENT_SCOPE",
        "LIMITED",
        "DASHER_DOMAIN_WITH_LINK",
        "DASHER_DOMAIN",
        "PUBLIC_WITH_LINK",
        "PUBLIC",
        "TEAM_DRIVE",
    ]

@typing.type_check_only
class EnterpriseTopazSidekickCommonDocumentJustification(
    typing_extensions.TypedDict, total=False
):
    justification: str
    reason: typing_extensions.Literal[
        "UNKNOWN",
        "TRENDING_IN_COLLABORATORS",
        "TRENDING_IN_DOMAIN",
        "FREQUENTLY_VIEWED",
        "FREQUENTLY_EDITED",
        "NEW_UPDATES",
        "NEW_COMMENTS",
        "EVENT_DESCRIPTION",
        "EVENT_ATTACHMENT",
        "EVENT_METADATA_ATTACHMENT",
        "MINED_DOCUMENT",
        "NEW_MENTIONS",
        "NEW_SHARES",
    ]

@typing.type_check_only
class EnterpriseTopazSidekickCommonPerson(typing_extensions.TypedDict, total=False):
    birthday: EnterpriseTopazSidekickCommonPersonBirthday
    cellPhone: str
    department: str
    deskLocation: str
    deskPhone: str
    displayName: str
    email: str
    familyName: str
    fullAddress: str
    gaiaId: str
    givenName: str
    jobTitle: str
    manager: EnterpriseTopazSidekickCommonPerson
    obfuscatedId: str
    photoUrl: str
    streetAddress: str

@typing.type_check_only
class EnterpriseTopazSidekickCommonPersonBirthday(
    typing_extensions.TypedDict, total=False
):
    value: str

@typing.type_check_only
class EnterpriseTopazSidekickConflictingEventsCardProto(
    typing_extensions.TypedDict, total=False
):
    conflictingEvent: _list[EnterpriseTopazSidekickAgendaEntry]
    mainEvent: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickDocumentGroup(typing_extensions.TypedDict, total=False):
    groupType: typing_extensions.Literal["UNKNOWN_TYPE", "ALL"]
    personalizedDocument: _list[EnterpriseTopazSidekickCommonDocument]

@typing.type_check_only
class EnterpriseTopazSidekickDocumentPerCategoryList(
    typing_extensions.TypedDict, total=False
):
    documents: _list[
        EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry
    ]
    helpMessage: str
    listType: typing_extensions.Literal[
        "UNKNOWN_LIST_TYPE", "MENTIONS", "SHARES", "NEEDS_ATTENTION", "VIEWS", "EDITS"
    ]
    listTypeDescription: str
    responseMessage: str

@typing.type_check_only
class EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry(
    typing_extensions.TypedDict, total=False
):
    category: typing_extensions.Literal[
        "UNKNOWN_DOCUMENT",
        "ACTIONABLE",
        "VIEWED",
        "REPLIED",
        "MENTION_VIEWED",
        "MENTION_REPLIED",
        "MENTION_NOT_VIEWED",
        "SHARED_AND_VIEWED",
        "SHARED_NOT_VIEWED",
        "EDITED",
    ]
    document: EnterpriseTopazSidekickCommonDocument
    rationale: str

@typing.type_check_only
class EnterpriseTopazSidekickFindMeetingTimeCardProto(
    typing_extensions.TypedDict, total=False
):
    commonAvailableTimeSlots: _list[EnterpriseTopazSidekickTimeSlot]
    invitees: _list[EnterpriseTopazSidekickPerson]
    requester: EnterpriseTopazSidekickPerson
    scheduledMeeting: EnterpriseTopazSidekickScheduledMeeting
    skippedInvitees: _list[EnterpriseTopazSidekickPerson]
    timeBoundaries: EnterpriseTopazSidekickTimeSlot
    timezoneId: str

@typing.type_check_only
class EnterpriseTopazSidekickGap(typing_extensions.TypedDict, total=False):
    displayRemainingTime: str
    endTime: str
    endTimeMs: str
    remainingTime: str
    startTime: str
    startTimeMs: str

@typing.type_check_only
class EnterpriseTopazSidekickGenericAnswerCard(
    typing_extensions.TypedDict, total=False
):
    answer: str
    title: str

@typing.type_check_only
class EnterpriseTopazSidekickGetAndKeepAheadCardProto(
    typing_extensions.TypedDict, total=False
):
    declinedEvents: EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEvents
    mentionedDocuments: EnterpriseTopazSidekickDocumentPerCategoryList
    sharedDocuments: EnterpriseTopazSidekickDocumentPerCategoryList

@typing.type_check_only
class EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEvents(
    typing_extensions.TypedDict, total=False
):
    events: _list[EnterpriseTopazSidekickAgendaEntry]

@typing.type_check_only
class EnterpriseTopazSidekickMeetingNotesCardError(
    typing_extensions.TypedDict, total=False
):
    description: str
    event: EnterpriseTopazSidekickAgendaEntry
    reason: typing_extensions.Literal["NONE", "NOT_OWNER", "UNKNOWN"]

@typing.type_check_only
class EnterpriseTopazSidekickMeetingNotesCardProto(
    typing_extensions.TypedDict, total=False
):
    event: EnterpriseTopazSidekickAgendaEntry
    fileId: str
    title: str
    url: str

@typing.type_check_only
class EnterpriseTopazSidekickMeetingNotesCardRequest(
    typing_extensions.TypedDict, total=False
):
    canCreateFor: _list[typing_extensions.Literal["UNKNOWN", "MYSELF", "ALL_ATTENDEES"]]
    error: EnterpriseTopazSidekickMeetingNotesCardError
    event: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickNlpMetadata(typing_extensions.TypedDict, total=False):
    confidence: float

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo(
    typing_extensions.TypedDict, total=False
):
    disambiguation: _list[
        EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPerson
    ]
    name: str

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPerson(
    typing_extensions.TypedDict, total=False
):
    person: EnterpriseTopazSidekickCommonPerson
    query: str

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader(
    typing_extensions.TypedDict, total=False
):
    title: str

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard(
    typing_extensions.TypedDict, total=False
):
    answer: _list[SafeHtmlProto]
    answerText: EnterpriseTopazSidekickAnswerAnswerList
    disambiguationInfo: EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo
    header: EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader
    responseStatus: typing_extensions.Literal[
        "UNKNOWN", "SUCCESS", "MISSING_PERSON", "MISSING_DATA"
    ]
    statusMessage: str
    subject: EnterpriseTopazSidekickCommonPerson

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard(
    typing_extensions.TypedDict, total=False
):
    disambiguationInfo: EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo
    header: EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader
    relatedPeople: _list[EnterpriseTopazSidekickCommonPerson]
    relationType: typing_extensions.Literal[
        "UNKNOWN", "DIRECT_REPORTS", "MANAGER", "PEERS"
    ]
    responseStatus: typing_extensions.Literal[
        "UNKNOWN", "SUCCESS", "MISSING_PERSON", "MISSING_DATA"
    ]
    statusMessage: str
    subject: EnterpriseTopazSidekickCommonPerson

@typing.type_check_only
class EnterpriseTopazSidekickPeopleDisambiguationCard(
    typing_extensions.TypedDict, total=False
):
    person: _list[EnterpriseTopazSidekickCommonPerson]

@typing.type_check_only
class EnterpriseTopazSidekickPerson(typing_extensions.TypedDict, total=False):
    affinityLevel: typing_extensions.Literal["UNKNOWN", "LOW", "MEDIUM", "HIGH"]
    attendingStatus: typing_extensions.Literal["AWAITING", "YES", "NO", "MAYBE"]
    email: str
    gaiaId: str
    isGroup: bool
    name: str
    obfuscatedGaiaId: str
    photoUrl: str

@typing.type_check_only
class EnterpriseTopazSidekickPersonProfileCard(
    typing_extensions.TypedDict, total=False
):
    relatedPeople: _list[EnterpriseTopazSidekickPersonProfileCardRelatedPeople]
    subject: EnterpriseTopazSidekickCommonPerson

@typing.type_check_only
class EnterpriseTopazSidekickPersonProfileCardRelatedPeople(
    typing_extensions.TypedDict, total=False
):
    relatedPerson: _list[EnterpriseTopazSidekickCommonPerson]
    relation: typing_extensions.Literal["UNKNOWN", "MANAGER", "DIRECT_REPORT"]

@typing.type_check_only
class EnterpriseTopazSidekickPersonalizedDocsCardProto(
    typing_extensions.TypedDict, total=False
):
    documentGroup: _list[EnterpriseTopazSidekickDocumentGroup]

@typing.type_check_only
class EnterpriseTopazSidekickRankingParams(typing_extensions.TypedDict, total=False):
    endTimeMs: str
    priority: typing_extensions.Literal[
        "UNKNOWN", "CRITICAL", "IMPORTANT", "HIGH", "NORMAL", "BEST_EFFORT"
    ]
    score: float
    spanMs: str
    startTimeMs: str
    type: typing_extensions.Literal["FIXED", "FLEXIBLE"]

@typing.type_check_only
class EnterpriseTopazSidekickRecentDocumentsCardProto(
    typing_extensions.TypedDict, total=False
):
    document: _list[EnterpriseTopazSidekickCommonDocument]

@typing.type_check_only
class EnterpriseTopazSidekickScheduledMeeting(typing_extensions.TypedDict, total=False):
    meetingLocation: str
    meetingTime: EnterpriseTopazSidekickTimeSlot
    meetingTitle: str

@typing.type_check_only
class EnterpriseTopazSidekickShareMeetingDocsCardProto(
    typing_extensions.TypedDict, total=False
):
    document: _list[EnterpriseTopazSidekickCommonDocument]
    event: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickTimeSlot(typing_extensions.TypedDict, total=False):
    endTimeDay: str
    endTimeHourAndMinute: str
    endTimeInMillis: str
    startTimeDay: str
    startTimeHourAndMinute: str
    startTimeInMillis: str

@typing.type_check_only
class EnumOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class EnumPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: EnumOperatorOptions
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]
    possibleValues: _list[EnumValuePair]

@typing.type_check_only
class EnumValuePair(typing_extensions.TypedDict, total=False):
    integerValue: int
    stringValue: str

@typing.type_check_only
class EnumValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ErrorInfo(typing_extensions.TypedDict, total=False):
    errorMessages: _list[ErrorMessage]

@typing.type_check_only
class ErrorMessage(typing_extensions.TypedDict, total=False):
    errorMessage: str
    source: Source

@typing.type_check_only
class FacetBucket(typing_extensions.TypedDict, total=False):
    count: int
    filter: Filter
    percentage: int
    value: Value

@typing.type_check_only
class FacetOptions(typing_extensions.TypedDict, total=False):
    integerFacetingOptions: IntegerFacetingOptions
    numFacetBuckets: int
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FacetResult(typing_extensions.TypedDict, total=False):
    buckets: _list[FacetBucket]
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FieldViolation(typing_extensions.TypedDict, total=False):
    description: str
    field: str

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    compositeFilter: CompositeFilter
    valueFilter: ValueFilter

@typing.type_check_only
class FilterOptions(typing_extensions.TypedDict, total=False):
    filter: Filter
    objectType: str

@typing.type_check_only
class FreshnessOptions(typing_extensions.TypedDict, total=False):
    freshnessDuration: str
    freshnessProperty: str

@typing.type_check_only
class GSuitePrincipal(typing_extensions.TypedDict, total=False):
    gsuiteDomain: bool
    gsuiteGroupEmail: str
    gsuiteUserEmail: str

@typing.type_check_only
class GetCustomerIndexStatsResponse(typing_extensions.TypedDict, total=False):
    averageIndexedItemCount: str
    stats: _list[CustomerIndexStats]

@typing.type_check_only
class GetCustomerQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerQueryStats]
    totalQueryCount: str

@typing.type_check_only
class GetCustomerSearchApplicationStatsResponse(
    typing_extensions.TypedDict, total=False
):
    averageSearchApplicationCount: str
    stats: _list[CustomerSearchApplicationStats]

@typing.type_check_only
class GetCustomerSessionStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerSessionStats]

@typing.type_check_only
class GetCustomerUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerUserStats]

@typing.type_check_only
class GetDataSourceIndexStatsResponse(typing_extensions.TypedDict, total=False):
    averageIndexedItemCount: str
    stats: _list[DataSourceIndexStats]

@typing.type_check_only
class GetSearchApplicationQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[SearchApplicationQueryStats]
    totalQueryCount: str

@typing.type_check_only
class GetSearchApplicationSessionStatsResponse(
    typing_extensions.TypedDict, total=False
):
    stats: _list[SearchApplicationSessionStats]

@typing.type_check_only
class GetSearchApplicationUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[SearchApplicationUserStats]

@typing.type_check_only
class HtmlOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class HtmlPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: HtmlOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class HtmlValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class IndexItemOptions(typing_extensions.TypedDict, total=False):
    allowUnknownGsuitePrincipals: bool

@typing.type_check_only
class IndexItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    indexItemOptions: IndexItemOptions
    item: Item
    mode: typing_extensions.Literal["UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"]

@typing.type_check_only
class InitializeCustomerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class IntegerFacetingOptions(typing_extensions.TypedDict, total=False):
    integerBuckets: _list[str]

@typing.type_check_only
class IntegerOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class IntegerPropertyOptions(typing_extensions.TypedDict, total=False):
    integerFacetingOptions: IntegerFacetingOptions
    maximumValue: str
    minimumValue: str
    operatorOptions: IntegerOperatorOptions
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class IntegerValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class Interaction(typing_extensions.TypedDict, total=False):
    interactionTime: str
    principal: Principal
    type: typing_extensions.Literal["UNSPECIFIED", "VIEW", "EDIT"]

@typing.type_check_only
class Item(typing_extensions.TypedDict, total=False):
    acl: ItemAcl
    content: ItemContent
    itemType: typing_extensions.Literal[
        "UNSPECIFIED", "CONTENT_ITEM", "CONTAINER_ITEM", "VIRTUAL_CONTAINER_ITEM"
    ]
    metadata: ItemMetadata
    name: str
    payload: str
    queue: str
    status: ItemStatus
    structuredData: ItemStructuredData
    version: str

@typing.type_check_only
class ItemAcl(typing_extensions.TypedDict, total=False):
    aclInheritanceType: typing_extensions.Literal[
        "NOT_APPLICABLE", "CHILD_OVERRIDE", "PARENT_OVERRIDE", "BOTH_PERMIT"
    ]
    deniedReaders: _list[Principal]
    inheritAclFrom: str
    owners: _list[Principal]
    readers: _list[Principal]

@typing.type_check_only
class ItemContent(typing_extensions.TypedDict, total=False):
    contentDataRef: UploadItemRef
    contentFormat: typing_extensions.Literal["UNSPECIFIED", "HTML", "TEXT", "RAW"]
    hash: str
    inlineContent: str

@typing.type_check_only
class ItemCountByStatus(typing_extensions.TypedDict, total=False):
    count: str
    indexedItemsCount: str
    statusCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]

@typing.type_check_only
class ItemMetadata(typing_extensions.TypedDict, total=False):
    containerName: str
    contentLanguage: str
    contextAttributes: _list[ContextAttribute]
    createTime: str
    hash: str
    interactions: _list[Interaction]
    keywords: _list[str]
    mimeType: str
    objectType: str
    searchQualityMetadata: SearchQualityMetadata
    sourceRepositoryUrl: str
    title: str
    updateTime: str

@typing.type_check_only
class ItemStatus(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]
    processingErrors: _list[ProcessingError]
    repositoryErrors: _list[RepositoryError]

@typing.type_check_only
class ItemStructuredData(typing_extensions.TypedDict, total=False):
    hash: str
    object: StructuredDataObject

@typing.type_check_only
class ListDataSourceResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[DataSource]

@typing.type_check_only
class ListItemNamesForUnmappedIdentityResponse(
    typing_extensions.TypedDict, total=False
):
    itemNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListItemsResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListQuerySourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[QuerySource]

@typing.type_check_only
class ListSearchApplicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    searchApplications: _list[SearchApplication]

@typing.type_check_only
class ListUnmappedIdentitiesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unmappedIdentities: _list[UnmappedIdentity]

@typing.type_check_only
class MapInfo(typing_extensions.TypedDict, total=False):
    lat: float
    locationUrl: SafeUrlProto
    long: float
    mapTile: _list[MapTile]
    zoom: int

@typing.type_check_only
class MapTile(typing_extensions.TypedDict, total=False):
    imageUrl: SafeUrlProto
    tileX: float
    tileY: float

@typing.type_check_only
class MatchRange(typing_extensions.TypedDict, total=False):
    end: int
    start: int

@typing.type_check_only
class Media(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    createTime: str
    displayOptions: ResultDisplayMetadata
    fields: _list[NamedProperty]
    mimeType: str
    objectType: str
    owner: Person
    source: Source
    thumbnailUrl: str
    updateTime: str

@typing.type_check_only
class Metaline(typing_extensions.TypedDict, total=False):
    properties: _list[DisplayedProperty]

@typing.type_check_only
class Name(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class NamedProperty(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    dateValues: DateValues
    doubleValues: DoubleValues
    enumValues: EnumValues
    htmlValues: HtmlValues
    integerValues: IntegerValues
    name: str
    objectValues: ObjectValues
    textValues: TextValues
    timestampValues: TimestampValues

@typing.type_check_only
class ObjectDefinition(typing_extensions.TypedDict, total=False):
    name: str
    options: ObjectOptions
    propertyDefinitions: _list[PropertyDefinition]

@typing.type_check_only
class ObjectDisplayOptions(typing_extensions.TypedDict, total=False):
    metalines: _list[Metaline]
    objectDisplayLabel: str

@typing.type_check_only
class ObjectOptions(typing_extensions.TypedDict, total=False):
    displayOptions: ObjectDisplayOptions
    freshnessOptions: FreshnessOptions
    suggestionFilteringOperators: _list[str]

@typing.type_check_only
class ObjectPropertyOptions(typing_extensions.TypedDict, total=False):
    subobjectProperties: _list[PropertyDefinition]

@typing.type_check_only
class ObjectValues(typing_extensions.TypedDict, total=False):
    values: _list[StructuredDataObject]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PeoplePromotionCard(typing_extensions.TypedDict, total=False):
    people: _list[PersonCore]

@typing.type_check_only
class PeopleSuggestion(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class Person(typing_extensions.TypedDict, total=False):
    emailAddresses: _list[EmailAddress]
    name: str
    obfuscatedId: str
    personNames: _list[Name]
    phoneNumbers: _list[PhoneNumber]
    photos: _list[Photo]

@typing.type_check_only
class PersonCore(typing_extensions.TypedDict, total=False):
    addressMeAs: str
    adminTo: _list[PersonCore]
    admins: _list[PersonCore]
    availabilityStatus: typing_extensions.Literal[
        "UNKNOWN", "OUT_OF_OFFICE", "OUTSIDE_WORKING_HOURS", "AVAILABLE"
    ]
    birthday: Date
    calendarUrl: SafeUrlProto
    chatUrl: SafeUrlProto
    costCenter: str
    department: str
    directReports: _list[PersonCore]
    dottedLineManagers: _list[PersonCore]
    dottedLineReports: _list[PersonCore]
    emails: _list[str]
    employeeId: str
    fingerprint: str
    ftePermille: str
    geoLocation: MapInfo
    gmailUrl: str
    jobTitle: str
    keywordTypes: _list[str]
    keywords: dict[str, typing.Any]
    links: _list[EnterpriseTopazFrontendTeamsLink]
    location: str
    managers: _list[PersonCore]
    mission: str
    name: str
    officeLocation: str
    personId: str
    phoneNumbers: _list[EnterpriseTopazFrontendTeamsPersonCorePhoneNumber]
    photoUrl: SafeUrlProto
    postalAddress: str
    totalDirectReportsCount: int
    totalDlrCount: int
    totalFteCount: str
    username: str
    waldoComeBackTime: str

@typing.type_check_only
class PhoneNumber(typing_extensions.TypedDict, total=False):
    phoneNumber: str
    type: typing_extensions.Literal["OTHER", "MOBILE", "OFFICE"]

@typing.type_check_only
class Photo(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class PollItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    limit: int
    queue: str
    statusCodes: _list[
        typing_extensions.Literal[
            "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
        ]
    ]

@typing.type_check_only
class PollItemsResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]

@typing.type_check_only
class Principal(typing_extensions.TypedDict, total=False):
    groupResourceName: str
    gsuitePrincipal: GSuitePrincipal
    userResourceName: str

@typing.type_check_only
class ProcessingError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "PROCESSING_ERROR_CODE_UNSPECIFIED",
        "MALFORMED_REQUEST",
        "UNSUPPORTED_CONTENT_FORMAT",
        "INDIRECT_BROKEN_ACL",
        "ACL_CYCLE",
    ]
    errorMessage: str
    fieldViolations: _list[FieldViolation]

@typing.type_check_only
class PropertyDefinition(typing_extensions.TypedDict, total=False):
    booleanPropertyOptions: BooleanPropertyOptions
    datePropertyOptions: DatePropertyOptions
    displayOptions: PropertyDisplayOptions
    doublePropertyOptions: DoublePropertyOptions
    enumPropertyOptions: EnumPropertyOptions
    htmlPropertyOptions: HtmlPropertyOptions
    integerPropertyOptions: IntegerPropertyOptions
    isFacetable: bool
    isRepeatable: bool
    isReturnable: bool
    isSortable: bool
    isSuggestable: bool
    isWildcardSearchable: bool
    name: str
    objectPropertyOptions: ObjectPropertyOptions
    textPropertyOptions: TextPropertyOptions
    timestampPropertyOptions: TimestampPropertyOptions

@typing.type_check_only
class PropertyDisplayOptions(typing_extensions.TypedDict, total=False):
    displayLabel: str

@typing.type_check_only
class PushItem(typing_extensions.TypedDict, total=False):
    contentHash: str
    metadataHash: str
    payload: str
    queue: str
    repositoryError: RepositoryError
    structuredDataHash: str
    type: typing_extensions.Literal[
        "UNSPECIFIED", "MODIFIED", "NOT_MODIFIED", "REPOSITORY_ERROR", "REQUEUE"
    ]

@typing.type_check_only
class PushItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    item: PushItem

@typing.type_check_only
class QueryActivity(typing_extensions.TypedDict, total=False):
    query: str

@typing.type_check_only
class QueryCountByStatus(typing_extensions.TypedDict, total=False):
    count: str
    statusCode: int

@typing.type_check_only
class QueryInterpretation(typing_extensions.TypedDict, total=False):
    interpretationType: typing_extensions.Literal["NONE", "BLEND", "REPLACE"]
    interpretedQuery: str
    reason: typing_extensions.Literal[
        "UNSPECIFIED",
        "QUERY_HAS_NATURAL_LANGUAGE_INTENT",
        "NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY",
    ]

@typing.type_check_only
class QueryInterpretationConfig(typing_extensions.TypedDict, total=False):
    forceDisableSupplementalResults: bool
    forceVerbatimMode: bool

@typing.type_check_only
class QueryInterpretationOptions(typing_extensions.TypedDict, total=False):
    disableNlInterpretation: bool
    disableSupplementalResults: bool
    enableVerbatimMode: bool

@typing.type_check_only
class QueryItem(typing_extensions.TypedDict, total=False):
    isSynthetic: bool

@typing.type_check_only
class QueryOperator(typing_extensions.TypedDict, total=False):
    displayName: str
    enumValues: _list[str]
    greaterThanOperatorName: str
    isFacetable: bool
    isRepeatable: bool
    isReturnable: bool
    isSortable: bool
    isSuggestable: bool
    lessThanOperatorName: str
    objectType: str
    operatorName: str
    type: typing_extensions.Literal[
        "UNKNOWN",
        "INTEGER",
        "DOUBLE",
        "TIMESTAMP",
        "BOOLEAN",
        "ENUM",
        "DATE",
        "TEXT",
        "HTML",
    ]

@typing.type_check_only
class QuerySource(typing_extensions.TypedDict, total=False):
    displayName: str
    operators: _list[QueryOperator]
    shortName: str
    source: Source

@typing.type_check_only
class QuerySuggestion(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveActivityRequest(typing_extensions.TypedDict, total=False):
    requestOptions: RequestOptions
    userActivity: UserActivity

@typing.type_check_only
class RemoveActivityResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RepositoryError(typing_extensions.TypedDict, total=False):
    errorMessage: str
    httpStatusCode: int
    type: typing_extensions.Literal[
        "UNKNOWN",
        "NETWORK_ERROR",
        "DNS_ERROR",
        "CONNECTION_ERROR",
        "AUTHENTICATION_ERROR",
        "AUTHORIZATION_ERROR",
        "SERVER_ERROR",
        "QUOTA_EXCEEDED",
        "SERVICE_UNAVAILABLE",
        "CLIENT_ERROR",
    ]

@typing.type_check_only
class RequestOptions(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    languageCode: str
    searchApplicationId: str
    timeZone: str

@typing.type_check_only
class ResetSearchApplicationRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions

@typing.type_check_only
class ResponseDebugInfo(typing_extensions.TypedDict, total=False):
    formattedDebugInfo: str

@typing.type_check_only
class RestrictItem(typing_extensions.TypedDict, total=False):
    driveFollowUpRestrict: DriveFollowUpRestrict
    driveLocationRestrict: DriveLocationRestrict
    driveMimeTypeRestrict: DriveMimeTypeRestrict
    driveTimeSpanRestrict: DriveTimeSpanRestrict
    searchOperator: str

@typing.type_check_only
class ResultCounts(typing_extensions.TypedDict, total=False):
    sourceResultCounts: _list[SourceResultCount]

@typing.type_check_only
class ResultDebugInfo(typing_extensions.TypedDict, total=False):
    formattedDebugInfo: str

@typing.type_check_only
class ResultDisplayField(typing_extensions.TypedDict, total=False):
    label: str
    operatorName: str
    property: NamedProperty

@typing.type_check_only
class ResultDisplayLine(typing_extensions.TypedDict, total=False):
    fields: _list[ResultDisplayField]

@typing.type_check_only
class ResultDisplayMetadata(typing_extensions.TypedDict, total=False):
    metalines: _list[ResultDisplayLine]
    objectTypeLabel: str

@typing.type_check_only
class RetrievalImportance(typing_extensions.TypedDict, total=False):
    importance: typing_extensions.Literal["DEFAULT", "HIGHEST", "HIGH", "LOW", "NONE"]

@typing.type_check_only
class SafeHtmlProto(typing_extensions.TypedDict, total=False):
    privateDoNotAccessOrElseSafeHtmlWrappedValue: str

@typing.type_check_only
class SafeUrlProto(typing_extensions.TypedDict, total=False):
    privateDoNotAccessOrElseSafeUrlWrappedValue: str

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    objectDefinitions: _list[ObjectDefinition]
    operationIds: _list[str]

@typing.type_check_only
class ScoringConfig(typing_extensions.TypedDict, total=False):
    disableFreshness: bool
    disablePersonalization: bool

@typing.type_check_only
class SearchApplication(typing_extensions.TypedDict, total=False):
    dataSourceRestrictions: _list[DataSourceRestriction]
    defaultFacetOptions: _list[FacetOptions]
    defaultSortOptions: SortOptions
    displayName: str
    enableAuditLog: bool
    name: str
    operationIds: _list[str]
    queryInterpretationConfig: QueryInterpretationConfig
    returnResultThumbnailUrls: bool
    scoringConfig: ScoringConfig
    sourceConfig: _list[SourceConfig]

@typing.type_check_only
class SearchApplicationQueryStats(typing_extensions.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class SearchApplicationSessionStats(typing_extensions.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class SearchApplicationUserStats(typing_extensions.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class SearchItemsByViewUrlRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    pageToken: str
    viewUrl: str

@typing.type_check_only
class SearchItemsByViewUrlResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class SearchQualityMetadata(typing_extensions.TypedDict, total=False):
    quality: float

@typing.type_check_only
class SearchRequest(typing_extensions.TypedDict, total=False):
    contextAttributes: _list[ContextAttribute]
    dataSourceRestrictions: _list[DataSourceRestriction]
    facetOptions: _list[FacetOptions]
    pageSize: int
    query: str
    queryInterpretationOptions: QueryInterpretationOptions
    requestOptions: RequestOptions
    sortOptions: SortOptions
    start: int

@typing.type_check_only
class SearchResponse(typing_extensions.TypedDict, total=False):
    debugInfo: ResponseDebugInfo
    errorInfo: ErrorInfo
    facetResults: _list[FacetResult]
    hasMoreResults: bool
    queryInterpretation: QueryInterpretation
    resultCountEstimate: str
    resultCountExact: str
    resultCounts: ResultCounts
    results: _list[SearchResult]
    spellResults: _list[SpellResult]
    structuredResults: _list[StructuredResult]

@typing.type_check_only
class SearchResult(typing_extensions.TypedDict, total=False):
    clusteredResults: _list[SearchResult]
    debugInfo: ResultDebugInfo
    metadata: Metadata
    snippet: Snippet
    title: str
    url: str

@typing.type_check_only
class Snippet(typing_extensions.TypedDict, total=False):
    matchRanges: _list[MatchRange]
    snippet: str

@typing.type_check_only
class SortOptions(typing_extensions.TypedDict, total=False):
    operatorName: str
    sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"]

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    name: str
    predefinedSource: typing_extensions.Literal[
        "NONE",
        "QUERY_HISTORY",
        "PERSON",
        "GOOGLE_DRIVE",
        "GOOGLE_GMAIL",
        "GOOGLE_SITES",
        "GOOGLE_GROUPS",
        "GOOGLE_CALENDAR",
        "GOOGLE_KEEP",
    ]

@typing.type_check_only
class SourceConfig(typing_extensions.TypedDict, total=False):
    crowdingConfig: SourceCrowdingConfig
    scoringConfig: SourceScoringConfig
    source: Source

@typing.type_check_only
class SourceCrowdingConfig(typing_extensions.TypedDict, total=False):
    numResults: int
    numSuggestions: int

@typing.type_check_only
class SourceResultCount(typing_extensions.TypedDict, total=False):
    hasMoreResults: bool
    resultCountEstimate: str
    resultCountExact: str
    source: Source

@typing.type_check_only
class SourceScoringConfig(typing_extensions.TypedDict, total=False):
    sourceImportance: typing_extensions.Literal["DEFAULT", "LOW", "HIGH"]

@typing.type_check_only
class SpellResult(typing_extensions.TypedDict, total=False):
    suggestedQuery: str
    suggestedQueryHtml: SafeHtmlProto
    suggestionType: typing_extensions.Literal[
        "SUGGESTION_TYPE_UNSPECIFIED",
        "NON_EMPTY_RESULTS_SPELL_SUGGESTION",
        "ZERO_RESULTS_FULL_PAGE_REPLACEMENT",
    ]

@typing.type_check_only
class StartUploadItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructuredDataObject(typing_extensions.TypedDict, total=False):
    properties: _list[NamedProperty]

@typing.type_check_only
class StructuredResult(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class SuggestRequest(typing_extensions.TypedDict, total=False):
    dataSourceRestrictions: _list[DataSourceRestriction]
    query: str
    requestOptions: RequestOptions

@typing.type_check_only
class SuggestResponse(typing_extensions.TypedDict, total=False):
    suggestResults: _list[SuggestResult]

@typing.type_check_only
class SuggestResult(typing_extensions.TypedDict, total=False):
    peopleSuggestion: PeopleSuggestion
    querySuggestion: QuerySuggestion
    source: Source
    suggestedQuery: str

@typing.type_check_only
class TextOperatorOptions(typing_extensions.TypedDict, total=False):
    exactMatchWithOperator: bool
    operatorName: str

@typing.type_check_only
class TextPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: TextOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class TextValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ThirdPartyGenericCard(typing_extensions.TypedDict, total=False):
    cardId: str
    category: str
    content: Content
    context: Context
    isDismissible: bool
    priority: int

@typing.type_check_only
class TimestampOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class TimestampPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: TimestampOperatorOptions

@typing.type_check_only
class TimestampValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class UnmappedIdentity(typing_extensions.TypedDict, total=False):
    externalIdentity: Principal
    resolutionStatusCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "NOT_FOUND",
        "IDENTITY_SOURCE_NOT_FOUND",
        "IDENTITY_SOURCE_MISCONFIGURED",
        "TOO_MANY_MAPPINGS_FOUND",
        "INTERNAL_ERROR",
    ]

@typing.type_check_only
class UnreserveItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class UpdateDataSourceRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    source: DataSource
    updateMask: str

@typing.type_check_only
class UpdateSchemaRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    schema: Schema
    validateOnly: bool

@typing.type_check_only
class UploadItemRef(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class UserActivity(typing_extensions.TypedDict, total=False):
    queryActivity: QueryActivity

@typing.type_check_only
class VPCSettings(typing_extensions.TypedDict, total=False):
    project: str

@typing.type_check_only
class Value(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    dateValue: Date
    doubleValue: float
    integerValue: str
    stringValue: str
    timestampValue: str

@typing.type_check_only
class ValueFilter(typing_extensions.TypedDict, total=False):
    operatorName: str
    value: Value
