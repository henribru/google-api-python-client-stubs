import typing

import typing_extensions

_list = list

@typing.type_check_only
class AnnotateFileResponse(typing_extensions.TypedDict, total=False):
    error: Status
    inputConfig: InputConfig
    responses: _list[AnnotateImageResponse]
    totalPages: int

@typing.type_check_only
class AnnotateImageResponse(typing_extensions.TypedDict, total=False):
    context: ImageAnnotationContext
    cropHintsAnnotation: CropHintsAnnotation
    error: Status
    faceAnnotations: _list[FaceAnnotation]
    fullTextAnnotation: TextAnnotation
    imagePropertiesAnnotation: ImageProperties
    labelAnnotations: _list[EntityAnnotation]
    landmarkAnnotations: _list[EntityAnnotation]
    localizedObjectAnnotations: _list[LocalizedObjectAnnotation]
    logoAnnotations: _list[EntityAnnotation]
    productSearchResults: ProductSearchResults
    safeSearchAnnotation: SafeSearchAnnotation
    textAnnotations: _list[EntityAnnotation]
    webDetection: WebDetection

@typing.type_check_only
class AsyncAnnotateFileResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

@typing.type_check_only
class AsyncBatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: _list[AsyncAnnotateFileResponse]

@typing.type_check_only
class AsyncBatchAnnotateImagesResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

@typing.type_check_only
class BatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: _list[AnnotateFileResponse]

@typing.type_check_only
class BatchOperationMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    submitTime: str

@typing.type_check_only
class Block(typing_extensions.TypedDict, total=False):
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: BoundingPoly
    confidence: float
    paragraphs: _list[Paragraph]
    property: TextProperty

@typing.type_check_only
class BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: _list[NormalizedVertex]
    vertices: _list[Vertex]

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    pixelFraction: float
    score: float

@typing.type_check_only
class CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: BoundingPoly
    confidence: float
    importanceFraction: float

@typing.type_check_only
class CropHintsAnnotation(typing_extensions.TypedDict, total=False):
    cropHints: _list[CropHint]

@typing.type_check_only
class DetectedBreak(typing_extensions.TypedDict, total=False):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

@typing.type_check_only
class DetectedLanguage(typing_extensions.TypedDict, total=False):
    confidence: float
    languageCode: str

@typing.type_check_only
class DominantColorsAnnotation(typing_extensions.TypedDict, total=False):
    colors: _list[ColorInfo]

@typing.type_check_only
class EntityAnnotation(typing_extensions.TypedDict, total=False):
    boundingPoly: BoundingPoly
    confidence: float
    description: str
    locale: str
    locations: _list[LocationInfo]
    mid: str
    properties: _list[Property]
    score: float
    topicality: float

@typing.type_check_only
class FaceAnnotation(typing_extensions.TypedDict, total=False):
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: BoundingPoly
    detectionConfidence: float
    fdBoundingPoly: BoundingPoly
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    landmarks: _list[Landmark]
    panAngle: float
    rollAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AnnotateFileRequest(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudVisionV1p1beta1Feature]
    imageContext: GoogleCloudVisionV1p1beta1ImageContext
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig
    pages: _list[int]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig
    responses: _list[GoogleCloudVisionV1p1beta1AnnotateImageResponse]
    totalPages: int

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AnnotateImageRequest(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudVisionV1p1beta1Feature]
    image: GoogleCloudVisionV1p1beta1Image
    imageContext: GoogleCloudVisionV1p1beta1ImageContext

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudVisionV1p1beta1ImageAnnotationContext
    cropHintsAnnotation: GoogleCloudVisionV1p1beta1CropHintsAnnotation
    error: Status
    faceAnnotations: _list[GoogleCloudVisionV1p1beta1FaceAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p1beta1TextAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p1beta1ImageProperties
    labelAnnotations: _list[GoogleCloudVisionV1p1beta1EntityAnnotation]
    landmarkAnnotations: _list[GoogleCloudVisionV1p1beta1EntityAnnotation]
    localizedObjectAnnotations: _list[
        GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation
    ]
    logoAnnotations: _list[GoogleCloudVisionV1p1beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p1beta1ProductSearchResults
    safeSearchAnnotation: GoogleCloudVisionV1p1beta1SafeSearchAnnotation
    textAnnotations: _list[GoogleCloudVisionV1p1beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p1beta1WebDetection

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AsyncAnnotateFileRequest(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudVisionV1p1beta1Feature]
    imageContext: GoogleCloudVisionV1p1beta1ImageContext
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    requests: _list[GoogleCloudVisionV1p1beta1AsyncAnnotateFileRequest]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateImagesRequest(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig
    parent: str
    requests: _list[GoogleCloudVisionV1p1beta1AnnotateImageRequest]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1BatchAnnotateFilesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    requests: _list[GoogleCloudVisionV1p1beta1AnnotateFileRequest]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1BatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudVisionV1p1beta1AnnotateFileResponse]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1BatchAnnotateImagesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    requests: _list[GoogleCloudVisionV1p1beta1AnnotateImageRequest]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1BatchAnnotateImagesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudVisionV1p1beta1AnnotateImageResponse]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Block(typing_extensions.TypedDict, total=False):
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    confidence: float
    paragraphs: _list[GoogleCloudVisionV1p1beta1Paragraph]
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty

@typing.type_check_only
class GoogleCloudVisionV1p1beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudVisionV1p1beta1NormalizedVertex]
    vertices: _list[GoogleCloudVisionV1p1beta1Vertex]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    pixelFraction: float
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    confidence: float
    importanceFraction: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: _list[GoogleCloudVisionV1p1beta1CropHint]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1CropHintsParams(
    typing_extensions.TypedDict, total=False
):
    aspectRatios: _list[float]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: _list[GoogleCloudVisionV1p1beta1ColorInfo]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    confidence: float
    description: str
    locale: str
    locations: _list[GoogleCloudVisionV1p1beta1LocationInfo]
    mid: str
    properties: _list[GoogleCloudVisionV1p1beta1Property]
    score: float
    topicality: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    detectionConfidence: float
    fdBoundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    landmarks: _list[GoogleCloudVisionV1p1beta1FaceAnnotationLandmark]
    panAngle: float
    rollAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1FaceAnnotationLandmark(
    typing_extensions.TypedDict, total=False
):
    position: GoogleCloudVisionV1p1beta1Position
    type: typing_extensions.Literal[
        "UNKNOWN_LANDMARK",
        "LEFT_EYE",
        "RIGHT_EYE",
        "LEFT_OF_LEFT_EYEBROW",
        "RIGHT_OF_LEFT_EYEBROW",
        "LEFT_OF_RIGHT_EYEBROW",
        "RIGHT_OF_RIGHT_EYEBROW",
        "MIDPOINT_BETWEEN_EYES",
        "NOSE_TIP",
        "UPPER_LIP",
        "LOWER_LIP",
        "MOUTH_LEFT",
        "MOUTH_RIGHT",
        "MOUTH_CENTER",
        "NOSE_BOTTOM_RIGHT",
        "NOSE_BOTTOM_LEFT",
        "NOSE_BOTTOM_CENTER",
        "LEFT_EYE_TOP_BOUNDARY",
        "LEFT_EYE_RIGHT_CORNER",
        "LEFT_EYE_BOTTOM_BOUNDARY",
        "LEFT_EYE_LEFT_CORNER",
        "RIGHT_EYE_TOP_BOUNDARY",
        "RIGHT_EYE_RIGHT_CORNER",
        "RIGHT_EYE_BOTTOM_BOUNDARY",
        "RIGHT_EYE_LEFT_CORNER",
        "LEFT_EYEBROW_UPPER_MIDPOINT",
        "RIGHT_EYEBROW_UPPER_MIDPOINT",
        "LEFT_EAR_TRAGION",
        "RIGHT_EAR_TRAGION",
        "LEFT_EYE_PUPIL",
        "RIGHT_EYE_PUPIL",
        "FOREHEAD_GLABELLA",
        "CHIN_GNATHION",
        "CHIN_LEFT_GONION",
        "CHIN_RIGHT_GONION",
        "LEFT_CHEEK_CENTER",
        "RIGHT_CHEEK_CENTER",
    ]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Feature(typing_extensions.TypedDict, total=False):
    maxResults: int
    model: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "FACE_DETECTION",
        "LANDMARK_DETECTION",
        "LOGO_DETECTION",
        "LABEL_DETECTION",
        "TEXT_DETECTION",
        "DOCUMENT_TEXT_DETECTION",
        "SAFE_SEARCH_DETECTION",
        "IMAGE_PROPERTIES",
        "CROP_HINTS",
        "WEB_DETECTION",
        "PRODUCT_SEARCH",
        "OBJECT_LOCALIZATION",
    ]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Image(typing_extensions.TypedDict, total=False):
    content: str
    source: GoogleCloudVisionV1p1beta1ImageSource

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ImageContext(typing_extensions.TypedDict, total=False):
    cropHintsParams: GoogleCloudVisionV1p1beta1CropHintsParams
    languageHints: _list[str]
    latLongRect: GoogleCloudVisionV1p1beta1LatLongRect
    productSearchParams: GoogleCloudVisionV1p1beta1ProductSearchParams
    textDetectionParams: GoogleCloudVisionV1p1beta1TextDetectionParams
    webDetectionParams: GoogleCloudVisionV1p1beta1WebDetectionParams

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p1beta1DominantColorsAnnotation

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ImageSource(typing_extensions.TypedDict, total=False):
    gcsImageUri: str
    imageUri: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GoogleCloudVisionV1p1beta1GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1LatLongRect(typing_extensions.TypedDict, total=False):
    maxLatLng: LatLng
    minLatLng: LatLng

@typing.type_check_only
class GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

@typing.type_check_only
class GoogleCloudVisionV1p1beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p1beta1GcsDestination

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Page(typing_extensions.TypedDict, total=False):
    blocks: _list[GoogleCloudVisionV1p1beta1Block]
    confidence: float
    height: int
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    width: int

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Paragraph(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    words: _list[GoogleCloudVisionV1p1beta1Word]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Product(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    productCategory: str
    productLabels: _list[GoogleCloudVisionV1p1beta1ProductKeyValue]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ProductSearchParams(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    filter: str
    productCategories: _list[str]
    productSet: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    indexTime: str
    productGroupedResults: _list[
        GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult
    ]
    results: _list[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    objectAnnotations: _list[
        GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation
    ]
    results: _list[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    product: GoogleCloudVisionV1p1beta1Product
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: _list[GoogleCloudVisionV1p1beta1Page]
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak
    detectedLanguages: _list[GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1TextDetectionParams(
    typing_extensions.TypedDict, total=False
):
    advancedOcrOptions: _list[str]
    enableTextDetectionConfidenceScore: bool

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudVisionV1p1beta1WebDetection(typing_extensions.TypedDict, total=False):
    bestGuessLabels: _list[GoogleCloudVisionV1p1beta1WebDetectionWebLabel]
    fullMatchingImages: _list[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    pagesWithMatchingImages: _list[GoogleCloudVisionV1p1beta1WebDetectionWebPage]
    partialMatchingImages: _list[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    visuallySimilarImages: _list[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    webEntities: _list[GoogleCloudVisionV1p1beta1WebDetectionWebEntity]

@typing.type_check_only
class GoogleCloudVisionV1p1beta1WebDetectionParams(
    typing_extensions.TypedDict, total=False
):
    includeGeoResults: bool

@typing.type_check_only
class GoogleCloudVisionV1p1beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p1beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    fullMatchingImages: _list[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    pageTitle: str
    partialMatchingImages: _list[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p1beta1Word(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    symbols: _list[GoogleCloudVisionV1p1beta1Symbol]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    inputConfig: GoogleCloudVisionV1p2beta1InputConfig
    responses: _list[GoogleCloudVisionV1p2beta1AnnotateImageResponse]
    totalPages: int

@typing.type_check_only
class GoogleCloudVisionV1p2beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudVisionV1p2beta1ImageAnnotationContext
    cropHintsAnnotation: GoogleCloudVisionV1p2beta1CropHintsAnnotation
    error: Status
    faceAnnotations: _list[GoogleCloudVisionV1p2beta1FaceAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p2beta1TextAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p2beta1ImageProperties
    labelAnnotations: _list[GoogleCloudVisionV1p2beta1EntityAnnotation]
    landmarkAnnotations: _list[GoogleCloudVisionV1p2beta1EntityAnnotation]
    localizedObjectAnnotations: _list[
        GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation
    ]
    logoAnnotations: _list[GoogleCloudVisionV1p2beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p2beta1ProductSearchResults
    safeSearchAnnotation: GoogleCloudVisionV1p2beta1SafeSearchAnnotation
    textAnnotations: _list[GoogleCloudVisionV1p2beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p2beta1WebDetection

@typing.type_check_only
class GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p2beta1OutputConfig

@typing.type_check_only
class GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Block(typing_extensions.TypedDict, total=False):
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    paragraphs: _list[GoogleCloudVisionV1p2beta1Paragraph]
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty

@typing.type_check_only
class GoogleCloudVisionV1p2beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudVisionV1p2beta1NormalizedVertex]
    vertices: _list[GoogleCloudVisionV1p2beta1Vertex]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    pixelFraction: float
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    importanceFraction: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: _list[GoogleCloudVisionV1p2beta1CropHint]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: _list[GoogleCloudVisionV1p2beta1ColorInfo]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    description: str
    locale: str
    locations: _list[GoogleCloudVisionV1p2beta1LocationInfo]
    mid: str
    properties: _list[GoogleCloudVisionV1p2beta1Property]
    score: float
    topicality: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    detectionConfidence: float
    fdBoundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    landmarks: _list[GoogleCloudVisionV1p2beta1FaceAnnotationLandmark]
    panAngle: float
    rollAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1FaceAnnotationLandmark(
    typing_extensions.TypedDict, total=False
):
    position: GoogleCloudVisionV1p2beta1Position
    type: typing_extensions.Literal[
        "UNKNOWN_LANDMARK",
        "LEFT_EYE",
        "RIGHT_EYE",
        "LEFT_OF_LEFT_EYEBROW",
        "RIGHT_OF_LEFT_EYEBROW",
        "LEFT_OF_RIGHT_EYEBROW",
        "RIGHT_OF_RIGHT_EYEBROW",
        "MIDPOINT_BETWEEN_EYES",
        "NOSE_TIP",
        "UPPER_LIP",
        "LOWER_LIP",
        "MOUTH_LEFT",
        "MOUTH_RIGHT",
        "MOUTH_CENTER",
        "NOSE_BOTTOM_RIGHT",
        "NOSE_BOTTOM_LEFT",
        "NOSE_BOTTOM_CENTER",
        "LEFT_EYE_TOP_BOUNDARY",
        "LEFT_EYE_RIGHT_CORNER",
        "LEFT_EYE_BOTTOM_BOUNDARY",
        "LEFT_EYE_LEFT_CORNER",
        "RIGHT_EYE_TOP_BOUNDARY",
        "RIGHT_EYE_RIGHT_CORNER",
        "RIGHT_EYE_BOTTOM_BOUNDARY",
        "RIGHT_EYE_LEFT_CORNER",
        "LEFT_EYEBROW_UPPER_MIDPOINT",
        "RIGHT_EYEBROW_UPPER_MIDPOINT",
        "LEFT_EAR_TRAGION",
        "RIGHT_EAR_TRAGION",
        "LEFT_EYE_PUPIL",
        "RIGHT_EYE_PUPIL",
        "FOREHEAD_GLABELLA",
        "CHIN_GNATHION",
        "CHIN_LEFT_GONION",
        "CHIN_RIGHT_GONION",
        "LEFT_CHEEK_CENTER",
        "RIGHT_CHEEK_CENTER",
    ]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p2beta1DominantColorsAnnotation

@typing.type_check_only
class GoogleCloudVisionV1p2beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GoogleCloudVisionV1p2beta1GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

@typing.type_check_only
class GoogleCloudVisionV1p2beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p2beta1GcsDestination

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Page(typing_extensions.TypedDict, total=False):
    blocks: _list[GoogleCloudVisionV1p2beta1Block]
    confidence: float
    height: int
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    width: int

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Paragraph(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    words: _list[GoogleCloudVisionV1p2beta1Word]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Product(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    productCategory: str
    productLabels: _list[GoogleCloudVisionV1p2beta1ProductKeyValue]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    indexTime: str
    productGroupedResults: _list[
        GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult
    ]
    results: _list[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    objectAnnotations: _list[
        GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation
    ]
    results: _list[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    product: GoogleCloudVisionV1p2beta1Product
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: _list[GoogleCloudVisionV1p2beta1Page]
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak
    detectedLanguages: _list[GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudVisionV1p2beta1WebDetection(typing_extensions.TypedDict, total=False):
    bestGuessLabels: _list[GoogleCloudVisionV1p2beta1WebDetectionWebLabel]
    fullMatchingImages: _list[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    pagesWithMatchingImages: _list[GoogleCloudVisionV1p2beta1WebDetectionWebPage]
    partialMatchingImages: _list[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    visuallySimilarImages: _list[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    webEntities: _list[GoogleCloudVisionV1p2beta1WebDetectionWebEntity]

@typing.type_check_only
class GoogleCloudVisionV1p2beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p2beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    fullMatchingImages: _list[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    pageTitle: str
    partialMatchingImages: _list[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p2beta1Word(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    symbols: _list[GoogleCloudVisionV1p2beta1Symbol]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    inputConfig: GoogleCloudVisionV1p3beta1InputConfig
    responses: _list[GoogleCloudVisionV1p3beta1AnnotateImageResponse]
    totalPages: int

@typing.type_check_only
class GoogleCloudVisionV1p3beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudVisionV1p3beta1ImageAnnotationContext
    cropHintsAnnotation: GoogleCloudVisionV1p3beta1CropHintsAnnotation
    error: Status
    faceAnnotations: _list[GoogleCloudVisionV1p3beta1FaceAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p3beta1TextAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p3beta1ImageProperties
    labelAnnotations: _list[GoogleCloudVisionV1p3beta1EntityAnnotation]
    landmarkAnnotations: _list[GoogleCloudVisionV1p3beta1EntityAnnotation]
    localizedObjectAnnotations: _list[
        GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation
    ]
    logoAnnotations: _list[GoogleCloudVisionV1p3beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p3beta1ProductSearchResults
    safeSearchAnnotation: GoogleCloudVisionV1p3beta1SafeSearchAnnotation
    textAnnotations: _list[GoogleCloudVisionV1p3beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p3beta1WebDetection

@typing.type_check_only
class GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p3beta1OutputConfig

@typing.type_check_only
class GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    submitTime: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Block(typing_extensions.TypedDict, total=False):
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    paragraphs: _list[GoogleCloudVisionV1p3beta1Paragraph]
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty

@typing.type_check_only
class GoogleCloudVisionV1p3beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudVisionV1p3beta1NormalizedVertex]
    vertices: _list[GoogleCloudVisionV1p3beta1Vertex]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    pixelFraction: float
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    importanceFraction: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: _list[GoogleCloudVisionV1p3beta1CropHint]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: _list[GoogleCloudVisionV1p3beta1ColorInfo]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    description: str
    locale: str
    locations: _list[GoogleCloudVisionV1p3beta1LocationInfo]
    mid: str
    properties: _list[GoogleCloudVisionV1p3beta1Property]
    score: float
    topicality: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    detectionConfidence: float
    fdBoundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    landmarks: _list[GoogleCloudVisionV1p3beta1FaceAnnotationLandmark]
    panAngle: float
    rollAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1FaceAnnotationLandmark(
    typing_extensions.TypedDict, total=False
):
    position: GoogleCloudVisionV1p3beta1Position
    type: typing_extensions.Literal[
        "UNKNOWN_LANDMARK",
        "LEFT_EYE",
        "RIGHT_EYE",
        "LEFT_OF_LEFT_EYEBROW",
        "RIGHT_OF_LEFT_EYEBROW",
        "LEFT_OF_RIGHT_EYEBROW",
        "RIGHT_OF_RIGHT_EYEBROW",
        "MIDPOINT_BETWEEN_EYES",
        "NOSE_TIP",
        "UPPER_LIP",
        "LOWER_LIP",
        "MOUTH_LEFT",
        "MOUTH_RIGHT",
        "MOUTH_CENTER",
        "NOSE_BOTTOM_RIGHT",
        "NOSE_BOTTOM_LEFT",
        "NOSE_BOTTOM_CENTER",
        "LEFT_EYE_TOP_BOUNDARY",
        "LEFT_EYE_RIGHT_CORNER",
        "LEFT_EYE_BOTTOM_BOUNDARY",
        "LEFT_EYE_LEFT_CORNER",
        "RIGHT_EYE_TOP_BOUNDARY",
        "RIGHT_EYE_RIGHT_CORNER",
        "RIGHT_EYE_BOTTOM_BOUNDARY",
        "RIGHT_EYE_LEFT_CORNER",
        "LEFT_EYEBROW_UPPER_MIDPOINT",
        "RIGHT_EYEBROW_UPPER_MIDPOINT",
        "LEFT_EAR_TRAGION",
        "RIGHT_EAR_TRAGION",
        "LEFT_EYE_PUPIL",
        "RIGHT_EYE_PUPIL",
        "FOREHEAD_GLABELLA",
        "CHIN_GNATHION",
        "CHIN_LEFT_GONION",
        "CHIN_RIGHT_GONION",
        "LEFT_CHEEK_CENTER",
        "RIGHT_CHEEK_CENTER",
    ]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p3beta1DominantColorsAnnotation

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    referenceImages: _list[GoogleCloudVisionV1p3beta1ReferenceImage]
    statuses: _list[Status]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GoogleCloudVisionV1p3beta1GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

@typing.type_check_only
class GoogleCloudVisionV1p3beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p3beta1GcsDestination

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Page(typing_extensions.TypedDict, total=False):
    blocks: _list[GoogleCloudVisionV1p3beta1Block]
    confidence: float
    height: int
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    width: int

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Paragraph(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    words: _list[GoogleCloudVisionV1p3beta1Word]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Product(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    productCategory: str
    productLabels: _list[GoogleCloudVisionV1p3beta1ProductKeyValue]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    indexTime: str
    productGroupedResults: _list[
        GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult
    ]
    results: _list[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    objectAnnotations: _list[
        GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation
    ]
    results: _list[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    product: GoogleCloudVisionV1p3beta1Product
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    boundingPolys: _list[GoogleCloudVisionV1p3beta1BoundingPoly]
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: _list[GoogleCloudVisionV1p3beta1Page]
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak
    detectedLanguages: _list[GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudVisionV1p3beta1WebDetection(typing_extensions.TypedDict, total=False):
    bestGuessLabels: _list[GoogleCloudVisionV1p3beta1WebDetectionWebLabel]
    fullMatchingImages: _list[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    pagesWithMatchingImages: _list[GoogleCloudVisionV1p3beta1WebDetectionWebPage]
    partialMatchingImages: _list[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    visuallySimilarImages: _list[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    webEntities: _list[GoogleCloudVisionV1p3beta1WebDetectionWebEntity]

@typing.type_check_only
class GoogleCloudVisionV1p3beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p3beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    fullMatchingImages: _list[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    pageTitle: str
    partialMatchingImages: _list[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p3beta1Word(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    symbols: _list[GoogleCloudVisionV1p3beta1Symbol]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    inputConfig: GoogleCloudVisionV1p4beta1InputConfig
    responses: _list[GoogleCloudVisionV1p4beta1AnnotateImageResponse]
    totalPages: int

@typing.type_check_only
class GoogleCloudVisionV1p4beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudVisionV1p4beta1ImageAnnotationContext
    cropHintsAnnotation: GoogleCloudVisionV1p4beta1CropHintsAnnotation
    error: Status
    faceAnnotations: _list[GoogleCloudVisionV1p4beta1FaceAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p4beta1TextAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p4beta1ImageProperties
    labelAnnotations: _list[GoogleCloudVisionV1p4beta1EntityAnnotation]
    landmarkAnnotations: _list[GoogleCloudVisionV1p4beta1EntityAnnotation]
    localizedObjectAnnotations: _list[
        GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation
    ]
    logoAnnotations: _list[GoogleCloudVisionV1p4beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p4beta1ProductSearchResults
    safeSearchAnnotation: GoogleCloudVisionV1p4beta1SafeSearchAnnotation
    textAnnotations: _list[GoogleCloudVisionV1p4beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p4beta1WebDetection

@typing.type_check_only
class GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

@typing.type_check_only
class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

@typing.type_check_only
class GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudVisionV1p4beta1AnnotateFileResponse]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    submitTime: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Block(typing_extensions.TypedDict, total=False):
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    paragraphs: _list[GoogleCloudVisionV1p4beta1Paragraph]
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty

@typing.type_check_only
class GoogleCloudVisionV1p4beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudVisionV1p4beta1NormalizedVertex]
    vertices: _list[GoogleCloudVisionV1p4beta1Vertex]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Celebrity(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    pixelFraction: float
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    importanceFraction: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: _list[GoogleCloudVisionV1p4beta1CropHint]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: _list[GoogleCloudVisionV1p4beta1ColorInfo]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    description: str
    locale: str
    locations: _list[GoogleCloudVisionV1p4beta1LocationInfo]
    mid: str
    properties: _list[GoogleCloudVisionV1p4beta1Property]
    score: float
    topicality: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    detectionConfidence: float
    fdBoundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    landmarks: _list[GoogleCloudVisionV1p4beta1FaceAnnotationLandmark]
    panAngle: float
    recognitionResult: _list[GoogleCloudVisionV1p4beta1FaceRecognitionResult]
    rollAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1FaceAnnotationLandmark(
    typing_extensions.TypedDict, total=False
):
    position: GoogleCloudVisionV1p4beta1Position
    type: typing_extensions.Literal[
        "UNKNOWN_LANDMARK",
        "LEFT_EYE",
        "RIGHT_EYE",
        "LEFT_OF_LEFT_EYEBROW",
        "RIGHT_OF_LEFT_EYEBROW",
        "LEFT_OF_RIGHT_EYEBROW",
        "RIGHT_OF_RIGHT_EYEBROW",
        "MIDPOINT_BETWEEN_EYES",
        "NOSE_TIP",
        "UPPER_LIP",
        "LOWER_LIP",
        "MOUTH_LEFT",
        "MOUTH_RIGHT",
        "MOUTH_CENTER",
        "NOSE_BOTTOM_RIGHT",
        "NOSE_BOTTOM_LEFT",
        "NOSE_BOTTOM_CENTER",
        "LEFT_EYE_TOP_BOUNDARY",
        "LEFT_EYE_RIGHT_CORNER",
        "LEFT_EYE_BOTTOM_BOUNDARY",
        "LEFT_EYE_LEFT_CORNER",
        "RIGHT_EYE_TOP_BOUNDARY",
        "RIGHT_EYE_RIGHT_CORNER",
        "RIGHT_EYE_BOTTOM_BOUNDARY",
        "RIGHT_EYE_LEFT_CORNER",
        "LEFT_EYEBROW_UPPER_MIDPOINT",
        "RIGHT_EYEBROW_UPPER_MIDPOINT",
        "LEFT_EAR_TRAGION",
        "RIGHT_EAR_TRAGION",
        "LEFT_EYE_PUPIL",
        "RIGHT_EYE_PUPIL",
        "FOREHEAD_GLABELLA",
        "CHIN_GNATHION",
        "CHIN_LEFT_GONION",
        "CHIN_RIGHT_GONION",
        "LEFT_CHEEK_CENTER",
        "RIGHT_CHEEK_CENTER",
    ]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1FaceRecognitionResult(
    typing_extensions.TypedDict, total=False
):
    celebrity: GoogleCloudVisionV1p4beta1Celebrity
    confidence: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p4beta1DominantColorsAnnotation

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    referenceImages: _list[GoogleCloudVisionV1p4beta1ReferenceImage]
    statuses: _list[Status]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GoogleCloudVisionV1p4beta1GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

@typing.type_check_only
class GoogleCloudVisionV1p4beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p4beta1GcsDestination

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Page(typing_extensions.TypedDict, total=False):
    blocks: _list[GoogleCloudVisionV1p4beta1Block]
    confidence: float
    height: int
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    width: int

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Paragraph(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    words: _list[GoogleCloudVisionV1p4beta1Word]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Product(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    productCategory: str
    productLabels: _list[GoogleCloudVisionV1p4beta1ProductKeyValue]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    indexTime: str
    productGroupedResults: _list[
        GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult
    ]
    results: _list[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    objectAnnotations: _list[
        GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation
    ]
    results: _list[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    product: GoogleCloudVisionV1p4beta1Product
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    boundingPolys: _list[GoogleCloudVisionV1p4beta1BoundingPoly]
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: _list[GoogleCloudVisionV1p4beta1Page]
    text: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak
    detectedLanguages: _list[GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudVisionV1p4beta1WebDetection(typing_extensions.TypedDict, total=False):
    bestGuessLabels: _list[GoogleCloudVisionV1p4beta1WebDetectionWebLabel]
    fullMatchingImages: _list[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    pagesWithMatchingImages: _list[GoogleCloudVisionV1p4beta1WebDetectionWebPage]
    partialMatchingImages: _list[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    visuallySimilarImages: _list[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    webEntities: _list[GoogleCloudVisionV1p4beta1WebDetectionWebEntity]

@typing.type_check_only
class GoogleCloudVisionV1p4beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    score: float

@typing.type_check_only
class GoogleCloudVisionV1p4beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    fullMatchingImages: _list[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    pageTitle: str
    partialMatchingImages: _list[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    score: float
    url: str

@typing.type_check_only
class GoogleCloudVisionV1p4beta1Word(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    symbols: _list[GoogleCloudVisionV1p4beta1Symbol]

@typing.type_check_only
class GroupedResult(typing_extensions.TypedDict, total=False):
    boundingPoly: BoundingPoly
    objectAnnotations: _list[ObjectAnnotation]
    results: _list[Result]

@typing.type_check_only
class ImageAnnotationContext(typing_extensions.TypedDict, total=False):
    pageNumber: int
    uri: str

@typing.type_check_only
class ImageProperties(typing_extensions.TypedDict, total=False):
    dominantColors: DominantColorsAnnotation

@typing.type_check_only
class ImportProductSetsResponse(typing_extensions.TypedDict, total=False):
    referenceImages: _list[ReferenceImage]
    statuses: _list[Status]

@typing.type_check_only
class InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GcsSource
    mimeType: str

@typing.type_check_only
class KeyValue(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class Landmark(typing_extensions.TypedDict, total=False):
    position: Position
    type: typing_extensions.Literal[
        "UNKNOWN_LANDMARK",
        "LEFT_EYE",
        "RIGHT_EYE",
        "LEFT_OF_LEFT_EYEBROW",
        "RIGHT_OF_LEFT_EYEBROW",
        "LEFT_OF_RIGHT_EYEBROW",
        "RIGHT_OF_RIGHT_EYEBROW",
        "MIDPOINT_BETWEEN_EYES",
        "NOSE_TIP",
        "UPPER_LIP",
        "LOWER_LIP",
        "MOUTH_LEFT",
        "MOUTH_RIGHT",
        "MOUTH_CENTER",
        "NOSE_BOTTOM_RIGHT",
        "NOSE_BOTTOM_LEFT",
        "NOSE_BOTTOM_CENTER",
        "LEFT_EYE_TOP_BOUNDARY",
        "LEFT_EYE_RIGHT_CORNER",
        "LEFT_EYE_BOTTOM_BOUNDARY",
        "LEFT_EYE_LEFT_CORNER",
        "RIGHT_EYE_TOP_BOUNDARY",
        "RIGHT_EYE_RIGHT_CORNER",
        "RIGHT_EYE_BOTTOM_BOUNDARY",
        "RIGHT_EYE_LEFT_CORNER",
        "LEFT_EYEBROW_UPPER_MIDPOINT",
        "RIGHT_EYEBROW_UPPER_MIDPOINT",
        "LEFT_EAR_TRAGION",
        "RIGHT_EAR_TRAGION",
        "LEFT_EYE_PUPIL",
        "RIGHT_EYE_PUPIL",
        "FOREHEAD_GLABELLA",
        "CHIN_GNATHION",
        "CHIN_LEFT_GONION",
        "CHIN_RIGHT_GONION",
        "LEFT_CHEEK_CENTER",
        "RIGHT_CHEEK_CENTER",
    ]

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LocalizedObjectAnnotation(typing_extensions.TypedDict, total=False):
    boundingPoly: BoundingPoly
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

@typing.type_check_only
class NormalizedVertex(typing_extensions.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class ObjectAnnotation(typing_extensions.TypedDict, total=False):
    languageCode: str
    mid: str
    name: str
    score: float

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GcsDestination

@typing.type_check_only
class Page(typing_extensions.TypedDict, total=False):
    blocks: _list[Block]
    confidence: float
    height: int
    property: TextProperty
    width: int

@typing.type_check_only
class Paragraph(typing_extensions.TypedDict, total=False):
    boundingBox: BoundingPoly
    confidence: float
    property: TextProperty
    words: _list[Word]

@typing.type_check_only
class Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    productCategory: str
    productLabels: _list[KeyValue]

@typing.type_check_only
class ProductSearchResults(typing_extensions.TypedDict, total=False):
    indexTime: str
    productGroupedResults: _list[GroupedResult]
    results: _list[Result]

@typing.type_check_only
class Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

@typing.type_check_only
class ReferenceImage(typing_extensions.TypedDict, total=False):
    boundingPolys: _list[BoundingPoly]
    name: str
    uri: str

@typing.type_check_only
class Result(typing_extensions.TypedDict, total=False):
    image: str
    product: Product
    score: float

@typing.type_check_only
class SafeSearchAnnotation(typing_extensions.TypedDict, total=False):
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: BoundingPoly
    confidence: float
    property: TextProperty
    text: str

@typing.type_check_only
class TextAnnotation(typing_extensions.TypedDict, total=False):
    pages: _list[Page]
    text: str

@typing.type_check_only
class TextProperty(typing_extensions.TypedDict, total=False):
    detectedBreak: DetectedBreak
    detectedLanguages: _list[DetectedLanguage]

@typing.type_check_only
class Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class WebDetection(typing_extensions.TypedDict, total=False):
    bestGuessLabels: _list[WebLabel]
    fullMatchingImages: _list[WebImage]
    pagesWithMatchingImages: _list[WebPage]
    partialMatchingImages: _list[WebImage]
    visuallySimilarImages: _list[WebImage]
    webEntities: _list[WebEntity]

@typing.type_check_only
class WebEntity(typing_extensions.TypedDict, total=False):
    description: str
    entityId: str
    score: float

@typing.type_check_only
class WebImage(typing_extensions.TypedDict, total=False):
    score: float
    url: str

@typing.type_check_only
class WebLabel(typing_extensions.TypedDict, total=False):
    label: str
    languageCode: str

@typing.type_check_only
class WebPage(typing_extensions.TypedDict, total=False):
    fullMatchingImages: _list[WebImage]
    pageTitle: str
    partialMatchingImages: _list[WebImage]
    score: float
    url: str

@typing.type_check_only
class Word(typing_extensions.TypedDict, total=False):
    boundingBox: BoundingPoly
    confidence: float
    property: TextProperty
    symbols: _list[Symbol]
