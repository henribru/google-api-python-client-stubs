import typing

import typing_extensions

class LocalizedStringBundle(typing_extensions.TypedDict, total=False):
    translations: typing.List[LocalizedString]
    kind: str

class LeaderboardConfigurationListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    items: typing.List[LeaderboardConfiguration]

class AchievementConfiguration(typing_extensions.TypedDict, total=False):
    id: str
    token: str
    initialState: typing_extensions.Literal[
        "INITIAL_STATE_UNSPECIFIED", "HIDDEN", "REVEALED"
    ]
    kind: str
    stepsToUnlock: int
    draft: AchievementConfigurationDetail
    published: AchievementConfigurationDetail
    achievementType: typing_extensions.Literal[
        "ACHIEVEMENT_TYPE_UNSPECIFIED", "STANDARD", "INCREMENTAL"
    ]

class AchievementConfigurationListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    items: typing.List[AchievementConfiguration]

class LeaderboardConfiguration(typing_extensions.TypedDict, total=False):
    scoreMin: str
    draft: LeaderboardConfigurationDetail
    kind: str
    scoreMax: str
    scoreOrder: typing_extensions.Literal[
        "SCORE_ORDER_UNSPECIFIED", "LARGER_IS_BETTER", "SMALLER_IS_BETTER"
    ]
    id: str
    published: LeaderboardConfigurationDetail
    token: str

class LeaderboardConfigurationDetail(typing_extensions.TypedDict, total=False):
    scoreFormat: GamesNumberFormatConfiguration
    iconUrl: str
    kind: str
    name: LocalizedStringBundle
    sortRank: int

class AchievementConfigurationDetail(typing_extensions.TypedDict, total=False):
    kind: str
    description: LocalizedStringBundle
    sortRank: int
    pointValue: int
    iconUrl: str
    name: LocalizedStringBundle

class GamesNumberAffixConfiguration(typing_extensions.TypedDict, total=False):
    one: LocalizedStringBundle
    two: LocalizedStringBundle
    zero: LocalizedStringBundle
    few: LocalizedStringBundle
    other: LocalizedStringBundle
    many: LocalizedStringBundle

class LocalizedString(typing_extensions.TypedDict, total=False):
    value: str
    kind: str
    locale: str

class GamesNumberFormatConfiguration(typing_extensions.TypedDict, total=False):
    suffix: GamesNumberAffixConfiguration
    numDecimalPlaces: int
    currencyCode: str
    numberFormatType: typing_extensions.Literal[
        "NUMBER_FORMAT_TYPE_UNSPECIFIED", "NUMERIC", "TIME_DURATION", "CURRENCY"
    ]

class ImageConfiguration(typing_extensions.TypedDict, total=False):
    url: str
    kind: str
    resourceId: str
    imageType: typing_extensions.Literal[
        "IMAGE_TYPE_UNSPECIFIED", "ACHIEVEMENT_ICON", "LEADERBOARD_ICON"
    ]
