import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActivateBiddingFunctionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ArchiveBiddingFunctionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BiddingFunction(typing_extensions.TypedDict, total=False):
    biddingFunction: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED"]
    type: typing_extensions.Literal[
        "FUNCTION_TYPE_UNSPECIFIED",
        "TURTLEDOVE_SIMULATION_BIDDING_FUNCTION",
        "FLEDGE_BIDDING_FUNCTION",
    ]

@typing.type_check_only
class ListBiddingFunctionsResponse(typing_extensions.TypedDict, total=False):
    biddingFunctions: _list[BiddingFunction]
    nextPageToken: str
