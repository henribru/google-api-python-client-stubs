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
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

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
    emissionsGramsPerPax: EmissionsGramsPerPax
    flight: Flight

@typing.type_check_only
class ModelVersion(typing_extensions.TypedDict, total=False):
    dated: str
    major: int
    minor: int
    patch: int
