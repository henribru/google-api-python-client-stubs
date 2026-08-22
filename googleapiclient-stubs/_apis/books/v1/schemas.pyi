import typing

_list = list

@typing.type_check_only
class Annotation(typing.TypedDict, total=False):
    afterSelectedText: str
    beforeSelectedText: str
    clientVersionRanges: dict[str, typing.Any]
    created: str
    currentVersionRanges: dict[str, typing.Any]
    data: str
    deleted: bool
    highlightStyle: str
    id: str
    kind: str
    layerId: str
    layerSummary: dict[str, typing.Any]
    pageIds: _list[str]
    selectedText: str
    selfLink: str
    updated: str
    volumeId: str

@typing.type_check_only
class Annotations(typing.TypedDict, total=False):
    items: _list[Annotation]
    kind: str
    nextPageToken: str
    totalItems: int

@typing.type_check_only
class AnnotationsSummary(typing.TypedDict, total=False):
    kind: str
    layers: _list[dict[str, typing.Any]]

@typing.type_check_only
class Annotationsdata(typing.TypedDict, total=False):
    items: _list[GeoAnnotationdata]
    kind: str
    nextPageToken: str
    totalItems: int

@typing.type_check_only
class BooksAnnotationsRange(typing.TypedDict, total=False):
    endOffset: str
    endPosition: str
    startOffset: str
    startPosition: str

@typing.type_check_only
class BooksCloudloadingResource(typing.TypedDict, total=False):
    author: str
    processingState: str
    title: str
    volumeId: str

@typing.type_check_only
class BooksVolumesRecommendedRateResponse(typing.TypedDict, total=False):
    consistency_token: str

@typing.type_check_only
class Bookshelf(typing.TypedDict, total=False):
    access: str
    created: str
    description: str
    id: int
    kind: str
    selfLink: str
    title: str
    updated: str
    volumeCount: int
    volumesLastUpdated: str

@typing.type_check_only
class Bookshelves(typing.TypedDict, total=False):
    items: _list[Bookshelf]
    kind: str

@typing.type_check_only
class Category(typing.TypedDict, total=False):
    items: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class ConcurrentAccessRestriction(typing.TypedDict, total=False):
    deviceAllowed: bool
    kind: str
    maxConcurrentDevices: int
    message: str
    nonce: str
    reasonCode: str
    restricted: bool
    signature: str
    source: str
    timeWindowSeconds: int
    volumeId: str

@typing.type_check_only
class DictionaryAnnotationdata(typing.TypedDict, total=False):
    annotationType: str
    data: Dictlayerdata
    encodedData: str
    id: str
    kind: str
    layerId: str
    selfLink: str
    updated: str
    volumeId: str

@typing.type_check_only
class Dictlayerdata(typing.TypedDict, total=False):
    common: dict[str, typing.Any]
    dict: dict[str, typing.Any]
    kind: str

@typing.type_check_only
class Discoveryclusters(typing.TypedDict, total=False):
    clusters: _list[dict[str, typing.Any]]
    kind: str
    totalClusters: int

@typing.type_check_only
class DownloadAccessRestriction(typing.TypedDict, total=False):
    deviceAllowed: bool
    downloadsAcquired: int
    justAcquired: bool
    kind: str
    maxDownloadDevices: int
    message: str
    nonce: str
    reasonCode: str
    restricted: bool
    signature: str
    source: str
    volumeId: str

@typing.type_check_only
class DownloadAccesses(typing.TypedDict, total=False):
    downloadAccessList: _list[DownloadAccessRestriction]
    kind: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FamilyInfo(typing.TypedDict, total=False):
    kind: str
    membership: dict[str, typing.Any]

@typing.type_check_only
class GeoAnnotationdata(typing.TypedDict, total=False):
    annotationType: str
    data: Geolayerdata
    encodedData: str
    id: str
    kind: str
    layerId: str
    selfLink: str
    updated: str
    volumeId: str

@typing.type_check_only
class Geolayerdata(typing.TypedDict, total=False):
    common: dict[str, typing.Any]
    geo: dict[str, typing.Any]
    kind: str

@typing.type_check_only
class Layersummaries(typing.TypedDict, total=False):
    items: _list[Layersummary]
    kind: str
    totalItems: int

@typing.type_check_only
class Layersummary(typing.TypedDict, total=False):
    annotationCount: int
    annotationTypes: _list[str]
    annotationsDataLink: str
    annotationsLink: str
    contentVersion: str
    dataCount: int
    id: str
    kind: str
    layerId: str
    selfLink: str
    updated: str
    volumeAnnotationsVersion: str
    volumeId: str

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    items: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class Notification(typing.TypedDict, total=False):
    body: str
    crmExperimentIds: _list[str]
    doc_id: str
    doc_type: str
    dont_show_notification: bool
    iconUrl: str
    is_document_mature: bool
    kind: str
    notificationGroup: str
    notification_type: str
    pcampaign_id: str
    reason: str
    show_notification_settings_action: bool
    targetUrl: str
    timeToExpireMs: str
    title: str

@typing.type_check_only
class Offers(typing.TypedDict, total=False):
    items: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class ReadingPosition(typing.TypedDict, total=False):
    epubCfiPosition: str
    gbImagePosition: str
    gbTextPosition: str
    kind: str
    pdfPosition: str
    updated: str
    volumeId: str

@typing.type_check_only
class RequestAccessData(typing.TypedDict, total=False):
    concurrentAccess: ConcurrentAccessRestriction
    downloadAccess: DownloadAccessRestriction
    kind: str

@typing.type_check_only
class Review(typing.TypedDict, total=False):
    author: dict[str, typing.Any]
    content: str
    date: str
    fullTextUrl: str
    kind: str
    rating: str
    source: dict[str, typing.Any]
    title: str
    type: str
    volumeId: str

@typing.type_check_only
class Series(typing.TypedDict, total=False):
    kind: str
    series: _list[dict[str, typing.Any]]

@typing.type_check_only
class Seriesmembership(typing.TypedDict, total=False):
    kind: str
    member: _list[Volume]
    nextPageToken: str

@typing.type_check_only
class Usersettings(typing.TypedDict, total=False):
    kind: str
    notesExport: dict[str, typing.Any]
    notification: dict[str, typing.Any]

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    accessInfo: dict[str, typing.Any]
    etag: str
    id: str
    kind: str
    layerInfo: dict[str, typing.Any]
    recommendedInfo: dict[str, typing.Any]
    saleInfo: dict[str, typing.Any]
    searchInfo: dict[str, typing.Any]
    selfLink: str
    userInfo: dict[str, typing.Any]
    volumeInfo: dict[str, typing.Any]

@typing.type_check_only
class Volume2(typing.TypedDict, total=False):
    items: _list[Volume]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Volumeannotation(typing.TypedDict, total=False):
    annotationDataId: str
    annotationDataLink: str
    annotationType: str
    contentRanges: dict[str, typing.Any]
    data: str
    deleted: bool
    id: str
    kind: str
    layerId: str
    pageIds: _list[str]
    selectedText: str
    selfLink: str
    updated: str
    volumeId: str

@typing.type_check_only
class Volumeannotations(typing.TypedDict, total=False):
    items: _list[Volumeannotation]
    kind: str
    nextPageToken: str
    totalItems: int
    version: str

@typing.type_check_only
class Volumes(typing.TypedDict, total=False):
    items: _list[Volume]
    kind: str
    totalItems: int

@typing.type_check_only
class Volumeseriesinfo(typing.TypedDict, total=False):
    bookDisplayNumber: str
    kind: str
    shortSeriesBookTitle: str
    volumeSeries: _list[dict[str, typing.Any]]
