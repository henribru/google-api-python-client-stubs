import typing

import typing_extensions

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListPlaceActionLinksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    placeActionLinks: typing.List[PlaceActionLink]

@typing.type_check_only
class ListPlaceActionTypeMetadataResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    placeActionTypeMetadata: typing.List[PlaceActionTypeMetadata]

@typing.type_check_only
class PlaceActionLink(typing_extensions.TypedDict, total=False):
    createTime: str
    isEditable: bool
    isPreferred: bool
    name: str
    placeActionType: typing_extensions.Literal[
        "PLACE_ACTION_TYPE_UNSPECIFIED",
        "APPOINTMENT",
        "ONLINE_APPOINTMENT",
        "DINING_RESERVATION",
        "FOOD_ORDERING",
        "FOOD_DELIVERY",
        "FOOD_TAKEOUT",
    ]
    providerType: typing_extensions.Literal[
        "PROVIDER_TYPE_UNSPECIFIED", "MERCHANT", "AGGREGATOR_3P"
    ]
    updateTime: str
    uri: str

@typing.type_check_only
class PlaceActionTypeMetadata(typing_extensions.TypedDict, total=False):
    displayName: str
    placeActionType: typing_extensions.Literal[
        "PLACE_ACTION_TYPE_UNSPECIFIED",
        "APPOINTMENT",
        "ONLINE_APPOINTMENT",
        "DINING_RESERVATION",
        "FOOD_ORDERING",
        "FOOD_DELIVERY",
        "FOOD_TAKEOUT",
    ]
