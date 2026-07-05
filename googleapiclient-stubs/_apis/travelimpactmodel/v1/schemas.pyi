import typing

import typing_extensions

_list = list

@typing.type_check_only
class ComputeDetailedFlightEmissionsRequest(typing_extensions.TypedDict, total=False):
    flights: _list[Flight]

@typing.type_check_only
class ComputeDetailedFlightEmissionsResponse(typing_extensions.TypedDict, total=False):
    flightsWithDetailedEmissions: _list[FlightWithDetailedEmissions]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeFlightEmissionsRequest(typing_extensions.TypedDict, total=False):
    flights: _list[Flight]

@typing.type_check_only
class ComputeFlightEmissionsResponse(typing_extensions.TypedDict, total=False):
    flightEmissions: _list[FlightWithEmissions]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeScope3FlightEmissionsRequest(typing_extensions.TypedDict, total=False):
    flights: _list[Scope3FlightSegment]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeScope3FlightEmissionsResponse(typing_extensions.TypedDict, total=False):
    flightEmissions: _list[Scope3FlightEmissions]
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
class EmissionsBreakdown(typing_extensions.TypedDict, total=False):
    ttwEmissionsGramsPerPax: EmissionsGramsPerPax
    wttEmissionsGramsPerPax: EmissionsGramsPerPax

@typing.type_check_only
class EmissionsGramsPerPax(typing_extensions.TypedDict, total=False):
    business: int
    economy: int
    first: int
    premiumEconomy: int

@typing.type_check_only
class EmissionsMetadata(typing_extensions.TypedDict, total=False):
    easaLabelMetadata: EasaLabelMetadata
    emissionsProvenance: EmissionsProvenance
    timWebsiteEmissionsCalculatorUrl: str

@typing.type_check_only
class EmissionsProvenance(typing_extensions.TypedDict, total=False):
    provenanceEntries: _list[EmissionsProvenanceEntry]

@typing.type_check_only
class EmissionsProvenanceEntry(typing_extensions.TypedDict, total=False):
    cargoMassFractionData: float
    cargoMassFractionT100Strategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED",
        "CARRIER_ROUTE_AIRCRAFT_CLASS",
        "ROUTE_AIRCRAFT_CLASS",
        "DISTANCE_AIRCRAFT_CLASS",
        "ACTUAL_CARRIER_ROUTE_YEAR_MONTH_AIRCRAFT_CLASS",
    ]
    dataCategory: typing_extensions.Literal[
        "DATA_CATEGORY_UNSPECIFIED", "PRIMARY", "MODELED", "DEFAULT"
    ]
    distanceAdjustmentStrategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED", "ORIGIN_DESTINATION", "COUNTRY_PAIR", "DEFAULT"
    ]
    estimatedFlightDistanceKm: int
    fuelBurnEeaStrategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED",
        "AIRCRAFT_MAPPING_FALLBACK_WITH_CORRECTION_FACTOR",
        "AIRCRAFT_MAPPING_EXACT",
        "AIRCRAFT_MAPPING_FALLBACK",
    ]
    loadFactorsChAviationStrategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED", "CARRIER_MONTH", "ACTUAL_CARRIER_YEAR_MONTH"
    ]
    loadFactorsData: float
    loadFactorsT100Strategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED",
        "CARRIER_ROUTE_MONTH",
        "CARRIER_MONTH",
        "ACTUAL_CARRIER_ROUTE_YEAR_MONTH",
    ]
    provenanceEntryType: typing_extensions.Literal[
        "EMISSIONS_PROVENANCE_ENTRY_TYPE_UNSPECIFIED",
        "FUEL_BURN",
        "LOAD_FACTORS",
        "CARGO_MASS_FRACTION",
        "SEATING_CONFIG",
        "SEAT_AREA_RATIOS",
        "DISTANCE_ADJUSTMENT",
    ]
    seatAreaRatioIataStrategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED", "NARROW_AIRCRAFT_BODY", "WIDE_AIRCRAFT_BODY"
    ]
    source: typing_extensions.Literal[
        "DATA_SOURCE_UNSPECIFIED",
        "EEA",
        "T100",
        "CH_AVIATION",
        "OAG",
        "OPERATING_CARRIER",
        "AIRCRAFT_MODEL_TYPICAL",
        "GLOBAL_DEFAULT",
        "IATA",
        "ICL",
    ]
    sourceVersion: str

@typing.type_check_only
class Flight(typing_extensions.TypedDict, total=False):
    departureDate: Date
    destination: str
    flightNumber: int
    operatingCarrierCode: str
    origin: str

@typing.type_check_only
class FlightEmissionsDetails(typing_extensions.TypedDict, total=False):
    contrailsImpactBucket: typing_extensions.Literal[
        "CONTRAILS_IMPACT_UNSPECIFIED",
        "CONTRAILS_IMPACT_NEGLIGIBLE",
        "CONTRAILS_IMPACT_MODERATE",
        "CONTRAILS_IMPACT_SEVERE",
    ]
    emissionsBreakdown: EmissionsBreakdown
    emissionsGramsPerPax: EmissionsGramsPerPax
    source: typing_extensions.Literal["SOURCE_UNSPECIFIED", "TIM", "EASA"]

@typing.type_check_only
class FlightWithDetailedEmissions(typing_extensions.TypedDict, total=False):
    emissionsMetadata: EmissionsMetadata
    flight: Flight
    flightEmissionsDetails: FlightEmissionsDetails

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
class Scope3FlightEmissions(typing_extensions.TypedDict, total=False):
    flight: Scope3FlightSegment
    source: typing_extensions.Literal[
        "SCOPE3_DATA_TYPE_UNSPECIFIED",
        "TIM_EMISSIONS",
        "TYPICAL_FLIGHT_EMISSIONS",
        "DISTANCE_BASED_EMISSIONS",
    ]
    ttwEmissionsGramsPerPax: str
    wttEmissionsGramsPerPax: str
    wtwEmissionsGramsPerPax: str

@typing.type_check_only
class Scope3FlightSegment(typing_extensions.TypedDict, total=False):
    cabinClass: typing_extensions.Literal[
        "CABIN_CLASS_UNSPECIFIED", "ECONOMY", "PREMIUM_ECONOMY", "BUSINESS", "FIRST"
    ]
    carrierCode: str
    departureDate: Date
    destination: str
    distanceKm: str
    flightNumber: int
    origin: str

@typing.type_check_only
class TypicalFlightEmissions(typing_extensions.TypedDict, total=False):
    emissionsGramsPerPax: EmissionsGramsPerPax
    market: Market
