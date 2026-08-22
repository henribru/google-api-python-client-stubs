import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListPlaceActionLinksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    placeActionLinks: _list[PlaceActionLink]

@typing.type_check_only
class ListPlaceActionTypeMetadataResponse(typing.TypedDict, total=False):
    nextPageToken: str
    placeActionTypeMetadata: _list[PlaceActionTypeMetadata]

@typing.type_check_only
class PlaceActionLink(typing.TypedDict, total=False):
    createTime: str
    isEditable: bool
    isPreferred: bool
    name: str
    placeActionType: typing.Literal[
        "PLACE_ACTION_TYPE_UNSPECIFIED",
        "APPOINTMENT",
        "ONLINE_APPOINTMENT",
        "DINING_RESERVATION",
        "FOOD_ORDERING",
        "FOOD_DELIVERY",
        "FOOD_TAKEOUT",
        "SHOP_ONLINE",
        "SOLOPRENEUR_APPOINTMENT",
    ]
    providerType: typing.Literal[
        "PROVIDER_TYPE_UNSPECIFIED", "MERCHANT", "AGGREGATOR_3P"
    ]
    updateTime: str
    uri: str

@typing.type_check_only
class PlaceActionTypeMetadata(typing.TypedDict, total=False):
    displayName: str
    placeActionType: typing.Literal[
        "PLACE_ACTION_TYPE_UNSPECIFIED",
        "APPOINTMENT",
        "ONLINE_APPOINTMENT",
        "DINING_RESERVATION",
        "FOOD_ORDERING",
        "FOOD_DELIVERY",
        "FOOD_TAKEOUT",
        "SHOP_ONLINE",
        "SOLOPRENEUR_APPOINTMENT",
    ]
