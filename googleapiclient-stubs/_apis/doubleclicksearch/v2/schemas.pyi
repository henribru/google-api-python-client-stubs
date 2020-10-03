import typing

import typing_extensions

class Availability(typing_extensions.TypedDict, total=False):
    segmentationType: str
    agencyId: str
    segmentationId: str
    advertiserId: str
    availabilityTimestamp: str
    segmentationName: str

class ConversionList(typing_extensions.TypedDict, total=False):
    conversion: typing.List[Conversion]
    kind: str

class CustomDimension(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class UpdateAvailabilityResponse(typing_extensions.TypedDict, total=False):
    availabilities: typing.List[Availability]

class CustomMetric(typing_extensions.TypedDict, total=False):
    name: str
    value: float

class ReportRequest(typing_extensions.TypedDict, total=False):
    statisticsCurrency: str
    downloadFormat: str
    maxRowsPerFile: int
    startRow: int
    timeRange: typing.Dict[str, typing.Any]
    includeDeletedEntities: bool
    verifySingleTimeZone: bool
    reportScope: typing.Dict[str, typing.Any]
    columns: typing.List[ReportApiColumnSpec]
    reportType: str
    orderBy: typing.List[typing.Dict[str, typing.Any]]
    filters: typing.List[typing.Dict[str, typing.Any]]
    rowCount: int
    includeRemovedEntities: bool

class Conversion(typing_extensions.TypedDict, total=False):
    conversionModifiedTimestamp: str
    campaignId: str
    quantityMillis: str
    deviceType: str
    clickId: str
    segmentationType: str
    advertiserId: str
    customDimension: typing.List[CustomDimension]
    engineAccountId: str
    productGroupId: str
    type: str
    segmentationId: str
    attributionModel: str
    floodlightOrderId: str
    productCountry: str
    storeId: str
    conversionId: str
    adId: str
    countMillis: str
    revenueMicros: str
    state: str
    channel: str
    customMetric: typing.List[CustomMetric]
    adGroupId: str
    conversionTimestamp: str
    inventoryAccountId: str
    productId: str
    dsConversionId: str
    criterionId: str
    currencyCode: str
    productLanguage: str
    segmentationName: str
    agencyId: str

class ReportRow(typing.Dict[str, typing.Any]): ...

class UpdateAvailabilityRequest(typing_extensions.TypedDict, total=False):
    availabilities: typing.List[Availability]

class Report(typing_extensions.TypedDict, total=False):
    id: str
    isReportReady: bool
    rowCount: int
    rows: typing.List[ReportRow]
    request: ReportRequest
    statisticsCurrencyCode: str
    files: typing.List[typing.Dict[str, typing.Any]]
    statisticsTimeZone: str
    kind: str

class SavedColumnList(typing_extensions.TypedDict, total=False):
    items: typing.List[SavedColumn]
    kind: str

class SavedColumn(typing_extensions.TypedDict, total=False):
    savedColumnName: str
    type: str
    kind: str

class ReportApiColumnSpec(typing_extensions.TypedDict, total=False):
    groupByColumn: bool
    productReportPerspective: str
    headerText: str
    columnName: str
    savedColumnName: str
    customDimensionName: str
    platformSource: str
    endDate: str
    startDate: str
    customMetricName: str
