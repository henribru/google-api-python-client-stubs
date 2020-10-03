import typing

import typing_extensions

class EventUpdateRequest(typing_extensions.TypedDict, total=False):
    updateCount: str
    kind: str
    definitionId: str

class LeaderboardScores(typing_extensions.TypedDict, total=False):
    items: typing.List[LeaderboardEntry]
    numScores: str
    kind: str
    playerScore: LeaderboardEntry
    nextPageToken: str
    prevPageToken: str

class EventChild(typing_extensions.TypedDict, total=False):
    childId: str
    kind: str

class PlayerLeaderboardScoreListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[PlayerLeaderboardScore]
    player: Player
    nextPageToken: str
    kind: str

class RevisionCheckResponse(typing_extensions.TypedDict, total=False):
    kind: str
    apiVersion: str
    revisionStatus: typing_extensions.Literal[
        "REVISION_STATUS_UNSPECIFIED", "OK", "DEPRECATED", "INVALID"
    ]

class Instance(typing_extensions.TypedDict, total=False):
    acquisitionUri: str
    kind: str
    realtimePlay: bool
    webInstance: InstanceWebDetails
    turnBasedPlay: bool
    androidInstance: InstanceAndroidDetails
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED", "ANDROID", "IOS", "WEB_APP"
    ]
    name: str
    iosInstance: InstanceIosDetails

class PlayerEventListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[PlayerEvent]
    nextPageToken: str
    kind: str

class LeaderboardEntry(typing_extensions.TypedDict, total=False):
    scoreValue: str
    timeSpan: typing_extensions.Literal[
        "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
    ]
    kind: str
    formattedScoreRank: str
    formattedScore: str
    player: Player
    scoreTag: str
    scoreRank: str
    writeTimestampMillis: str

class Category(typing_extensions.TypedDict, total=False):
    category: str
    experiencePoints: str
    kind: str

class EventDefinition(typing_extensions.TypedDict, total=False):
    description: str
    id: str
    childEvents: typing.List[EventChild]
    kind: str
    visibility: typing_extensions.Literal[
        "EVENT_VISIBILITY_UNSPECIFIED", "REVEALED", "HIDDEN"
    ]
    displayName: str
    imageUrl: str
    isDefaultImageUrl: bool

class PlayerEvent(typing_extensions.TypedDict, total=False):
    playerId: str
    numEvents: str
    definitionId: str
    formattedNumEvents: str
    kind: str

class SnapshotListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Snapshot]
    kind: str
    nextPageToken: str

class AchievementDefinition(typing_extensions.TypedDict, total=False):
    totalSteps: int
    isRevealedIconUrlDefault: bool
    formattedTotalSteps: str
    revealedIconUrl: str
    isUnlockedIconUrlDefault: bool
    kind: str
    unlockedIconUrl: str
    name: str
    id: str
    initialState: typing_extensions.Literal[
        "INITIAL_ACHIEVEMENT_STATE_UNSPECIFIED", "HIDDEN", "REVEALED", "UNLOCKED"
    ]
    experiencePoints: str
    description: str
    achievementType: typing_extensions.Literal[
        "ACHIEVEMENT_TYPE_UNSPECIFIED", "STANDARD", "INCREMENTAL"
    ]

class LeaderboardScoreRank(typing_extensions.TypedDict, total=False):
    formattedNumScores: str
    rank: str
    numScores: str
    kind: str
    formattedRank: str

class LeaderboardListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Leaderboard]
    kind: str
    nextPageToken: str

class PlayerAchievement(typing_extensions.TypedDict, total=False):
    achievementState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "HIDDEN", "REVEALED", "UNLOCKED"
    ]
    kind: str
    experiencePoints: str
    formattedCurrentStepsString: str
    id: str
    lastUpdatedTimestamp: str
    currentSteps: int

class EventRecordRequest(typing_extensions.TypedDict, total=False):
    currentTimeMillis: str
    timePeriods: typing.List[EventPeriodUpdate]
    kind: str
    requestId: str

class InstanceWebDetails(typing_extensions.TypedDict, total=False):
    preferred: bool
    kind: str
    launchUrl: str

class ProfileSettings(typing_extensions.TypedDict, total=False):
    kind: str
    friendsListVisibility: typing_extensions.Literal[
        "FRIENDS_LIST_VISIBILITY_UNSPECIFIED",
        "VISIBLE",
        "REQUEST_REQUIRED",
        "UNAVAILABLE",
    ]
    profileVisible: bool

class GamesAchievementSetStepsAtLeast(typing_extensions.TypedDict, total=False):
    steps: int
    kind: str

class InstanceIosDetails(typing_extensions.TypedDict, total=False):
    itunesAppId: str
    kind: str
    bundleIdentifier: str
    supportIphone: bool
    preferredForIpad: bool
    supportIpad: bool
    preferredForIphone: bool

class InstanceAndroidDetails(typing_extensions.TypedDict, total=False):
    packageName: str
    preferred: bool
    enablePiracyCheck: bool
    kind: str

class GamesAchievementIncrement(typing_extensions.TypedDict, total=False):
    kind: str
    steps: int
    requestId: str

class EventPeriodRange(typing_extensions.TypedDict, total=False):
    periodStartMillis: str
    kind: str
    periodEndMillis: str

class AchievementRevealResponse(typing_extensions.TypedDict, total=False):
    currentState: typing_extensions.Literal[
        "REVEAL_ACHIEVEMENT_STATE_UNSPECIFIED", "REVEALED", "UNLOCKED"
    ]
    kind: str

class AchievementUpdateMultipleResponse(typing_extensions.TypedDict, total=False):
    updatedAchievements: typing.List[AchievementUpdateResponse]
    kind: str

class ScoreSubmission(typing_extensions.TypedDict, total=False):
    signature: str
    scoreTag: str
    kind: str
    leaderboardId: str
    score: str

class PlayerScoreResponse(typing_extensions.TypedDict, total=False):
    scoreTag: str
    formattedScore: str
    kind: str
    beatenScoreTimeSpans: typing.List[str]
    unbeatenScores: typing.List[PlayerScore]
    leaderboardId: str

class AchievementUnlockResponse(typing_extensions.TypedDict, total=False):
    kind: str
    newlyUnlocked: bool

class AchievementDefinitionsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[AchievementDefinition]
    kind: str

class ApplicationCategory(typing_extensions.TypedDict, total=False):
    secondary: str
    kind: str
    primary: str

class PlayerListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[Player]
    kind: str

class EventRecordFailure(typing_extensions.TypedDict, total=False):
    failureCause: typing_extensions.Literal[
        "EVENT_UPDATE_FAILURE_CAUSE_UNSPECIFIED", "NOT_FOUND", "INVALID_UPDATE_VALUE"
    ]
    kind: str
    eventId: str

class MetagameConfig(typing_extensions.TypedDict, total=False):
    currentVersion: int
    playerLevels: typing.List[PlayerLevel]
    kind: str

class CategoryListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[Category]
    kind: str

class Application(typing_extensions.TypedDict, total=False):
    category: ApplicationCategory
    kind: str
    lastUpdatedTimestamp: str
    assets: typing.List[ImageAsset]
    instances: typing.List[Instance]
    id: str
    themeColor: str
    enabledFeatures: typing.List[str]
    achievement_count: int
    name: str
    description: str
    author: str
    leaderboard_count: int

class AchievementUpdateRequest(typing_extensions.TypedDict, total=False):
    achievementId: str
    kind: str
    setStepsAtLeastPayload: GamesAchievementSetStepsAtLeast
    updateType: typing_extensions.Literal[
        "ACHIEVEMENT_UPDATE_TYPE_UNSPECIFIED",
        "REVEAL",
        "UNLOCK",
        "INCREMENT",
        "SET_STEPS_AT_LEAST",
    ]
    incrementPayload: GamesAchievementIncrement

class Snapshot(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["SNAPSHOT_TYPE_UNSPECIFIED", "SAVE_GAME"]
    coverImage: SnapshotImage
    id: str
    uniqueName: str
    lastModifiedMillis: str
    title: str
    durationMillis: str
    description: str
    progressValue: str
    kind: str
    driveId: str

class SnapshotImage(typing_extensions.TypedDict, total=False):
    kind: str
    width: int
    mime_type: str
    height: int
    url: str

class AchievementUpdateMultipleRequest(typing_extensions.TypedDict, total=False):
    updates: typing.List[AchievementUpdateRequest]
    kind: str

class AchievementUpdateResponse(typing_extensions.TypedDict, total=False):
    currentSteps: int
    updateOccurred: bool
    kind: str
    achievementId: str
    newlyUnlocked: bool
    currentState: typing_extensions.Literal[
        "UPDATED_ACHIEVEMENT_STATE_UNSPECIFIED", "HIDDEN", "REVEALED", "UNLOCKED"
    ]

class AchievementSetStepsAtLeastResponse(typing_extensions.TypedDict, total=False):
    newlyUnlocked: bool
    kind: str
    currentSteps: int

class EventDefinitionListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    items: typing.List[EventDefinition]

class ImageAsset(typing_extensions.TypedDict, total=False):
    url: str
    name: str
    kind: str
    width: int
    height: int

class PlayerScoreSubmissionList(typing_extensions.TypedDict, total=False):
    scores: typing.List[ScoreSubmission]
    kind: str

class StatsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    days_since_last_played: int
    spend_probability: float
    avg_session_length_minutes: float
    num_sessions: int
    spend_percentile: float
    num_purchases: int
    churn_probability: float
    num_sessions_percentile: float
    total_spend_next_28_days: float
    high_spender_probability: float

class PlayerScoreListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    submittedScores: typing.List[PlayerScoreResponse]

class EventUpdateResponse(typing_extensions.TypedDict, total=False):
    playerEvents: typing.List[PlayerEvent]
    kind: str
    batchFailures: typing.List[EventBatchRecordFailure]
    eventFailures: typing.List[EventRecordFailure]

class Leaderboard(typing_extensions.TypedDict, total=False):
    name: str
    kind: str
    iconUrl: str
    isIconUrlDefault: bool
    id: str
    order: typing_extensions.Literal[
        "SCORE_ORDER_UNSPECIFIED", "LARGER_IS_BETTER", "SMALLER_IS_BETTER"
    ]

class Player(typing_extensions.TypedDict, total=False):
    bannerUrlPortrait: str
    originalPlayerId: str
    title: str
    kind: str
    avatarImageUrl: str
    bannerUrlLandscape: str
    experienceInfo: PlayerExperienceInfo
    name: typing.Dict[str, typing.Any]
    displayName: str
    friendStatus: typing_extensions.Literal[
        "FRIEND_STATUS_UNSPECIFIED", "NO_RELATIONSHIP", "FRIEND"
    ]
    profileSettings: ProfileSettings
    playerId: str

class PlayerLeaderboardScore(typing_extensions.TypedDict, total=False):
    publicRank: LeaderboardScoreRank
    timeSpan: typing_extensions.Literal[
        "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
    ]
    kind: str
    leaderboard_id: str
    scoreString: str
    writeTimestamp: str
    friendsRank: LeaderboardScoreRank
    scoreValue: str
    scoreTag: str
    socialRank: LeaderboardScoreRank

class AchievementIncrementResponse(typing_extensions.TypedDict, total=False):
    kind: str
    currentSteps: int
    newlyUnlocked: bool

class PlayerScore(typing_extensions.TypedDict, total=False):
    formattedScore: str
    kind: str
    timeSpan: typing_extensions.Literal[
        "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
    ]
    scoreTag: str
    score: str

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

class ApplicationVerifyResponse(typing_extensions.TypedDict, total=False):
    alternate_player_id: str
    player_id: str
    kind: str

class EventPeriodUpdate(typing_extensions.TypedDict, total=False):
    timePeriod: EventPeriodRange
    kind: str
    updates: typing.List[EventUpdateRequest]

class PlayerLevel(typing_extensions.TypedDict, total=False):
    minExperiencePoints: str
    level: int
    kind: str
    maxExperiencePoints: str

class PlayerExperienceInfo(typing_extensions.TypedDict, total=False):
    kind: str
    lastLevelUpTimestampMillis: str
    currentExperiencePoints: str
    nextLevel: PlayerLevel
    currentLevel: PlayerLevel

class PlayerAchievementListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[PlayerAchievement]
    nextPageToken: str
