import typing

_list = list

@typing.type_check_only
class AchievementDefinition(typing.TypedDict, total=False):
    achievementLifecycleState: typing.Literal[
        "ACHIEVEMENT_LIFECYCLE_STATE_UNSPECIFIED",
        "ACHIEVEMENT_LIFECYCLE_STATE_ACTIVE",
        "ACHIEVEMENT_LIFECYCLE_STATE_ARCHIVED",
    ]
    achievementType: typing.Literal["STANDARD", "INCREMENTAL"]
    description: str
    experiencePoints: str
    formattedTotalSteps: str
    id: str
    initialState: typing.Literal["HIDDEN", "REVEALED", "UNLOCKED"]
    isRevealedIconUrlDefault: bool
    isUnlockedIconUrlDefault: bool
    kind: str
    name: str
    revealedIconUrl: str
    totalSteps: int
    unlockedIconUrl: str

@typing.type_check_only
class AchievementDefinitionsListResponse(typing.TypedDict, total=False):
    items: _list[AchievementDefinition]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AchievementIncrementResponse(typing.TypedDict, total=False):
    currentSteps: int
    kind: str
    newlyUnlocked: bool

@typing.type_check_only
class AchievementRevealResponse(typing.TypedDict, total=False):
    currentState: typing.Literal["REVEALED", "UNLOCKED"]
    kind: str

@typing.type_check_only
class AchievementSetStepsAtLeastResponse(typing.TypedDict, total=False):
    currentSteps: int
    kind: str
    newlyUnlocked: bool

@typing.type_check_only
class AchievementUnlockResponse(typing.TypedDict, total=False):
    kind: str
    newlyUnlocked: bool

@typing.type_check_only
class AchievementUpdateMultipleRequest(typing.TypedDict, total=False):
    kind: str
    updates: _list[AchievementUpdateRequest]

@typing.type_check_only
class AchievementUpdateMultipleResponse(typing.TypedDict, total=False):
    kind: str
    updatedAchievements: _list[AchievementUpdateResponse]

@typing.type_check_only
class AchievementUpdateRequest(typing.TypedDict, total=False):
    achievementId: str
    incrementPayload: GamesAchievementIncrement
    kind: str
    setStepsAtLeastPayload: GamesAchievementSetStepsAtLeast
    updateType: typing.Literal["REVEAL", "UNLOCK", "INCREMENT", "SET_STEPS_AT_LEAST"]

@typing.type_check_only
class AchievementUpdateResponse(typing.TypedDict, total=False):
    achievementId: str
    currentState: typing.Literal["HIDDEN", "REVEALED", "UNLOCKED"]
    currentSteps: int
    kind: str
    newlyUnlocked: bool
    updateOccurred: bool

@typing.type_check_only
class Application(typing.TypedDict, total=False):
    achievement_count: int
    assets: _list[ImageAsset]
    author: str
    category: ApplicationCategory
    description: str
    enabledFeatures: _list[typing.Literal["SNAPSHOTS"]]
    id: str
    instances: _list[Instance]
    kind: str
    lastUpdatedTimestamp: str
    leaderboard_count: int
    name: str
    themeColor: str

@typing.type_check_only
class ApplicationCategory(typing.TypedDict, total=False):
    kind: str
    primary: str
    secondary: str

@typing.type_check_only
class ApplicationPlayerId(typing.TypedDict, total=False):
    applicationId: str
    playerId: str

@typing.type_check_only
class ApplicationVerifyResponse(typing.TypedDict, total=False):
    alternate_player_id: str
    kind: str
    player_id: str

@typing.type_check_only
class BatchRecordEventsRequest(typing.TypedDict, total=False):
    droidGuardBlob: str
    events: _list[PlayerGameEvent]
    packageName: str
    requestTime: str
    salt: str

@typing.type_check_only
class BatchRecordEventsResponse(typing.TypedDict, total=False):
    failedRequests: dict[str, typing.Any]

@typing.type_check_only
class Category(typing.TypedDict, total=False):
    category: str
    experiencePoints: str
    kind: str

@typing.type_check_only
class CategoryListResponse(typing.TypedDict, total=False):
    items: _list[Category]
    kind: str
    nextPageToken: str

@typing.type_check_only
class EndPoint(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class EventBatchRecordFailure(typing.TypedDict, total=False):
    failureCause: typing.Literal[
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
class EventChild(typing.TypedDict, total=False):
    childId: str
    kind: str

@typing.type_check_only
class EventDefinition(typing.TypedDict, total=False):
    childEvents: _list[EventChild]
    description: str
    displayName: str
    id: str
    imageUrl: str
    isDefaultImageUrl: bool
    kind: str
    visibility: typing.Literal["REVEALED", "HIDDEN"]

@typing.type_check_only
class EventDefinitionListResponse(typing.TypedDict, total=False):
    items: _list[EventDefinition]
    kind: str
    nextPageToken: str

@typing.type_check_only
class EventPeriodRange(typing.TypedDict, total=False):
    kind: str
    periodEndMillis: str
    periodStartMillis: str

@typing.type_check_only
class EventPeriodUpdate(typing.TypedDict, total=False):
    kind: str
    timePeriod: EventPeriodRange
    updates: _list[EventUpdateRequest]

@typing.type_check_only
class EventRecordFailure(typing.TypedDict, total=False):
    eventId: str
    failureCause: typing.Literal["NOT_FOUND", "INVALID_UPDATE_VALUE"]
    kind: str

@typing.type_check_only
class EventRecordRequest(typing.TypedDict, total=False):
    currentTimeMillis: str
    kind: str
    requestId: str
    timePeriods: _list[EventPeriodUpdate]

@typing.type_check_only
class EventUpdateRequest(typing.TypedDict, total=False):
    definitionId: str
    kind: str
    updateCount: str

@typing.type_check_only
class EventUpdateResponse(typing.TypedDict, total=False):
    batchFailures: _list[EventBatchRecordFailure]
    eventFailures: _list[EventRecordFailure]
    kind: str
    playerEvents: _list[PlayerEvent]

@typing.type_check_only
class GamePlayerToken(typing.TypedDict, total=False):
    applicationId: str
    recallToken: RecallToken

@typing.type_check_only
class GamesAchievementIncrement(typing.TypedDict, total=False):
    kind: str
    requestId: str
    steps: int

@typing.type_check_only
class GamesAchievementSetStepsAtLeast(typing.TypedDict, total=False):
    kind: str
    steps: int

@typing.type_check_only
class GeneratePlayGroupingApiTokenResponse(typing.TypedDict, total=False):
    token: PlayGroupingApiToken

@typing.type_check_only
class GenerateRecallPlayGroupingApiTokenResponse(typing.TypedDict, total=False):
    token: PlayGroupingApiToken

@typing.type_check_only
class GetMultipleApplicationPlayerIdsResponse(typing.TypedDict, total=False):
    playerIds: _list[ApplicationPlayerId]

@typing.type_check_only
class ImageAsset(typing.TypedDict, total=False):
    height: int
    kind: str
    name: str
    url: str
    width: int

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    acquisitionUri: str
    androidInstance: InstanceAndroidDetails
    iosInstance: InstanceIosDetails
    kind: str
    name: str
    platformType: typing.Literal["ANDROID", "IOS", "WEB_APP"]
    realtimePlay: bool
    turnBasedPlay: bool
    webInstance: InstanceWebDetails

@typing.type_check_only
class InstanceAndroidDetails(typing.TypedDict, total=False):
    enablePiracyCheck: bool
    kind: str
    packageName: str
    preferred: bool

@typing.type_check_only
class InstanceIosDetails(typing.TypedDict, total=False):
    bundleIdentifier: str
    itunesAppId: str
    kind: str
    preferredForIpad: bool
    preferredForIphone: bool
    supportIpad: bool
    supportIphone: bool

@typing.type_check_only
class InstanceWebDetails(typing.TypedDict, total=False):
    kind: str
    launchUrl: str
    preferred: bool

@typing.type_check_only
class Leaderboard(typing.TypedDict, total=False):
    iconUrl: str
    id: str
    isIconUrlDefault: bool
    kind: str
    name: str
    order: typing.Literal["LARGER_IS_BETTER", "SMALLER_IS_BETTER"]

@typing.type_check_only
class LeaderboardEntry(typing.TypedDict, total=False):
    formattedScore: str
    formattedScoreRank: str
    kind: str
    player: Player
    scoreRank: str
    scoreTag: str
    scoreValue: str
    timeSpan: typing.Literal["ALL_TIME", "WEEKLY", "DAILY"]
    writeTimestampMillis: str

@typing.type_check_only
class LeaderboardListResponse(typing.TypedDict, total=False):
    items: _list[Leaderboard]
    kind: str
    nextPageToken: str

@typing.type_check_only
class LeaderboardScoreRank(typing.TypedDict, total=False):
    formattedNumScores: str
    formattedRank: str
    kind: str
    numScores: str
    rank: str

@typing.type_check_only
class LeaderboardScores(typing.TypedDict, total=False):
    items: _list[LeaderboardEntry]
    kind: str
    nextPageToken: str
    numScores: str
    playerScore: LeaderboardEntry
    prevPageToken: str

@typing.type_check_only
class LinkPersonaRequest(typing.TypedDict, total=False):
    cardinalityConstraint: typing.Literal["ONE_PERSONA_TO_ONE_PLAYER"]
    conflictingLinksResolutionPolicy: typing.Literal[
        "KEEP_EXISTING_LINKS", "CREATE_NEW_LINK"
    ]
    expireTime: str
    persona: str
    sessionId: str
    token: str
    ttl: str

@typing.type_check_only
class LinkPersonaResponse(typing.TypedDict, total=False):
    state: typing.Literal["LINK_CREATED", "PERSONA_OR_PLAYER_ALREADY_LINKED"]

@typing.type_check_only
class MetagameConfig(typing.TypedDict, total=False):
    currentVersion: int
    kind: str
    playerLevels: _list[PlayerLevel]

@typing.type_check_only
class PlayGroupingApiToken(typing.TypedDict, total=False):
    tokenValue: str

@typing.type_check_only
class Player(typing.TypedDict, total=False):
    avatarImageUrl: str
    bannerUrlLandscape: str
    bannerUrlPortrait: str
    displayName: str
    experienceInfo: PlayerExperienceInfo
    friendStatus: typing.Literal["NO_RELATIONSHIP", "FRIEND"]
    gamePlayerId: str
    kind: str
    name: dict[str, typing.Any]
    originalPlayerId: str
    playerId: str
    profileSettings: ProfileSettings
    title: str

@typing.type_check_only
class PlayerAchievement(typing.TypedDict, total=False):
    achievementState: typing.Literal["HIDDEN", "REVEALED", "UNLOCKED"]
    currentSteps: int
    experiencePoints: str
    formattedCurrentStepsString: str
    id: str
    kind: str
    lastUpdatedTimestamp: str

@typing.type_check_only
class PlayerAchievementListResponse(typing.TypedDict, total=False):
    items: _list[PlayerAchievement]
    kind: str
    nextPageToken: str

@typing.type_check_only
class PlayerEvent(typing.TypedDict, total=False):
    definitionId: str
    formattedNumEvents: str
    kind: str
    numEvents: str
    playerId: str

@typing.type_check_only
class PlayerEventListResponse(typing.TypedDict, total=False):
    items: _list[PlayerEvent]
    kind: str
    nextPageToken: str

@typing.type_check_only
class PlayerExperienceInfo(typing.TypedDict, total=False):
    currentExperiencePoints: str
    currentLevel: PlayerLevel
    kind: str
    lastLevelUpTimestampMillis: str
    nextLevel: PlayerLevel

@typing.type_check_only
class PlayerGameEvent(typing.TypedDict, total=False):
    eventId: str
    eventName: str
    eventProperties: dict[str, typing.Any]
    eventTime: str

@typing.type_check_only
class PlayerLeaderboardScore(typing.TypedDict, total=False):
    friendsRank: LeaderboardScoreRank
    kind: str
    leaderboard_id: str
    publicRank: LeaderboardScoreRank
    scoreString: str
    scoreTag: str
    scoreValue: str
    socialRank: LeaderboardScoreRank
    timeSpan: typing.Literal["ALL_TIME", "WEEKLY", "DAILY"]
    writeTimestamp: str

@typing.type_check_only
class PlayerLeaderboardScoreListResponse(typing.TypedDict, total=False):
    items: _list[PlayerLeaderboardScore]
    kind: str
    nextPageToken: str
    player: Player

@typing.type_check_only
class PlayerLevel(typing.TypedDict, total=False):
    kind: str
    level: int
    maxExperiencePoints: str
    minExperiencePoints: str

@typing.type_check_only
class PlayerListResponse(typing.TypedDict, total=False):
    items: _list[Player]
    kind: str
    nextPageToken: str

@typing.type_check_only
class PlayerScore(typing.TypedDict, total=False):
    formattedScore: str
    kind: str
    score: str
    scoreTag: str
    timeSpan: typing.Literal["ALL_TIME", "WEEKLY", "DAILY"]

@typing.type_check_only
class PlayerScoreListResponse(typing.TypedDict, total=False):
    kind: str
    submittedScores: _list[PlayerScoreResponse]

@typing.type_check_only
class PlayerScoreResponse(typing.TypedDict, total=False):
    beatenScoreTimeSpans: _list[typing.Literal["ALL_TIME", "WEEKLY", "DAILY"]]
    formattedScore: str
    kind: str
    leaderboardId: str
    scoreTag: str
    unbeatenScores: _list[PlayerScore]

@typing.type_check_only
class PlayerScoreSubmissionList(typing.TypedDict, total=False):
    kind: str
    scores: _list[ScoreSubmission]

@typing.type_check_only
class ProfileSettings(typing.TypedDict, total=False):
    friendsListVisibility: typing.Literal["VISIBLE", "REQUEST_REQUIRED", "UNAVAILABLE"]
    kind: str
    profileVisible: bool

@typing.type_check_only
class PropertyValue(typing.TypedDict, total=False):
    boolValue: bool
    doubleValue: float
    durationValue: str
    intValue: str
    stringValue: str
    timestampValue: str

@typing.type_check_only
class RecallToken(typing.TypedDict, total=False):
    expireTime: str
    multiPlayerPersona: bool
    token: str

@typing.type_check_only
class ResetPersonaRequest(typing.TypedDict, total=False):
    persona: str

@typing.type_check_only
class ResetPersonaResponse(typing.TypedDict, total=False):
    unlinked: bool

@typing.type_check_only
class RetrieveDeveloperGamesLastPlayerTokenResponse(typing.TypedDict, total=False):
    gamePlayerToken: GamePlayerToken

@typing.type_check_only
class RetrieveGamesPlayerTokensResponse(typing.TypedDict, total=False):
    gamePlayerTokens: _list[GamePlayerToken]

@typing.type_check_only
class RetrievePlayerTokensResponse(typing.TypedDict, total=False):
    tokens: _list[RecallToken]

@typing.type_check_only
class RevisionCheckResponse(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    revisionStatus: typing.Literal["OK", "DEPRECATED", "INVALID"]

@typing.type_check_only
class ScopedPlayerIds(typing.TypedDict, total=False):
    developerPlayerKey: str
    gamePlayerId: str

@typing.type_check_only
class ScoreSubmission(typing.TypedDict, total=False):
    kind: str
    leaderboardId: str
    score: str
    scoreTag: str
    signature: str

@typing.type_check_only
class Snapshot(typing.TypedDict, total=False):
    coverImage: SnapshotImage
    description: str
    driveId: str
    durationMillis: str
    id: str
    kind: str
    lastModifiedMillis: str
    progressValue: str
    title: str
    type: typing.Literal["SAVE_GAME"]
    uniqueName: str

@typing.type_check_only
class SnapshotImage(typing.TypedDict, total=False):
    height: int
    kind: str
    mime_type: str
    url: str
    width: int

@typing.type_check_only
class SnapshotListResponse(typing.TypedDict, total=False):
    items: _list[Snapshot]
    kind: str
    nextPageToken: str

@typing.type_check_only
class StatsResponse(typing.TypedDict, total=False):
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

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UnlinkPersonaRequest(typing.TypedDict, total=False):
    persona: str
    sessionId: str
    token: str

@typing.type_check_only
class UnlinkPersonaResponse(typing.TypedDict, total=False):
    unlinked: bool
