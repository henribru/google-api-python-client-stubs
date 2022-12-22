import typing

import typing_extensions

_list = list

@typing.type_check_only
class CacheFillRegions(typing_extensions.TypedDict, total=False):
    destinationRegion: typing_extensions.Literal[
        "CACHE_FILL_DESTINATION_REGION_UNSPECIFIED",
        "CACHE_FILL_DESTINATION_REGION_ASIA_PACIFIC",
        "CACHE_FILL_DESTINATION_REGION_EUROPE",
        "CACHE_FILL_DESTINATION_REGION_NORTH_AMERICA",
        "CACHE_FILL_DESTINATION_REGION_OCEANIA",
        "CACHE_FILL_DESTINATION_REGION_SOUTH_AMERICA",
        "CACHE_FILL_DESTINATION_REGION_CHINA",
        "CACHE_FILL_DESTINATION_REGION_OTHERS",
    ]
    sourceRegion: typing_extensions.Literal[
        "CACHE_FILL_SOURCE_REGION_UNSPECIFIED",
        "CACHE_FILL_REGION_ASIA_PACIFIC",
        "CACHE_FILL_SOURCE_REGION_EUROPE",
        "CACHE_FILL_SOURCE_REGION_NORTH_AMERICA",
        "CACHE_FILL_SOURCE_REGION_OCEANIA",
        "CACHE_FILL_SOURCE_REGION_SOUTH_AMERICA",
    ]

@typing.type_check_only
class CloudCdnEgressWorkload(typing_extensions.TypedDict, total=False):
    cacheEgressDestination: typing_extensions.Literal[
        "CACHE_EGRESS_DESTINATION_UNSPECIFIED",
        "CACHE_EGRESS_DESTINATION_ASIA_PACIFIC",
        "CACHE_EGRESS_DESTINATION_CHINA",
        "CACHE_EGRESS_DESTINATION_EUROPE",
        "CACHE_EGRESS_DESTINATION_NORTH_AMERICA",
        "CACHE_EGRESS_DESTINATION_OCEANIA",
        "CACHE_EGRESS_DESTINATION_LATIN_AMERICA",
        "CACHE_EGRESS_DESTINATION_OTHER_DESTINATIONS",
    ]
    cacheEgressRate: Usage

@typing.type_check_only
class CloudCdnWorkload(typing_extensions.TypedDict, total=False):
    cacheFillOriginService: typing_extensions.Literal[
        "CACHE_FILL_ORIGIN_SERVICE_UNSPECIFIED",
        "CACHE_FILL_ORIGIN_SERVICE_GOOGLE_CLOUD_STORAGE_BUCKET",
        "CACHE_FILL_ORIGIN_SERVICE_BACKEND_SERVICE",
    ]
    cacheFillRate: Usage
    cacheFillRegions: CacheFillRegions
    cacheLookUpRate: Usage

@typing.type_check_only
class CloudInterconnectEgressWorkload(typing_extensions.TypedDict, total=False):
    egressRate: Usage
    interconnectConnectionLocation: typing_extensions.Literal[
        "INTERCONNECT_CONNECTION_LOCATION_UNSPECIFIED",
        "INTERCONNECT_CONNECTION_LOCATION_ASIA",
        "INTERCONNECT_CONNECTION_LOCATION_EUROPE",
        "INTERCONNECT_CONNECTION_LOCATION_NORTH_AMERICA",
        "INTERCONNECT_CONNECTION_LOCATION_SOUTH_AMERICA",
        "INTERCONNECT_CONNECTION_LOCATION_AUSTRALIA",
    ]

@typing.type_check_only
class CloudInterconnectWorkload(typing_extensions.TypedDict, total=False):
    interconnectAttachments: _list[VlanAttachment]
    interconnectType: typing_extensions.Literal[
        "INTERCONNECT_TYPE_UNSPECIFIED",
        "INTERCONNECT_TYPE_DEDICATED",
        "INTERCONNECT_TYPE_PARTNER",
    ]
    linkType: typing_extensions.Literal[
        "LINK_TYPE_UNSPECIFIED",
        "LINK_TYPE_ETHERNET_10G_LR",
        "LINK_TYPE_ETHERNET_100G_LR",
    ]
    provisionedLinkCount: Usage

@typing.type_check_only
class CloudStorageEgressWorkload(typing_extensions.TypedDict, total=False):
    destinationContinent: typing_extensions.Literal[
        "DESTINATION_CONTINENT_UNSPECIFIED",
        "DESTINATION_CONTINENT_ASIA_PACIFIC",
        "DESTINATION_CONTINENT_AUTRALIA",
        "DESTINATION_CONTINENT_EUROPE",
        "DESTINATION_CONTINENT_NORTH_AMERICA",
        "DESTINATION_CONTINENT_SOUTH_AMERICA",
    ]
    egressRate: Usage
    sourceContinent: typing_extensions.Literal[
        "SOURCE_CONTINENT_UNSPECIFIED",
        "SOURCE_CONTINENT_ASIA_PACIFIC",
        "SOURCE_CONTINENT_AUSTRALIA",
        "SOURCE_CONTINENT_EUROPE",
        "SOURCE_CONTINENT_NORTH_AMERICA",
        "SOURCE_CONTINENT_SOUTH_AMERICA",
    ]

@typing.type_check_only
class CloudStorageWorkload(typing_extensions.TypedDict, total=False):
    dataRetrieval: Usage
    dataStored: Usage
    dualRegion: DualRegional
    multiRegion: MultiRegional
    operationA: Usage
    operationB: Usage
    region: Regional
    storageClass: str

@typing.type_check_only
class Commitment(typing_extensions.TypedDict, total=False):
    name: str
    vmResourceBasedCud: VmResourceBasedCud

@typing.type_check_only
class CommitmentCostEstimate(typing_extensions.TypedDict, total=False):
    commitmentTotalCostEstimate: CostEstimate
    name: str
    skuCostEstimates: _list[SkuCostEstimate]

@typing.type_check_only
class ComputeVmWorkload(typing_extensions.TypedDict, total=False):
    enableConfidentialCompute: bool
    guestAccelerator: GuestAccelerator
    instancesRunning: Usage
    licenses: _list[str]
    machineType: MachineType
    persistentDisks: _list[PersistentDisk]
    preemptible: bool
    region: str

@typing.type_check_only
class CostEstimate(typing_extensions.TypedDict, total=False):
    creditEstimates: _list[CreditEstimate]
    netCostEstimate: Money
    preCreditCostEstimate: Money

@typing.type_check_only
class CostEstimationResult(typing_extensions.TypedDict, total=False):
    currencyCode: str
    segmentCostEstimates: _list[SegmentCostEstimate]
    skus: _list[Sku]

@typing.type_check_only
class CostScenario(typing_extensions.TypedDict, total=False):
    commitments: _list[Commitment]
    scenarioConfig: ScenarioConfig
    workloads: _list[Workload]

@typing.type_check_only
class CreditEstimate(typing_extensions.TypedDict, total=False):
    creditAmount: Money
    creditDescription: str
    creditType: str

@typing.type_check_only
class CustomMachineType(typing_extensions.TypedDict, total=False):
    machineSeries: str
    memorySizeGb: float
    virtualCpuCount: str

@typing.type_check_only
class DualRegional(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class EstimateCostScenarioForBillingAccountRequest(
    typing_extensions.TypedDict, total=False
):
    costScenario: CostScenario

@typing.type_check_only
class EstimateCostScenarioForBillingAccountResponse(
    typing_extensions.TypedDict, total=False
):
    costEstimationResult: CostEstimationResult

@typing.type_check_only
class EstimateCostScenarioWithListPriceRequest(
    typing_extensions.TypedDict, total=False
):
    costScenario: CostScenario

@typing.type_check_only
class EstimateCostScenarioWithListPriceResponse(
    typing_extensions.TypedDict, total=False
):
    costEstimationResult: CostEstimationResult

@typing.type_check_only
class EstimationTimePoint(typing_extensions.TypedDict, total=False):
    estimationTimeFrameOffset: str

@typing.type_check_only
class GuestAccelerator(typing_extensions.TypedDict, total=False):
    acceleratorCount: str
    acceleratorType: str

@typing.type_check_only
class MachineType(typing_extensions.TypedDict, total=False):
    customMachineType: CustomMachineType
    predefinedMachineType: PredefinedMachineType

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MultiRegional(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class PersistentDisk(typing_extensions.TypedDict, total=False):
    diskSize: Usage
    diskType: str
    provisionedIops: Usage
    scope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_ZONAL", "SCOPE_REGIONAL"
    ]

@typing.type_check_only
class PredefinedMachineType(typing_extensions.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class PremiumTierEgressWorkload(typing_extensions.TypedDict, total=False):
    destinationContinent: typing_extensions.Literal[
        "DESTINATION_CONTINENT_UNSPECIFIED",
        "DESTINATION_CONTINENT_ASIA_PACIFIC",
        "DESTINATION_CONTINENT_AFRICA",
        "DESTINATION_CONTINENT_NORTH_AMERICA",
        "DESTINATION_CONTINENT_AUTRALIA",
        "DESTINATION_CONTINENT_CENTRAL_AMERICA",
        "DESTINATION_CONTINENT_CHINA",
        "DESTINATION_CONTINENT_EASTERN_EUROPE",
        "DESTINATION_CONTINENT_WESTERN_EUROPE",
        "DESTINATION_CONTINENT_EMEA",
        "DESTINATION_CONTINENT_INDIA",
        "DESTINATION_CONTINENT_MIDDLE_EAST",
        "DESTINATION_CONTINENT_SOUTH_AMERICA",
    ]
    egressRate: Usage
    sourceRegion: str

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    effectiveTime: EstimationTimePoint
    priceType: str
    rate: Rate

@typing.type_check_only
class Rate(typing_extensions.TypedDict, total=False):
    tiers: _list[RateTier]
    unit: str
    unitCount: float

@typing.type_check_only
class RateTier(typing_extensions.TypedDict, total=False):
    price: Money
    startAmount: float

@typing.type_check_only
class Regional(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class ScenarioConfig(typing_extensions.TypedDict, total=False):
    estimateDuration: str

@typing.type_check_only
class SegmentCostEstimate(typing_extensions.TypedDict, total=False):
    commitmentCostEstimates: _list[CommitmentCostEstimate]
    segmentStartTime: EstimationTimePoint
    segmentTotalCostEstimate: CostEstimate
    workloadCostEstimates: _list[WorkloadCostEstimate]

@typing.type_check_only
class Sku(typing_extensions.TypedDict, total=False):
    displayName: str
    prices: _list[Price]
    sku: str

@typing.type_check_only
class SkuCostEstimate(typing_extensions.TypedDict, total=False):
    costEstimate: CostEstimate
    sku: str
    usageAmount: float
    usageUnit: str

@typing.type_check_only
class StandardTierEgressWorkload(typing_extensions.TypedDict, total=False):
    egressRate: Usage
    sourceRegion: str

@typing.type_check_only
class Usage(typing_extensions.TypedDict, total=False):
    usageRateTimeline: UsageRateTimeline

@typing.type_check_only
class UsageRateTimeline(typing_extensions.TypedDict, total=False):
    unit: str
    usageRateTimelineEntries: _list[UsageRateTimelineEntry]

@typing.type_check_only
class UsageRateTimelineEntry(typing_extensions.TypedDict, total=False):
    effectiveTime: EstimationTimePoint
    usageRate: float

@typing.type_check_only
class VlanAttachment(typing_extensions.TypedDict, total=False):
    bandwidth: typing_extensions.Literal[
        "BANDWIDTH_UNSPECIFIED",
        "BANDWIDTH_BPS_50M",
        "BANDWIDTH_BPS_100M",
        "BANDWIDTH_BPS_200M",
        "BANDWIDTH_BPS_300M",
        "BANDWIDTH_BPS_400M",
        "BANDWIDTH_BPS_500M",
        "BANDWIDTH_BPS_1G",
        "BANDWIDTH_BPS_2G",
        "BANDWIDTH_BPS_5G",
        "BANDWIDTH_BPS_10G",
        "BANDWIDTH_BPS_20G",
        "BANDWIDTH_BPS_50G",
    ]
    vlanCount: Usage

@typing.type_check_only
class VmResourceBasedCud(typing_extensions.TypedDict, total=False):
    guestAccelerator: GuestAccelerator
    machineSeries: str
    memorySizeGb: float
    plan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "TWELVE_MONTH", "THIRTY_SIX_MONTH"
    ]
    region: str
    virtualCpuCount: str

@typing.type_check_only
class Workload(typing_extensions.TypedDict, total=False):
    cloudCdnEgressWorkload: CloudCdnEgressWorkload
    cloudCdnWorkload: CloudCdnWorkload
    cloudInterconnectEgressWorkload: CloudInterconnectEgressWorkload
    cloudInterconnectWorkload: CloudInterconnectWorkload
    cloudStorageEgressWorkload: CloudStorageEgressWorkload
    cloudStorageWorkload: CloudStorageWorkload
    computeVmWorkload: ComputeVmWorkload
    name: str
    premiumTierEgressWorkload: PremiumTierEgressWorkload
    standardTierEgressWorkload: StandardTierEgressWorkload

@typing.type_check_only
class WorkloadCostEstimate(typing_extensions.TypedDict, total=False):
    name: str
    skuCostEstimates: _list[SkuCostEstimate]
    workloadTotalCostEstimate: CostEstimate
