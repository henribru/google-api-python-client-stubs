import typing

import typing_extensions

class BooksVolumesRecommendedRateResponse(typing_extensions.TypedDict, total=False):
    consistency_token: str

class FamilyInfo(typing_extensions.TypedDict, total=False):
    membership: typing.Dict[str, typing.Any]
    kind: str

class BooksAnnotationsRange(typing_extensions.TypedDict, total=False):
    endPosition: str
    startOffset: str
    endOffset: str
    startPosition: str

class GeoAnnotationdata(typing_extensions.TypedDict, total=False):
    data: Geolayerdata
    id: str
    annotationType: str
    volumeId: str
    encodedData: str
    kind: str
    layerId: str
    updated: str
    selfLink: str

class Seriesmembership(typing_extensions.TypedDict, total=False):
    kind: str
    member: typing.List[Volume]
    nextPageToken: str

class Volumes(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[Volume]
    totalItems: int

class Review(typing_extensions.TypedDict, total=False):
    author: typing.Dict[str, typing.Any]
    type: str
    source: typing.Dict[str, typing.Any]
    kind: str
    title: str
    content: str
    fullTextUrl: str
    date: str
    rating: str
    volumeId: str

class Volume2(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[Volume]
    kind: str

class Usersettings(typing_extensions.TypedDict, total=False):
    notification: typing.Dict[str, typing.Any]
    kind: str
    notesExport: typing.Dict[str, typing.Any]

class Volumeannotations(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    version: str
    kind: str
    totalItems: int
    items: typing.List[Volumeannotation]

class Volume(typing_extensions.TypedDict, total=False):
    saleInfo: typing.Dict[str, typing.Any]
    recommendedInfo: typing.Dict[str, typing.Any]
    searchInfo: typing.Dict[str, typing.Any]
    selfLink: str
    id: str
    accessInfo: typing.Dict[str, typing.Any]
    userInfo: typing.Dict[str, typing.Any]
    volumeInfo: typing.Dict[str, typing.Any]
    layerInfo: typing.Dict[str, typing.Any]
    kind: str
    etag: str

class BooksCloudloadingResource(typing_extensions.TypedDict, total=False):
    author: str
    processingState: str
    title: str
    volumeId: str

class Annotationsdata(typing_extensions.TypedDict, total=False):
    items: typing.List[GeoAnnotationdata]
    kind: str
    nextPageToken: str
    totalItems: int

class Dictlayerdata(typing_extensions.TypedDict, total=False):
    dict: typing.Dict[str, typing.Any]
    common: typing.Dict[str, typing.Any]
    kind: str

class Discoveryclusters(typing_extensions.TypedDict, total=False):
    totalClusters: int
    kind: str
    clusters: typing.List[typing.Dict[str, typing.Any]]

class Bookshelves(typing_extensions.TypedDict, total=False):
    items: typing.List[Bookshelf]
    kind: str

class Series(typing_extensions.TypedDict, total=False):
    series: typing.List[typing.Dict[str, typing.Any]]
    kind: str

class DownloadAccessRestriction(typing_extensions.TypedDict, total=False):
    kind: str
    restricted: bool
    deviceAllowed: bool
    downloadsAcquired: int
    reasonCode: str
    source: str
    justAcquired: bool
    nonce: str
    message: str
    volumeId: str
    signature: str
    maxDownloadDevices: int

class AnnotationsSummary(typing_extensions.TypedDict, total=False):
    kind: str
    layers: typing.List[typing.Dict[str, typing.Any]]

class Geolayerdata(typing_extensions.TypedDict, total=False):
    kind: str
    common: typing.Dict[str, typing.Any]
    geo: typing.Dict[str, typing.Any]

class RequestAccessData(typing_extensions.TypedDict, total=False):
    downloadAccess: DownloadAccessRestriction
    concurrentAccess: ConcurrentAccessRestriction
    kind: str

class Notification(typing_extensions.TypedDict, total=False):
    doc_type: str
    notificationGroup: str
    body: str
    pcampaign_id: str
    targetUrl: str
    show_notification_settings_action: bool
    kind: str
    doc_id: str
    timeToExpireMs: str
    dont_show_notification: bool
    crmExperimentIds: typing.List[str]
    reason: str
    iconUrl: str
    title: str
    is_document_mature: bool
    notification_type: str

class Offers(typing_extensions.TypedDict, total=False):
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Metadata(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[typing.Dict[str, typing.Any]]

class Annotation(typing_extensions.TypedDict, total=False):
    data: str
    created: str
    updated: str
    volumeId: str
    kind: str
    beforeSelectedText: str
    pageIds: typing.List[str]
    afterSelectedText: str
    currentVersionRanges: typing.Dict[str, typing.Any]
    clientVersionRanges: typing.Dict[str, typing.Any]
    selectedText: str
    selfLink: str
    deleted: bool
    layerSummary: typing.Dict[str, typing.Any]
    highlightStyle: str
    layerId: str
    id: str

class ReadingPosition(typing_extensions.TypedDict, total=False):
    pdfPosition: str
    kind: str
    gbTextPosition: str
    volumeId: str
    gbImagePosition: str
    epubCfiPosition: str
    updated: str

class Layersummary(typing_extensions.TypedDict, total=False):
    annotationCount: int
    id: str
    volumeId: str
    kind: str
    volumeAnnotationsVersion: str
    annotationsLink: str
    layerId: str
    annotationTypes: typing.List[str]
    dataCount: int
    updated: str
    selfLink: str
    annotationsDataLink: str
    contentVersion: str

class Bookshelf(typing_extensions.TypedDict, total=False):
    kind: str
    volumesLastUpdated: str
    updated: str
    selfLink: str
    title: str
    id: int
    created: str
    access: str
    volumeCount: int
    description: str

class ConcurrentAccessRestriction(typing_extensions.TypedDict, total=False):
    nonce: str
    timeWindowSeconds: int
    volumeId: str
    reasonCode: str
    signature: str
    restricted: bool
    message: str
    kind: str
    source: str
    maxConcurrentDevices: int
    deviceAllowed: bool

class DictionaryAnnotationdata(typing_extensions.TypedDict, total=False):
    kind: str
    layerId: str
    volumeId: str
    id: str
    data: Dictlayerdata
    selfLink: str
    updated: str
    encodedData: str
    annotationType: str

class Volumeannotation(typing_extensions.TypedDict, total=False):
    data: str
    annotationType: str
    kind: str
    deleted: bool
    pageIds: typing.List[str]
    id: str
    annotationDataLink: str
    annotationDataId: str
    selfLink: str
    volumeId: str
    contentRanges: typing.Dict[str, typing.Any]
    selectedText: str
    updated: str
    layerId: str

class Annotations(typing_extensions.TypedDict, total=False):
    items: typing.List[Annotation]
    nextPageToken: str
    totalItems: int
    kind: str

class Volumeseriesinfo(typing_extensions.TypedDict, total=False):
    volumeSeries: typing.List[typing.Dict[str, typing.Any]]
    bookDisplayNumber: str
    kind: str
    shortSeriesBookTitle: str

class DownloadAccesses(typing_extensions.TypedDict, total=False):
    downloadAccessList: typing.List[DownloadAccessRestriction]
    kind: str

class Category(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[typing.Dict[str, typing.Any]]

class Layersummaries(typing_extensions.TypedDict, total=False):
    items: typing.List[Layersummary]
    totalItems: int
    kind: str
