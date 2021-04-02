import typing

import typing_extensions
@typing.type_check_only
class BiddingFunction(typing_extensions.TypedDict, total=False):
    biddingFunction: str
    name: str

@typing.type_check_only
class ListBiddingFunctionsResponse(typing_extensions.TypedDict, total=False):
    biddingFunctions: typing.List[BiddingFunction]
    nextPageToken: str
