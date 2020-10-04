import typing

import typing_extensions
@typing.type_check_only
class AchievementResetAllResponse(typing_extensions.TypedDict, total=False):
    kind: str
    results: typing.List[AchievementResetResponse]

@typing.type_check_only
class AchievementResetMultipleForAllRequest(typing_extensions.TypedDict, total=False):
    achievement_ids: typing.List[str]
    kind: str

@typing.type_check_only
class AchievementResetResponse(typing_extensions.TypedDict, total=False):
    currentState: str
    definitionId: str
    kind: str
    updateOccurred: bool

@typing.type_check_only
class EventsResetMultipleForAllRequest(typing_extensions.TypedDict, total=False):
    event_ids: typing.List[str]
    kind: str

@typing.type_check_only
class GamesPlayerExperienceInfoResource(typing_extensions.TypedDict, total=False):
    currentExperiencePoints: str
    currentLevel: GamesPlayerLevelResource
    lastLevelUpTimestampMillis: str
    nextLevel: GamesPlayerLevelResource

@typing.type_check_only
class GamesPlayerLevelResource(typing_extensions.TypedDict, total=False):
    level: int
    maxExperiencePoints: str
    minExperiencePoints: str

@typing.type_check_only
class HiddenPlayer(typing_extensions.TypedDict, total=False):
    hiddenTimeMillis: str
    kind: str
    player: Player

@typing.type_check_only
class HiddenPlayerList(typing_extensions.TypedDict, total=False):
    items: typing.List[HiddenPlayer]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Player(typing_extensions.TypedDict, total=False):
    avatarImageUrl: str
    bannerUrlLandscape: str
    bannerUrlPortrait: str
    displayName: str
    experienceInfo: GamesPlayerExperienceInfoResource
    kind: str
    name: typing.Dict[str, typing.Any]
    originalPlayerId: str
    playerId: str
    profileSettings: ProfileSettings
    title: str

@typing.type_check_only
class PlayerScoreResetAllResponse(typing_extensions.TypedDict, total=False):
    kind: str
    results: typing.List[PlayerScoreResetResponse]

@typing.type_check_only
class PlayerScoreResetResponse(typing_extensions.TypedDict, total=False):
    definitionId: str
    kind: str
    resetScoreTimeSpans: typing.List[str]

@typing.type_check_only
class ProfileSettings(typing_extensions.TypedDict, total=False):
    kind: str
    profileVisible: bool

@typing.type_check_only
class ScoresResetMultipleForAllRequest(typing_extensions.TypedDict, total=False):
    kind: str
    leaderboard_ids: typing.List[str]
