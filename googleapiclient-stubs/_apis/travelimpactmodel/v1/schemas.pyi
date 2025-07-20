import typing

import typing_extensions

_list = list

@typing.type_check_only
class ComputeFlightEmissionsRequest(typing_extensions.TypedDict, total=False):
    flights: _list[Flight]

@typing.type_check_only
class ComputeFlightEmissionsResponse(typing_extensions.TypedDict, total=False):
    flightEmissions: _list[FlightWithEmissions]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeTypicalFlightEmissionsRequest(typing_extensions.TypedDict, total=False):
    markets: _list[Market]

@typing.type_check_only
class ComputeTypicalFlightEmissionsResponse(typing_extensions.TypedDict, total=False):
    modelVersion: ModelVersion
    typicalFlightEmissions: _list[TypicalFlightEmissions]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class EasaLabelMetadata(typing_extensions.TypedDict, total=False):
    labelExpiryDate: Date
    labelIssueDate: Date
    labelVersion: str
    safDiscountPercentage: float

@typing.type_check_only
class EmissionsGramsPerPax(typing_extensions.TypedDict, total=False):
    business: int
    economy: int
    first: int
    premiumEconomy: int

@typing.type_check_only
class Flight(typing_extensions.TypedDict, total=False):
    departureDate: Date
    destination: str
    flightNumber: int
    operatingCarrierCode: str
    origin: str

@typing.type_check_only
class FlightWithEmissions(typing_extensions.TypedDict, total=False):
    contrailsImpactBucket: typing_extensions.Literal[
        "CONTRAILS_IMPACT_UNSPECIFIED",
        "CONTRAILS_IMPACT_NEGLIGIBLE",
        "CONTRAILS_IMPACT_MODERATE",
        "CONTRAILS_IMPACT_SEVERE",
    ]
    easaLabelMetadata: EasaLabelMetadata
    emissionsGramsPerPax: EmissionsGramsPerPax
    flight: Flight
    source: typing_extensions.Literal["SOURCE_UNSPECIFIED", "TIM", "EASA"]

@typing.type_check_only
class Market(typing_extensions.TypedDict, total=False):
    destination: str
    origin: str

@typing.type_check_only
class ModelVersion(typing_extensions.TypedDict, total=False):
    dated: str
    major: int
    minor: int
    patch: int

@typing.type_check_only
class TypicalFlightEmissions(typing_extensions.TypedDict, total=False):
    emissionsGramsPerPax: EmissionsGramsPerPax
    market: Market
