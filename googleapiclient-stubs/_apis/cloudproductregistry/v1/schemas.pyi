import typing

import typing_extensions

_list = list

@typing.type_check_only
class ListLogicalProductVariantsResponse(typing_extensions.TypedDict, total=False):
    logicalProductVariants: _list[LogicalProductVariant]
    nextPageToken: str

@typing.type_check_only
class ListLogicalProductsResponse(typing_extensions.TypedDict, total=False):
    logicalProducts: _list[LogicalProduct]
    nextPageToken: str

@typing.type_check_only
class ListProductSuitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    productSuites: _list[ProductSuite]

@typing.type_check_only
class LogicalProduct(typing_extensions.TypedDict, total=False):
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "LIFECYCLE_STATE_PUBLIC_PREVIEW",
        "LIFECYCLE_STATE_PRIVATE_GA",
        "LIFECYCLE_STATE_GA",
        "LIFECYCLE_STATE_DEPRECATED",
    ]
    name: str
    productSuite: str
    replaced: bool
    replacement: str
    title: str
    variants: _list[str]

@typing.type_check_only
class LogicalProductVariant(typing_extensions.TypedDict, total=False):
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "LIFECYCLE_STATE_PUBLIC_PREVIEW",
        "LIFECYCLE_STATE_PRIVATE_GA",
        "LIFECYCLE_STATE_GA",
        "LIFECYCLE_STATE_DEPRECATED",
    ]
    name: str
    replaced: bool
    replacement: str
    title: str

@typing.type_check_only
class LookupEntityResponse(typing_extensions.TypedDict, total=False):
    logicalProduct: LogicalProduct
    logicalProductVariant: LogicalProductVariant
    productSuite: ProductSuite

@typing.type_check_only
class ProductSuite(typing_extensions.TypedDict, total=False):
    logicalProducts: _list[str]
    name: str
    replaced: bool
    replacement: str
    title: str
