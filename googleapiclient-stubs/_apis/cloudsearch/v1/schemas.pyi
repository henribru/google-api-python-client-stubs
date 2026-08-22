import typing

_list = list

@typing.type_check_only
class Action(typing.TypedDict, total=False):
    title: str
    url: str

@typing.type_check_only
class AuditLoggingSettings(typing.TypedDict, total=False):
    logAdminReadActions: bool
    logDataReadActions: bool
    logDataWriteActions: bool
    project: str

@typing.type_check_only
class BackgroundColoredText(typing.TypedDict, total=False):
    backgroundColor: typing.Literal[
        "UNKNOWN_COLOR", "WHITE", "YELLOW", "ORANGE", "GREEN", "BLUE", "GREY"
    ]
    text: str

@typing.type_check_only
class BooleanOperatorOptions(typing.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class BooleanPropertyOptions(typing.TypedDict, total=False):
    operatorOptions: BooleanOperatorOptions

@typing.type_check_only
class CheckAccessResponse(typing.TypedDict, total=False):
    hasAccess: bool

@typing.type_check_only
class CompositeFilter(typing.TypedDict, total=False):
    logicOperator: typing.Literal["AND", "OR", "NOT"]
    subFilters: _list[Filter]

@typing.type_check_only
class Content(typing.TypedDict, total=False):
    actions: _list[Action]
    description: SafeHtmlProto
    subtitle: BackgroundColoredText
    title: BackgroundColoredText

@typing.type_check_only
class Context(typing.TypedDict, total=False):
    app: _list[typing.Literal["UNKNOWN_APP", "TOPAZ", "MOMA"]]
    dayOfWeek: _list[int]
    endDateSec: str
    endDayOffsetSec: str
    locale: _list[str]
    location: _list[str]
    query: _list[str]
    startDateSec: str
    startDayOffsetSec: str
    surface: _list[
        typing.Literal["UNKNOWN_SURFACE", "DESKTOP", "ANDROID", "IOS", "MOBILE", "ANY"]
    ]
    type: _list[
        typing.Literal["UNKNOWN_CARD_TYPE", "HOMEPAGE_CARD", "ANSWER_CARD", "RHS_CARD"]
    ]

@typing.type_check_only
class ContextAttribute(typing.TypedDict, total=False):
    name: str
    values: _list[str]

@typing.type_check_only
class CustomerIndexStats(typing.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class CustomerQueryStats(typing.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class CustomerSearchApplicationStats(typing.TypedDict, total=False):
    count: str
    date: Date

@typing.type_check_only
class CustomerSessionStats(typing.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class CustomerSettings(typing.TypedDict, total=False):
    auditLoggingSettings: AuditLoggingSettings
    vpcSettings: VPCSettings

@typing.type_check_only
class CustomerUserStats(typing.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class DataSource(typing.TypedDict, total=False):
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
class DataSourceIndexStats(typing.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class DataSourceRestriction(typing.TypedDict, total=False):
    filterOptions: _list[FilterOptions]
    source: Source

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateOperatorOptions(typing.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class DatePropertyOptions(typing.TypedDict, total=False):
    operatorOptions: DateOperatorOptions

@typing.type_check_only
class DateValues(typing.TypedDict, total=False):
    values: _list[Date]

@typing.type_check_only
class DebugOptions(typing.TypedDict, total=False):
    enableDebugging: bool

@typing.type_check_only
class DeleteQueueItemsRequest(typing.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class DisplayedProperty(typing.TypedDict, total=False):
    propertyName: str

@typing.type_check_only
class DoubleOperatorOptions(typing.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class DoublePropertyOptions(typing.TypedDict, total=False):
    operatorOptions: DoubleOperatorOptions

@typing.type_check_only
class DoubleValues(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class DriveFollowUpRestrict(typing.TypedDict, total=False):
    type: typing.Literal["UNSPECIFIED", "FOLLOWUP_SUGGESTIONS", "FOLLOWUP_ACTION_ITEMS"]

@typing.type_check_only
class DriveLocationRestrict(typing.TypedDict, total=False):
    type: typing.Literal["UNSPECIFIED", "TRASHED", "STARRED"]

@typing.type_check_only
class DriveMimeTypeRestrict(typing.TypedDict, total=False):
    type: typing.Literal[
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
class DriveTimeSpanRestrict(typing.TypedDict, total=False):
    type: typing.Literal[
        "UNSPECIFIED",
        "TODAY",
        "YESTERDAY",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
    ]

@typing.type_check_only
class EmailAddress(typing.TypedDict, total=False):
    customType: str
    emailAddress: str
    emailUrl: str
    primary: bool
    type: str

@typing.type_check_only
class EnterpriseTopazFrontendTeamsLink(typing.TypedDict, total=False):
    type: str
    url: SafeUrlProto

@typing.type_check_only
class EnterpriseTopazFrontendTeamsPersonCorePhoneNumber(typing.TypedDict, total=False):
    phoneNumber: str
    phoneUrl: SafeUrlProto
    type: typing.Literal["UNKNOWN", "MOBILE", "OFFICE", "OTHER"]

@typing.type_check_only
class EnterpriseTopazSidekickAgendaEntry(typing.TypedDict, total=False):
    agendaItemUrl: str
    chronology: typing.Literal[
        "STALE", "ALL_DAY", "PAST", "RECENTLY_PAST", "PRESENT", "NEAR_FUTURE", "FUTURE"
    ]
    creator: EnterpriseTopazSidekickPerson
    currentUserAttendingStatus: typing.Literal["AWAITING", "YES", "NO", "MAYBE"]
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
class EnterpriseTopazSidekickAgendaGroupCardProto(typing.TypedDict, total=False):
    agendaItem: _list[EnterpriseTopazSidekickAgendaItem]
    context: EnterpriseTopazSidekickAgendaGroupCardProtoContext
    currentAgendaItem: EnterpriseTopazSidekickAgendaItem

@typing.type_check_only
class EnterpriseTopazSidekickAgendaGroupCardProtoContext(typing.TypedDict, total=False):
    context: str
    date: str
    eventsRestrict: typing.Literal["NONE", "NEXT_MEETING"]

@typing.type_check_only
class EnterpriseTopazSidekickAgendaItem(typing.TypedDict, total=False):
    conflictedGroup: EnterpriseTopazSidekickConflictingEventsCardProto
    gapBefore: EnterpriseTopazSidekickGap
    meeting: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickAnswerAnswerList(typing.TypedDict, total=False):
    labeledAnswer: _list[EnterpriseTopazSidekickAnswerAnswerListLabeledAnswer]
    type: typing.Literal[
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
    typing.TypedDict, total=False
):
    answer: str
    label: str

@typing.type_check_only
class EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCard(
    typing.TypedDict, total=False
):
    suggestedQueryCategory: _list[EnterpriseTopazSidekickAnswerSuggestedQueryCategory]

@typing.type_check_only
class EnterpriseTopazSidekickAnswerSuggestedQueryCategory(
    typing.TypedDict, total=False
):
    category: typing.Literal["UNKNOWN", "CALENDAR", "DOCUMENT", "PEOPLE"]
    isEnabled: bool
    query: _list[str]

@typing.type_check_only
class EnterpriseTopazSidekickAssistCardProto(typing.TypedDict, total=False):
    agendaGroupCardProto: EnterpriseTopazSidekickAgendaGroupCardProto
    cardMetadata: EnterpriseTopazSidekickCardMetadata
    cardType: typing.Literal[
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
class EnterpriseTopazSidekickCardMetadata(typing.TypedDict, total=False):
    cardCategory: typing.Literal["DEFAULT", "ANSWER", "KNOWLEDGE", "HOMEPAGE"]
    cardId: str
    chronology: typing.Literal[
        "UNKNOWN", "PAST", "RECENTLY_PAST", "PRESENT", "NEAR_FUTURE", "FUTURE"
    ]
    debugInfo: str
    nlpMetadata: EnterpriseTopazSidekickNlpMetadata
    rankingParams: EnterpriseTopazSidekickRankingParams
    renderMode: typing.Literal["UNKNOWN_RENDER", "COLLAPSED", "EXPANDED"]

@typing.type_check_only
class EnterpriseTopazSidekickCommonDebugInfo(typing.TypedDict, total=False):
    message: str

@typing.type_check_only
class EnterpriseTopazSidekickCommonDocument(typing.TypedDict, total=False):
    accessType: typing.Literal["UNKNOWN_ACCESS", "ALLOWED", "NOT_ALLOWED"]
    debugInfo: EnterpriseTopazSidekickCommonDebugInfo
    documentId: str
    driveDocumentMetadata: EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata
    genericUrl: str
    justification: EnterpriseTopazSidekickCommonDocumentJustification
    mimeType: str
    provenance: typing.Literal[
        "UNKNOWN_PROVENANCE",
        "CALENDAR_DESCRIPTION",
        "CALENDAR_ATTACHMENT",
        "MINED",
        "CALENDAR_ASSIST_ATTACHMENT",
    ]
    reason: typing.Literal[
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
    type: typing.Literal[
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
    typing.TypedDict, total=False
):
    documentId: str
    isPrivate: bool
    lastCommentTimeMs: str
    lastEditTimeMs: str
    lastModificationTimeMillis: str
    lastUpdatedTimeMs: str
    lastViewTimeMs: str
    owner: EnterpriseTopazSidekickCommonPerson
    scope: typing.Literal[
        "UNKNOWN_DOCUMENT_SCOPE",
        "LIMITED",
        "DASHER_DOMAIN_WITH_LINK",
        "DASHER_DOMAIN",
        "PUBLIC_WITH_LINK",
        "PUBLIC",
        "TEAM_DRIVE",
    ]

@typing.type_check_only
class EnterpriseTopazSidekickCommonDocumentJustification(typing.TypedDict, total=False):
    justification: str
    reason: typing.Literal[
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
class EnterpriseTopazSidekickCommonPerson(typing.TypedDict, total=False):
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
class EnterpriseTopazSidekickCommonPersonBirthday(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class EnterpriseTopazSidekickConflictingEventsCardProto(typing.TypedDict, total=False):
    conflictingEvent: _list[EnterpriseTopazSidekickAgendaEntry]
    mainEvent: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickDocumentGroup(typing.TypedDict, total=False):
    groupType: typing.Literal["UNKNOWN_TYPE", "ALL"]
    personalizedDocument: _list[EnterpriseTopazSidekickCommonDocument]

@typing.type_check_only
class EnterpriseTopazSidekickDocumentPerCategoryList(typing.TypedDict, total=False):
    documents: _list[
        EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry
    ]
    helpMessage: str
    listType: typing.Literal[
        "UNKNOWN_LIST_TYPE", "MENTIONS", "SHARES", "NEEDS_ATTENTION", "VIEWS", "EDITS"
    ]
    listTypeDescription: str
    responseMessage: str

@typing.type_check_only
class EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry(
    typing.TypedDict, total=False
):
    category: typing.Literal[
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
class EnterpriseTopazSidekickFindMeetingTimeCardProto(typing.TypedDict, total=False):
    commonAvailableTimeSlots: _list[EnterpriseTopazSidekickTimeSlot]
    invitees: _list[EnterpriseTopazSidekickPerson]
    requester: EnterpriseTopazSidekickPerson
    scheduledMeeting: EnterpriseTopazSidekickScheduledMeeting
    skippedInvitees: _list[EnterpriseTopazSidekickPerson]
    timeBoundaries: EnterpriseTopazSidekickTimeSlot
    timezoneId: str

@typing.type_check_only
class EnterpriseTopazSidekickGap(typing.TypedDict, total=False):
    displayRemainingTime: str
    endTime: str
    endTimeMs: str
    remainingTime: str
    startTime: str
    startTimeMs: str

@typing.type_check_only
class EnterpriseTopazSidekickGenericAnswerCard(typing.TypedDict, total=False):
    answer: str
    title: str

@typing.type_check_only
class EnterpriseTopazSidekickGetAndKeepAheadCardProto(typing.TypedDict, total=False):
    declinedEvents: EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEvents
    mentionedDocuments: EnterpriseTopazSidekickDocumentPerCategoryList
    sharedDocuments: EnterpriseTopazSidekickDocumentPerCategoryList

@typing.type_check_only
class EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEvents(
    typing.TypedDict, total=False
):
    events: _list[EnterpriseTopazSidekickAgendaEntry]

@typing.type_check_only
class EnterpriseTopazSidekickMeetingNotesCardError(typing.TypedDict, total=False):
    description: str
    event: EnterpriseTopazSidekickAgendaEntry
    reason: typing.Literal["NONE", "NOT_OWNER", "UNKNOWN"]

@typing.type_check_only
class EnterpriseTopazSidekickMeetingNotesCardProto(typing.TypedDict, total=False):
    event: EnterpriseTopazSidekickAgendaEntry
    fileId: str
    title: str
    url: str

@typing.type_check_only
class EnterpriseTopazSidekickMeetingNotesCardRequest(typing.TypedDict, total=False):
    canCreateFor: _list[typing.Literal["UNKNOWN", "MYSELF", "ALL_ATTENDEES"]]
    error: EnterpriseTopazSidekickMeetingNotesCardError
    event: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickNlpMetadata(typing.TypedDict, total=False):
    confidence: float

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo(
    typing.TypedDict, total=False
):
    disambiguation: _list[
        EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPerson
    ]
    name: str

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPerson(
    typing.TypedDict, total=False
):
    person: EnterpriseTopazSidekickCommonPerson
    query: str

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader(
    typing.TypedDict, total=False
):
    title: str

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard(
    typing.TypedDict, total=False
):
    answer: _list[SafeHtmlProto]
    answerText: EnterpriseTopazSidekickAnswerAnswerList
    disambiguationInfo: EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo
    header: EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader
    responseStatus: typing.Literal[
        "UNKNOWN", "SUCCESS", "MISSING_PERSON", "MISSING_DATA"
    ]
    statusMessage: str
    subject: EnterpriseTopazSidekickCommonPerson

@typing.type_check_only
class EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard(
    typing.TypedDict, total=False
):
    disambiguationInfo: EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo
    header: EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader
    relatedPeople: _list[EnterpriseTopazSidekickCommonPerson]
    relationType: typing.Literal["UNKNOWN", "DIRECT_REPORTS", "MANAGER", "PEERS"]
    responseStatus: typing.Literal[
        "UNKNOWN", "SUCCESS", "MISSING_PERSON", "MISSING_DATA"
    ]
    statusMessage: str
    subject: EnterpriseTopazSidekickCommonPerson

@typing.type_check_only
class EnterpriseTopazSidekickPeopleDisambiguationCard(typing.TypedDict, total=False):
    person: _list[EnterpriseTopazSidekickCommonPerson]

@typing.type_check_only
class EnterpriseTopazSidekickPerson(typing.TypedDict, total=False):
    affinityLevel: typing.Literal["UNKNOWN", "LOW", "MEDIUM", "HIGH"]
    attendingStatus: typing.Literal["AWAITING", "YES", "NO", "MAYBE"]
    email: str
    gaiaId: str
    isGroup: bool
    name: str
    obfuscatedGaiaId: str
    photoUrl: str

@typing.type_check_only
class EnterpriseTopazSidekickPersonProfileCard(typing.TypedDict, total=False):
    relatedPeople: _list[EnterpriseTopazSidekickPersonProfileCardRelatedPeople]
    subject: EnterpriseTopazSidekickCommonPerson

@typing.type_check_only
class EnterpriseTopazSidekickPersonProfileCardRelatedPeople(
    typing.TypedDict, total=False
):
    relatedPerson: _list[EnterpriseTopazSidekickCommonPerson]
    relation: typing.Literal["UNKNOWN", "MANAGER", "DIRECT_REPORT"]

@typing.type_check_only
class EnterpriseTopazSidekickPersonalizedDocsCardProto(typing.TypedDict, total=False):
    documentGroup: _list[EnterpriseTopazSidekickDocumentGroup]

@typing.type_check_only
class EnterpriseTopazSidekickRankingParams(typing.TypedDict, total=False):
    endTimeMs: str
    priority: typing.Literal[
        "UNKNOWN", "CRITICAL", "IMPORTANT", "HIGH", "NORMAL", "BEST_EFFORT"
    ]
    score: float
    spanMs: str
    startTimeMs: str
    type: typing.Literal["FIXED", "FLEXIBLE"]

@typing.type_check_only
class EnterpriseTopazSidekickRecentDocumentsCardProto(typing.TypedDict, total=False):
    document: _list[EnterpriseTopazSidekickCommonDocument]

@typing.type_check_only
class EnterpriseTopazSidekickScheduledMeeting(typing.TypedDict, total=False):
    meetingLocation: str
    meetingTime: EnterpriseTopazSidekickTimeSlot
    meetingTitle: str

@typing.type_check_only
class EnterpriseTopazSidekickShareMeetingDocsCardProto(typing.TypedDict, total=False):
    document: _list[EnterpriseTopazSidekickCommonDocument]
    event: EnterpriseTopazSidekickAgendaEntry

@typing.type_check_only
class EnterpriseTopazSidekickTimeSlot(typing.TypedDict, total=False):
    endTimeDay: str
    endTimeHourAndMinute: str
    endTimeInMillis: str
    startTimeDay: str
    startTimeHourAndMinute: str
    startTimeInMillis: str

@typing.type_check_only
class EnumOperatorOptions(typing.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class EnumPropertyOptions(typing.TypedDict, total=False):
    operatorOptions: EnumOperatorOptions
    orderedRanking: typing.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]
    possibleValues: _list[EnumValuePair]

@typing.type_check_only
class EnumValuePair(typing.TypedDict, total=False):
    integerValue: int
    stringValue: str

@typing.type_check_only
class EnumValues(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ErrorInfo(typing.TypedDict, total=False):
    errorMessages: _list[ErrorMessage]

@typing.type_check_only
class ErrorMessage(typing.TypedDict, total=False):
    errorMessage: str
    source: Source

@typing.type_check_only
class FacetBucket(typing.TypedDict, total=False):
    count: int
    filter: Filter
    percentage: int
    value: Value

@typing.type_check_only
class FacetOptions(typing.TypedDict, total=False):
    integerFacetingOptions: IntegerFacetingOptions
    numFacetBuckets: int
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FacetResult(typing.TypedDict, total=False):
    buckets: _list[FacetBucket]
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FieldViolation(typing.TypedDict, total=False):
    description: str
    field: str

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    compositeFilter: CompositeFilter
    valueFilter: ValueFilter

@typing.type_check_only
class FilterOptions(typing.TypedDict, total=False):
    filter: Filter
    objectType: str

@typing.type_check_only
class FreshnessOptions(typing.TypedDict, total=False):
    freshnessDuration: str
    freshnessProperty: str

@typing.type_check_only
class GSuitePrincipal(typing.TypedDict, total=False):
    gsuiteDomain: bool
    gsuiteGroupEmail: str
    gsuiteUserEmail: str

@typing.type_check_only
class GetCustomerIndexStatsResponse(typing.TypedDict, total=False):
    averageIndexedItemCount: str
    stats: _list[CustomerIndexStats]

@typing.type_check_only
class GetCustomerQueryStatsResponse(typing.TypedDict, total=False):
    stats: _list[CustomerQueryStats]
    totalQueryCount: str

@typing.type_check_only
class GetCustomerSearchApplicationStatsResponse(typing.TypedDict, total=False):
    averageSearchApplicationCount: str
    stats: _list[CustomerSearchApplicationStats]

@typing.type_check_only
class GetCustomerSessionStatsResponse(typing.TypedDict, total=False):
    stats: _list[CustomerSessionStats]

@typing.type_check_only
class GetCustomerUserStatsResponse(typing.TypedDict, total=False):
    stats: _list[CustomerUserStats]

@typing.type_check_only
class GetDataSourceIndexStatsResponse(typing.TypedDict, total=False):
    averageIndexedItemCount: str
    stats: _list[DataSourceIndexStats]

@typing.type_check_only
class GetSearchApplicationQueryStatsResponse(typing.TypedDict, total=False):
    stats: _list[SearchApplicationQueryStats]
    totalQueryCount: str

@typing.type_check_only
class GetSearchApplicationSessionStatsResponse(typing.TypedDict, total=False):
    stats: _list[SearchApplicationSessionStats]

@typing.type_check_only
class GetSearchApplicationUserStatsResponse(typing.TypedDict, total=False):
    stats: _list[SearchApplicationUserStats]

@typing.type_check_only
class HtmlOperatorOptions(typing.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class HtmlPropertyOptions(typing.TypedDict, total=False):
    operatorOptions: HtmlOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class HtmlValues(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class IndexItemOptions(typing.TypedDict, total=False):
    allowUnknownGsuitePrincipals: bool

@typing.type_check_only
class IndexItemRequest(typing.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    indexItemOptions: IndexItemOptions
    item: Item
    mode: typing.Literal["UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"]

@typing.type_check_only
class InitializeCustomerRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class IntegerFacetingOptions(typing.TypedDict, total=False):
    integerBuckets: _list[str]

@typing.type_check_only
class IntegerOperatorOptions(typing.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class IntegerPropertyOptions(typing.TypedDict, total=False):
    integerFacetingOptions: IntegerFacetingOptions
    maximumValue: str
    minimumValue: str
    operatorOptions: IntegerOperatorOptions
    orderedRanking: typing.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class IntegerValues(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class Interaction(typing.TypedDict, total=False):
    interactionTime: str
    principal: Principal
    type: typing.Literal["UNSPECIFIED", "VIEW", "EDIT"]

@typing.type_check_only
class Item(typing.TypedDict, total=False):
    acl: ItemAcl
    content: ItemContent
    itemType: typing.Literal[
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
class ItemAcl(typing.TypedDict, total=False):
    aclInheritanceType: typing.Literal[
        "NOT_APPLICABLE", "CHILD_OVERRIDE", "PARENT_OVERRIDE", "BOTH_PERMIT"
    ]
    deniedReaders: _list[Principal]
    inheritAclFrom: str
    owners: _list[Principal]
    readers: _list[Principal]

@typing.type_check_only
class ItemContent(typing.TypedDict, total=False):
    contentDataRef: UploadItemRef
    contentFormat: typing.Literal["UNSPECIFIED", "HTML", "TEXT", "RAW"]
    hash: str
    inlineContent: str

@typing.type_check_only
class ItemCountByStatus(typing.TypedDict, total=False):
    count: str
    indexedItemsCount: str
    statusCode: typing.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]

@typing.type_check_only
class ItemMetadata(typing.TypedDict, total=False):
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
class ItemStatus(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]
    processingErrors: _list[ProcessingError]
    repositoryErrors: _list[RepositoryError]

@typing.type_check_only
class ItemStructuredData(typing.TypedDict, total=False):
    hash: str
    object: StructuredDataObject

@typing.type_check_only
class ListDataSourceResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sources: _list[DataSource]

@typing.type_check_only
class ListItemNamesForUnmappedIdentityResponse(typing.TypedDict, total=False):
    itemNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListItemsResponse(typing.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListQuerySourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sources: _list[QuerySource]

@typing.type_check_only
class ListSearchApplicationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    searchApplications: _list[SearchApplication]

@typing.type_check_only
class ListUnmappedIdentitiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unmappedIdentities: _list[UnmappedIdentity]

@typing.type_check_only
class MapInfo(typing.TypedDict, total=False):
    lat: float
    locationUrl: SafeUrlProto
    long: float
    mapTile: _list[MapTile]
    zoom: int

@typing.type_check_only
class MapTile(typing.TypedDict, total=False):
    imageUrl: SafeUrlProto
    tileX: float
    tileY: float

@typing.type_check_only
class MatchRange(typing.TypedDict, total=False):
    end: int
    start: int

@typing.type_check_only
class Media(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
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
class Metaline(typing.TypedDict, total=False):
    properties: _list[DisplayedProperty]

@typing.type_check_only
class Name(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class NamedProperty(typing.TypedDict, total=False):
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
class ObjectDefinition(typing.TypedDict, total=False):
    name: str
    options: ObjectOptions
    propertyDefinitions: _list[PropertyDefinition]

@typing.type_check_only
class ObjectDisplayOptions(typing.TypedDict, total=False):
    metalines: _list[Metaline]
    objectDisplayLabel: str

@typing.type_check_only
class ObjectOptions(typing.TypedDict, total=False):
    displayOptions: ObjectDisplayOptions
    freshnessOptions: FreshnessOptions
    suggestionFilteringOperators: _list[str]

@typing.type_check_only
class ObjectPropertyOptions(typing.TypedDict, total=False):
    subobjectProperties: _list[PropertyDefinition]

@typing.type_check_only
class ObjectValues(typing.TypedDict, total=False):
    values: _list[StructuredDataObject]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PeoplePromotionCard(typing.TypedDict, total=False):
    people: _list[PersonCore]

@typing.type_check_only
class PeopleSuggestion(typing.TypedDict, total=False):
    person: Person

@typing.type_check_only
class Person(typing.TypedDict, total=False):
    emailAddresses: _list[EmailAddress]
    name: str
    obfuscatedId: str
    personNames: _list[Name]
    phoneNumbers: _list[PhoneNumber]
    photos: _list[Photo]

@typing.type_check_only
class PersonCore(typing.TypedDict, total=False):
    addressMeAs: str
    adminTo: _list[PersonCore]
    admins: _list[PersonCore]
    availabilityStatus: typing.Literal[
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
class PhoneNumber(typing.TypedDict, total=False):
    phoneNumber: str
    type: typing.Literal["OTHER", "MOBILE", "OFFICE"]

@typing.type_check_only
class Photo(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class PollItemsRequest(typing.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    limit: int
    queue: str
    statusCodes: _list[
        typing.Literal["CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"]
    ]

@typing.type_check_only
class PollItemsResponse(typing.TypedDict, total=False):
    items: _list[Item]

@typing.type_check_only
class Principal(typing.TypedDict, total=False):
    groupResourceName: str
    gsuitePrincipal: GSuitePrincipal
    userResourceName: str

@typing.type_check_only
class ProcessingError(typing.TypedDict, total=False):
    code: typing.Literal[
        "PROCESSING_ERROR_CODE_UNSPECIFIED",
        "MALFORMED_REQUEST",
        "UNSUPPORTED_CONTENT_FORMAT",
        "INDIRECT_BROKEN_ACL",
        "ACL_CYCLE",
    ]
    errorMessage: str
    fieldViolations: _list[FieldViolation]

@typing.type_check_only
class PropertyDefinition(typing.TypedDict, total=False):
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
class PropertyDisplayOptions(typing.TypedDict, total=False):
    displayLabel: str

@typing.type_check_only
class PushItem(typing.TypedDict, total=False):
    contentHash: str
    metadataHash: str
    payload: str
    queue: str
    repositoryError: RepositoryError
    structuredDataHash: str
    type: typing.Literal[
        "UNSPECIFIED", "MODIFIED", "NOT_MODIFIED", "REPOSITORY_ERROR", "REQUEUE"
    ]

@typing.type_check_only
class PushItemRequest(typing.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    item: PushItem

@typing.type_check_only
class QueryActivity(typing.TypedDict, total=False):
    query: str

@typing.type_check_only
class QueryCountByStatus(typing.TypedDict, total=False):
    count: str
    statusCode: int

@typing.type_check_only
class QueryInterpretation(typing.TypedDict, total=False):
    interpretationType: typing.Literal["NONE", "BLEND", "REPLACE"]
    interpretedQuery: str
    interpretedQueryActualResultCount: int
    interpretedQueryEstimatedResultCount: str
    reason: typing.Literal[
        "UNSPECIFIED",
        "QUERY_HAS_NATURAL_LANGUAGE_INTENT",
        "NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY",
    ]

@typing.type_check_only
class QueryInterpretationConfig(typing.TypedDict, total=False):
    forceDisableSupplementalResults: bool
    forceVerbatimMode: bool

@typing.type_check_only
class QueryInterpretationOptions(typing.TypedDict, total=False):
    disableNlInterpretation: bool
    disableSupplementalResults: bool
    enableVerbatimMode: bool

@typing.type_check_only
class QueryItem(typing.TypedDict, total=False):
    isSynthetic: bool

@typing.type_check_only
class QueryOperator(typing.TypedDict, total=False):
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
    type: typing.Literal[
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
class QuerySource(typing.TypedDict, total=False):
    displayName: str
    operators: _list[QueryOperator]
    shortName: str
    source: Source

@typing.type_check_only
class QuerySuggestion(typing.TypedDict, total=False):
    lastQueryTime: str
    sourceCorpus: typing.Literal[
        "SOURCE_CORPUS_UNSPECIFIED", "GMAIL", "DRIVE", "CHAT", "CALENDAR"
    ]

@typing.type_check_only
class RemoveActivityRequest(typing.TypedDict, total=False):
    requestOptions: RequestOptions
    userActivity: UserActivity

@typing.type_check_only
class RemoveActivityResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RepositoryError(typing.TypedDict, total=False):
    errorMessage: str
    httpStatusCode: int
    type: typing.Literal[
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
class RequestOptions(typing.TypedDict, total=False):
    clientDisplayLanguageCode: str
    countryCode: str
    debugOptions: DebugOptions
    languageCode: str
    searchApplicationId: str
    timeZone: str

@typing.type_check_only
class ResetSearchApplicationRequest(typing.TypedDict, total=False):
    debugOptions: DebugOptions

@typing.type_check_only
class ResponseDebugInfo(typing.TypedDict, total=False):
    formattedDebugInfo: str

@typing.type_check_only
class RestrictItem(typing.TypedDict, total=False):
    driveFollowUpRestrict: DriveFollowUpRestrict
    driveLocationRestrict: DriveLocationRestrict
    driveMimeTypeRestrict: DriveMimeTypeRestrict
    driveTimeSpanRestrict: DriveTimeSpanRestrict
    searchOperator: str

@typing.type_check_only
class ResultCounts(typing.TypedDict, total=False):
    sourceResultCounts: _list[SourceResultCount]

@typing.type_check_only
class ResultDebugInfo(typing.TypedDict, total=False):
    formattedDebugInfo: str

@typing.type_check_only
class ResultDisplayField(typing.TypedDict, total=False):
    label: str
    operatorName: str
    property: NamedProperty

@typing.type_check_only
class ResultDisplayLine(typing.TypedDict, total=False):
    fields: _list[ResultDisplayField]

@typing.type_check_only
class ResultDisplayMetadata(typing.TypedDict, total=False):
    metalines: _list[ResultDisplayLine]
    objectTypeLabel: str

@typing.type_check_only
class RetrievalImportance(typing.TypedDict, total=False):
    importance: typing.Literal["DEFAULT", "HIGHEST", "HIGH", "LOW", "NONE"]

@typing.type_check_only
class SafeHtmlProto(typing.TypedDict, total=False):
    privateDoNotAccessOrElseSafeHtmlWrappedValue: str

@typing.type_check_only
class SafeUrlProto(typing.TypedDict, total=False):
    privateDoNotAccessOrElseSafeUrlWrappedValue: str

@typing.type_check_only
class Schema(typing.TypedDict, total=False):
    objectDefinitions: _list[ObjectDefinition]
    operationIds: _list[str]

@typing.type_check_only
class ScoringConfig(typing.TypedDict, total=False):
    disableFreshness: bool
    disablePersonalization: bool

@typing.type_check_only
class SearchApplication(typing.TypedDict, total=False):
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
class SearchApplicationQueryStats(typing.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class SearchApplicationSessionStats(typing.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class SearchApplicationUserStats(typing.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class SearchItemsByViewUrlRequest(typing.TypedDict, total=False):
    debugOptions: DebugOptions
    pageToken: str
    viewUrl: str

@typing.type_check_only
class SearchItemsByViewUrlResponse(typing.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class SearchQualityMetadata(typing.TypedDict, total=False):
    quality: float

@typing.type_check_only
class SearchRequest(typing.TypedDict, total=False):
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
class SearchResponse(typing.TypedDict, total=False):
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
class SearchResult(typing.TypedDict, total=False):
    clusteredResults: _list[SearchResult]
    debugInfo: ResultDebugInfo
    metadata: Metadata
    snippet: Snippet
    title: str
    url: str

@typing.type_check_only
class Snippet(typing.TypedDict, total=False):
    matchRanges: _list[MatchRange]
    snippet: str

@typing.type_check_only
class SortOptions(typing.TypedDict, total=False):
    operatorName: str
    sortOrder: typing.Literal["ASCENDING", "DESCENDING"]

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    name: str
    predefinedSource: typing.Literal[
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
class SourceConfig(typing.TypedDict, total=False):
    crowdingConfig: SourceCrowdingConfig
    scoringConfig: SourceScoringConfig
    source: Source

@typing.type_check_only
class SourceCrowdingConfig(typing.TypedDict, total=False):
    numResults: int
    numSuggestions: int

@typing.type_check_only
class SourceResultCount(typing.TypedDict, total=False):
    hasMoreResults: bool
    resultCountEstimate: str
    resultCountExact: str
    source: Source

@typing.type_check_only
class SourceScoringConfig(typing.TypedDict, total=False):
    sourceImportance: typing.Literal["DEFAULT", "LOW", "HIGH"]

@typing.type_check_only
class SpellResult(typing.TypedDict, total=False):
    suggestedQuery: str
    suggestedQueryHtml: SafeHtmlProto
    suggestionType: typing.Literal[
        "SUGGESTION_TYPE_UNSPECIFIED",
        "NON_EMPTY_RESULTS_SPELL_SUGGESTION",
        "ZERO_RESULTS_FULL_PAGE_REPLACEMENT",
    ]

@typing.type_check_only
class StartUploadItemRequest(typing.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructuredDataObject(typing.TypedDict, total=False):
    properties: _list[NamedProperty]

@typing.type_check_only
class StructuredResult(typing.TypedDict, total=False):
    person: Person

@typing.type_check_only
class SuggestRequest(typing.TypedDict, total=False):
    dataSourceRestrictions: _list[DataSourceRestriction]
    query: str
    requestOptions: RequestOptions

@typing.type_check_only
class SuggestResponse(typing.TypedDict, total=False):
    suggestResults: _list[SuggestResult]

@typing.type_check_only
class SuggestResult(typing.TypedDict, total=False):
    peopleSuggestion: PeopleSuggestion
    querySuggestion: QuerySuggestion
    source: Source
    suggestedQuery: str

@typing.type_check_only
class TextOperatorOptions(typing.TypedDict, total=False):
    exactMatchWithOperator: bool
    operatorName: str

@typing.type_check_only
class TextPropertyOptions(typing.TypedDict, total=False):
    operatorOptions: TextOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class TextValues(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ThirdPartyGenericCard(typing.TypedDict, total=False):
    cardId: str
    category: str
    content: Content
    context: Context
    isDismissible: bool
    priority: int

@typing.type_check_only
class TimestampOperatorOptions(typing.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class TimestampPropertyOptions(typing.TypedDict, total=False):
    operatorOptions: TimestampOperatorOptions

@typing.type_check_only
class TimestampValues(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class UnmappedIdentity(typing.TypedDict, total=False):
    externalIdentity: Principal
    resolutionStatusCode: typing.Literal[
        "CODE_UNSPECIFIED",
        "NOT_FOUND",
        "IDENTITY_SOURCE_NOT_FOUND",
        "IDENTITY_SOURCE_MISCONFIGURED",
        "TOO_MANY_MAPPINGS_FOUND",
        "INTERNAL_ERROR",
    ]

@typing.type_check_only
class UnreserveItemsRequest(typing.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class UpdateDataSourceRequest(typing.TypedDict, total=False):
    debugOptions: DebugOptions
    source: DataSource
    updateMask: str

@typing.type_check_only
class UpdateSchemaRequest(typing.TypedDict, total=False):
    debugOptions: DebugOptions
    schema: Schema
    validateOnly: bool

@typing.type_check_only
class UploadItemRef(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class UserActivity(typing.TypedDict, total=False):
    queryActivity: QueryActivity

@typing.type_check_only
class VPCSettings(typing.TypedDict, total=False):
    project: str

@typing.type_check_only
class Value(typing.TypedDict, total=False):
    booleanValue: bool
    dateValue: Date
    doubleValue: float
    integerValue: str
    stringValue: str
    timestampValue: str

@typing.type_check_only
class ValueFilter(typing.TypedDict, total=False):
    operatorName: str
    value: Value
