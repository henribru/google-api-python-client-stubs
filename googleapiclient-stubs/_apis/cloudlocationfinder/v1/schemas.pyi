import typing

import typing_extensions

_list = list

@typing.type_check_only
class CloudLocation(typing_extensions.TypedDict, total=False):
    carbonFreeEnergyPercentage: float
    cloudLocationType: typing_extensions.Literal[
        "CLOUD_LOCATION_TYPE_UNSPECIFIED",
        "CLOUD_LOCATION_TYPE_REGION",
        "CLOUD_LOCATION_TYPE_ZONE",
        "CLOUD_LOCATION_TYPE_REGION_EXTENSION",
        "CLOUD_LOCATION_TYPE_GDCC_ZONE",
    ]
    cloudProvider: typing_extensions.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "CLOUD_PROVIDER_GCP",
        "CLOUD_PROVIDER_AWS",
        "CLOUD_PROVIDER_AZURE",
        "CLOUD_PROVIDER_OCI",
    ]
    containingCloudLocation: str
    displayName: str
    name: str
    territoryCode: str

@typing.type_check_only
class ListCloudLocationsResponse(typing_extensions.TypedDict, total=False):
    cloudLocations: _list[CloudLocation]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class SearchCloudLocationsResponse(typing_extensions.TypedDict, total=False):
    cloudLocations: _list[CloudLocation]
    nextPageToken: str
