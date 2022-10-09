import typing

import typing_extensions

_list = list

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
    cloudStorageWorkload: CloudStorageWorkload
    computeVmWorkload: ComputeVmWorkload
    name: str

@typing.type_check_only
class WorkloadCostEstimate(typing_extensions.TypedDict, total=False):
    name: str
    skuCostEstimates: _list[SkuCostEstimate]
    workloadTotalCostEstimate: CostEstimate
