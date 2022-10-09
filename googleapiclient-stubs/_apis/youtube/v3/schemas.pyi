import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbuseReport(typing_extensions.TypedDict, total=False):
    abuseTypes: _list[AbuseType]
    description: str
    relatedEntities: _list[RelatedEntity]
    subject: Entity

@typing.type_check_only
class AbuseType(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class AccessPolicy(typing_extensions.TypedDict, total=False):
    allowed: bool
    exception: _list[str]

@typing.type_check_only
class Activity(typing_extensions.TypedDict, total=False):
    contentDetails: ActivityContentDetails
    etag: str
    id: str
    kind: str
    snippet: ActivitySnippet

@typing.type_check_only
class ActivityContentDetails(typing_extensions.TypedDict, total=False):
    bulletin: ActivityContentDetailsBulletin
    channelItem: ActivityContentDetailsChannelItem
    comment: ActivityContentDetailsComment
    favorite: ActivityContentDetailsFavorite
    like: ActivityContentDetailsLike
    playlistItem: ActivityContentDetailsPlaylistItem
    promotedItem: ActivityContentDetailsPromotedItem
    recommendation: ActivityContentDetailsRecommendation
    social: ActivityContentDetailsSocial
    subscription: ActivityContentDetailsSubscription
    upload: ActivityContentDetailsUpload

@typing.type_check_only
class ActivityContentDetailsBulletin(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsChannelItem(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsComment(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsFavorite(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsLike(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsPlaylistItem(typing_extensions.TypedDict, total=False):
    playlistId: str
    playlistItemId: str
    resourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsPromotedItem(typing_extensions.TypedDict, total=False):
    adTag: str
    clickTrackingUrl: str
    creativeViewUrl: str
    ctaType: typing_extensions.Literal["ctaTypeUnspecified", "visitAdvertiserSite"]
    customCtaButtonText: str
    descriptionText: str
    destinationUrl: str
    forecastingUrl: _list[str]
    impressionUrl: _list[str]
    videoId: str

@typing.type_check_only
class ActivityContentDetailsRecommendation(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "reasonUnspecified", "videoFavorited", "videoLiked", "videoWatched"
    ]
    resourceId: ResourceId
    seedResourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsSocial(typing_extensions.TypedDict, total=False):
    author: str
    imageUrl: str
    referenceUrl: str
    resourceId: ResourceId
    type: typing_extensions.Literal["unspecified", "googlePlus", "facebook", "twitter"]

@typing.type_check_only
class ActivityContentDetailsSubscription(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

@typing.type_check_only
class ActivityContentDetailsUpload(typing_extensions.TypedDict, total=False):
    videoId: str

@typing.type_check_only
class ActivityListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Activity]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class ActivitySnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    channelTitle: str
    description: str
    groupId: str
    publishedAt: str
    thumbnails: ThumbnailDetails
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

@typing.type_check_only
class Caption(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: CaptionSnippet

@typing.type_check_only
class CaptionListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Caption]
    kind: str
    visitorId: str

@typing.type_check_only
class CaptionSnippet(typing_extensions.TypedDict, total=False):
    audioTrackType: typing_extensions.Literal[
        "unknown", "primary", "commentary", "descriptive"
    ]
    failureReason: typing_extensions.Literal[
        "unknownFormat", "unsupportedFormat", "processingFailed"
    ]
    isAutoSynced: bool
    isCC: bool
    isDraft: bool
    isEasyReader: bool
    isLarge: bool
    language: str
    lastUpdated: str
    name: str
    status: typing_extensions.Literal["serving", "syncing", "failed"]
    trackKind: typing_extensions.Literal["standard", "ASR", "forced"]
    videoId: str

@typing.type_check_only
class CdnSettings(typing_extensions.TypedDict, total=False):
    format: str
    frameRate: typing_extensions.Literal["30fps", "60fps", "variable"]
    ingestionInfo: IngestionInfo
    ingestionType: typing_extensions.Literal["rtmp", "dash", "webrtc", "hls"]
    resolution: typing_extensions.Literal[
        "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "variable"
    ]

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    auditDetails: ChannelAuditDetails
    brandingSettings: ChannelBrandingSettings
    contentDetails: ChannelContentDetails
    contentOwnerDetails: ChannelContentOwnerDetails
    conversionPings: ChannelConversionPings
    etag: str
    id: str
    kind: str
    localizations: dict[str, typing.Any]
    snippet: ChannelSnippet
    statistics: ChannelStatistics
    status: ChannelStatus
    topicDetails: ChannelTopicDetails

@typing.type_check_only
class ChannelAuditDetails(typing_extensions.TypedDict, total=False):
    communityGuidelinesGoodStanding: bool
    contentIdClaimsGoodStanding: bool
    copyrightStrikesGoodStanding: bool

@typing.type_check_only
class ChannelBannerResource(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    url: str

@typing.type_check_only
class ChannelBrandingSettings(typing_extensions.TypedDict, total=False):
    channel: ChannelSettings
    hints: _list[PropertyValue]
    image: ImageSettings
    watch: WatchSettings

@typing.type_check_only
class ChannelContentDetails(typing_extensions.TypedDict, total=False):
    relatedPlaylists: dict[str, typing.Any]

@typing.type_check_only
class ChannelContentOwnerDetails(typing_extensions.TypedDict, total=False):
    contentOwner: str
    timeLinked: str

@typing.type_check_only
class ChannelConversionPing(typing_extensions.TypedDict, total=False):
    context: typing_extensions.Literal["subscribe", "unsubscribe", "cview"]
    conversionUrl: str

@typing.type_check_only
class ChannelConversionPings(typing_extensions.TypedDict, total=False):
    pings: _list[ChannelConversionPing]

@typing.type_check_only
class ChannelListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Channel]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class ChannelLocalization(typing_extensions.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class ChannelProfileDetails(typing_extensions.TypedDict, total=False):
    channelId: str
    channelUrl: str
    displayName: str
    profileImageUrl: str

@typing.type_check_only
class ChannelSection(typing_extensions.TypedDict, total=False):
    contentDetails: ChannelSectionContentDetails
    etag: str
    id: str
    kind: str
    localizations: dict[str, typing.Any]
    snippet: ChannelSectionSnippet
    targeting: ChannelSectionTargeting

@typing.type_check_only
class ChannelSectionContentDetails(typing_extensions.TypedDict, total=False):
    channels: _list[str]
    playlists: _list[str]

@typing.type_check_only
class ChannelSectionListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[ChannelSection]
    kind: str
    visitorId: str

@typing.type_check_only
class ChannelSectionLocalization(typing_extensions.TypedDict, total=False):
    title: str

@typing.type_check_only
class ChannelSectionSnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    defaultLanguage: str
    localized: ChannelSectionLocalization
    position: int
    style: typing_extensions.Literal[
        "channelsectionStyleUnspecified", "horizontalRow", "verticalList"
    ]
    title: str
    type: typing_extensions.Literal[
        "channelsectionTypeUndefined",
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

@typing.type_check_only
class ChannelSectionTargeting(typing_extensions.TypedDict, total=False):
    countries: _list[str]
    languages: _list[str]
    regions: _list[str]

@typing.type_check_only
class ChannelSettings(typing_extensions.TypedDict, total=False):
    country: str
    defaultLanguage: str
    defaultTab: str
    description: str
    featuredChannelsTitle: str
    featuredChannelsUrls: _list[str]
    keywords: str
    moderateComments: bool
    profileColor: str
    showBrowseView: bool
    showRelatedChannels: bool
    title: str
    trackingAnalyticsAccountId: str
    unsubscribedTrailer: str

@typing.type_check_only
class ChannelSnippet(typing_extensions.TypedDict, total=False):
    country: str
    customUrl: str
    defaultLanguage: str
    description: str
    localized: ChannelLocalization
    publishedAt: str
    thumbnails: ThumbnailDetails
    title: str

@typing.type_check_only
class ChannelStatistics(typing_extensions.TypedDict, total=False):
    commentCount: str
    hiddenSubscriberCount: bool
    subscriberCount: str
    videoCount: str
    viewCount: str

@typing.type_check_only
class ChannelStatus(typing_extensions.TypedDict, total=False):
    isLinked: bool
    longUploadsStatus: typing_extensions.Literal[
        "longUploadsUnspecified", "allowed", "eligible", "disallowed"
    ]
    madeForKids: bool
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]
    selfDeclaredMadeForKids: bool

@typing.type_check_only
class ChannelToStoreLinkDetails(typing_extensions.TypedDict, total=False):
    merchantId: str
    storeName: str
    storeUrl: str

@typing.type_check_only
class ChannelTopicDetails(typing_extensions.TypedDict, total=False):
    topicCategories: _list[str]
    topicIds: _list[str]

@typing.type_check_only
class Comment(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: CommentSnippet

@typing.type_check_only
class CommentListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Comment]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class CommentSnippet(typing_extensions.TypedDict, total=False):
    authorChannelId: CommentSnippetAuthorChannelId
    authorChannelUrl: str
    authorDisplayName: str
    authorProfileImageUrl: str
    canRate: bool
    channelId: str
    likeCount: int
    moderationStatus: typing_extensions.Literal[
        "published", "heldForReview", "likelySpam", "rejected"
    ]
    parentId: str
    publishedAt: str
    textDisplay: str
    textOriginal: str
    updatedAt: str
    videoId: str
    viewerRating: typing_extensions.Literal["none", "like", "dislike"]

@typing.type_check_only
class CommentSnippetAuthorChannelId(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class CommentThread(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    replies: CommentThreadReplies
    snippet: CommentThreadSnippet

@typing.type_check_only
class CommentThreadListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[CommentThread]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class CommentThreadReplies(typing_extensions.TypedDict, total=False):
    comments: _list[Comment]

@typing.type_check_only
class CommentThreadSnippet(typing_extensions.TypedDict, total=False):
    canReply: bool
    channelId: str
    isPublic: bool
    topLevelComment: Comment
    totalReplyCount: int
    videoId: str

@typing.type_check_only
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
    agcomRating: typing_extensions.Literal[
        "agcomUnspecified", "agcomT", "agcomVm14", "agcomVm18", "agcomUnrated"
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
    cbfcRating: typing_extensions.Literal[
        "cbfcUnspecified",
        "cbfcU",
        "cbfcUA",
        "cbfcUA7plus",
        "cbfcUA13plus",
        "cbfcUA16plus",
        "cbfcA",
        "cbfcS",
        "cbfcUnrated",
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
    chfilmRating: typing_extensions.Literal[
        "chfilmUnspecified",
        "chfilm0",
        "chfilm6",
        "chfilm12",
        "chfilm16",
        "chfilm18",
        "chfilmUnrated",
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
    cicfRating: typing_extensions.Literal[
        "cicfUnspecified", "cicfE", "cicfKtEa", "cicfKntEna", "cicfUnrated"
    ]
    cnaRating: typing_extensions.Literal[
        "cnaUnspecified", "cnaAp", "cna12", "cna15", "cna18", "cna18plus", "cnaUnrated"
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
    czfilmRating: typing_extensions.Literal[
        "czfilmUnspecified",
        "czfilmU",
        "czfilm12",
        "czfilm14",
        "czfilm18",
        "czfilmUnrated",
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
    djctqRatingReasons: _list[str]
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
    egfilmRating: typing_extensions.Literal[
        "egfilmUnspecified", "egfilmGn", "egfilm18", "egfilmBn", "egfilmUnrated"
    ]
    eirinRating: typing_extensions.Literal[
        "eirinUnspecified",
        "eirinG",
        "eirinPg12",
        "eirinR15plus",
        "eirinR18plus",
        "eirinUnrated",
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
    fcoRating: typing_extensions.Literal[
        "fcoUnspecified", "fcoI", "fcoIia", "fcoIib", "fcoIi", "fcoIii", "fcoUnrated"
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
    fpbRatingReasons: _list[str]
    fskRating: typing_extensions.Literal[
        "fskUnspecified", "fsk0", "fsk6", "fsk12", "fsk16", "fsk18", "fskUnrated"
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
    ilfilmRating: typing_extensions.Literal[
        "ilfilmUnspecified",
        "ilfilmAa",
        "ilfilm12",
        "ilfilm14",
        "ilfilm16",
        "ilfilm18",
        "ilfilmUnrated",
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
    kfcbRating: typing_extensions.Literal[
        "kfcbUnspecified", "kfcbG", "kfcbPg", "kfcb16plus", "kfcbR", "kfcbUnrated"
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
    mccypRating: typing_extensions.Literal[
        "mccypUnspecified", "mccypA", "mccyp7", "mccyp11", "mccyp15", "mccypUnrated"
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
    mekuRating: typing_extensions.Literal[
        "mekuUnspecified", "mekuS", "meku7", "meku12", "meku16", "meku18", "mekuUnrated"
    ]
    menaMpaaRating: typing_extensions.Literal[
        "menaMpaaUnspecified",
        "menaMpaaG",
        "menaMpaaPg",
        "menaMpaaPg13",
        "menaMpaaR",
        "menaMpaaUnrated",
    ]
    mibacRating: typing_extensions.Literal[
        "mibacUnspecified",
        "mibacT",
        "mibacVap",
        "mibacVm6",
        "mibacVm12",
        "mibacVm14",
        "mibacVm16",
        "mibacVm18",
        "mibacUnrated",
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
    mpaatRating: typing_extensions.Literal["mpaatUnspecified", "mpaatGb", "mpaatRb"]
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
    nbcplRating: typing_extensions.Literal[
        "nbcplUnspecified",
        "nbcplI",
        "nbcplIi",
        "nbcplIii",
        "nbcplIv",
        "nbcpl18plus",
        "nbcplUnrated",
    ]
    nfrcRating: typing_extensions.Literal[
        "nfrcUnspecified", "nfrcA", "nfrcB", "nfrcC", "nfrcD", "nfrcX", "nfrcUnrated"
    ]
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
    nkclvRating: typing_extensions.Literal[
        "nkclvUnspecified",
        "nkclvU",
        "nkclv7plus",
        "nkclv12plus",
        "nkclv16plus",
        "nkclv18plus",
        "nkclvUnrated",
    ]
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
    pefilmRating: typing_extensions.Literal[
        "pefilmUnspecified",
        "pefilmPt",
        "pefilmPg",
        "pefilm14",
        "pefilm18",
        "pefilmUnrated",
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
    resorteviolenciaRating: typing_extensions.Literal[
        "resorteviolenciaUnspecified",
        "resorteviolenciaA",
        "resorteviolenciaB",
        "resorteviolenciaC",
        "resorteviolenciaD",
        "resorteviolenciaE",
        "resorteviolenciaUnrated",
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
    rteRating: typing_extensions.Literal[
        "rteUnspecified", "rteGa", "rteCh", "rtePs", "rteMa", "rteUnrated"
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
    skfilmRating: typing_extensions.Literal[
        "skfilmUnspecified",
        "skfilmG",
        "skfilmP2",
        "skfilmP5",
        "skfilmP8",
        "skfilmUnrated",
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
    smsaRating: typing_extensions.Literal[
        "smsaUnspecified", "smsaA", "smsa7", "smsa11", "smsa15", "smsaUnrated"
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
    ytRating: typing_extensions.Literal["ytUnspecified", "ytAgeRestricted"]

@typing.type_check_only
class Cuepoint(typing_extensions.TypedDict, total=False):
    cueType: typing_extensions.Literal["cueTypeUnspecified", "cueTypeAd"]
    durationSecs: int
    etag: str
    id: str
    insertionOffsetTimeMs: str
    walltimeMs: str

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    id: str
    typeId: str
    url: str

@typing.type_check_only
class GeoPoint(typing_extensions.TypedDict, total=False):
    altitude: float
    latitude: float
    longitude: float

@typing.type_check_only
class I18nLanguage(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: I18nLanguageSnippet

@typing.type_check_only
class I18nLanguageListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[I18nLanguage]
    kind: str
    visitorId: str

@typing.type_check_only
class I18nLanguageSnippet(typing_extensions.TypedDict, total=False):
    hl: str
    name: str

@typing.type_check_only
class I18nRegion(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: I18nRegionSnippet

@typing.type_check_only
class I18nRegionListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[I18nRegion]
    kind: str
    visitorId: str

@typing.type_check_only
class I18nRegionSnippet(typing_extensions.TypedDict, total=False):
    gl: str
    name: str

@typing.type_check_only
class ImageSettings(typing_extensions.TypedDict, total=False):
    backgroundImageUrl: LocalizedProperty
    bannerExternalUrl: str
    bannerImageUrl: str
    bannerMobileExtraHdImageUrl: str
    bannerMobileHdImageUrl: str
    bannerMobileImageUrl: str
    bannerMobileLowImageUrl: str
    bannerMobileMediumHdImageUrl: str
    bannerTabletExtraHdImageUrl: str
    bannerTabletHdImageUrl: str
    bannerTabletImageUrl: str
    bannerTabletLowImageUrl: str
    bannerTvHighImageUrl: str
    bannerTvImageUrl: str
    bannerTvLowImageUrl: str
    bannerTvMediumImageUrl: str
    largeBrandedBannerImageImapScript: LocalizedProperty
    largeBrandedBannerImageUrl: LocalizedProperty
    smallBrandedBannerImageImapScript: LocalizedProperty
    smallBrandedBannerImageUrl: LocalizedProperty
    trackingImageUrl: str
    watchIconImageUrl: str

@typing.type_check_only
class IngestionInfo(typing_extensions.TypedDict, total=False):
    backupIngestionAddress: str
    ingestionAddress: str
    rtmpsBackupIngestionAddress: str
    rtmpsIngestionAddress: str
    streamName: str

@typing.type_check_only
class InvideoBranding(typing_extensions.TypedDict, total=False):
    imageBytes: str
    imageUrl: str
    position: InvideoPosition
    targetChannelId: str
    timing: InvideoTiming

@typing.type_check_only
class InvideoPosition(typing_extensions.TypedDict, total=False):
    cornerPosition: typing_extensions.Literal[
        "topLeft", "topRight", "bottomLeft", "bottomRight"
    ]
    type: typing_extensions.Literal["corner"]

@typing.type_check_only
class InvideoTiming(typing_extensions.TypedDict, total=False):
    durationMs: str
    offsetMs: str
    type: typing_extensions.Literal["offsetFromStart", "offsetFromEnd"]

@typing.type_check_only
class LanguageTag(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class LevelDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class LiveBroadcast(typing_extensions.TypedDict, total=False):
    contentDetails: LiveBroadcastContentDetails
    etag: str
    id: str
    kind: str
    snippet: LiveBroadcastSnippet
    statistics: LiveBroadcastStatistics
    status: LiveBroadcastStatus

@typing.type_check_only
class LiveBroadcastContentDetails(typing_extensions.TypedDict, total=False):
    boundStreamId: str
    boundStreamLastUpdateTimeMs: str
    closedCaptionsType: typing_extensions.Literal[
        "closedCaptionsTypeUnspecified",
        "closedCaptionsDisabled",
        "closedCaptionsHttpPost",
        "closedCaptionsEmbedded",
    ]
    enableAutoStart: bool
    enableAutoStop: bool
    enableClosedCaptions: bool
    enableContentEncryption: bool
    enableDvr: bool
    enableEmbed: bool
    enableLowLatency: bool
    latencyPreference: typing_extensions.Literal[
        "latencyPreferenceUnspecified", "normal", "low", "ultraLow"
    ]
    mesh: str
    monitorStream: MonitorStreamInfo
    projection: typing_extensions.Literal[
        "projectionUnspecified", "rectangular", "360", "mesh"
    ]
    recordFromStart: bool
    startWithSlate: bool
    stereoLayout: typing_extensions.Literal[
        "stereoLayoutUnspecified", "mono", "leftRight", "topBottom"
    ]

@typing.type_check_only
class LiveBroadcastListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[LiveBroadcast]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class LiveBroadcastSnippet(typing_extensions.TypedDict, total=False):
    actualEndTime: str
    actualStartTime: str
    channelId: str
    description: str
    isDefaultBroadcast: bool
    liveChatId: str
    publishedAt: str
    scheduledEndTime: str
    scheduledStartTime: str
    thumbnails: ThumbnailDetails
    title: str

@typing.type_check_only
class LiveBroadcastStatistics(typing_extensions.TypedDict, total=False):
    concurrentViewers: str
    totalChatCount: str

@typing.type_check_only
class LiveBroadcastStatus(typing_extensions.TypedDict, total=False):
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
    liveBroadcastPriority: typing_extensions.Literal[
        "liveBroadcastPriorityUnspecified", "low", "normal", "high"
    ]
    madeForKids: bool
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]
    recordingStatus: typing_extensions.Literal[
        "liveBroadcastRecordingStatusUnspecified",
        "notRecording",
        "recording",
        "recorded",
    ]
    selfDeclaredMadeForKids: bool

@typing.type_check_only
class LiveChatBan(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: LiveChatBanSnippet

@typing.type_check_only
class LiveChatBanSnippet(typing_extensions.TypedDict, total=False):
    banDurationSeconds: str
    bannedUserDetails: ChannelProfileDetails
    liveChatId: str
    type: typing_extensions.Literal[
        "liveChatBanTypeUnspecified", "permanent", "temporary"
    ]

@typing.type_check_only
class LiveChatFanFundingEventDetails(typing_extensions.TypedDict, total=False):
    amountDisplayString: str
    amountMicros: str
    currency: str
    userComment: str

@typing.type_check_only
class LiveChatGiftMembershipReceivedDetails(typing_extensions.TypedDict, total=False):
    associatedMembershipGiftingMessageId: str
    gifterChannelId: str
    memberLevelName: str

@typing.type_check_only
class LiveChatMemberMilestoneChatDetails(typing_extensions.TypedDict, total=False):
    memberLevelName: str
    memberMonth: int
    userComment: str

@typing.type_check_only
class LiveChatMembershipGiftingDetails(typing_extensions.TypedDict, total=False):
    giftMembershipsCount: int
    giftMembershipsLevelName: str

@typing.type_check_only
class LiveChatMessage(typing_extensions.TypedDict, total=False):
    authorDetails: LiveChatMessageAuthorDetails
    etag: str
    id: str
    kind: str
    snippet: LiveChatMessageSnippet

@typing.type_check_only
class LiveChatMessageAuthorDetails(typing_extensions.TypedDict, total=False):
    channelId: str
    channelUrl: str
    displayName: str
    isChatModerator: bool
    isChatOwner: bool
    isChatSponsor: bool
    isVerified: bool
    profileImageUrl: str

@typing.type_check_only
class LiveChatMessageDeletedDetails(typing_extensions.TypedDict, total=False):
    deletedMessageId: str

@typing.type_check_only
class LiveChatMessageListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[LiveChatMessage]
    kind: str
    nextPageToken: str
    offlineAt: str
    pageInfo: PageInfo
    pollingIntervalMillis: int
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class LiveChatMessageRetractedDetails(typing_extensions.TypedDict, total=False):
    retractedMessageId: str

@typing.type_check_only
class LiveChatMessageSnippet(typing_extensions.TypedDict, total=False):
    authorChannelId: str
    displayMessage: str
    fanFundingEventDetails: LiveChatFanFundingEventDetails
    giftMembershipReceivedDetails: LiveChatGiftMembershipReceivedDetails
    hasDisplayContent: bool
    liveChatId: str
    memberMilestoneChatDetails: LiveChatMemberMilestoneChatDetails
    membershipGiftingDetails: LiveChatMembershipGiftingDetails
    messageDeletedDetails: LiveChatMessageDeletedDetails
    messageRetractedDetails: LiveChatMessageRetractedDetails
    newSponsorDetails: LiveChatNewSponsorDetails
    publishedAt: str
    superChatDetails: LiveChatSuperChatDetails
    superStickerDetails: LiveChatSuperStickerDetails
    textMessageDetails: LiveChatTextMessageDetails
    type: typing_extensions.Literal[
        "invalidType",
        "textMessageEvent",
        "tombstone",
        "fanFundingEvent",
        "chatEndedEvent",
        "sponsorOnlyModeStartedEvent",
        "sponsorOnlyModeEndedEvent",
        "newSponsorEvent",
        "memberMilestoneChatEvent",
        "membershipGiftingEvent",
        "giftMembershipReceivedEvent",
        "messageDeletedEvent",
        "messageRetractedEvent",
        "userBannedEvent",
        "superChatEvent",
        "superStickerEvent",
    ]
    userBannedDetails: LiveChatUserBannedMessageDetails

@typing.type_check_only
class LiveChatModerator(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: LiveChatModeratorSnippet

@typing.type_check_only
class LiveChatModeratorListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[LiveChatModerator]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class LiveChatModeratorSnippet(typing_extensions.TypedDict, total=False):
    liveChatId: str
    moderatorDetails: ChannelProfileDetails

@typing.type_check_only
class LiveChatNewSponsorDetails(typing_extensions.TypedDict, total=False):
    isUpgrade: bool
    memberLevelName: str

@typing.type_check_only
class LiveChatSuperChatDetails(typing_extensions.TypedDict, total=False):
    amountDisplayString: str
    amountMicros: str
    currency: str
    tier: int
    userComment: str

@typing.type_check_only
class LiveChatSuperStickerDetails(typing_extensions.TypedDict, total=False):
    amountDisplayString: str
    amountMicros: str
    currency: str
    superStickerMetadata: SuperStickerMetadata
    tier: int

@typing.type_check_only
class LiveChatTextMessageDetails(typing_extensions.TypedDict, total=False):
    messageText: str

@typing.type_check_only
class LiveChatUserBannedMessageDetails(typing_extensions.TypedDict, total=False):
    banDurationSeconds: str
    banType: typing_extensions.Literal["permanent", "temporary"]
    bannedUserDetails: ChannelProfileDetails

@typing.type_check_only
class LiveStream(typing_extensions.TypedDict, total=False):
    cdn: CdnSettings
    contentDetails: LiveStreamContentDetails
    etag: str
    id: str
    kind: str
    snippet: LiveStreamSnippet
    status: LiveStreamStatus

@typing.type_check_only
class LiveStreamConfigurationIssue(typing_extensions.TypedDict, total=False):
    description: str
    reason: str
    severity: typing_extensions.Literal["info", "warning", "error"]
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

@typing.type_check_only
class LiveStreamContentDetails(typing_extensions.TypedDict, total=False):
    closedCaptionsIngestionUrl: str
    isReusable: bool

@typing.type_check_only
class LiveStreamHealthStatus(typing_extensions.TypedDict, total=False):
    configurationIssues: _list[LiveStreamConfigurationIssue]
    lastUpdateTimeSeconds: str
    status: typing_extensions.Literal["good", "ok", "bad", "noData", "revoked"]

@typing.type_check_only
class LiveStreamListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[LiveStream]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class LiveStreamSnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    description: str
    isDefaultStream: bool
    publishedAt: str
    title: str

@typing.type_check_only
class LiveStreamStatus(typing_extensions.TypedDict, total=False):
    healthStatus: LiveStreamHealthStatus
    streamStatus: typing_extensions.Literal[
        "created", "ready", "active", "inactive", "error"
    ]

@typing.type_check_only
class LocalizedProperty(typing_extensions.TypedDict, total=False):
    default: str
    defaultLanguage: LanguageTag
    localized: _list[LocalizedString]

@typing.type_check_only
class LocalizedString(typing_extensions.TypedDict, total=False):
    language: str
    value: str

@typing.type_check_only
class Member(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    snippet: MemberSnippet

@typing.type_check_only
class MemberListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Member]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class MemberSnippet(typing_extensions.TypedDict, total=False):
    creatorChannelId: str
    memberDetails: ChannelProfileDetails
    membershipsDetails: MembershipsDetails

@typing.type_check_only
class MembershipsDetails(typing_extensions.TypedDict, total=False):
    accessibleLevels: _list[str]
    highestAccessibleLevel: str
    highestAccessibleLevelDisplayName: str
    membershipsDuration: MembershipsDuration
    membershipsDurationAtLevels: _list[MembershipsDurationAtLevel]

@typing.type_check_only
class MembershipsDuration(typing_extensions.TypedDict, total=False):
    memberSince: str
    memberTotalDurationMonths: int

@typing.type_check_only
class MembershipsDurationAtLevel(typing_extensions.TypedDict, total=False):
    level: str
    memberSince: str
    memberTotalDurationMonths: int

@typing.type_check_only
class MembershipsLevel(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: MembershipsLevelSnippet

@typing.type_check_only
class MembershipsLevelListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[MembershipsLevel]
    kind: str
    visitorId: str

@typing.type_check_only
class MembershipsLevelSnippet(typing_extensions.TypedDict, total=False):
    creatorChannelId: str
    levelDetails: LevelDetails

@typing.type_check_only
class MonitorStreamInfo(typing_extensions.TypedDict, total=False):
    broadcastStreamDelayMs: int
    embedHtml: str
    enableMonitorStream: bool

@typing.type_check_only
class PageInfo(typing_extensions.TypedDict, total=False):
    resultsPerPage: int
    totalResults: int

@typing.type_check_only
class Playlist(typing_extensions.TypedDict, total=False):
    contentDetails: PlaylistContentDetails
    etag: str
    id: str
    kind: str
    localizations: dict[str, typing.Any]
    player: PlaylistPlayer
    snippet: PlaylistSnippet
    status: PlaylistStatus

@typing.type_check_only
class PlaylistContentDetails(typing_extensions.TypedDict, total=False):
    itemCount: int

@typing.type_check_only
class PlaylistItem(typing_extensions.TypedDict, total=False):
    contentDetails: PlaylistItemContentDetails
    etag: str
    id: str
    kind: str
    snippet: PlaylistItemSnippet
    status: PlaylistItemStatus

@typing.type_check_only
class PlaylistItemContentDetails(typing_extensions.TypedDict, total=False):
    endAt: str
    note: str
    startAt: str
    videoId: str
    videoPublishedAt: str

@typing.type_check_only
class PlaylistItemListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[PlaylistItem]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class PlaylistItemSnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    channelTitle: str
    description: str
    playlistId: str
    position: int
    publishedAt: str
    resourceId: ResourceId
    thumbnails: ThumbnailDetails
    title: str
    videoOwnerChannelId: str
    videoOwnerChannelTitle: str

@typing.type_check_only
class PlaylistItemStatus(typing_extensions.TypedDict, total=False):
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]

@typing.type_check_only
class PlaylistListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Playlist]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class PlaylistLocalization(typing_extensions.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class PlaylistPlayer(typing_extensions.TypedDict, total=False):
    embedHtml: str

@typing.type_check_only
class PlaylistSnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    channelTitle: str
    defaultLanguage: str
    description: str
    localized: PlaylistLocalization
    publishedAt: str
    tags: _list[str]
    thumbnailVideoId: str
    thumbnails: ThumbnailDetails
    title: str

@typing.type_check_only
class PlaylistStatus(typing_extensions.TypedDict, total=False):
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]

@typing.type_check_only
class PropertyValue(typing_extensions.TypedDict, total=False):
    property: str
    value: str

@typing.type_check_only
class RelatedEntity(typing_extensions.TypedDict, total=False):
    entity: Entity

@typing.type_check_only
class ResourceId(typing_extensions.TypedDict, total=False):
    channelId: str
    kind: str
    playlistId: str
    videoId: str

@typing.type_check_only
class SearchListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[SearchResult]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    regionCode: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class SearchResult(typing_extensions.TypedDict, total=False):
    etag: str
    id: ResourceId
    kind: str
    snippet: SearchResultSnippet

@typing.type_check_only
class SearchResultSnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    channelTitle: str
    description: str
    liveBroadcastContent: typing_extensions.Literal[
        "none", "upcoming", "live", "completed"
    ]
    publishedAt: str
    thumbnails: ThumbnailDetails
    title: str

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    contentDetails: SubscriptionContentDetails
    etag: str
    id: str
    kind: str
    snippet: SubscriptionSnippet
    subscriberSnippet: SubscriptionSubscriberSnippet

@typing.type_check_only
class SubscriptionContentDetails(typing_extensions.TypedDict, total=False):
    activityType: typing_extensions.Literal[
        "subscriptionActivityTypeUnspecified", "all", "uploads"
    ]
    newItemCount: int
    totalItemCount: int

@typing.type_check_only
class SubscriptionListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Subscription]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class SubscriptionSnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    channelTitle: str
    description: str
    publishedAt: str
    resourceId: ResourceId
    thumbnails: ThumbnailDetails
    title: str

@typing.type_check_only
class SubscriptionSubscriberSnippet(typing_extensions.TypedDict, total=False):
    channelId: str
    description: str
    thumbnails: ThumbnailDetails
    title: str

@typing.type_check_only
class SuperChatEvent(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: SuperChatEventSnippet

@typing.type_check_only
class SuperChatEventListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[SuperChatEvent]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class SuperChatEventSnippet(typing_extensions.TypedDict, total=False):
    amountMicros: str
    channelId: str
    commentText: str
    createdAt: str
    currency: str
    displayString: str
    isSuperStickerEvent: bool
    messageType: int
    superStickerMetadata: SuperStickerMetadata
    supporterDetails: ChannelProfileDetails

@typing.type_check_only
class SuperStickerMetadata(typing_extensions.TypedDict, total=False):
    altText: str
    altTextLanguage: str
    stickerId: str

@typing.type_check_only
class TestItem(typing_extensions.TypedDict, total=False):
    featuredPart: bool
    gaia: str
    id: str
    snippet: TestItemTestItemSnippet

@typing.type_check_only
class TestItemTestItemSnippet(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ThirdPartyLink(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    linkingToken: str
    snippet: ThirdPartyLinkSnippet
    status: ThirdPartyLinkStatus

@typing.type_check_only
class ThirdPartyLinkListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[ThirdPartyLink]
    kind: str

@typing.type_check_only
class ThirdPartyLinkSnippet(typing_extensions.TypedDict, total=False):
    channelToStoreLink: ChannelToStoreLinkDetails
    type: typing_extensions.Literal["linkUnspecified", "channelToStoreLink"]

@typing.type_check_only
class ThirdPartyLinkStatus(typing_extensions.TypedDict, total=False):
    linkStatus: typing_extensions.Literal["unknown", "failed", "pending", "linked"]

@typing.type_check_only
class Thumbnail(typing_extensions.TypedDict, total=False):
    height: int
    url: str
    width: int

@typing.type_check_only
class ThumbnailDetails(typing_extensions.TypedDict, total=False):
    default: Thumbnail
    high: Thumbnail
    maxres: Thumbnail
    medium: Thumbnail
    standard: Thumbnail

@typing.type_check_only
class ThumbnailSetResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[ThumbnailDetails]
    kind: str
    visitorId: str

@typing.type_check_only
class TokenPagination(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Video(typing_extensions.TypedDict, total=False):
    ageGating: VideoAgeGating
    contentDetails: VideoContentDetails
    etag: str
    fileDetails: VideoFileDetails
    id: str
    kind: str
    liveStreamingDetails: VideoLiveStreamingDetails
    localizations: dict[str, typing.Any]
    monetizationDetails: VideoMonetizationDetails
    player: VideoPlayer
    processingDetails: VideoProcessingDetails
    projectDetails: VideoProjectDetails
    recordingDetails: VideoRecordingDetails
    snippet: VideoSnippet
    statistics: VideoStatistics
    status: VideoStatus
    suggestions: VideoSuggestions
    topicDetails: VideoTopicDetails

@typing.type_check_only
class VideoAbuseReport(typing_extensions.TypedDict, total=False):
    comments: str
    language: str
    reasonId: str
    secondaryReasonId: str
    videoId: str

@typing.type_check_only
class VideoAbuseReportReason(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: VideoAbuseReportReasonSnippet

@typing.type_check_only
class VideoAbuseReportReasonListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[VideoAbuseReportReason]
    kind: str
    visitorId: str

@typing.type_check_only
class VideoAbuseReportReasonSnippet(typing_extensions.TypedDict, total=False):
    label: str
    secondaryReasons: _list[VideoAbuseReportSecondaryReason]

@typing.type_check_only
class VideoAbuseReportSecondaryReason(typing_extensions.TypedDict, total=False):
    id: str
    label: str

@typing.type_check_only
class VideoAgeGating(typing_extensions.TypedDict, total=False):
    alcoholContent: bool
    restricted: bool
    videoGameRating: typing_extensions.Literal[
        "anyone", "m15Plus", "m16Plus", "m17Plus"
    ]

@typing.type_check_only
class VideoCategory(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    snippet: VideoCategorySnippet

@typing.type_check_only
class VideoCategoryListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[VideoCategory]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class VideoCategorySnippet(typing_extensions.TypedDict, total=False):
    assignable: bool
    channelId: str
    title: str

@typing.type_check_only
class VideoContentDetails(typing_extensions.TypedDict, total=False):
    caption: typing_extensions.Literal["true", "false"]
    contentRating: ContentRating
    countryRestriction: AccessPolicy
    definition: typing_extensions.Literal["sd", "hd"]
    dimension: str
    duration: str
    hasCustomThumbnail: bool
    licensedContent: bool
    projection: typing_extensions.Literal["rectangular", "360"]
    regionRestriction: VideoContentDetailsRegionRestriction

@typing.type_check_only
class VideoContentDetailsRegionRestriction(typing_extensions.TypedDict, total=False):
    allowed: _list[str]
    blocked: _list[str]

@typing.type_check_only
class VideoFileDetails(typing_extensions.TypedDict, total=False):
    audioStreams: _list[VideoFileDetailsAudioStream]
    bitrateBps: str
    container: str
    creationTime: str
    durationMs: str
    fileName: str
    fileSize: str
    fileType: typing_extensions.Literal[
        "video", "audio", "image", "archive", "document", "project", "other"
    ]
    videoStreams: _list[VideoFileDetailsVideoStream]

@typing.type_check_only
class VideoFileDetailsAudioStream(typing_extensions.TypedDict, total=False):
    bitrateBps: str
    channelCount: int
    codec: str
    vendor: str

@typing.type_check_only
class VideoFileDetailsVideoStream(typing_extensions.TypedDict, total=False):
    aspectRatio: float
    bitrateBps: str
    codec: str
    frameRateFps: float
    heightPixels: int
    rotation: typing_extensions.Literal[
        "none", "clockwise", "upsideDown", "counterClockwise", "other"
    ]
    vendor: str
    widthPixels: int

@typing.type_check_only
class VideoGetRatingResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[VideoRating]
    kind: str
    visitorId: str

@typing.type_check_only
class VideoListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    eventId: str
    items: _list[Video]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    prevPageToken: str
    tokenPagination: TokenPagination
    visitorId: str

@typing.type_check_only
class VideoLiveStreamingDetails(typing_extensions.TypedDict, total=False):
    activeLiveChatId: str
    actualEndTime: str
    actualStartTime: str
    concurrentViewers: str
    scheduledEndTime: str
    scheduledStartTime: str

@typing.type_check_only
class VideoLocalization(typing_extensions.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class VideoMonetizationDetails(typing_extensions.TypedDict, total=False):
    access: AccessPolicy

@typing.type_check_only
class VideoPlayer(typing_extensions.TypedDict, total=False):
    embedHeight: str
    embedHtml: str
    embedWidth: str

@typing.type_check_only
class VideoProcessingDetails(typing_extensions.TypedDict, total=False):
    editorSuggestionsAvailability: str
    fileDetailsAvailability: str
    processingFailureReason: typing_extensions.Literal[
        "uploadFailed", "transcodeFailed", "streamingFailed", "other"
    ]
    processingIssuesAvailability: str
    processingProgress: VideoProcessingDetailsProcessingProgress
    processingStatus: typing_extensions.Literal[
        "processing", "succeeded", "failed", "terminated"
    ]
    tagSuggestionsAvailability: str
    thumbnailsAvailability: str

@typing.type_check_only
class VideoProcessingDetailsProcessingProgress(
    typing_extensions.TypedDict, total=False
):
    partsProcessed: str
    partsTotal: str
    timeLeftMs: str

@typing.type_check_only
class VideoProjectDetails(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VideoRating(typing_extensions.TypedDict, total=False):
    rating: typing_extensions.Literal["none", "like", "dislike"]
    videoId: str

@typing.type_check_only
class VideoRecordingDetails(typing_extensions.TypedDict, total=False):
    location: GeoPoint
    locationDescription: str
    recordingDate: str

@typing.type_check_only
class VideoSnippet(typing_extensions.TypedDict, total=False):
    categoryId: str
    channelId: str
    channelTitle: str
    defaultAudioLanguage: str
    defaultLanguage: str
    description: str
    liveBroadcastContent: typing_extensions.Literal[
        "none", "upcoming", "live", "completed"
    ]
    localized: VideoLocalization
    publishedAt: str
    tags: _list[str]
    thumbnails: ThumbnailDetails
    title: str

@typing.type_check_only
class VideoStatistics(typing_extensions.TypedDict, total=False):
    commentCount: str
    dislikeCount: str
    favoriteCount: str
    likeCount: str
    viewCount: str

@typing.type_check_only
class VideoStatus(typing_extensions.TypedDict, total=False):
    embeddable: bool
    failureReason: typing_extensions.Literal[
        "conversion", "invalidFile", "emptyFile", "tooSmall", "codec", "uploadAborted"
    ]
    license: typing_extensions.Literal["youtube", "creativeCommon"]
    madeForKids: bool
    privacyStatus: typing_extensions.Literal["public", "unlisted", "private"]
    publicStatsViewable: bool
    publishAt: str
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
    selfDeclaredMadeForKids: bool
    uploadStatus: typing_extensions.Literal[
        "uploaded", "processed", "failed", "rejected", "deleted"
    ]

@typing.type_check_only
class VideoSuggestions(typing_extensions.TypedDict, total=False):
    editorSuggestions: _list[str]
    processingErrors: _list[str]
    processingHints: _list[str]
    processingWarnings: _list[str]
    tagSuggestions: _list[VideoSuggestionsTagSuggestion]

@typing.type_check_only
class VideoSuggestionsTagSuggestion(typing_extensions.TypedDict, total=False):
    categoryRestricts: _list[str]
    tag: str

@typing.type_check_only
class VideoTopicDetails(typing_extensions.TypedDict, total=False):
    relevantTopicIds: _list[str]
    topicCategories: _list[str]
    topicIds: _list[str]

@typing.type_check_only
class WatchSettings(typing_extensions.TypedDict, total=False):
    backgroundColor: str
    featuredPlaylistId: str
    textColor: str
