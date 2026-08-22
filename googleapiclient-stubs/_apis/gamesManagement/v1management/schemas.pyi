import typing

_list = list

@typing.type_check_only
class AchievementResetAllResponse(typing.TypedDict, total=False):
    kind: str
    results: _list[AchievementResetResponse]

@typing.type_check_only
class AchievementResetMultipleForAllRequest(typing.TypedDict, total=False):
    achievement_ids: _list[str]
    kind: str

@typing.type_check_only
class AchievementResetResponse(typing.TypedDict, total=False):
    currentState: str
    definitionId: str
    kind: str
    updateOccurred: bool

@typing.type_check_only
class EventsResetMultipleForAllRequest(typing.TypedDict, total=False):
    event_ids: _list[str]
    kind: str

@typing.type_check_only
class GamesPlayerExperienceInfoResource(typing.TypedDict, total=False):
    currentExperiencePoints: str
    currentLevel: GamesPlayerLevelResource
    lastLevelUpTimestampMillis: str
    nextLevel: GamesPlayerLevelResource

@typing.type_check_only
class GamesPlayerLevelResource(typing.TypedDict, total=False):
    level: int
    maxExperiencePoints: str
    minExperiencePoints: str

@typing.type_check_only
class HiddenPlayer(typing.TypedDict, total=False):
    hiddenTimeMillis: str
    kind: str
    player: Player

@typing.type_check_only
class HiddenPlayerList(typing.TypedDict, total=False):
    items: _list[HiddenPlayer]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Player(typing.TypedDict, total=False):
    avatarImageUrl: str
    bannerUrlLandscape: str
    bannerUrlPortrait: str
    displayName: str
    experienceInfo: GamesPlayerExperienceInfoResource
    kind: str
    name: dict[str, typing.Any]
    originalPlayerId: str
    playerId: str
    profileSettings: ProfileSettings
    title: str

@typing.type_check_only
class PlayerScoreResetAllResponse(typing.TypedDict, total=False):
    kind: str
    results: _list[PlayerScoreResetResponse]

@typing.type_check_only
class PlayerScoreResetResponse(typing.TypedDict, total=False):
    definitionId: str
    kind: str
    resetScoreTimeSpans: _list[str]

@typing.type_check_only
class ProfileSettings(typing.TypedDict, total=False):
    kind: str
    profileVisible: bool

@typing.type_check_only
class ScoresResetMultipleForAllRequest(typing.TypedDict, total=False):
    kind: str
    leaderboard_ids: _list[str]
