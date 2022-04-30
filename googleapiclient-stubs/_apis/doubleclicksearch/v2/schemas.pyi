import typing

import typing_extensions

_list = list

@typing.type_check_only
class Availability(typing_extensions.TypedDict, total=False):
    advertiserId: str
    agencyId: str
    availabilityTimestamp: str
    segmentationId: str
    segmentationName: str
    segmentationType: str

@typing.type_check_only
class Conversion(typing_extensions.TypedDict, total=False):
    adGroupId: str
    adId: str
    advertiserId: str
    agencyId: str
    attributionModel: str
    campaignId: str
    channel: str
    clickId: str
    conversionId: str
    conversionModifiedTimestamp: str
    conversionTimestamp: str
    countMillis: str
    criterionId: str
    currencyCode: str
    customDimension: _list[CustomDimension]
    customMetric: _list[CustomMetric]
    deviceType: str
    dsConversionId: str
    engineAccountId: str
    floodlightOrderId: str
    inventoryAccountId: str
    productCountry: str
    productGroupId: str
    productId: str
    productLanguage: str
    quantityMillis: str
    revenueMicros: str
    segmentationId: str
    segmentationName: str
    segmentationType: str
    state: str
    storeId: str
    type: str

@typing.type_check_only
class ConversionList(typing_extensions.TypedDict, total=False):
    conversion: _list[Conversion]
    kind: str

@typing.type_check_only
class CustomDimension(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class CustomMetric(typing_extensions.TypedDict, total=False):
    name: str
    value: float

@typing.type_check_only
class IdMappingFile(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    files: _list[dict[str, typing.Any]]
    id: str
    isReportReady: bool
    kind: str
    request: ReportRequest
    rowCount: int
    rows: _list[ReportRow]
    statisticsCurrencyCode: str
    statisticsTimeZone: str

@typing.type_check_only
class ReportApiColumnSpec(typing_extensions.TypedDict, total=False):
    columnName: str
    customDimensionName: str
    customMetricName: str
    endDate: str
    groupByColumn: bool
    headerText: str
    platformSource: str
    productReportPerspective: str
    savedColumnName: str
    startDate: str

@typing.type_check_only
class ReportRequest(typing_extensions.TypedDict, total=False):
    columns: _list[ReportApiColumnSpec]
    downloadFormat: str
    filters: _list[dict[str, typing.Any]]
    includeDeletedEntities: bool
    includeRemovedEntities: bool
    maxRowsPerFile: int
    orderBy: _list[dict[str, typing.Any]]
    reportScope: dict[str, typing.Any]
    reportType: str
    rowCount: int
    startRow: int
    statisticsCurrency: str
    timeRange: dict[str, typing.Any]
    verifySingleTimeZone: bool

@typing.type_check_only
class ReportRow(dict[str, typing.Any]): ...

@typing.type_check_only
class SavedColumn(typing_extensions.TypedDict, total=False):
    kind: str
    savedColumnName: str
    type: str

@typing.type_check_only
class SavedColumnList(typing_extensions.TypedDict, total=False):
    items: _list[SavedColumn]
    kind: str

@typing.type_check_only
class UpdateAvailabilityRequest(typing_extensions.TypedDict, total=False):
    availabilities: _list[Availability]

@typing.type_check_only
class UpdateAvailabilityResponse(typing_extensions.TypedDict, total=False):
    availabilities: _list[Availability]
