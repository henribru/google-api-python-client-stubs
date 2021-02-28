import typing

import typing_extensions
@typing.type_check_only
class AchievementDefinition(typing_extensions.TypedDict, total=False):
    achievementType: typing_extensions.Literal[
        "ACHIEVEMENT_TYPE_UNSPECIFIED", "STANDARD", "INCREMENTAL"
    ]
    description: str
    experiencePoints: str
    formattedTotalSteps: str
    id: str
    initialState: typing_extensions.Literal[
        "INITIAL_ACHIEVEMENT_STATE_UNSPECIFIED", "HIDDEN", "REVEALED", "UNLOCKED"
    ]
    isRevealedIconUrlDefault: bool
    isUnlockedIconUrlDefault: bool
    kind: str
    name: str
    revealedIconUrl: str
    totalSteps: int
    unlockedIconUrl: str

@typing.type_check_only
class AchievementDefinitionsListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[AchievementDefinition]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AchievementIncrementResponse(typing_extensions.TypedDict, total=False):
    currentSteps: int
    kind: str
    newlyUnlocked: bool

@typing.type_check_only
class AchievementRevealResponse(typing_extensions.TypedDict, total=False):
    currentState: typing_extensions.Literal[
        "REVEAL_ACHIEVEMENT_STATE_UNSPECIFIED", "REVEALED", "UNLOCKED"
    ]
    kind: str

@typing.type_check_only
class AchievementSetStepsAtLeastResponse(typing_extensions.TypedDict, total=False):
    currentSteps: int
    kind: str
    newlyUnlocked: bool

@typing.type_check_only
class AchievementUnlockResponse(typing_extensions.TypedDict, total=False):
    kind: str
    newlyUnlocked: bool

@typing.type_check_only
class AchievementUpdateMultipleRequest(typing_extensions.TypedDict, total=False):
    kind: str
    updates: typing.List[AchievementUpdateRequest]

@typing.type_check_only
class AchievementUpdateMultipleResponse(typing_extensions.TypedDict, total=False):
    kind: str
    updatedAchievements: typing.List[AchievementUpdateResponse]

@typing.type_check_only
class AchievementUpdateRequest(typing_extensions.TypedDict, total=False):
    achievementId: str
    incrementPayload: GamesAchievementIncrement
    kind: str
    setStepsAtLeastPayload: GamesAchievementSetStepsAtLeast
    updateType: typing_extensions.Literal[
        "ACHIEVEMENT_UPDATE_TYPE_UNSPECIFIED",
        "REVEAL",
        "UNLOCK",
        "INCREMENT",
        "SET_STEPS_AT_LEAST",
    ]

@typing.type_check_only
class AchievementUpdateResponse(typing_extensions.TypedDict, total=False):
    achievementId: str
    currentState: typing_extensions.Literal[
        "UPDATED_ACHIEVEMENT_STATE_UNSPECIFIED", "HIDDEN", "REVEALED", "UNLOCKED"
    ]
    currentSteps: int
    kind: str
    newlyUnlocked: bool
    updateOccurred: bool

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    achievement_count: int
    assets: typing.List[ImageAsset]
    author: str
    category: ApplicationCategory
    description: str
    enabledFeatures: typing.List[str]
    id: str
    instances: typing.List[Instance]
    kind: str
    lastUpdatedTimestamp: str
    leaderboard_count: int
    name: str
    themeColor: str

@typing.type_check_only
class ApplicationCategory(typing_extensions.TypedDict, total=False):
    kind: str
    primary: str
    secondary: str

@typing.type_check_only
class ApplicationVerifyResponse(typing_extensions.TypedDict, total=False):
    alternate_player_id: str
    kind: str
    player_id: str

@typing.type_check_only
class Category(typing_extensions.TypedDict, total=False):
    category: str
    experiencePoints: str
    kind: str

@typing.type_check_only
class CategoryListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Category]
    kind: str
    nextPageToken: str

@typing.type_check_only
class EndPoint(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class EventBatchRecordFailure(typing_extensions.TypedDict, total=False):
    failureCause: typing_extensions.Literal[
        "EVENT_FAILURE_CAUSE_UNSPECIFIED",
        "TOO_LARGE",
        "TIME_PERIOD_EXPIRED",
        "TIME_PERIOD_SHORT",
        "TIME_PERIOD_LONG",
        "ALREADY_UPDATED",
        "RECORD_RATE_HIGH",
    ]
    kind: str
    range: EventPeriodRange

@typing.type_check_only
class EventChild(typing_extensions.TypedDict, total=False):
    childId: str
    kind: str

@typing.type_check_only
class EventDefinition(typing_extensions.TypedDict, total=False):
    childEvents: typing.List[EventChild]
    description: str
    displayName: str
    id: str
    imageUrl: str
    isDefaultImageUrl: bool
    kind: str
    visibility: typing_extensions.Literal[
        "EVENT_VISIBILITY_UNSPECIFIED", "REVEALED", "HIDDEN"
    ]

@typing.type_check_only
class EventDefinitionListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[EventDefinition]
    kind: str
    nextPageToken: str

@typing.type_check_only
class EventPeriodRange(typing_extensions.TypedDict, total=False):
    kind: str
    periodEndMillis: str
    periodStartMillis: str

@typing.type_check_only
class EventPeriodUpdate(typing_extensions.TypedDict, total=False):
    kind: str
    timePeriod: EventPeriodRange
    updates: typing.List[EventUpdateRequest]

@typing.type_check_only
class EventRecordFailure(typing_extensions.TypedDict, total=False):
    eventId: str
    failureCause: typing_extensions.Literal[
        "EVENT_UPDATE_FAILURE_CAUSE_UNSPECIFIED", "NOT_FOUND", "INVALID_UPDATE_VALUE"
    ]
    kind: str

@typing.type_check_only
class EventRecordRequest(typing_extensions.TypedDict, total=False):
    currentTimeMillis: str
    kind: str
    requestId: str
    timePeriods: typing.List[EventPeriodUpdate]

@typing.type_check_only
class EventUpdateRequest(typing_extensions.TypedDict, total=False):
    definitionId: str
    kind: str
    updateCount: str

@typing.type_check_only
class EventUpdateResponse(typing_extensions.TypedDict, total=False):
    batchFailures: typing.List[EventBatchRecordFailure]
    eventFailures: typing.List[EventRecordFailure]
    kind: str
    playerEvents: typing.List[PlayerEvent]

@typing.type_check_only
class GamesAchievementIncrement(typing_extensions.TypedDict, total=False):
    kind: str
    requestId: str
    steps: int

@typing.type_check_only
class GamesAchievementSetStepsAtLeast(typing_extensions.TypedDict, total=False):
    kind: str
    steps: int

@typing.type_check_only
class ImageAsset(typing_extensions.TypedDict, total=False):
    height: int
    kind: str
    name: str
    url: str
    width: int

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    acquisitionUri: str
    androidInstance: InstanceAndroidDetails
    iosInstance: InstanceIosDetails
    kind: str
    name: str
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED", "ANDROID", "IOS", "WEB_APP"
    ]
    realtimePlay: bool
    turnBasedPlay: bool
    webInstance: InstanceWebDetails

@typing.type_check_only
class InstanceAndroidDetails(typing_extensions.TypedDict, total=False):
    enablePiracyCheck: bool
    kind: str
    packageName: str
    preferred: bool

@typing.type_check_only
class InstanceIosDetails(typing_extensions.TypedDict, total=False):
    bundleIdentifier: str
    itunesAppId: str
    kind: str
    preferredForIpad: bool
    preferredForIphone: bool
    supportIpad: bool
    supportIphone: bool

@typing.type_check_only
class InstanceWebDetails(typing_extensions.TypedDict, total=False):
    kind: str
    launchUrl: str
    preferred: bool

@typing.type_check_only
class Leaderboard(typing_extensions.TypedDict, total=False):
    iconUrl: str
    id: str
    isIconUrlDefault: bool
    kind: str
    name: str
    order: typing_extensions.Literal[
        "SCORE_ORDER_UNSPECIFIED", "LARGER_IS_BETTER", "SMALLER_IS_BETTER"
    ]

@typing.type_check_only
class LeaderboardEntry(typing_extensions.TypedDict, total=False):
    formattedScore: str
    formattedScoreRank: str
    kind: str
    player: Player
    scoreRank: str
    scoreTag: str
    scoreValue: str
    timeSpan: typing_extensions.Literal[
        "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
    ]
    writeTimestampMillis: str

@typing.type_check_only
class LeaderboardListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Leaderboard]
    kind: str
    nextPageToken: str

@typing.type_check_only
class LeaderboardScoreRank(typing_extensions.TypedDict, total=False):
    formattedNumScores: str
    formattedRank: str
    kind: str
    numScores: str
    rank: str

@typing.type_check_only
class LeaderboardScores(typing_extensions.TypedDict, total=False):
    items: typing.List[LeaderboardEntry]
    kind: str
    nextPageToken: str
    numScores: str
    playerScore: LeaderboardEntry
    prevPageToken: str

@typing.type_check_only
class MetagameConfig(typing_extensions.TypedDict, total=False):
    currentVersion: int
    kind: str
    playerLevels: typing.List[PlayerLevel]

@typing.type_check_only
class Player(typing_extensions.TypedDict, total=False):
    avatarImageUrl: str
    bannerUrlLandscape: str
    bannerUrlPortrait: str
    displayName: str
    experienceInfo: PlayerExperienceInfo
    friendStatus: typing_extensions.Literal[
        "FRIEND_STATUS_UNSPECIFIED", "NO_RELATIONSHIP", "FRIEND"
    ]
    kind: str
    name: typing.Dict[str, typing.Any]
    originalPlayerId: str
    playerId: str
    profileSettings: ProfileSettings
    title: str

@typing.type_check_only
class PlayerAchievement(typing_extensions.TypedDict, total=False):
    achievementState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "HIDDEN", "REVEALED", "UNLOCKED"
    ]
    currentSteps: int
    experiencePoints: str
    formattedCurrentStepsString: str
    id: str
    kind: str
    lastUpdatedTimestamp: str

@typing.type_check_only
class PlayerAchievementListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[PlayerAchievement]
    kind: str
    nextPageToken: str

@typing.type_check_only
class PlayerEvent(typing_extensions.TypedDict, total=False):
    definitionId: str
    formattedNumEvents: str
    kind: str
    numEvents: str
    playerId: str

@typing.type_check_only
class PlayerEventListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[PlayerEvent]
    kind: str
    nextPageToken: str

@typing.type_check_only
class PlayerExperienceInfo(typing_extensions.TypedDict, total=False):
    currentExperiencePoints: str
    currentLevel: PlayerLevel
    kind: str
    lastLevelUpTimestampMillis: str
    nextLevel: PlayerLevel

@typing.type_check_only
class PlayerLeaderboardScore(typing_extensions.TypedDict, total=False):
    friendsRank: LeaderboardScoreRank
    kind: str
    leaderboard_id: str
    publicRank: LeaderboardScoreRank
    scoreString: str
    scoreTag: str
    scoreValue: str
    socialRank: LeaderboardScoreRank
    timeSpan: typing_extensions.Literal[
        "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
    ]
    writeTimestamp: str

@typing.type_check_only
class PlayerLeaderboardScoreListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[PlayerLeaderboardScore]
    kind: str
    nextPageToken: str
    player: Player

@typing.type_check_only
class PlayerLevel(typing_extensions.TypedDict, total=False):
    kind: str
    level: int
    maxExperiencePoints: str
    minExperiencePoints: str

@typing.type_check_only
class PlayerListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Player]
    kind: str
    nextPageToken: str

@typing.type_check_only
class PlayerScore(typing_extensions.TypedDict, total=False):
    formattedScore: str
    kind: str
    score: str
    scoreTag: str
    timeSpan: typing_extensions.Literal[
        "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
    ]

@typing.type_check_only
class PlayerScoreListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    submittedScores: typing.List[PlayerScoreResponse]

@typing.type_check_only
class PlayerScoreResponse(typing_extensions.TypedDict, total=False):
    beatenScoreTimeSpans: typing.List[str]
    formattedScore: str
    kind: str
    leaderboardId: str
    scoreTag: str
    unbeatenScores: typing.List[PlayerScore]

@typing.type_check_only
class PlayerScoreSubmissionList(typing_extensions.TypedDict, total=False):
    kind: str
    scores: typing.List[ScoreSubmission]

@typing.type_check_only
class ProfileSettings(typing_extensions.TypedDict, total=False):
    friendsListVisibility: typing_extensions.Literal[
        "FRIENDS_LIST_VISIBILITY_UNSPECIFIED",
        "VISIBLE",
        "REQUEST_REQUIRED",
        "UNAVAILABLE",
    ]
    kind: str
    profileVisible: bool

@typing.type_check_only
class ResolveSnapshotHeadRequest(typing_extensions.TypedDict, total=False):
    maxConflictsPerSnapshot: int
    resolutionPolicy: typing_extensions.Literal[
        "RESOLUTION_POLICY_UNSPECIFIED",
        "USE_HEAD",
        "LONGEST_PLAYTIME",
        "MOST_RECENTLY_MODIFIED",
        "HIGHEST_PROGRESS",
        "NO_AUTOMATIC_RESOLUTION",
    ]

@typing.type_check_only
class ResolveSnapshotHeadResponse(typing_extensions.TypedDict, total=False):
    snapshot: SnapshotExtended

@typing.type_check_only
class RevisionCheckResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    revisionStatus: typing_extensions.Literal[
        "REVISION_STATUS_UNSPECIFIED", "OK", "DEPRECATED", "INVALID"
    ]

@typing.type_check_only
class ScoreSubmission(typing_extensions.TypedDict, total=False):
    kind: str
    leaderboardId: str
    score: str
    scoreTag: str
    signature: str

@typing.type_check_only
class Snapshot(typing_extensions.TypedDict, total=False):
    coverImage: SnapshotImage
    description: str
    driveId: str
    durationMillis: str
    id: str
    kind: str
    lastModifiedMillis: str
    progressValue: str
    title: str
    type: typing_extensions.Literal["SNAPSHOT_TYPE_UNSPECIFIED", "SAVE_GAME"]
    uniqueName: str

@typing.type_check_only
class SnapshotCoverImageResource(typing_extensions.TypedDict, total=False):
    contentHash: str
    downloadUrl: str
    height: int
    mimeType: str
    resourceId: str
    width: int

@typing.type_check_only
class SnapshotDataResource(typing_extensions.TypedDict, total=False):
    contentHash: str
    downloadUrl: str
    resourceId: str
    size: str

@typing.type_check_only
class SnapshotExtended(typing_extensions.TypedDict, total=False):
    conflictingRevisions: typing.List[SnapshotRevision]
    hasConflictingRevisions: bool
    headRevision: SnapshotRevision
    snapshotName: str

@typing.type_check_only
class SnapshotImage(typing_extensions.TypedDict, total=False):
    height: int
    kind: str
    mime_type: str
    url: str
    width: int

@typing.type_check_only
class SnapshotListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Snapshot]
    kind: str
    nextPageToken: str

@typing.type_check_only
class SnapshotMetadata(typing_extensions.TypedDict, total=False):
    description: str
    deviceName: str
    gameplayDuration: str
    lastModifyTime: str
    progressValue: str

@typing.type_check_only
class SnapshotRevision(typing_extensions.TypedDict, total=False):
    blob: SnapshotDataResource
    coverImage: SnapshotCoverImageResource
    id: str
    metadata: SnapshotMetadata

@typing.type_check_only
class StatsResponse(typing_extensions.TypedDict, total=False):
    avg_session_length_minutes: float
    churn_probability: float
    days_since_last_played: int
    high_spender_probability: float
    kind: str
    num_purchases: int
    num_sessions: int
    num_sessions_percentile: float
    spend_percentile: float
    spend_probability: float
    total_spend_next_28_days: float
