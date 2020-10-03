import typing

import typing_extensions

class PlayerScoreResetResponse(typing_extensions.TypedDict, total=False):
    resetScoreTimeSpans: typing.List[str]
    kind: str
    definitionId: str

class ProfileSettings(typing_extensions.TypedDict, total=False):
    kind: str
    profileVisible: bool

class AchievementResetResponse(typing_extensions.TypedDict, total=False):
    currentState: str
    kind: str
    updateOccurred: bool
    definitionId: str

class ScoresResetMultipleForAllRequest(typing_extensions.TypedDict, total=False):
    leaderboard_ids: typing.List[str]
    kind: str

class AchievementResetAllResponse(typing_extensions.TypedDict, total=False):
    kind: str
    results: typing.List[AchievementResetResponse]

class GamesPlayerExperienceInfoResource(typing_extensions.TypedDict, total=False):
    currentLevel: GamesPlayerLevelResource
    nextLevel: GamesPlayerLevelResource
    lastLevelUpTimestampMillis: str
    currentExperiencePoints: str

class EventsResetMultipleForAllRequest(typing_extensions.TypedDict, total=False):
    event_ids: typing.List[str]
    kind: str

class Player(typing_extensions.TypedDict, total=False):
    bannerUrlLandscape: str
    avatarImageUrl: str
    title: str
    kind: str
    bannerUrlPortrait: str
    originalPlayerId: str
    profileSettings: ProfileSettings
    experienceInfo: GamesPlayerExperienceInfoResource
    playerId: str
    displayName: str
    name: typing.Dict[str, typing.Any]

class GamesPlayerLevelResource(typing_extensions.TypedDict, total=False):
    minExperiencePoints: str
    level: int
    maxExperiencePoints: str

class PlayerScoreResetAllResponse(typing_extensions.TypedDict, total=False):
    kind: str
    results: typing.List[PlayerScoreResetResponse]

class HiddenPlayer(typing_extensions.TypedDict, total=False):
    hiddenTimeMillis: str
    player: Player
    kind: str

class HiddenPlayerList(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    items: typing.List[HiddenPlayer]

class AchievementResetMultipleForAllRequest(typing_extensions.TypedDict, total=False):
    achievement_ids: typing.List[str]
    kind: str
