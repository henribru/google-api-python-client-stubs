import typing

import typing_extensions

class AbuseType(typing_extensions.TypedDict, total=False):
    id: str

class ActivityContentDetailsSubscription(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class VideoPlayer(typing_extensions.TypedDict, total=False):
    embedHtml: str
    embedHeight: str
    embedWidth: str

class SearchResultSnippet(typing_extensions.TypedDict, total=False):
    liveBroadcastContent: typing_extensions.Literal[
        "none", "upcoming", "live", "completed"
    ]
    channelTitle: str
    description: str
    channelId: str
    publishedAt: str
    thumbnails: ThumbnailDetails
    title: str

class SponsorListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    etag: str
    tokenPagination: TokenPagination
    pageInfo: PageInfo
    visitorId: str
    items: typing.List[Sponsor]
    eventId: str

class TokenPagination(typing_extensions.TypedDict, total=False): ...

class SubscriptionListResponse(typing_extensions.TypedDict, total=False):
    tokenPagination: TokenPagination
    prevPageToken: str
    pageInfo: PageInfo
    etag: str
    visitorId: str
    nextPageToken: str
    items: typing.List[Subscription]
    kind: str
    eventId: str

class PlaylistContentDetails(typing_extensions.TypedDict, total=False):
    itemCount: int

class PlaylistPlayer(typing_extensions.TypedDict, total=False):
    embedHtml: str

class ChannelConversionPings(typing_extensions.TypedDict, total=False):
    pings: typing.List[ChannelConversionPing]

class PlaylistItemStatus(typing_extensions.TypedDict, total=False):
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]

class TestItem(typing_extensions.TypedDict, total=False):
    id: str
    gaia: str
    snippet: TestItemTestItemSnippet

class I18nLanguageListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    visitorId: str
    kind: str
    items: typing.List[I18nLanguage]
    eventId: str

class LiveBroadcastStatus(typing_extensions.TypedDict, total=False):
    liveBroadcastPriority: typing_extensions.Literal[
        "liveBroadcastPriorityUnspecified", "low", "normal", "high"
    ]
    lifeCycleStatus: typing_extensions.Literal[
        "lifeCycleStatusUnspecified",
        "created",
        "ready",
        "testing",
        "live",
        "complete",
        "revoked",
        "testStarting",
        "liveStarting",
    ]
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]
    madeForKids: bool
    selfDeclaredMadeForKids: bool
    recordingStatus: typing_extensions.Literal[
        "liveBroadcastRecordingStatusUnspecified",
        "notRecording",
        "recording",
        "recorded",
    ]

class VideoStatistics(typing_extensions.TypedDict, total=False):
    likeCount: str
    commentCount: str
    viewCount: str
    favoriteCount: str
    dislikeCount: str

class MemberSnippet(typing_extensions.TypedDict, total=False):
    membershipsDetails: MembershipsDetails
    creatorChannelId: str
    memberDetails: ChannelProfileDetails

class Playlist(typing_extensions.TypedDict, total=False):
    contentDetails: PlaylistContentDetails
    player: PlaylistPlayer
    snippet: PlaylistSnippet
    id: str
    etag: str
    localizations: typing.Dict[str, typing.Any]
    status: PlaylistStatus
    kind: str

class I18nRegion(typing_extensions.TypedDict, total=False):
    kind: str
    snippet: I18nRegionSnippet
    etag: str
    id: str

class VideoContentDetails(typing_extensions.TypedDict, total=False):
    duration: str
    licensedContent: bool
    hasCustomThumbnail: bool
    regionRestriction: VideoContentDetailsRegionRestriction
    projection: typing_extensions.Literal["rectangular", "360"]
    caption: typing_extensions.Literal["true", "false"]
    dimension: str
    definition: typing_extensions.Literal["sd", "hd"]
    countryRestriction: AccessPolicy
    contentRating: ContentRating

class MembershipsLevelListResponse(typing_extensions.TypedDict, total=False):
    eventId: str
    etag: str
    items: typing.List[MembershipsLevel]
    visitorId: str
    kind: str

class LiveChatMessageDeletedDetails(typing_extensions.TypedDict, total=False):
    deletedMessageId: str

class CaptionListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    eventId: str
    etag: str
    items: typing.List[Caption]
    visitorId: str

class VideoMonetizationDetails(typing_extensions.TypedDict, total=False):
    access: AccessPolicy

class Video(typing_extensions.TypedDict, total=False):
    recordingDetails: VideoRecordingDetails
    liveStreamingDetails: VideoLiveStreamingDetails
    processingDetails: VideoProcessingDetails
    kind: str
    etag: str
    contentDetails: VideoContentDetails
    player: VideoPlayer
    id: str
    localizations: typing.Dict[str, typing.Any]
    suggestions: VideoSuggestions
    monetizationDetails: VideoMonetizationDetails
    ageGating: VideoAgeGating
    statistics: VideoStatistics
    fileDetails: VideoFileDetails
    snippet: VideoSnippet
    topicDetails: VideoTopicDetails
    projectDetails: VideoProjectDetails
    status: VideoStatus

class PlaylistItemSnippet(typing_extensions.TypedDict, total=False):
    title: str
    channelTitle: str
    resourceId: ResourceId
    playlistId: str
    channelId: str
    thumbnails: ThumbnailDetails
    description: str
    publishedAt: str
    position: int

class MembershipsDetails(typing_extensions.TypedDict, total=False):
    membershipsDuration: MembershipsDuration
    highestAccessibleLevel: str
    accessibleLevels: typing.List[str]
    highestAccessibleLevelDisplayName: str
    membershipsDurationAtLevels: typing.List[MembershipsDurationAtLevel]

class PlaylistLocalization(typing_extensions.TypedDict, total=False):
    title: str
    description: str

class ChannelToStoreLinkDetails(typing_extensions.TypedDict, total=False):
    storeUrl: str
    storeName: str

class VideoCategoryListResponse(typing_extensions.TypedDict, total=False):
    prevPageToken: str
    items: typing.List[VideoCategory]
    etag: str
    pageInfo: PageInfo
    eventId: str
    kind: str
    nextPageToken: str
    visitorId: str
    tokenPagination: TokenPagination

class ThirdPartyLinkSnippet(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["linkUnspecified", "channelToStoreLink"]
    channelToStoreLink: ChannelToStoreLinkDetails

class VideoStatus(typing_extensions.TypedDict, total=False):
    license: typing_extensions.Literal["youtube", "creativeCommon"]
    failureReason: typing_extensions.Literal[
        "conversion", "invalidFile", "emptyFile", "tooSmall", "codec", "uploadAborted"
    ]
    publicStatsViewable: bool
    uploadStatus: typing_extensions.Literal[
        "uploaded", "processed", "failed", "rejected", "deleted"
    ]
    selfDeclaredMadeForKids: bool
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]
    embeddable: bool
    publishAt: str
    madeForKids: bool
    rejectionReason: typing_extensions.Literal[
        "copyright",
        "inappropriate",
        "duplicate",
        "termsOfUse",
        "uploaderAccountSuspended",
        "length",
        "claim",
        "uploaderAccountClosed",
        "trademark",
        "legal",
    ]

class ChannelStatus(typing_extensions.TypedDict, total=False):
    longUploadsStatus: typing_extensions.Literal[
        "longUploadsUnspecified", "allowed", "eligible", "disallowed"
    ]
    selfDeclaredMadeForKids: bool
    isLinked: bool
    madeForKids: bool
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]

class Caption(typing_extensions.TypedDict, total=False):
    id: str
    etag: str
    snippet: CaptionSnippet
    kind: str

class VideoSnippet(typing_extensions.TypedDict, total=False):
    title: str
    categoryId: str
    tags: typing.List[str]
    defaultAudioLanguage: str
    thumbnails: ThumbnailDetails
    channelTitle: str
    publishedAt: str
    defaultLanguage: str
    liveBroadcastContent: typing_extensions.Literal[
        "none", "upcoming", "live", "completed"
    ]
    channelId: str
    localized: VideoLocalization
    description: str

class MembershipsDuration(typing_extensions.TypedDict, total=False):
    memberTotalDurationMonths: int
    memberSince: str

class CommentThreadSnippet(typing_extensions.TypedDict, total=False):
    topLevelComment: Comment
    channelId: str
    isPublic: bool
    canReply: bool
    videoId: str
    totalReplyCount: int

class Member(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    snippet: MemberSnippet

class LiveStreamContentDetails(typing_extensions.TypedDict, total=False):
    isReusable: bool
    closedCaptionsIngestionUrl: str

class ActivityContentDetailsComment(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class VideoTopicDetails(typing_extensions.TypedDict, total=False):
    topicCategories: typing.List[str]
    relevantTopicIds: typing.List[str]
    topicIds: typing.List[str]

class LiveChatMessageAuthorDetails(typing_extensions.TypedDict, total=False):
    isVerified: bool
    isChatSponsor: bool
    isChatModerator: bool
    isChatOwner: bool
    channelId: str
    profileImageUrl: str
    channelUrl: str
    displayName: str

class LiveChatModeratorListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[LiveChatModerator]
    nextPageToken: str
    etag: str
    visitorId: str
    eventId: str
    prevPageToken: str
    tokenPagination: TokenPagination
    kind: str
    pageInfo: PageInfo

class ActivityContentDetailsSocial(typing_extensions.TypedDict, total=False):
    author: str
    imageUrl: str
    resourceId: ResourceId
    referenceUrl: str
    type: typing_extensions.Literal[
        "typeUnspecified", "googlePlus", "facebook", "twitter"
    ]

class LiveBroadcastStatistics(typing_extensions.TypedDict, total=False):
    totalChatCount: str

class ChannelSectionContentDetails(typing_extensions.TypedDict, total=False):
    channels: typing.List[str]
    playlists: typing.List[str]

class LiveBroadcast(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    etag: str
    contentDetails: LiveBroadcastContentDetails
    statistics: LiveBroadcastStatistics
    snippet: LiveBroadcastSnippet
    status: LiveBroadcastStatus

class I18nLanguageSnippet(typing_extensions.TypedDict, total=False):
    name: str
    hl: str

class ChannelAuditDetails(typing_extensions.TypedDict, total=False):
    contentIdClaimsGoodStanding: bool
    copyrightStrikesGoodStanding: bool
    communityGuidelinesGoodStanding: bool

class LiveStreamHealthStatus(typing_extensions.TypedDict, total=False):
    lastUpdateTimeSeconds: str
    configurationIssues: typing.List[LiveStreamConfigurationIssue]
    status: typing_extensions.Literal["good", "ok", "bad", "noData", "revoked"]

class LiveChatMessageSnippet(typing_extensions.TypedDict, total=False):
    userBannedDetails: LiveChatUserBannedMessageDetails
    publishedAt: str
    fanFundingEventDetails: LiveChatFanFundingEventDetails
    liveChatId: str
    type: typing_extensions.Literal[
        "invalidType",
        "textMessageEvent",
        "tombstone",
        "fanFundingEvent",
        "chatEndedEvent",
        "sponsorOnlyModeStartedEvent",
        "sponsorOnlyModeEndedEvent",
        "newSponsorEvent",
        "messageDeletedEvent",
        "messageRetractedEvent",
        "userBannedEvent",
        "superChatEvent",
        "superStickerEvent",
    ]
    textMessageDetails: LiveChatTextMessageDetails
    hasDisplayContent: bool
    superStickerDetails: LiveChatSuperStickerDetails
    messageDeletedDetails: LiveChatMessageDeletedDetails
    messageRetractedDetails: LiveChatMessageRetractedDetails
    displayMessage: str
    superChatDetails: LiveChatSuperChatDetails
    authorChannelId: str

class LiveChatModeratorSnippet(typing_extensions.TypedDict, total=False):
    moderatorDetails: ChannelProfileDetails
    liveChatId: str

class ActivityContentDetailsRecommendation(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "reasonUnspecified", "videoFavorited", "videoLiked", "videoWatched"
    ]
    resourceId: ResourceId
    seedResourceId: ResourceId

class VideoSuggestionsTagSuggestion(typing_extensions.TypedDict, total=False):
    categoryRestricts: typing.List[str]
    tag: str

class MembershipsLevel(typing_extensions.TypedDict, total=False):
    snippet: MembershipsLevelSnippet
    id: str
    etag: str
    kind: str

class VideoAbuseReportReasonSnippet(typing_extensions.TypedDict, total=False):
    secondaryReasons: typing.List[VideoAbuseReportSecondaryReason]
    label: str

class VideoFileDetails(typing_extensions.TypedDict, total=False):
    videoStreams: typing.List[VideoFileDetailsVideoStream]
    bitrateBps: str
    audioStreams: typing.List[VideoFileDetailsAudioStream]
    fileType: typing_extensions.Literal[
        "video", "audio", "image", "archive", "document", "project", "other"
    ]
    fileSize: str
    creationTime: str
    container: str
    fileName: str
    durationMs: str

class ChannelSettings(typing_extensions.TypedDict, total=False):
    keywords: str
    defaultTab: str
    showRelatedChannels: bool
    description: str
    profileColor: str
    moderateComments: bool
    trackingAnalyticsAccountId: str
    country: str
    featuredChannelsUrls: typing.List[str]
    unsubscribedTrailer: str
    defaultLanguage: str
    featuredChannelsTitle: str
    title: str
    showBrowseView: bool

class ChannelStatistics(typing_extensions.TypedDict, total=False):
    viewCount: str
    videoCount: str
    hiddenSubscriberCount: bool
    commentCount: str
    subscriberCount: str

class VideoLiveStreamingDetails(typing_extensions.TypedDict, total=False):
    scheduledStartTime: str
    actualStartTime: str
    actualEndTime: str
    concurrentViewers: str
    scheduledEndTime: str
    activeLiveChatId: str

class ContentRating(typing_extensions.TypedDict, total=False):
    acbRating: typing_extensions.Literal[
        "acbUnspecified",
        "acbE",
        "acbP",
        "acbC",
        "acbG",
        "acbPg",
        "acbM",
        "acbMa15plus",
        "acbR18plus",
        "acbUnrated",
    ]
    fmocRating: typing_extensions.Literal[
        "fmocUnspecified",
        "fmocU",
        "fmoc10",
        "fmoc12",
        "fmoc16",
        "fmoc18",
        "fmocE",
        "fmocUnrated",
    ]
    fcoRating: typing_extensions.Literal[
        "fcoUnspecified", "fcoI", "fcoIia", "fcoIib", "fcoIi", "fcoIii", "fcoUnrated"
    ]
    nfrcRating: typing_extensions.Literal[
        "nfrcUnspecified", "nfrcA", "nfrcB", "nfrcC", "nfrcD", "nfrcX", "nfrcUnrated"
    ]
    anatelRating: typing_extensions.Literal[
        "anatelUnspecified",
        "anatelF",
        "anatelI",
        "anatelI7",
        "anatelI10",
        "anatelI12",
        "anatelR",
        "anatelA",
        "anatelUnrated",
    ]
    bfvcRating: typing_extensions.Literal[
        "bfvcUnspecified",
        "bfvcG",
        "bfvcE",
        "bfvc13",
        "bfvc15",
        "bfvc18",
        "bfvc20",
        "bfvcB",
        "bfvcUnrated",
    ]
    djctqRatingReasons: typing.List[str]
    nfvcbRating: typing_extensions.Literal[
        "nfvcbUnspecified",
        "nfvcbG",
        "nfvcbPg",
        "nfvcb12",
        "nfvcb12a",
        "nfvcb15",
        "nfvcb18",
        "nfvcbRe",
        "nfvcbUnrated",
    ]
    kfcbRating: typing_extensions.Literal[
        "kfcbUnspecified", "kfcbG", "kfcbPg", "kfcb16plus", "kfcbR", "kfcbUnrated"
    ]
    catvRating: typing_extensions.Literal[
        "catvUnspecified",
        "catvC",
        "catvC8",
        "catvG",
        "catvPg",
        "catv14plus",
        "catv18plus",
        "catvUnrated",
        "catvE",
    ]
    egfilmRating: typing_extensions.Literal[
        "egfilmUnspecified", "egfilmGn", "egfilm18", "egfilmBn", "egfilmUnrated"
    ]
    icaaRating: typing_extensions.Literal[
        "icaaUnspecified",
        "icaaApta",
        "icaa7",
        "icaa12",
        "icaa13",
        "icaa16",
        "icaa18",
        "icaaX",
        "icaaUnrated",
    ]
    catvfrRating: typing_extensions.Literal[
        "catvfrUnspecified",
        "catvfrG",
        "catvfr8plus",
        "catvfr13plus",
        "catvfr16plus",
        "catvfr18plus",
        "catvfrUnrated",
        "catvfrE",
    ]
    lsfRating: typing_extensions.Literal[
        "lsfUnspecified",
        "lsfSu",
        "lsfA",
        "lsfBo",
        "lsf13",
        "lsfR",
        "lsf17",
        "lsfD",
        "lsf21",
        "lsfUnrated",
    ]
    kijkwijzerRating: typing_extensions.Literal[
        "kijkwijzerUnspecified",
        "kijkwijzerAl",
        "kijkwijzer6",
        "kijkwijzer9",
        "kijkwijzer12",
        "kijkwijzer16",
        "kijkwijzer18",
        "kijkwijzerUnrated",
    ]
    kmrbRating: typing_extensions.Literal[
        "kmrbUnspecified",
        "kmrbAll",
        "kmrb12plus",
        "kmrb15plus",
        "kmrbTeenr",
        "kmrbR",
        "kmrbUnrated",
    ]
    nbcplRating: typing_extensions.Literal[
        "nbcplUnspecified",
        "nbcplI",
        "nbcplIi",
        "nbcplIii",
        "nbcplIv",
        "nbcpl18plus",
        "nbcplUnrated",
    ]
    resorteviolenciaRating: typing_extensions.Literal[
        "resorteviolenciaUnspecified",
        "resorteviolenciaA",
        "resorteviolenciaB",
        "resorteviolenciaC",
        "resorteviolenciaD",
        "resorteviolenciaE",
        "resorteviolenciaUnrated",
    ]
    mdaRating: typing_extensions.Literal[
        "mdaUnspecified",
        "mdaG",
        "mdaPg",
        "mdaPg13",
        "mdaNc16",
        "mdaM18",
        "mdaR21",
        "mdaUnrated",
    ]
    cicfRating: typing_extensions.Literal[
        "cicfUnspecified", "cicfE", "cicfKtEa", "cicfKntEna", "cicfUnrated"
    ]
    russiaRating: typing_extensions.Literal[
        "russiaUnspecified",
        "russia0",
        "russia6",
        "russia12",
        "russia16",
        "russia18",
        "russiaUnrated",
    ]
    fcbmRating: typing_extensions.Literal[
        "fcbmUnspecified",
        "fcbmU",
        "fcbmPg13",
        "fcbmP13",
        "fcbm18",
        "fcbm18sx",
        "fcbm18pa",
        "fcbm18sg",
        "fcbm18pl",
        "fcbmUnrated",
    ]
    csaRating: typing_extensions.Literal[
        "csaUnspecified",
        "csaT",
        "csa10",
        "csa12",
        "csa16",
        "csa18",
        "csaInterdiction",
        "csaUnrated",
    ]
    mibacRating: typing_extensions.Literal[
        "mibacUnspecified",
        "mibacT",
        "mibacVap",
        "mibacVm12",
        "mibacVm14",
        "mibacVm18",
        "mibacUnrated",
    ]
    fpbRatingReasons: typing.List[str]
    ilfilmRating: typing_extensions.Literal[
        "ilfilmUnspecified",
        "ilfilmAa",
        "ilfilm12",
        "ilfilm14",
        "ilfilm16",
        "ilfilm18",
        "ilfilmUnrated",
    ]
    bbfcRating: typing_extensions.Literal[
        "bbfcUnspecified",
        "bbfcU",
        "bbfcPg",
        "bbfc12a",
        "bbfc12",
        "bbfc15",
        "bbfc18",
        "bbfcR18",
        "bbfcUnrated",
    ]
    ifcoRating: typing_extensions.Literal[
        "ifcoUnspecified",
        "ifcoG",
        "ifcoPg",
        "ifco12",
        "ifco12a",
        "ifco15",
        "ifco15a",
        "ifco16",
        "ifco18",
        "ifcoUnrated",
    ]
    mekuRating: typing_extensions.Literal[
        "mekuUnspecified", "mekuS", "meku7", "meku12", "meku16", "meku18", "mekuUnrated"
    ]
    djctqRating: typing_extensions.Literal[
        "djctqUnspecified",
        "djctqL",
        "djctq10",
        "djctq12",
        "djctq14",
        "djctq16",
        "djctq18",
        "djctqEr",
        "djctqL10",
        "djctqL12",
        "djctqL14",
        "djctqL16",
        "djctqL18",
        "djctq1012",
        "djctq1014",
        "djctq1016",
        "djctq1018",
        "djctq1214",
        "djctq1216",
        "djctq1218",
        "djctq1416",
        "djctq1418",
        "djctq1618",
        "djctqUnrated",
    ]
    oflcRating: typing_extensions.Literal[
        "oflcUnspecified",
        "oflcG",
        "oflcPg",
        "oflcM",
        "oflcR13",
        "oflcR15",
        "oflcR16",
        "oflcR18",
        "oflcUnrated",
        "oflcRp13",
        "oflcRp16",
        "oflcRp18",
    ]
    incaaRating: typing_extensions.Literal[
        "incaaUnspecified",
        "incaaAtp",
        "incaaSam13",
        "incaaSam16",
        "incaaSam18",
        "incaaC",
        "incaaUnrated",
    ]
    ytRating: typing_extensions.Literal["ytUnspecified", "ytAgeRestricted"]
    nmcRating: typing_extensions.Literal[
        "nmcUnspecified",
        "nmcG",
        "nmcPg",
        "nmcPg13",
        "nmcPg15",
        "nmc15plus",
        "nmc18plus",
        "nmc18tc",
        "nmcUnrated",
    ]
    moctwRating: typing_extensions.Literal[
        "moctwUnspecified",
        "moctwG",
        "moctwP",
        "moctwPg",
        "moctwR",
        "moctwUnrated",
        "moctwR12",
        "moctwR15",
    ]
    pefilmRating: typing_extensions.Literal[
        "pefilmUnspecified",
        "pefilmPt",
        "pefilmPg",
        "pefilm14",
        "pefilm18",
        "pefilmUnrated",
    ]
    cnaRating: typing_extensions.Literal[
        "cnaUnspecified", "cnaAp", "cna12", "cna15", "cna18", "cna18plus", "cnaUnrated"
    ]
    cbfcRating: typing_extensions.Literal[
        "cbfcUnspecified", "cbfcU", "cbfcUA", "cbfcA", "cbfcS", "cbfcUnrated"
    ]
    mcstRating: typing_extensions.Literal[
        "mcstUnspecified",
        "mcstP",
        "mcst0",
        "mcstC13",
        "mcstC16",
        "mcst16plus",
        "mcstC18",
        "mcstGPg",
        "mcstUnrated",
    ]
    cscfRating: typing_extensions.Literal[
        "cscfUnspecified",
        "cscfAl",
        "cscfA",
        "cscf6",
        "cscf9",
        "cscf12",
        "cscf16",
        "cscf18",
        "cscfUnrated",
    ]
    eefilmRating: typing_extensions.Literal[
        "eefilmUnspecified",
        "eefilmPere",
        "eefilmL",
        "eefilmMs6",
        "eefilmK6",
        "eefilmMs12",
        "eefilmK12",
        "eefilmK14",
        "eefilmK16",
        "eefilmUnrated",
    ]
    mpaaRating: typing_extensions.Literal[
        "mpaaUnspecified",
        "mpaaG",
        "mpaaPg",
        "mpaaPg13",
        "mpaaR",
        "mpaaNc17",
        "mpaaX",
        "mpaaUnrated",
    ]
    tvpgRating: typing_extensions.Literal[
        "tvpgUnspecified",
        "tvpgY",
        "tvpgY7",
        "tvpgY7Fv",
        "tvpgG",
        "tvpgPg",
        "pg14",
        "tvpgMa",
        "tvpgUnrated",
    ]
    skfilmRating: typing_extensions.Literal[
        "skfilmUnspecified",
        "skfilmG",
        "skfilmP2",
        "skfilmP5",
        "skfilmP8",
        "skfilmUnrated",
    ]
    medietilsynetRating: typing_extensions.Literal[
        "medietilsynetUnspecified",
        "medietilsynetA",
        "medietilsynet6",
        "medietilsynet7",
        "medietilsynet9",
        "medietilsynet11",
        "medietilsynet12",
        "medietilsynet15",
        "medietilsynet18",
        "medietilsynetUnrated",
    ]
    rcnofRating: typing_extensions.Literal[
        "rcnofUnspecified",
        "rcnofI",
        "rcnofIi",
        "rcnofIii",
        "rcnofIv",
        "rcnofV",
        "rcnofVi",
        "rcnofUnrated",
    ]
    nkclvRating: typing_extensions.Literal[
        "nkclvUnspecified",
        "nkclvU",
        "nkclv7plus",
        "nkclv12plus",
        "nkclv16plus",
        "nkclv18plus",
        "nkclvUnrated",
    ]
    rteRating: typing_extensions.Literal[
        "rteUnspecified", "rteGa", "rteCh", "rtePs", "rteMa", "rteUnrated"
    ]
    mocRating: typing_extensions.Literal[
        "mocUnspecified",
        "mocE",
        "mocT",
        "moc7",
        "moc12",
        "moc15",
        "moc18",
        "mocX",
        "mocBanned",
        "mocUnrated",
    ]
    chvrsRating: typing_extensions.Literal[
        "chvrsUnspecified",
        "chvrsG",
        "chvrsPg",
        "chvrs14a",
        "chvrs18a",
        "chvrsR",
        "chvrsE",
        "chvrsUnrated",
    ]
    mccypRating: typing_extensions.Literal[
        "mccypUnspecified", "mccypA", "mccyp7", "mccyp11", "mccyp15", "mccypUnrated"
    ]
    mpaatRating: typing_extensions.Literal["mpaatUnspecified", "mpaatGb", "mpaatRb"]
    ecbmctRating: typing_extensions.Literal[
        "ecbmctUnspecified",
        "ecbmctG",
        "ecbmct7a",
        "ecbmct7plus",
        "ecbmct13a",
        "ecbmct13plus",
        "ecbmct15a",
        "ecbmct15plus",
        "ecbmct18plus",
        "ecbmctUnrated",
    ]
    menaMpaaRating: typing_extensions.Literal[
        "menaMpaaUnspecified",
        "menaMpaaG",
        "menaMpaaPg",
        "menaMpaaPg13",
        "menaMpaaR",
        "menaMpaaUnrated",
    ]
    fpbRating: typing_extensions.Literal[
        "fpbUnspecified",
        "fpbA",
        "fpbPg",
        "fpb79Pg",
        "fpb1012Pg",
        "fpb13",
        "fpb16",
        "fpb18",
        "fpbX18",
        "fpbXx",
        "fpbUnrated",
        "fpb10",
    ]
    bmukkRating: typing_extensions.Literal[
        "bmukkUnspecified",
        "bmukkAa",
        "bmukk6",
        "bmukk8",
        "bmukk10",
        "bmukk12",
        "bmukk14",
        "bmukk16",
        "bmukkUnrated",
    ]
    chfilmRating: typing_extensions.Literal[
        "chfilmUnspecified",
        "chfilm0",
        "chfilm6",
        "chfilm12",
        "chfilm16",
        "chfilm18",
        "chfilmUnrated",
    ]
    cceRating: typing_extensions.Literal[
        "cceUnspecified",
        "cceM4",
        "cceM6",
        "cceM12",
        "cceM16",
        "cceM18",
        "cceUnrated",
        "cceM14",
    ]
    mtrcbRating: typing_extensions.Literal[
        "mtrcbUnspecified",
        "mtrcbG",
        "mtrcbPg",
        "mtrcbR13",
        "mtrcbR16",
        "mtrcbR18",
        "mtrcbX",
        "mtrcbUnrated",
    ]
    czfilmRating: typing_extensions.Literal[
        "czfilmUnspecified",
        "czfilmU",
        "czfilm12",
        "czfilm14",
        "czfilm18",
        "czfilmUnrated",
    ]
    cccRating: typing_extensions.Literal[
        "cccUnspecified",
        "cccTe",
        "ccc6",
        "ccc14",
        "ccc18",
        "ccc18v",
        "ccc18s",
        "cccUnrated",
    ]
    fskRating: typing_extensions.Literal[
        "fskUnspecified", "fsk0", "fsk6", "fsk12", "fsk16", "fsk18", "fskUnrated"
    ]
    rtcRating: typing_extensions.Literal[
        "rtcUnspecified",
        "rtcAa",
        "rtcA",
        "rtcB",
        "rtcB15",
        "rtcC",
        "rtcD",
        "rtcUnrated",
    ]
    eirinRating: typing_extensions.Literal[
        "eirinUnspecified",
        "eirinG",
        "eirinPg12",
        "eirinR15plus",
        "eirinR18plus",
        "eirinUnrated",
    ]
    cncRating: typing_extensions.Literal[
        "cncUnspecified",
        "cncT",
        "cnc10",
        "cnc12",
        "cnc16",
        "cnc18",
        "cncE",
        "cncInterdiction",
        "cncUnrated",
    ]
    smsaRating: typing_extensions.Literal[
        "smsaUnspecified", "smsaA", "smsa7", "smsa11", "smsa15", "smsaUnrated"
    ]
    mccaaRating: typing_extensions.Literal[
        "mccaaUnspecified",
        "mccaaU",
        "mccaaPg",
        "mccaa12a",
        "mccaa12",
        "mccaa14",
        "mccaa15",
        "mccaa16",
        "mccaa18",
        "mccaaUnrated",
    ]
    grfilmRating: typing_extensions.Literal[
        "grfilmUnspecified",
        "grfilmK",
        "grfilmE",
        "grfilmK12",
        "grfilmK13",
        "grfilmK15",
        "grfilmK17",
        "grfilmK18",
        "grfilmUnrated",
    ]
    smaisRating: typing_extensions.Literal[
        "smaisUnspecified",
        "smaisL",
        "smais7",
        "smais12",
        "smais14",
        "smais16",
        "smais18",
        "smaisUnrated",
    ]
    nbcRating: typing_extensions.Literal[
        "nbcUnspecified",
        "nbcG",
        "nbcPg",
        "nbc12plus",
        "nbc15plus",
        "nbc18plus",
        "nbc18plusr",
        "nbcPu",
        "nbcUnrated",
    ]
    agcomRating: typing_extensions.Literal[
        "agcomUnspecified", "agcomT", "agcomVm14", "agcomVm18", "agcomUnrated"
    ]

class Thumbnail(typing_extensions.TypedDict, total=False):
    height: int
    url: str
    width: int

class InvideoPosition(typing_extensions.TypedDict, total=False):
    cornerPosition: typing_extensions.Literal[
        "topLeft", "topRight", "bottomLeft", "bottomRight"
    ]
    type: typing_extensions.Literal["corner"]

class SuperStickerMetadata(typing_extensions.TypedDict, total=False):
    altTextLanguage: str
    stickerId: str
    altText: str

class ChannelProfileDetails(typing_extensions.TypedDict, total=False):
    profileImageUrl: str
    channelUrl: str
    channelId: str
    displayName: str

class LiveStreamListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[LiveStream]
    etag: str
    visitorId: str
    pageInfo: PageInfo
    nextPageToken: str
    eventId: str
    prevPageToken: str
    tokenPagination: TokenPagination
    kind: str

class Channel(typing_extensions.TypedDict, total=False):
    topicDetails: ChannelTopicDetails
    contentOwnerDetails: ChannelContentOwnerDetails
    statistics: ChannelStatistics
    brandingSettings: ChannelBrandingSettings
    etag: str
    conversionPings: ChannelConversionPings
    localizations: typing.Dict[str, typing.Any]
    status: ChannelStatus
    contentDetails: ChannelContentDetails
    id: str
    snippet: ChannelSnippet
    auditDetails: ChannelAuditDetails
    kind: str

class ActivityContentDetails(typing_extensions.TypedDict, total=False):
    subscription: ActivityContentDetailsSubscription
    upload: ActivityContentDetailsUpload
    channelItem: ActivityContentDetailsChannelItem
    like: ActivityContentDetailsLike
    social: ActivityContentDetailsSocial
    bulletin: ActivityContentDetailsBulletin
    favorite: ActivityContentDetailsFavorite
    comment: ActivityContentDetailsComment
    recommendation: ActivityContentDetailsRecommendation
    promotedItem: ActivityContentDetailsPromotedItem
    playlistItem: ActivityContentDetailsPlaylistItem

class VideoSuggestions(typing_extensions.TypedDict, total=False):
    processingWarnings: typing.List[str]
    tagSuggestions: typing.List[VideoSuggestionsTagSuggestion]
    processingErrors: typing.List[str]
    editorSuggestions: typing.List[str]
    processingHints: typing.List[str]

class LiveStreamSnippet(typing_extensions.TypedDict, total=False):
    isDefaultStream: bool
    description: str
    channelId: str
    title: str
    publishedAt: str

class RelatedEntity(typing_extensions.TypedDict, total=False):
    entity: Entity

class ActivityContentDetailsFavorite(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class MemberListResponse(typing_extensions.TypedDict, total=False):
    eventId: str
    tokenPagination: TokenPagination
    visitorId: str
    items: typing.List[Member]
    etag: str
    nextPageToken: str
    pageInfo: PageInfo
    kind: str

class ActivityContentDetailsPromotedItem(typing_extensions.TypedDict, total=False):
    forecastingUrl: typing.List[str]
    customCtaButtonText: str
    destinationUrl: str
    ctaType: typing_extensions.Literal["ctaTypeUnspecified", "visitAdvertiserSite"]
    creativeViewUrl: str
    impressionUrl: typing.List[str]
    videoId: str
    descriptionText: str
    adTag: str
    clickTrackingUrl: str

class LiveChatMessage(typing_extensions.TypedDict, total=False):
    kind: str
    authorDetails: LiveChatMessageAuthorDetails
    etag: str
    id: str
    snippet: LiveChatMessageSnippet

class SuperChatEventListResponse(typing_extensions.TypedDict, total=False):
    tokenPagination: TokenPagination
    nextPageToken: str
    visitorId: str
    pageInfo: PageInfo
    items: typing.List[SuperChatEvent]
    eventId: str
    kind: str
    etag: str

class ChannelSectionTargeting(typing_extensions.TypedDict, total=False):
    countries: typing.List[str]
    regions: typing.List[str]
    languages: typing.List[str]

class LanguageTag(typing_extensions.TypedDict, total=False):
    value: str

class ChannelSectionLocalization(typing_extensions.TypedDict, total=False):
    title: str

class Comment(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    snippet: CommentSnippet
    id: str

class VideoAbuseReport(typing_extensions.TypedDict, total=False):
    secondaryReasonId: str
    reasonId: str
    videoId: str
    comments: str
    language: str

class VideoRecordingDetails(typing_extensions.TypedDict, total=False):
    location: GeoPoint
    locationDescription: str
    recordingDate: str

class VideoFileDetailsAudioStream(typing_extensions.TypedDict, total=False):
    channelCount: int
    codec: str
    vendor: str
    bitrateBps: str

class VideoContentDetailsRegionRestriction(typing_extensions.TypedDict, total=False):
    allowed: typing.List[str]
    blocked: typing.List[str]

class SearchResult(typing_extensions.TypedDict, total=False):
    snippet: SearchResultSnippet
    etag: str
    id: ResourceId
    kind: str

class IngestionInfo(typing_extensions.TypedDict, total=False):
    streamName: str
    rtmpsBackupIngestionAddress: str
    ingestionAddress: str
    rtmpsIngestionAddress: str
    backupIngestionAddress: str

class LiveChatMessageRetractedDetails(typing_extensions.TypedDict, total=False):
    retractedMessageId: str

class VideoFileDetailsVideoStream(typing_extensions.TypedDict, total=False):
    vendor: str
    bitrateBps: str
    aspectRatio: float
    heightPixels: int
    widthPixels: int
    frameRateFps: float
    codec: str
    rotation: typing_extensions.Literal[
        "none", "clockwise", "upsideDown", "counterClockwise", "other"
    ]

class LiveChatUserBannedMessageDetails(typing_extensions.TypedDict, total=False):
    bannedUserDetails: ChannelProfileDetails
    banDurationSeconds: str
    banType: typing_extensions.Literal["permanent", "temporary"]

class CommentListResponse(typing_extensions.TypedDict, total=False):
    tokenPagination: TokenPagination
    kind: str
    visitorId: str
    pageInfo: PageInfo
    etag: str
    items: typing.List[Comment]
    eventId: str
    nextPageToken: str

class ImageSettings(typing_extensions.TypedDict, total=False):
    watchIconImageUrl: str
    backgroundImageUrl: LocalizedProperty
    bannerTvImageUrl: str
    bannerTvLowImageUrl: str
    bannerTabletImageUrl: str
    smallBrandedBannerImageUrl: LocalizedProperty
    bannerMobileHdImageUrl: str
    bannerTabletLowImageUrl: str
    bannerTabletHdImageUrl: str
    bannerTabletExtraHdImageUrl: str
    bannerMobileLowImageUrl: str
    smallBrandedBannerImageImapScript: LocalizedProperty
    bannerTvHighImageUrl: str
    bannerTvMediumImageUrl: str
    bannerMobileExtraHdImageUrl: str
    largeBrandedBannerImageImapScript: LocalizedProperty
    bannerImageUrl: str
    trackingImageUrl: str
    largeBrandedBannerImageUrl: LocalizedProperty
    bannerMobileImageUrl: str
    bannerExternalUrl: str
    bannerMobileMediumHdImageUrl: str

class VideoRatingListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[VideoRating]
    eventId: str
    visitorId: str
    etag: str
    kind: str

class CommentThreadReplies(typing_extensions.TypedDict, total=False):
    comments: typing.List[Comment]

class SponsorSnippet(typing_extensions.TypedDict, total=False):
    cumulativeDurationMonths: int
    sponsorSince: str
    channelId: str
    sponsorDetails: ChannelProfileDetails

class PageInfo(typing_extensions.TypedDict, total=False):
    totalResults: int
    resultsPerPage: int

class AbuseReport(typing_extensions.TypedDict, total=False):
    relatedEntities: typing.List[RelatedEntity]
    description: str
    subject: Entity
    abuseTypes: typing.List[AbuseType]

class VideoAbuseReportReasonListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    visitorId: str
    items: typing.List[VideoAbuseReportReason]
    kind: str
    eventId: str

class ActivityContentDetailsUpload(typing_extensions.TypedDict, total=False):
    videoId: str

class InvideoBranding(typing_extensions.TypedDict, total=False):
    position: InvideoPosition
    targetChannelId: str
    imageBytes: str
    imageUrl: str
    timing: InvideoTiming

class LiveChatSuperStickerDetails(typing_extensions.TypedDict, total=False):
    superStickerMetadata: SuperStickerMetadata
    amountMicros: str
    amountDisplayString: str
    tier: int
    currency: str

class VideoRating(typing_extensions.TypedDict, total=False):
    rating: typing_extensions.Literal["none", "like", "dislike"]
    videoId: str

class ChannelContentDetails(typing_extensions.TypedDict, total=False):
    relatedPlaylists: typing.Dict[str, typing.Any]

class LiveStream(typing_extensions.TypedDict, total=False):
    snippet: LiveStreamSnippet
    cdn: CdnSettings
    contentDetails: LiveStreamContentDetails
    status: LiveStreamStatus
    etag: str
    id: str
    kind: str

class ChannelBannerResource(typing_extensions.TypedDict, total=False):
    kind: str
    url: str
    etag: str

class ResourceId(typing_extensions.TypedDict, total=False):
    playlistId: str
    videoId: str
    kind: str
    channelId: str

class CommentSnippet(typing_extensions.TypedDict, total=False):
    canRate: bool
    textOriginal: str
    parentId: str
    authorDisplayName: str
    authorChannelId: CommentSnippetAuthorChannelId
    videoId: str
    moderationStatus: typing_extensions.Literal[
        "published", "heldForReview", "likelySpam", "rejected"
    ]
    viewerRating: typing_extensions.Literal["none", "like", "dislike"]
    textDisplay: str
    authorChannelUrl: str
    channelId: str
    authorProfileImageUrl: str
    publishedAt: str
    likeCount: int
    updatedAt: str

class InvideoTiming(typing_extensions.TypedDict, total=False):
    offsetMs: str
    type: typing_extensions.Literal["offsetFromStart", "offsetFromEnd"]
    durationMs: str

class CommentSnippetAuthorChannelId(typing_extensions.TypedDict, total=False):
    value: str

class LiveChatSuperChatDetails(typing_extensions.TypedDict, total=False):
    currency: str
    amountMicros: str
    userComment: str
    amountDisplayString: str
    tier: int

class LocalizedString(typing_extensions.TypedDict, total=False):
    language: str
    value: str

class SuperChatEventSnippet(typing_extensions.TypedDict, total=False):
    currency: str
    messageType: int
    isSuperStickerEvent: bool
    channelId: str
    commentText: str
    amountMicros: str
    displayString: str
    superStickerMetadata: SuperStickerMetadata
    supporterDetails: ChannelProfileDetails
    createdAt: str

class Subscription(typing_extensions.TypedDict, total=False):
    kind: str
    subscriberSnippet: SubscriptionSubscriberSnippet
    snippet: SubscriptionSnippet
    contentDetails: SubscriptionContentDetails
    id: str
    etag: str

class ThirdPartyLink(typing_extensions.TypedDict, total=False):
    snippet: ThirdPartyLinkSnippet
    kind: str
    status: ThirdPartyLinkStatus
    etag: str
    linkingToken: str

class PlaylistItemListResponse(typing_extensions.TypedDict, total=False):
    prevPageToken: str
    visitorId: str
    tokenPagination: TokenPagination
    items: typing.List[PlaylistItem]
    kind: str
    pageInfo: PageInfo
    eventId: str
    nextPageToken: str
    etag: str

class LiveChatBanSnippet(typing_extensions.TypedDict, total=False):
    liveChatId: str
    type: typing_extensions.Literal[
        "liveChatBanTypeUnspecified", "permanent", "temporary"
    ]
    banDurationSeconds: str
    bannedUserDetails: ChannelProfileDetails

class ActivityListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[Activity]
    eventId: str
    visitorId: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    etag: str

class ChannelSection(typing_extensions.TypedDict, total=False):
    kind: str
    contentDetails: ChannelSectionContentDetails
    targeting: ChannelSectionTargeting
    etag: str
    localizations: typing.Dict[str, typing.Any]
    id: str
    snippet: ChannelSectionSnippet

class PlaylistSnippet(typing_extensions.TypedDict, total=False):
    channelTitle: str
    description: str
    channelId: str
    publishedAt: str
    tags: typing.List[str]
    localized: PlaylistLocalization
    title: str
    thumbnails: ThumbnailDetails
    defaultLanguage: str

class LiveStreamStatus(typing_extensions.TypedDict, total=False):
    healthStatus: LiveStreamHealthStatus
    streamStatus: typing_extensions.Literal[
        "created", "ready", "active", "inactive", "error"
    ]

class VideoProjectDetails(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]

class ActivityContentDetailsPlaylistItem(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId
    playlistItemId: str
    playlistId: str

class LiveChatBan(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    id: str
    snippet: LiveChatBanSnippet

class ChannelBrandingSettings(typing_extensions.TypedDict, total=False):
    image: ImageSettings
    hints: typing.List[PropertyValue]
    channel: ChannelSettings
    watch: WatchSettings

class I18nLanguage(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    snippet: I18nLanguageSnippet
    id: str

class MonitorStreamInfo(typing_extensions.TypedDict, total=False):
    broadcastStreamDelayMs: int
    enableMonitorStream: bool
    embedHtml: str

class VideoProcessingDetailsProcessingProgress(
    typing_extensions.TypedDict, total=False
):
    partsProcessed: str
    partsTotal: str
    timeLeftMs: str

class ChannelSectionListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[ChannelSection]
    kind: str
    visitorId: str
    eventId: str
    etag: str

class VideoProcessingDetails(typing_extensions.TypedDict, total=False):
    editorSuggestionsAvailability: str
    tagSuggestionsAvailability: str
    processingProgress: VideoProcessingDetailsProcessingProgress
    thumbnailsAvailability: str
    processingIssuesAvailability: str
    fileDetailsAvailability: str
    processingFailureReason: typing_extensions.Literal[
        "uploadFailed", "transcodeFailed", "streamingFailed", "other"
    ]
    processingStatus: typing_extensions.Literal[
        "processing", "succeeded", "failed", "terminated"
    ]

class LiveBroadcastListResponse(typing_extensions.TypedDict, total=False):
    prevPageToken: str
    etag: str
    nextPageToken: str
    eventId: str
    items: typing.List[LiveBroadcast]
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    kind: str
    visitorId: str

class AccessPolicy(typing_extensions.TypedDict, total=False):
    exception: typing.List[str]
    allowed: bool

class PropertyValue(typing_extensions.TypedDict, total=False):
    property: str
    value: str

class CdnSettings(typing_extensions.TypedDict, total=False):
    ingestionInfo: IngestionInfo
    format: str
    ingestionType: typing_extensions.Literal["rtmp", "dash", "webrtc", "hls"]
    frameRate: typing_extensions.Literal["30fps", "60fps", "variable"]
    resolution: typing_extensions.Literal[
        "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "variable"
    ]

class ActivitySnippet(typing_extensions.TypedDict, total=False):
    groupId: str
    channelId: str
    thumbnails: ThumbnailDetails
    channelTitle: str
    description: str
    publishedAt: str
    title: str
    type: typing_extensions.Literal[
        "typeUnspecified",
        "upload",
        "like",
        "favorite",
        "comment",
        "subscription",
        "playlistItem",
        "recommendation",
        "bulletin",
        "social",
        "channelItem",
        "promotedItem",
    ]

class LiveChatMessageListResponse(typing_extensions.TypedDict, total=False):
    visitorId: str
    items: typing.List[LiveChatMessage]
    etag: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    nextPageToken: str
    eventId: str
    kind: str
    offlineAt: str
    pollingIntervalMillis: int

class MembershipsLevelSnippet(typing_extensions.TypedDict, total=False):
    creatorChannelId: str
    levelDetails: LevelDetails

class I18nRegionListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    eventId: str
    items: typing.List[I18nRegion]
    visitorId: str
    etag: str

class VideoAbuseReportReason(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    snippet: VideoAbuseReportReasonSnippet
    id: str

class ChannelSnippet(typing_extensions.TypedDict, total=False):
    defaultLanguage: str
    title: str
    publishedAt: str
    customUrl: str
    localized: ChannelLocalization
    description: str
    thumbnails: ThumbnailDetails
    country: str

class I18nRegionSnippet(typing_extensions.TypedDict, total=False):
    name: str
    gl: str

class LiveChatTextMessageDetails(typing_extensions.TypedDict, total=False):
    messageText: str

class LevelDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class ThumbnailSetResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[ThumbnailDetails]
    visitorId: str
    etag: str
    kind: str
    eventId: str

class ActivityContentDetailsChannelItem(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class VideoCategorySnippet(typing_extensions.TypedDict, total=False):
    title: str
    channelId: str
    assignable: bool

class PlaylistListResponse(typing_extensions.TypedDict, total=False):
    prevPageToken: str
    nextPageToken: str
    eventId: str
    kind: str
    items: typing.List[Playlist]
    visitorId: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    etag: str

class WatchSettings(typing_extensions.TypedDict, total=False):
    featuredPlaylistId: str
    textColor: str
    backgroundColor: str

class Entity(typing_extensions.TypedDict, total=False):
    url: str
    typeId: str
    id: str

class LiveChatFanFundingEventDetails(typing_extensions.TypedDict, total=False):
    amountDisplayString: str
    userComment: str
    currency: str
    amountMicros: str

class VideoAbuseReportSecondaryReason(typing_extensions.TypedDict, total=False):
    id: str
    label: str

class ActivityContentDetailsLike(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class TestItemTestItemSnippet(typing_extensions.TypedDict, total=False): ...

class LocalizedProperty(typing_extensions.TypedDict, total=False):
    defaultLanguage: LanguageTag
    localized: typing.List[LocalizedString]
    default: str

class Sponsor(typing_extensions.TypedDict, total=False):
    snippet: SponsorSnippet
    etag: str
    kind: str

class SearchListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    nextPageToken: str
    kind: str
    tokenPagination: TokenPagination
    items: typing.List[SearchResult]
    regionCode: str
    visitorId: str
    pageInfo: PageInfo
    prevPageToken: str
    eventId: str

class PlaylistStatus(typing_extensions.TypedDict, total=False):
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]

class VideoAgeGating(typing_extensions.TypedDict, total=False):
    restricted: bool
    alcoholContent: bool
    videoGameRating: typing_extensions.Literal[
        "anyone", "m15Plus", "m16Plus", "m17Plus"
    ]

class CommentThread(typing_extensions.TypedDict, total=False):
    snippet: CommentThreadSnippet
    id: str
    kind: str
    replies: CommentThreadReplies
    etag: str

class Activity(typing_extensions.TypedDict, total=False):
    id: str
    etag: str
    contentDetails: ActivityContentDetails
    snippet: ActivitySnippet
    kind: str

class ChannelConversionPing(typing_extensions.TypedDict, total=False):
    conversionUrl: str
    context: typing_extensions.Literal["subscribe", "unsubscribe", "cview"]

class GeoPoint(typing_extensions.TypedDict, total=False):
    latitude: float
    altitude: float
    longitude: float

class LiveBroadcastContentDetails(typing_extensions.TypedDict, total=False):
    recordFromStart: bool
    enableDvr: bool
    closedCaptionsType: typing_extensions.Literal[
        "closedCaptionsTypeUnspecified",
        "closedCaptionsDisabled",
        "closedCaptionsHttpPost",
        "closedCaptionsEmbedded",
    ]
    startWithSlate: bool
    enableEmbed: bool
    projection: typing_extensions.Literal[
        "projectionUnspecified", "rectangular", "360", "mesh"
    ]
    enableAutoStop: bool
    mesh: str
    enableAutoStart: bool
    enableLowLatency: bool
    latencyPreference: typing_extensions.Literal[
        "latencyPreferenceUnspecified", "normal", "low", "ultraLow"
    ]
    enableContentEncryption: bool
    monitorStream: MonitorStreamInfo
    boundStreamId: str
    boundStreamLastUpdateTimeMs: str
    enableClosedCaptions: bool

class SuperChatEvent(typing_extensions.TypedDict, total=False):
    snippet: SuperChatEventSnippet
    id: str
    kind: str
    etag: str

class ChannelContentOwnerDetails(typing_extensions.TypedDict, total=False):
    contentOwner: str
    timeLinked: str

class ThumbnailDetails(typing_extensions.TypedDict, total=False):
    default: Thumbnail
    high: Thumbnail
    maxres: Thumbnail
    standard: Thumbnail
    medium: Thumbnail

class ChannelTopicDetails(typing_extensions.TypedDict, total=False):
    topicIds: typing.List[str]
    topicCategories: typing.List[str]

class ChannelLocalization(typing_extensions.TypedDict, total=False):
    description: str
    title: str

class LiveBroadcastSnippet(typing_extensions.TypedDict, total=False):
    liveChatId: str
    actualEndTime: str
    description: str
    thumbnails: ThumbnailDetails
    publishedAt: str
    channelId: str
    scheduledEndTime: str
    scheduledStartTime: str
    title: str
    isDefaultBroadcast: bool
    actualStartTime: str

class SubscriptionSnippet(typing_extensions.TypedDict, total=False):
    description: str
    publishedAt: str
    resourceId: ResourceId
    thumbnails: ThumbnailDetails
    channelId: str
    channelTitle: str
    title: str

class VideoListResponse(typing_extensions.TypedDict, total=False):
    tokenPagination: TokenPagination
    items: typing.List[Video]
    visitorId: str
    pageInfo: PageInfo
    nextPageToken: str
    kind: str
    etag: str
    eventId: str
    prevPageToken: str

class MembershipsDurationAtLevel(typing_extensions.TypedDict, total=False):
    memberTotalDurationMonths: int
    level: str
    memberSince: str

class VideoCategory(typing_extensions.TypedDict, total=False):
    id: str
    snippet: VideoCategorySnippet
    kind: str
    etag: str

class ActivityContentDetailsBulletin(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class ThirdPartyLinkStatus(typing_extensions.TypedDict, total=False):
    linkStatus: typing_extensions.Literal["unknown", "failed", "pending", "linked"]

class ChannelListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Channel]
    prevPageToken: str
    pageInfo: PageInfo
    nextPageToken: str
    etag: str
    kind: str
    tokenPagination: TokenPagination
    visitorId: str
    eventId: str

class CaptionSnippet(typing_extensions.TypedDict, total=False):
    videoId: str
    name: str
    status: typing_extensions.Literal["serving", "syncing", "failed"]
    isDraft: bool
    failureReason: typing_extensions.Literal[
        "unknownFormat", "unsupportedFormat", "processingFailed"
    ]
    isEasyReader: bool
    isCC: bool
    audioTrackType: typing_extensions.Literal[
        "unknown", "primary", "commentary", "descriptive"
    ]
    isAutoSynced: bool
    language: str
    lastUpdated: str
    trackKind: typing_extensions.Literal["standard", "ASR", "forced"]
    isLarge: bool

class CommentThreadListResponse(typing_extensions.TypedDict, total=False):
    eventId: str
    tokenPagination: TokenPagination
    etag: str
    items: typing.List[CommentThread]
    nextPageToken: str
    visitorId: str
    pageInfo: PageInfo
    kind: str

class ChannelSectionSnippet(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "channelsectionTypeUnspecified",
        "singlePlaylist",
        "multiplePlaylists",
        "popularUploads",
        "recentUploads",
        "likes",
        "allPlaylists",
        "likedPlaylists",
        "recentPosts",
        "recentActivity",
        "liveEvents",
        "upcomingEvents",
        "completedEvents",
        "multipleChannels",
        "postedVideos",
        "postedPlaylists",
        "subscriptions",
    ]
    localized: ChannelSectionLocalization
    channelId: str
    position: int
    style: typing_extensions.Literal[
        "channelsectionStyleUnspecified", "horizontalRow", "verticalList"
    ]
    title: str
    defaultLanguage: str

class LiveStreamConfigurationIssue(typing_extensions.TypedDict, total=False):
    reason: str
    description: str
    type: typing_extensions.Literal[
        "gopSizeOver",
        "gopSizeLong",
        "gopSizeShort",
        "openGop",
        "badContainer",
        "audioBitrateHigh",
        "audioBitrateLow",
        "audioSampleRate",
        "bitrateHigh",
        "bitrateLow",
        "audioCodec",
        "videoCodec",
        "noAudioStream",
        "noVideoStream",
        "multipleVideoStreams",
        "multipleAudioStreams",
        "audioTooManyChannels",
        "interlacedVideo",
        "frameRateHigh",
        "resolutionMismatch",
        "videoCodecMismatch",
        "videoInterlaceMismatch",
        "videoProfileMismatch",
        "videoBitrateMismatch",
        "framerateMismatch",
        "gopMismatch",
        "audioSampleRateMismatch",
        "audioStereoMismatch",
        "audioCodecMismatch",
        "audioBitrateMismatch",
        "videoResolutionSuboptimal",
        "videoResolutionUnsupported",
        "videoIngestionStarved",
        "videoIngestionFasterThanRealtime",
    ]
    severity: typing_extensions.Literal["info", "warning", "error"]

class LiveChatModerator(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    id: str
    snippet: LiveChatModeratorSnippet

class SubscriptionContentDetails(typing_extensions.TypedDict, total=False):
    newItemCount: int
    totalItemCount: int
    activityType: typing_extensions.Literal[
        "subscriptionActivityTypeUnspecified", "all", "uploads"
    ]

class PlaylistItem(typing_extensions.TypedDict, total=False):
    status: PlaylistItemStatus
    kind: str
    snippet: PlaylistItemSnippet
    contentDetails: PlaylistItemContentDetails
    etag: str
    id: str

class PlaylistItemContentDetails(typing_extensions.TypedDict, total=False):
    note: str
    endAt: str
    videoId: str
    startAt: str
    videoPublishedAt: str

class VideoLocalization(typing_extensions.TypedDict, total=False):
    description: str
    title: str

class SubscriptionSubscriberSnippet(typing_extensions.TypedDict, total=False):
    description: str
    title: str
    thumbnails: ThumbnailDetails
    channelId: str
