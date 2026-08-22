import typing

_list = list

@typing.type_check_only
class ActivateBiddingFunctionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ArchiveBiddingFunctionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class BiddingFunction(typing.TypedDict, total=False):
    biddingFunction: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED"]
    type: typing.Literal[
        "FUNCTION_TYPE_UNSPECIFIED",
        "TURTLEDOVE_SIMULATION_BIDDING_FUNCTION",
        "FLEDGE_BIDDING_FUNCTION",
    ]

@typing.type_check_only
class ListBiddingFunctionsResponse(typing.TypedDict, total=False):
    biddingFunctions: _list[BiddingFunction]
    nextPageToken: str
