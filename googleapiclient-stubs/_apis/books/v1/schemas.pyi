import typing

import typing_extensions
@typing.type_check_only
class Annotation(typing_extensions.TypedDict, total=False):
    afterSelectedText: str
    beforeSelectedText: str
    clientVersionRanges: typing.Dict[str, typing.Any]
    created: str
    currentVersionRanges: typing.Dict[str, typing.Any]
    data: str
    deleted: bool
    highlightStyle: str
    id: str
    kind: str
    layerId: str
    layerSummary: typing.Dict[str, typing.Any]
    pageIds: typing.List[str]
    selectedText: str
    selfLink: str
    updated: str
    volumeId: str

@typing.type_check_only
class Annotations(typing_extensions.TypedDict, total=False):
    items: typing.List[Annotation]
    kind: str
    nextPageToken: str
    totalItems: int

@typing.type_check_only
class AnnotationsSummary(typing_extensions.TypedDict, total=False):
    kind: str
    layers: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class Annotationsdata(typing_extensions.TypedDict, total=False):
    items: typing.List[GeoAnnotationdata]
    kind: str
    nextPageToken: str
    totalItems: int

@typing.type_check_only
class BooksAnnotationsRange(typing_extensions.TypedDict, total=False):
    endOffset: str
    endPosition: str
    startOffset: str
    startPosition: str

@typing.type_check_only
class BooksCloudloadingResource(typing_extensions.TypedDict, total=False):
    author: str
    processingState: str
    title: str
    volumeId: str

@typing.type_check_only
class BooksVolumesRecommendedRateResponse(typing_extensions.TypedDict, total=False):
    consistency_token: str

@typing.type_check_only
class Bookshelf(typing_extensions.TypedDict, total=False):
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
class Bookshelves(typing_extensions.TypedDict, total=False):
    items: typing.List[Bookshelf]
    kind: str

@typing.type_check_only
class Category(typing_extensions.TypedDict, total=False):
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class ConcurrentAccessRestriction(typing_extensions.TypedDict, total=False):
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
class DictionaryAnnotationdata(typing_extensions.TypedDict, total=False):
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
class Dictlayerdata(typing_extensions.TypedDict, total=False):
    common: typing.Dict[str, typing.Any]
    dict: typing.Dict[str, typing.Any]
    kind: str

@typing.type_check_only
class Discoveryclusters(typing_extensions.TypedDict, total=False):
    clusters: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    totalClusters: int

@typing.type_check_only
class DownloadAccessRestriction(typing_extensions.TypedDict, total=False):
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
class DownloadAccesses(typing_extensions.TypedDict, total=False):
    downloadAccessList: typing.List[DownloadAccessRestriction]
    kind: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FamilyInfo(typing_extensions.TypedDict, total=False):
    kind: str
    membership: typing.Dict[str, typing.Any]

@typing.type_check_only
class GeoAnnotationdata(typing_extensions.TypedDict, total=False):
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
class Geolayerdata(typing_extensions.TypedDict, total=False):
    common: typing.Dict[str, typing.Any]
    geo: typing.Dict[str, typing.Any]
    kind: str

@typing.type_check_only
class Layersummaries(typing_extensions.TypedDict, total=False):
    items: typing.List[Layersummary]
    kind: str
    totalItems: int

@typing.type_check_only
class Layersummary(typing_extensions.TypedDict, total=False):
    annotationCount: int
    annotationTypes: typing.List[str]
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
class Metadata(typing_extensions.TypedDict, total=False):
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    body: str
    crmExperimentIds: typing.List[str]
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
class Offers(typing_extensions.TypedDict, total=False):
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class ReadingPosition(typing_extensions.TypedDict, total=False):
    epubCfiPosition: str
    gbImagePosition: str
    gbTextPosition: str
    kind: str
    pdfPosition: str
    updated: str
    volumeId: str

@typing.type_check_only
class RequestAccessData(typing_extensions.TypedDict, total=False):
    concurrentAccess: ConcurrentAccessRestriction
    downloadAccess: DownloadAccessRestriction
    kind: str

@typing.type_check_only
class Review(typing_extensions.TypedDict, total=False):
    author: typing.Dict[str, typing.Any]
    content: str
    date: str
    fullTextUrl: str
    kind: str
    rating: str
    source: typing.Dict[str, typing.Any]
    title: str
    type: str
    volumeId: str

@typing.type_check_only
class Series(typing_extensions.TypedDict, total=False):
    kind: str
    series: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class Seriesmembership(typing_extensions.TypedDict, total=False):
    kind: str
    member: typing.List[Volume]
    nextPageToken: str

@typing.type_check_only
class Usersettings(typing_extensions.TypedDict, total=False):
    kind: str
    notesExport: typing.Dict[str, typing.Any]
    notification: typing.Dict[str, typing.Any]

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    accessInfo: typing.Dict[str, typing.Any]
    etag: str
    id: str
    kind: str
    layerInfo: typing.Dict[str, typing.Any]
    recommendedInfo: typing.Dict[str, typing.Any]
    saleInfo: typing.Dict[str, typing.Any]
    searchInfo: typing.Dict[str, typing.Any]
    selfLink: str
    userInfo: typing.Dict[str, typing.Any]
    volumeInfo: typing.Dict[str, typing.Any]

@typing.type_check_only
class Volume2(typing_extensions.TypedDict, total=False):
    items: typing.List[Volume]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Volumeannotation(typing_extensions.TypedDict, total=False):
    annotationDataId: str
    annotationDataLink: str
    annotationType: str
    contentRanges: typing.Dict[str, typing.Any]
    data: str
    deleted: bool
    id: str
    kind: str
    layerId: str
    pageIds: typing.List[str]
    selectedText: str
    selfLink: str
    updated: str
    volumeId: str

@typing.type_check_only
class Volumeannotations(typing_extensions.TypedDict, total=False):
    items: typing.List[Volumeannotation]
    kind: str
    nextPageToken: str
    totalItems: int
    version: str

@typing.type_check_only
class Volumes(typing_extensions.TypedDict, total=False):
    items: typing.List[Volume]
    kind: str
    totalItems: int

@typing.type_check_only
class Volumeseriesinfo(typing_extensions.TypedDict, total=False):
    bookDisplayNumber: str
    kind: str
    shortSeriesBookTitle: str
    volumeSeries: typing.List[typing.Dict[str, typing.Any]]
