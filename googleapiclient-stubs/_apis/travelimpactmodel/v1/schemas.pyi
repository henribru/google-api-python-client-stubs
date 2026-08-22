import typing

_list = list

@typing.type_check_only
class ComputeDetailedFlightEmissionsRequest(typing.TypedDict, total=False):
    flights: _list[Flight]

@typing.type_check_only
class ComputeDetailedFlightEmissionsResponse(typing.TypedDict, total=False):
    flightsWithDetailedEmissions: _list[FlightWithDetailedEmissions]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeFlightEmissionsRequest(typing.TypedDict, total=False):
    flights: _list[Flight]

@typing.type_check_only
class ComputeFlightEmissionsResponse(typing.TypedDict, total=False):
    flightEmissions: _list[FlightWithEmissions]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeScope3FlightEmissionsRequest(typing.TypedDict, total=False):
    flights: _list[Scope3FlightSegment]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeScope3FlightEmissionsResponse(typing.TypedDict, total=False):
    flightEmissions: _list[Scope3FlightEmissions]
    modelVersion: ModelVersion

@typing.type_check_only
class ComputeTypicalFlightEmissionsRequest(typing.TypedDict, total=False):
    markets: _list[Market]

@typing.type_check_only
class ComputeTypicalFlightEmissionsResponse(typing.TypedDict, total=False):
    modelVersion: ModelVersion
    typicalFlightEmissions: _list[TypicalFlightEmissions]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class EasaLabelMetadata(typing.TypedDict, total=False):
    labelExpiryDate: Date
    labelIssueDate: Date
    labelVersion: str
    safDiscountPercentage: float

@typing.type_check_only
class EmissionsBreakdown(typing.TypedDict, total=False):
    ttwEmissionsGramsPerPax: EmissionsGramsPerPax
    wttEmissionsGramsPerPax: EmissionsGramsPerPax

@typing.type_check_only
class EmissionsGramsPerPax(typing.TypedDict, total=False):
    business: int
    economy: int
    first: int
    premiumEconomy: int

@typing.type_check_only
class EmissionsMetadata(typing.TypedDict, total=False):
    easaLabelMetadata: EasaLabelMetadata
    emissionsProvenance: EmissionsProvenance
    timWebsiteEmissionsCalculatorUrl: str

@typing.type_check_only
class EmissionsProvenance(typing.TypedDict, total=False):
    provenanceEntries: _list[EmissionsProvenanceEntry]

@typing.type_check_only
class EmissionsProvenanceEntry(typing.TypedDict, total=False):
    cargoMassFractionData: float
    cargoMassFractionT100Strategy: typing.Literal[
        "STRATEGY_UNSPECIFIED",
        "CARRIER_ROUTE_AIRCRAFT_CLASS",
        "ROUTE_AIRCRAFT_CLASS",
        "DISTANCE_AIRCRAFT_CLASS",
        "ACTUAL_CARRIER_ROUTE_YEAR_MONTH_AIRCRAFT_CLASS",
    ]
    dataCategory: typing.Literal[
        "DATA_CATEGORY_UNSPECIFIED", "PRIMARY", "MODELED", "DEFAULT"
    ]
    distanceAdjustmentStrategy: typing.Literal[
        "STRATEGY_UNSPECIFIED", "ORIGIN_DESTINATION", "COUNTRY_PAIR", "DEFAULT"
    ]
    estimatedFlightDistanceKm: int
    fuelBurnEeaStrategy: typing.Literal[
        "STRATEGY_UNSPECIFIED",
        "AIRCRAFT_MAPPING_FALLBACK_WITH_CORRECTION_FACTOR",
        "AIRCRAFT_MAPPING_EXACT",
        "AIRCRAFT_MAPPING_FALLBACK",
    ]
    loadFactorsChAviationStrategy: typing.Literal[
        "STRATEGY_UNSPECIFIED", "CARRIER_MONTH", "ACTUAL_CARRIER_YEAR_MONTH"
    ]
    loadFactorsData: float
    loadFactorsT100Strategy: typing.Literal[
        "STRATEGY_UNSPECIFIED",
        "CARRIER_ROUTE_MONTH",
        "CARRIER_MONTH",
        "ACTUAL_CARRIER_ROUTE_YEAR_MONTH",
    ]
    provenanceEntryType: typing.Literal[
        "EMISSIONS_PROVENANCE_ENTRY_TYPE_UNSPECIFIED",
        "FUEL_BURN",
        "LOAD_FACTORS",
        "CARGO_MASS_FRACTION",
        "SEATING_CONFIG",
        "SEAT_AREA_RATIOS",
        "DISTANCE_ADJUSTMENT",
    ]
    seatAreaRatioIataStrategy: typing.Literal[
        "STRATEGY_UNSPECIFIED", "NARROW_AIRCRAFT_BODY", "WIDE_AIRCRAFT_BODY"
    ]
    source: typing.Literal[
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
class Flight(typing.TypedDict, total=False):
    departureDate: Date
    destination: str
    flightNumber: int
    operatingCarrierCode: str
    origin: str

@typing.type_check_only
class FlightEmissionsDetails(typing.TypedDict, total=False):
    contrailsImpactBucket: typing.Literal[
        "CONTRAILS_IMPACT_UNSPECIFIED",
        "CONTRAILS_IMPACT_NEGLIGIBLE",
        "CONTRAILS_IMPACT_MODERATE",
        "CONTRAILS_IMPACT_SEVERE",
    ]
    emissionsBreakdown: EmissionsBreakdown
    emissionsGramsPerPax: EmissionsGramsPerPax
    source: typing.Literal["SOURCE_UNSPECIFIED", "TIM", "EASA"]

@typing.type_check_only
class FlightWithDetailedEmissions(typing.TypedDict, total=False):
    emissionsMetadata: EmissionsMetadata
    flight: Flight
    flightEmissionsDetails: FlightEmissionsDetails

@typing.type_check_only
class FlightWithEmissions(typing.TypedDict, total=False):
    contrailsImpactBucket: typing.Literal[
        "CONTRAILS_IMPACT_UNSPECIFIED",
        "CONTRAILS_IMPACT_NEGLIGIBLE",
        "CONTRAILS_IMPACT_MODERATE",
        "CONTRAILS_IMPACT_SEVERE",
    ]
    easaLabelMetadata: EasaLabelMetadata
    emissionsGramsPerPax: EmissionsGramsPerPax
    flight: Flight
    source: typing.Literal["SOURCE_UNSPECIFIED", "TIM", "EASA"]

@typing.type_check_only
class Market(typing.TypedDict, total=False):
    destination: str
    origin: str

@typing.type_check_only
class ModelVersion(typing.TypedDict, total=False):
    dated: str
    major: int
    minor: int
    patch: int

@typing.type_check_only
class Scope3FlightEmissions(typing.TypedDict, total=False):
    flight: Scope3FlightSegment
    source: typing.Literal[
        "SCOPE3_DATA_TYPE_UNSPECIFIED",
        "TIM_EMISSIONS",
        "TYPICAL_FLIGHT_EMISSIONS",
        "DISTANCE_BASED_EMISSIONS",
    ]
    ttwEmissionsGramsPerPax: str
    wttEmissionsGramsPerPax: str
    wtwEmissionsGramsPerPax: str

@typing.type_check_only
class Scope3FlightSegment(typing.TypedDict, total=False):
    cabinClass: typing.Literal[
        "CABIN_CLASS_UNSPECIFIED", "ECONOMY", "PREMIUM_ECONOMY", "BUSINESS", "FIRST"
    ]
    carrierCode: str
    departureDate: Date
    destination: str
    distanceKm: str
    flightNumber: int
    origin: str

@typing.type_check_only
class TypicalFlightEmissions(typing.TypedDict, total=False):
    emissionsGramsPerPax: EmissionsGramsPerPax
    market: Market
