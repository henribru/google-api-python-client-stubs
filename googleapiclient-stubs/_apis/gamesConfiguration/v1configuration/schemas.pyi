import typing

import typing_extensions

_list = list

@typing.type_check_only
class AchievementConfiguration(typing_extensions.TypedDict, total=False):
    achievementType: typing_extensions.Literal[
        "ACHIEVEMENT_TYPE_UNSPECIFIED", "STANDARD", "INCREMENTAL"
    ]
    draft: AchievementConfigurationDetail
    id: str
    initialState: typing_extensions.Literal[
        "INITIAL_STATE_UNSPECIFIED", "HIDDEN", "REVEALED"
    ]
    kind: str
    published: AchievementConfigurationDetail
    stepsToUnlock: int
    token: str

@typing.type_check_only
class AchievementConfigurationDetail(typing_extensions.TypedDict, total=False):
    description: LocalizedStringBundle
    iconUrl: str
    kind: str
    name: LocalizedStringBundle
    pointValue: int
    sortRank: int

@typing.type_check_only
class AchievementConfigurationListResponse(typing_extensions.TypedDict, total=False):
    items: _list[AchievementConfiguration]
    kind: str
    nextPageToken: str

@typing.type_check_only
class GamesNumberAffixConfiguration(typing_extensions.TypedDict, total=False):
    few: LocalizedStringBundle
    many: LocalizedStringBundle
    one: LocalizedStringBundle
    other: LocalizedStringBundle
    two: LocalizedStringBundle
    zero: LocalizedStringBundle

@typing.type_check_only
class GamesNumberFormatConfiguration(typing_extensions.TypedDict, total=False):
    currencyCode: str
    numDecimalPlaces: int
    numberFormatType: typing_extensions.Literal[
        "NUMBER_FORMAT_TYPE_UNSPECIFIED", "NUMERIC", "TIME_DURATION", "CURRENCY"
    ]
    suffix: GamesNumberAffixConfiguration

@typing.type_check_only
class ImageConfiguration(typing_extensions.TypedDict, total=False):
    imageType: typing_extensions.Literal[
        "IMAGE_TYPE_UNSPECIFIED", "ACHIEVEMENT_ICON", "LEADERBOARD_ICON"
    ]
    kind: str
    resourceId: str
    url: str

@typing.type_check_only
class LeaderboardConfiguration(typing_extensions.TypedDict, total=False):
    draft: LeaderboardConfigurationDetail
    id: str
    kind: str
    published: LeaderboardConfigurationDetail
    scoreMax: str
    scoreMin: str
    scoreOrder: typing_extensions.Literal[
        "SCORE_ORDER_UNSPECIFIED", "LARGER_IS_BETTER", "SMALLER_IS_BETTER"
    ]
    token: str

@typing.type_check_only
class LeaderboardConfigurationDetail(typing_extensions.TypedDict, total=False):
    iconUrl: str
    kind: str
    name: LocalizedStringBundle
    scoreFormat: GamesNumberFormatConfiguration
    sortRank: int

@typing.type_check_only
class LeaderboardConfigurationListResponse(typing_extensions.TypedDict, total=False):
    items: _list[LeaderboardConfiguration]
    kind: str
    nextPageToken: str

@typing.type_check_only
class LocalizedString(typing_extensions.TypedDict, total=False):
    kind: str
    locale: str
    value: str

@typing.type_check_only
class LocalizedStringBundle(typing_extensions.TypedDict, total=False):
    kind: str
    translations: _list[LocalizedString]
