import typing

import typing_extensions

_list = list

@typing.type_check_only
class BuildingInsights(typing_extensions.TypedDict, total=False):
    administrativeArea: str
    boundingBox: LatLngBox
    center: LatLng
    imageryDate: Date
    imageryProcessedDate: Date
    imageryQuality: typing_extensions.Literal[
        "IMAGERY_QUALITY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BASE"
    ]
    name: str
    postalCode: str
    regionCode: str
    solarPotential: SolarPotential
    statisticalArea: str

@typing.type_check_only
class CashPurchaseSavings(typing_extensions.TypedDict, total=False):
    outOfPocketCost: Money
    paybackYears: float
    rebateValue: Money
    savings: SavingsOverTime
    upfrontCost: Money

@typing.type_check_only
class DataLayers(typing_extensions.TypedDict, total=False):
    annualFluxUrl: str
    dsmUrl: str
    hourlyShadeUrls: _list[str]
    imageryDate: Date
    imageryProcessedDate: Date
    imageryQuality: typing_extensions.Literal[
        "IMAGERY_QUALITY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BASE"
    ]
    maskUrl: str
    monthlyFluxUrl: str
    rgbUrl: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class FinancedPurchaseSavings(typing_extensions.TypedDict, total=False):
    annualLoanPayment: Money
    loanInterestRate: float
    rebateValue: Money
    savings: SavingsOverTime

@typing.type_check_only
class FinancialAnalysis(typing_extensions.TypedDict, total=False):
    averageKwhPerMonth: float
    cashPurchaseSavings: CashPurchaseSavings
    defaultBill: bool
    financedPurchaseSavings: FinancedPurchaseSavings
    financialDetails: FinancialDetails
    leasingSavings: LeasingSavings
    monthlyBill: Money
    panelConfigIndex: int

@typing.type_check_only
class FinancialDetails(typing_extensions.TypedDict, total=False):
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
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LatLngBox(typing_extensions.TypedDict, total=False):
    ne: LatLng
    sw: LatLng

@typing.type_check_only
class LeasingSavings(typing_extensions.TypedDict, total=False):
    annualLeasingCost: Money
    leasesAllowed: bool
    leasesSupported: bool
    savings: SavingsOverTime

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class RoofSegmentSizeAndSunshineStats(typing_extensions.TypedDict, total=False):
    azimuthDegrees: float
    boundingBox: LatLngBox
    center: LatLng
    pitchDegrees: float
    planeHeightAtCenterMeters: float
    stats: SizeAndSunshineStats

@typing.type_check_only
class RoofSegmentSummary(typing_extensions.TypedDict, total=False):
    azimuthDegrees: float
    panelsCount: int
    pitchDegrees: float
    segmentIndex: int
    yearlyEnergyDcKwh: float

@typing.type_check_only
class SavingsOverTime(typing_extensions.TypedDict, total=False):
    financiallyViable: bool
    presentValueOfSavingsLifetime: Money
    presentValueOfSavingsYear20: Money
    savingsLifetime: Money
    savingsYear1: Money
    savingsYear20: Money

@typing.type_check_only
class SizeAndSunshineStats(typing_extensions.TypedDict, total=False):
    areaMeters2: float
    groundAreaMeters2: float
    sunshineQuantiles: _list[float]

@typing.type_check_only
class SolarPanel(typing_extensions.TypedDict, total=False):
    center: LatLng
    orientation: typing_extensions.Literal[
        "SOLAR_PANEL_ORIENTATION_UNSPECIFIED", "LANDSCAPE", "PORTRAIT"
    ]
    segmentIndex: int
    yearlyEnergyDcKwh: float

@typing.type_check_only
class SolarPanelConfig(typing_extensions.TypedDict, total=False):
    panelsCount: int
    roofSegmentSummaries: _list[RoofSegmentSummary]
    yearlyEnergyDcKwh: float

@typing.type_check_only
class SolarPotential(typing_extensions.TypedDict, total=False):
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
