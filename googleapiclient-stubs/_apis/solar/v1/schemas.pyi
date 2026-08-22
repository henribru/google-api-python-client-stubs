import typing

_list = list

@typing.type_check_only
class BuildingInsights(typing.TypedDict, total=False):
    administrativeArea: str
    boundingBox: LatLngBox
    center: LatLng
    detectedArrays: BuildingInsightsDetectedArrays
    imageryDate: Date
    imageryProcessedDate: Date
    imageryQuality: typing.Literal[
        "IMAGERY_QUALITY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BASE"
    ]
    name: str
    postalCode: str
    regionCode: str
    solarPotential: SolarPotential
    statisticalArea: str

@typing.type_check_only
class BuildingInsightsDetectedArrays(typing.TypedDict, total=False):
    detectionStatus: typing.Literal[
        "DETECTION_STATUS_UNSPECIFIED",
        "DETECTION_STATUS_DATA_UNAVAILABLE",
        "DETECTION_STATUS_ARRAYS_DETECTED",
        "DETECTION_STATUS_NO_ARRAYS_DETECTED",
    ]
    latestCaptureDate: Date

@typing.type_check_only
class CashPurchaseSavings(typing.TypedDict, total=False):
    outOfPocketCost: Money
    paybackYears: float
    rebateValue: Money
    savings: SavingsOverTime
    upfrontCost: Money

@typing.type_check_only
class DataLayers(typing.TypedDict, total=False):
    annualFluxUrl: str
    dsmUrl: str
    hourlyShadeUrls: _list[str]
    imageryDate: Date
    imageryProcessedDate: Date
    imageryQuality: typing.Literal[
        "IMAGERY_QUALITY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BASE"
    ]
    maskUrl: str
    monthlyFluxUrl: str
    rgbUrl: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class FinancedPurchaseSavings(typing.TypedDict, total=False):
    annualLoanPayment: Money
    loanInterestRate: float
    rebateValue: Money
    savings: SavingsOverTime

@typing.type_check_only
class FinancialAnalysis(typing.TypedDict, total=False):
    averageKwhPerMonth: float
    cashPurchaseSavings: CashPurchaseSavings
    defaultBill: bool
    financedPurchaseSavings: FinancedPurchaseSavings
    financialDetails: FinancialDetails
    leasingSavings: LeasingSavings
    monthlyBill: Money
    panelConfigIndex: int

@typing.type_check_only
class FinancialDetails(typing.TypedDict, total=False):
    costOfElectricityWithoutSolar: Money
    federalIncentive: Money
    initialAcKwhPerYear: float
    lifetimeSrecTotal: Money
    netMeteringAllowed: bool
    percentageExportedToGrid: float
    remainingLifetimeUtilityBill: Money
    solarPercentage: float
    stateIncentive: Money
    utilityIncentive: Money

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LatLngBox(typing.TypedDict, total=False):
    ne: LatLng
    sw: LatLng

@typing.type_check_only
class LeasingSavings(typing.TypedDict, total=False):
    annualLeasingCost: Money
    leasesAllowed: bool
    leasesSupported: bool
    savings: SavingsOverTime

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class RoofSegmentSizeAndSunshineStats(typing.TypedDict, total=False):
    azimuthDegrees: float
    boundingBox: LatLngBox
    center: LatLng
    pitchDegrees: float
    planeHeightAtCenterMeters: float
    stats: SizeAndSunshineStats

@typing.type_check_only
class RoofSegmentSummary(typing.TypedDict, total=False):
    azimuthDegrees: float
    panelsCount: int
    pitchDegrees: float
    segmentIndex: int
    yearlyEnergyDcKwh: float

@typing.type_check_only
class SavingsOverTime(typing.TypedDict, total=False):
    financiallyViable: bool
    presentValueOfSavingsLifetime: Money
    presentValueOfSavingsYear20: Money
    savingsLifetime: Money
    savingsYear1: Money
    savingsYear20: Money

@typing.type_check_only
class SizeAndSunshineStats(typing.TypedDict, total=False):
    areaMeters2: float
    groundAreaMeters2: float
    sunshineQuantiles: _list[float]

@typing.type_check_only
class SolarPanel(typing.TypedDict, total=False):
    center: LatLng
    orientation: typing.Literal[
        "SOLAR_PANEL_ORIENTATION_UNSPECIFIED", "LANDSCAPE", "PORTRAIT"
    ]
    segmentIndex: int
    yearlyEnergyDcKwh: float

@typing.type_check_only
class SolarPanelConfig(typing.TypedDict, total=False):
    panelsCount: int
    roofSegmentSummaries: _list[RoofSegmentSummary]
    yearlyEnergyDcKwh: float

@typing.type_check_only
class SolarPotential(typing.TypedDict, total=False):
    buildingStats: SizeAndSunshineStats
    carbonOffsetFactorKgPerMwh: float
    financialAnalyses: _list[FinancialAnalysis]
    maxArrayAreaMeters2: float
    maxArrayPanelsCount: int
    maxSunshineHoursPerYear: float
    panelCapacityWatts: float
    panelHeightMeters: float
    panelLifetimeYears: int
    panelWidthMeters: float
    roofSegmentStats: _list[RoofSegmentSizeAndSunshineStats]
    solarPanelConfigs: _list[SolarPanelConfig]
    solarPanels: _list[SolarPanel]
    wholeRoofStats: SizeAndSunshineStats
