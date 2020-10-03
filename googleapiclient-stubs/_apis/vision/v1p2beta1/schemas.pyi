import typing

import typing_extensions

class GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    name: str
    mid: str
    score: float
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    languageCode: str

class BatchOperationMetadata(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    endTime: str
    submitTime: str

class InputConfig(typing_extensions.TypedDict, total=False):
    mimeType: str
    gcsSource: GcsSource
    content: str

class AnnotateImageResponse(typing_extensions.TypedDict, total=False):
    imagePropertiesAnnotation: ImageProperties
    webDetection: WebDetection
    logoAnnotations: typing.List[EntityAnnotation]
    error: Status
    productSearchResults: ProductSearchResults
    faceAnnotations: typing.List[FaceAnnotation]
    safeSearchAnnotation: SafeSearchAnnotation
    context: ImageAnnotationContext
    labelAnnotations: typing.List[EntityAnnotation]
    cropHintsAnnotation: CropHintsAnnotation
    textAnnotations: typing.List[EntityAnnotation]
    landmarkAnnotations: typing.List[EntityAnnotation]
    fullTextAnnotation: TextAnnotation
    localizedObjectAnnotations: typing.List[LocalizedObjectAnnotation]

class GoogleCloudVisionV1p2beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p2beta1ColorInfo]

class GoogleCloudVisionV1p3beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

class GoogleCloudVisionV1p4beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

class GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p4beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    uri: str
    boundingPolys: typing.List[GoogleCloudVisionV1p4beta1BoundingPoly]
    name: str

class GoogleCloudVisionV1p2beta1ImageContext(typing_extensions.TypedDict, total=False):
    latLongRect: GoogleCloudVisionV1p2beta1LatLongRect
    languageHints: typing.List[str]
    productSearchParams: GoogleCloudVisionV1p2beta1ProductSearchParams
    webDetectionParams: GoogleCloudVisionV1p2beta1WebDetectionParams
    cropHintsParams: GoogleCloudVisionV1p2beta1CropHintsParams

class GoogleCloudVisionV1p1beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    indexTime: str
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult
    ]
    results: typing.List[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p4beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage
    ]
    detectedBreak: GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak

class AsyncBatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p1beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

class GoogleCloudVisionV1p3beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p3beta1ColorInfo]

class GoogleCloudVisionV1p1beta1Paragraph(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    words: typing.List[GoogleCloudVisionV1p1beta1Word]
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    confidence: float

class LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class FaceAnnotation(typing_extensions.TypedDict, total=False):
    landmarks: typing.List[Landmark]
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    panAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: BoundingPoly
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    boundingPoly: BoundingPoly
    landmarkingConfidence: float
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    rollAngle: float

class GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p3beta1OutputConfig

class GoogleCloudVisionV1p1beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p1beta1DominantColorsAnnotation

class GoogleCloudVisionV1p4beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p4beta1ColorInfo]

class GoogleCloudVisionV1p1beta1Page(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    width: int
    blocks: typing.List[GoogleCloudVisionV1p1beta1Block]
    height: int
    confidence: float

class GoogleCloudVisionV1p3beta1Product(typing_extensions.TypedDict, total=False):
    displayName: str
    productCategory: str
    productLabels: typing.List[GoogleCloudVisionV1p3beta1ProductKeyValue]
    description: str
    name: str

class GoogleCloudVisionV1p2beta1Page(typing_extensions.TypedDict, total=False):
    width: int
    blocks: typing.List[GoogleCloudVisionV1p2beta1Block]
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    height: int

class Landmark(typing_extensions.TypedDict, total=False):
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
    position: Position

class GoogleCloudVisionV1p3beta1Position(typing_extensions.TypedDict, total=False):
    z: float
    y: float
    x: float

class GoogleCloudVisionV1p4beta1Paragraph(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    words: typing.List[GoogleCloudVisionV1p4beta1Word]

class GoogleCloudVisionV1p1beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    pixelFraction: float
    score: float

class GoogleCloudVisionV1p2beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p2beta1CropHint]

class GoogleCloudVisionV1p2beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVisionV1p4beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p4beta1CropHint]

class GoogleCloudVisionV1p3beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

class GoogleCloudVisionV1p4beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    pages: typing.List[GoogleCloudVisionV1p4beta1Page]

class GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

class GoogleCloudVisionV1p4beta1InputConfig(typing_extensions.TypedDict, total=False):
    mimeType: str
    gcsSource: GoogleCloudVisionV1p4beta1GcsSource
    content: str

class GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

class GoogleCloudVisionV1p2beta1AsyncAnnotateFileRequest(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudVisionV1p2beta1InputConfig
    outputConfig: GoogleCloudVisionV1p2beta1OutputConfig
    imageContext: GoogleCloudVisionV1p2beta1ImageContext
    features: typing.List[GoogleCloudVisionV1p2beta1Feature]

class AnnotateFileResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AnnotateImageResponse]
    inputConfig: InputConfig
    error: Status
    totalPages: int

class GoogleCloudVisionV1p1beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

class GoogleCloudVisionV1p1beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class Symbol(typing_extensions.TypedDict, total=False):
    property: TextProperty
    text: str
    confidence: float
    boundingBox: BoundingPoly

class GoogleCloudVisionV1p2beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p3beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GoogleCloudVisionV1p3beta1GcsSource
    mimeType: str

class GoogleCloudVisionV1p4beta1Position(typing_extensions.TypedDict, total=False):
    y: float
    x: float
    z: float

class GoogleCloudVisionV1p4beta1WebDetection(typing_extensions.TypedDict, total=False):
    partialMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebLabel]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebPage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    webEntities: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebEntity]

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

class KeyValue(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class GoogleCloudVisionV1p1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p2beta1LatLongRect(typing_extensions.TypedDict, total=False):
    minLatLng: LatLng
    maxLatLng: LatLng

class GoogleCloudVisionV1p2beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p4beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    value: str
    key: str

class GoogleCloudVisionV1p4beta1Celebrity(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    description: str

class GoogleCloudVisionV1p4beta1Word(typing_extensions.TypedDict, total=False):
    symbols: typing.List[GoogleCloudVisionV1p4beta1Symbol]
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    confidence: float

class NormalizedVertex(typing_extensions.TypedDict, total=False):
    x: float
    y: float

class GoogleCloudVisionV1p2beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    score: float
    description: str
    entityId: str

class GoogleCloudVisionV1p2beta1WebDetectionParams(
    typing_extensions.TypedDict, total=False
):
    includeGeoResults: bool

class GoogleCloudVisionV1p1beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    score: float
    description: str
    entityId: str

class GoogleCloudVisionV1p2beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    label: str

class GoogleCloudVisionV1p2beta1Paragraph(typing_extensions.TypedDict, total=False):
    confidence: float
    words: typing.List[GoogleCloudVisionV1p2beta1Word]
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly

class Product(typing_extensions.TypedDict, total=False):
    productCategory: str
    displayName: str
    description: str
    productLabels: typing.List[KeyValue]
    name: str

class GoogleCloudVisionV1p2beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    inputConfig: GoogleCloudVisionV1p2beta1InputConfig
    totalPages: int
    responses: typing.List[GoogleCloudVisionV1p2beta1AnnotateImageResponse]

class GoogleCloudVisionV1p2beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[GoogleCloudVisionV1p2beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudVisionV1p2beta1Vertex]

class GoogleCloudVisionV1p2beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p3beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    score: float
    pixelFraction: float

class ObjectAnnotation(typing_extensions.TypedDict, total=False):
    name: str
    score: float
    languageCode: str
    mid: str

class GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p4beta1Product(typing_extensions.TypedDict, total=False):
    description: str
    productLabels: typing.List[GoogleCloudVisionV1p4beta1ProductKeyValue]
    displayName: str
    productCategory: str
    name: str

class GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    score: float
    languageCode: str
    name: str
    mid: str

class GoogleCloudVisionV1p4beta1Page(typing_extensions.TypedDict, total=False):
    height: int
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    blocks: typing.List[GoogleCloudVisionV1p4beta1Block]
    width: int
    confidence: float

class AsyncAnnotateFileResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class GoogleCloudVisionV1p1beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    score: float
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    description: str
    topicality: float
    locale: str
    confidence: float
    mid: str
    properties: typing.List[GoogleCloudVisionV1p1beta1Property]
    locations: typing.List[GoogleCloudVisionV1p1beta1LocationInfo]

class GoogleCloudVisionV1p2beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    rollAngle: float
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    landmarkingConfidence: float
    panAngle: float
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarks: typing.List[GoogleCloudVisionV1p2beta1FaceAnnotationLandmark]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly

class GoogleCloudVisionV1p3beta1Paragraph(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    confidence: float
    words: typing.List[GoogleCloudVisionV1p3beta1Word]
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly

class GoogleCloudVisionV1p4beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    statuses: typing.List[Status]
    referenceImages: typing.List[GoogleCloudVisionV1p4beta1ReferenceImage]

class GoogleCloudVisionV1p3beta1WebDetection(typing_extensions.TypedDict, total=False):
    webEntities: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebEntity]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebPage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebLabel]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]

class GoogleCloudVisionV1p4beta1CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    importanceFraction: float
    confidence: float

class GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p2beta1OutputConfig

class GoogleCloudVisionV1p3beta1Word(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    symbols: typing.List[GoogleCloudVisionV1p3beta1Symbol]
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty

class GoogleCloudVisionV1p4beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p3beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    score: float
    entityId: str
    description: str

class GoogleCloudVisionV1p4beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    mid: str
    description: str
    topicality: float
    score: float
    properties: typing.List[GoogleCloudVisionV1p4beta1Property]
    locations: typing.List[GoogleCloudVisionV1p4beta1LocationInfo]
    confidence: float
    locale: str

class TextAnnotation(typing_extensions.TypedDict, total=False):
    pages: typing.List[Page]
    text: str

class DetectedLanguage(typing_extensions.TypedDict, total=False):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p2beta1AnnotateImageRequest(
    typing_extensions.TypedDict, total=False
):
    features: typing.List[GoogleCloudVisionV1p2beta1Feature]
    image: GoogleCloudVisionV1p2beta1Image
    imageContext: GoogleCloudVisionV1p2beta1ImageContext

class GoogleCloudVisionV1p3beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p4beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float

class GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p2beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    pages: typing.List[GoogleCloudVisionV1p2beta1Page]

class GoogleCloudVisionV1p4beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    endTime: str
    submitTime: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]

class GoogleCloudVisionV1p4beta1FaceRecognitionResult(
    typing_extensions.TypedDict, total=False
):
    celebrity: GoogleCloudVisionV1p4beta1Celebrity
    confidence: float

class GoogleCloudVisionV1p3beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

class ImageProperties(typing_extensions.TypedDict, total=False):
    dominantColors: DominantColorsAnnotation

class GoogleCloudVisionV1p4beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class ImportProductSetsResponse(typing_extensions.TypedDict, total=False):
    statuses: typing.List[Status]
    referenceImages: typing.List[ReferenceImage]

class GoogleCloudVisionV1p2beta1BatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p2beta1AnnotateFileResponse]

class GoogleCloudVisionV1p1beta1CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    confidence: float
    importanceFraction: float

class Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

class GoogleCloudVisionV1p3beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    value: str
    key: str

class GoogleCloudVisionV1p4beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    score: float
    description: str
    entityId: str

class GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    mid: str
    languageCode: str
    score: float
    name: str
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly

class GoogleCloudVisionV1p3beta1Page(typing_extensions.TypedDict, total=False):
    width: int
    height: int
    confidence: float
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    blocks: typing.List[GoogleCloudVisionV1p3beta1Block]

class GoogleCloudVisionV1p2beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class DetectedBreak(typing_extensions.TypedDict, total=False):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class WebPage(typing_extensions.TypedDict, total=False):
    score: float
    url: str
    partialMatchingImages: typing.List[WebImage]
    pageTitle: str
    fullMatchingImages: typing.List[WebImage]

class GoogleCloudVisionV1p4beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    safeSearchAnnotation: GoogleCloudVisionV1p4beta1SafeSearchAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p4beta1ImageProperties
    logoAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p4beta1WebDetection
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation
    ]
    labelAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    cropHintsAnnotation: GoogleCloudVisionV1p4beta1CropHintsAnnotation
    context: GoogleCloudVisionV1p4beta1ImageAnnotationContext
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p4beta1TextAnnotation
    faceAnnotations: typing.List[GoogleCloudVisionV1p4beta1FaceAnnotation]
    textAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p4beta1ProductSearchResults

class GoogleCloudVisionV1p2beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    product: GoogleCloudVisionV1p2beta1Product
    score: float

class GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation
    ]
    results: typing.List[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p1beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    vertices: typing.List[GoogleCloudVisionV1p1beta1Vertex]
    normalizedVertices: typing.List[GoogleCloudVisionV1p1beta1NormalizedVertex]

class GoogleCloudVisionV1p2beta1Word(typing_extensions.TypedDict, total=False):
    symbols: typing.List[GoogleCloudVisionV1p2beta1Symbol]
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    confidence: float

class GoogleCloudVisionV1p1beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p2beta1Image(typing_extensions.TypedDict, total=False):
    source: GoogleCloudVisionV1p2beta1ImageSource
    content: str

class GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation
    ]
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    results: typing.List[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p1beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    url: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    pageTitle: str
    fullMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    score: float

class TextProperty(typing_extensions.TypedDict, total=False):
    detectedBreak: DetectedBreak
    detectedLanguages: typing.List[DetectedLanguage]

class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p3beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

class GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation
    ]
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly

class GoogleCloudVisionV1p2beta1ProductSearchParams(
    typing_extensions.TypedDict, total=False
):
    filter: str
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    productCategories: typing.List[str]
    productSet: str

class GoogleCloudVisionV1p1beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

class CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingPoly: BoundingPoly
    importanceFraction: float

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination
    batchSize: int

class GoogleCloudVisionV1p3beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float
    partialMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    pageTitle: str
    fullMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]

class ReferenceImage(typing_extensions.TypedDict, total=False):
    name: str
    uri: str
    boundingPolys: typing.List[BoundingPoly]

class DominantColorsAnnotation(typing_extensions.TypedDict, total=False):
    colors: typing.List[ColorInfo]

class ImageAnnotationContext(typing_extensions.TypedDict, total=False):
    pageNumber: int
    uri: str

class GoogleCloudVisionV1p4beta1Block(typing_extensions.TypedDict, total=False):
    paragraphs: typing.List[GoogleCloudVisionV1p4beta1Paragraph]
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    confidence: float
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly

class GoogleCloudVisionV1p2beta1AsyncBatchAnnotateImagesRequest(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p2beta1OutputConfig
    requests: typing.List[GoogleCloudVisionV1p2beta1AnnotateImageRequest]
    parent: str

class GoogleCloudVisionV1p1beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    fdBoundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    detectionConfidence: float
    rollAngle: float
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    panAngle: float
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarks: typing.List[GoogleCloudVisionV1p1beta1FaceAnnotationLandmark]

class GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    name: str
    mid: str
    score: float
    languageCode: str

class GoogleCloudVisionV1p2beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

class GoogleCloudVisionV1p4beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    pageTitle: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    score: float
    url: str

class GoogleCloudVisionV1p2beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    mimeType: str
    gcsSource: GoogleCloudVisionV1p2beta1GcsSource

class GoogleCloudVisionV1p3beta1CropHint(typing_extensions.TypedDict, total=False):
    importanceFraction: float
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float

class GoogleCloudVisionV1p4beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p3beta1FaceAnnotationLandmark(
    typing_extensions.TypedDict, total=False
):
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
    position: GoogleCloudVisionV1p3beta1Position

class Color(typing_extensions.TypedDict, total=False):
    red: float
    green: float
    alpha: float
    blue: float

class GoogleCloudVisionV1p3beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    submitTime: str

class GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig

class GoogleCloudVisionV1p3beta1Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    confidence: float
    text: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    name: str
    metadata: typing.Dict[str, typing.Any]
    done: bool
    response: typing.Dict[str, typing.Any]

class GoogleCloudVisionV1p2beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p3beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class WebDetection(typing_extensions.TypedDict, total=False):
    visuallySimilarImages: typing.List[WebImage]
    webEntities: typing.List[WebEntity]
    fullMatchingImages: typing.List[WebImage]
    bestGuessLabels: typing.List[WebLabel]
    partialMatchingImages: typing.List[WebImage]
    pagesWithMatchingImages: typing.List[WebPage]

class GoogleCloudVisionV1p3beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class Result(typing_extensions.TypedDict, total=False):
    score: float
    product: Product
    image: str

class GoogleCloudVisionV1p3beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p3beta1CropHint]

class GoogleCloudVisionV1p4beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p4beta1DominantColorsAnnotation

class Page(typing_extensions.TypedDict, total=False):
    blocks: typing.List[Block]
    width: int
    height: int
    confidence: float
    property: TextProperty

class BatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AnnotateFileResponse]

class WebLabel(typing_extensions.TypedDict, total=False):
    languageCode: str
    label: str

class GoogleCloudVisionV1p3beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]
    indexTime: str
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult
    ]

class GoogleCloudVisionV1p4beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p1beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p1beta1ColorInfo]

class GoogleCloudVisionV1p1beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    value: str
    key: str

class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p1beta1InputConfig(typing_extensions.TypedDict, total=False):
    mimeType: str
    content: str
    gcsSource: GoogleCloudVisionV1p1beta1GcsSource

class GoogleCloudVisionV1p2beta1WebDetection(typing_extensions.TypedDict, total=False):
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebPage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebLabel]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    webEntities: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebEntity]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]

class GoogleCloudVisionV1p3beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p3beta1GcsDestination

class GoogleCloudVisionV1p2beta1BatchAnnotateFilesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleCloudVisionV1p2beta1AnnotateFileRequest]
    parent: str

class GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p4beta1AnnotateFileResponse]

class GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleCloudVisionV1p2beta1AsyncAnnotateFileRequest]
    parent: str

class GoogleCloudVisionV1p3beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    properties: typing.List[GoogleCloudVisionV1p3beta1Property]
    description: str
    confidence: float
    mid: str
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    locations: typing.List[GoogleCloudVisionV1p3beta1LocationInfo]
    topicality: float
    locale: str
    score: float

class GoogleCloudVisionV1p3beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

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

class Block(typing_extensions.TypedDict, total=False):
    property: TextProperty
    paragraphs: typing.List[Paragraph]
    boundingBox: BoundingPoly
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    confidence: float

class GoogleCloudVisionV1p3beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    uri: str
    boundingPolys: typing.List[GoogleCloudVisionV1p3beta1BoundingPoly]
    name: str

class GoogleCloudVisionV1p3beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p2beta1BatchAnnotateImagesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p2beta1AnnotateImageResponse]

class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p3beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    score: float
    product: GoogleCloudVisionV1p3beta1Product
    image: str

class GoogleCloudVisionV1p1beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    webDetection: GoogleCloudVisionV1p1beta1WebDetection
    safeSearchAnnotation: GoogleCloudVisionV1p1beta1SafeSearchAnnotation
    textAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    imagePropertiesAnnotation: GoogleCloudVisionV1p1beta1ImageProperties
    labelAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p1beta1TextAnnotation
    logoAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    faceAnnotations: typing.List[GoogleCloudVisionV1p1beta1FaceAnnotation]
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation
    ]
    error: Status
    context: GoogleCloudVisionV1p1beta1ImageAnnotationContext
    cropHintsAnnotation: GoogleCloudVisionV1p1beta1CropHintsAnnotation
    productSearchResults: GoogleCloudVisionV1p1beta1ProductSearchResults

class GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

class GoogleCloudVisionV1p2beta1Feature(typing_extensions.TypedDict, total=False):
    maxResults: int
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
    model: str

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

class GoogleCloudVisionV1p1beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p1beta1CropHint]

class BoundingPoly(typing_extensions.TypedDict, total=False):
    vertices: typing.List[Vertex]
    normalizedVertices: typing.List[NormalizedVertex]

class GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p1beta1Block(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    paragraphs: typing.List[GoogleCloudVisionV1p1beta1Paragraph]
    confidence: float
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty

class WebImage(typing_extensions.TypedDict, total=False):
    score: float
    url: str

class GoogleCloudVisionV1p4beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    inputConfig: GoogleCloudVisionV1p4beta1InputConfig
    totalPages: int
    responses: typing.List[GoogleCloudVisionV1p4beta1AnnotateImageResponse]

class GoogleCloudVisionV1p1beta1FaceAnnotationLandmark(
    typing_extensions.TypedDict, total=False
):
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
    position: GoogleCloudVisionV1p1beta1Position

class GoogleCloudVisionV1p1beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: typing.List[GoogleCloudVisionV1p1beta1Page]
    text: str

class GoogleCloudVisionV1p1beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    score: float
    languageCode: str
    name: str
    mid: str

class GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p2beta1BatchAnnotateImagesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleCloudVisionV1p2beta1AnnotateImageRequest]
    parent: str

class GoogleCloudVisionV1p4beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p1beta1Product(typing_extensions.TypedDict, total=False):
    productCategory: str
    name: str
    productLabels: typing.List[GoogleCloudVisionV1p1beta1ProductKeyValue]
    description: str
    displayName: str

class GoogleCloudVisionV1p4beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]

class GoogleCloudVisionV1p2beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float

class GoogleCloudVisionV1p3beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p2beta1CropHintsParams(
    typing_extensions.TypedDict, total=False
):
    aspectRatios: typing.List[float]

class Word(typing_extensions.TypedDict, total=False):
    symbols: typing.List[Symbol]
    boundingBox: BoundingPoly
    property: TextProperty
    confidence: float

class WebEntity(typing_extensions.TypedDict, total=False):
    entityId: str
    score: float
    description: str

class ColorInfo(typing_extensions.TypedDict, total=False):
    pixelFraction: float
    color: Color
    score: float

class Paragraph(typing_extensions.TypedDict, total=False):
    property: TextProperty
    confidence: float
    boundingBox: BoundingPoly
    words: typing.List[Word]

class GoogleCloudVisionV1p1beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    totalPages: int
    error: Status
    responses: typing.List[GoogleCloudVisionV1p1beta1AnnotateImageResponse]
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig

class GoogleCloudVisionV1p4beta1Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    text: str

class GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation
    ]
    results: typing.List[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p1beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]

class GoogleCloudVisionV1p1beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class GoogleCloudVisionV1p2beta1CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    importanceFraction: float

class GoogleCloudVisionV1p3beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: typing.List[GoogleCloudVisionV1p3beta1Page]
    text: str

class GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    name: str
    score: float
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    mid: str
    languageCode: str

class GoogleCloudVisionV1p2beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    score: float
    pixelFraction: float

class GoogleCloudVisionV1p3beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    statuses: typing.List[Status]
    referenceImages: typing.List[GoogleCloudVisionV1p3beta1ReferenceImage]

class GoogleCloudVisionV1p4beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    label: str

class GoogleCloudVisionV1p3beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[GoogleCloudVisionV1p3beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudVisionV1p3beta1Vertex]

class GoogleCloudVisionV1p2beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    locations: typing.List[GoogleCloudVisionV1p2beta1LocationInfo]
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    description: str
    mid: str
    score: float
    properties: typing.List[GoogleCloudVisionV1p2beta1Property]
    locale: str
    topicality: float

class GoogleCloudVisionV1p3beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p3beta1DominantColorsAnnotation

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class ProductSearchResults(typing_extensions.TypedDict, total=False):
    productGroupedResults: typing.List[GroupedResult]
    indexTime: str
    results: typing.List[Result]

class SafeSearchAnnotation(typing_extensions.TypedDict, total=False):
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p3beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    totalPages: int
    inputConfig: GoogleCloudVisionV1p3beta1InputConfig
    responses: typing.List[GoogleCloudVisionV1p3beta1AnnotateImageResponse]
    error: Status

class AsyncBatchAnnotateImagesResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class GoogleCloudVisionV1p4beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    score: float
    product: GoogleCloudVisionV1p4beta1Product
    image: str

class GoogleCloudVisionV1p1beta1OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudVisionV1p1beta1GcsDestination
    batchSize: int

class GoogleCloudVisionV1p4beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

class GoogleCloudVisionV1p3beta1Block(typing_extensions.TypedDict, total=False):
    confidence: float
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    paragraphs: typing.List[GoogleCloudVisionV1p3beta1Paragraph]
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty

class GoogleCloudVisionV1p3beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    uint64Value: str

class Position(typing_extensions.TypedDict, total=False):
    y: float
    x: float
    z: float

class GroupedResult(typing_extensions.TypedDict, total=False):
    objectAnnotations: typing.List[ObjectAnnotation]
    boundingPoly: BoundingPoly
    results: typing.List[Result]

class GoogleCloudVisionV1p4beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    rollAngle: float
    panAngle: float
    detectionConfidence: float
    landmarks: typing.List[GoogleCloudVisionV1p4beta1FaceAnnotationLandmark]
    recognitionResult: typing.List[GoogleCloudVisionV1p4beta1FaceRecognitionResult]
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float

class GoogleCloudVisionV1p2beta1AnnotateFileRequest(
    typing_extensions.TypedDict, total=False
):
    features: typing.List[GoogleCloudVisionV1p2beta1Feature]
    pages: typing.List[int]
    imageContext: GoogleCloudVisionV1p2beta1ImageContext
    inputConfig: GoogleCloudVisionV1p2beta1InputConfig

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleCloudVisionV1p2beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    pageTitle: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    score: float
    url: str

class GoogleCloudVisionV1p2beta1OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudVisionV1p2beta1GcsDestination
    batchSize: int

class GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class CropHintsAnnotation(typing_extensions.TypedDict, total=False):
    cropHints: typing.List[CropHint]

class GoogleCloudVisionV1p2beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult
    ]
    results: typing.List[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]
    indexTime: str

class GoogleCloudVisionV1p3beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    imagePropertiesAnnotation: GoogleCloudVisionV1p3beta1ImageProperties
    fullTextAnnotation: GoogleCloudVisionV1p3beta1TextAnnotation
    faceAnnotations: typing.List[GoogleCloudVisionV1p3beta1FaceAnnotation]
    safeSearchAnnotation: GoogleCloudVisionV1p3beta1SafeSearchAnnotation
    logoAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p3beta1ProductSearchResults
    cropHintsAnnotation: GoogleCloudVisionV1p3beta1CropHintsAnnotation
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation
    ]
    error: Status
    webDetection: GoogleCloudVisionV1p3beta1WebDetection
    labelAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    context: GoogleCloudVisionV1p3beta1ImageAnnotationContext
    textAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]

class GoogleCloudVisionV1p3beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    tiltAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    rollAngle: float
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    fdBoundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    panAngle: float
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarks: typing.List[GoogleCloudVisionV1p3beta1FaceAnnotationLandmark]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float

class GoogleCloudVisionV1p1beta1Symbol(typing_extensions.TypedDict, total=False):
    confidence: float
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    text: str
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly

class LocalizedObjectAnnotation(typing_extensions.TypedDict, total=False):
    score: float
    languageCode: str
    name: str
    boundingPoly: BoundingPoly
    mid: str

class GoogleCloudVisionV1p4beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult
    ]
    indexTime: str
    results: typing.List[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p4beta1ColorInfo(typing_extensions.TypedDict, total=False):
    pixelFraction: float
    color: Color
    score: float

class GoogleCloudVisionV1p1beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p2beta1Block(typing_extensions.TypedDict, total=False):
    paragraphs: typing.List[GoogleCloudVisionV1p2beta1Paragraph]
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]

class GoogleCloudVisionV1p2beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    faceAnnotations: typing.List[GoogleCloudVisionV1p2beta1FaceAnnotation]
    logoAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    labelAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    context: GoogleCloudVisionV1p2beta1ImageAnnotationContext
    error: Status
    cropHintsAnnotation: GoogleCloudVisionV1p2beta1CropHintsAnnotation
    safeSearchAnnotation: GoogleCloudVisionV1p2beta1SafeSearchAnnotation
    fullTextAnnotation: GoogleCloudVisionV1p2beta1TextAnnotation
    webDetection: GoogleCloudVisionV1p2beta1WebDetection
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation
    ]
    productSearchResults: GoogleCloudVisionV1p2beta1ProductSearchResults
    textAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    imagePropertiesAnnotation: GoogleCloudVisionV1p2beta1ImageProperties

class GoogleCloudVisionV1p1beta1WebDetection(typing_extensions.TypedDict, total=False):
    webEntities: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebEntity]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebLabel]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebPage]

class GoogleCloudVisionV1p2beta1Product(typing_extensions.TypedDict, total=False):
    description: str
    productLabels: typing.List[GoogleCloudVisionV1p2beta1ProductKeyValue]
    name: str
    productCategory: str
    displayName: str

class GoogleCloudVisionV1p4beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p2beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p1beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

class GoogleCloudVisionV1p1beta1Word(typing_extensions.TypedDict, total=False):
    symbols: typing.List[GoogleCloudVisionV1p1beta1Symbol]
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    confidence: float

class GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    mid: str
    name: str
    score: float

class GoogleCloudVisionV1p1beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

class GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    mid: str
    name: str
    score: float
    languageCode: str

class EntityAnnotation(typing_extensions.TypedDict, total=False):
    properties: typing.List[Property]
    locale: str
    boundingPoly: BoundingPoly
    mid: str
    score: float
    topicality: float
    confidence: float
    locations: typing.List[LocationInfo]
    description: str

class GoogleCloudVisionV1p2beta1ImageSource(typing_extensions.TypedDict, total=False):
    gcsImageUri: str
    imageUri: str

class GoogleCloudVisionV1p1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p4beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p4beta1GcsDestination

class GoogleCloudVisionV1p1beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    product: GoogleCloudVisionV1p1beta1Product
    score: float
    image: str

class GoogleCloudVisionV1p2beta1Position(typing_extensions.TypedDict, total=False):
    z: float
    y: float
    x: float

class GoogleCloudVisionV1p2beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p2beta1DominantColorsAnnotation

class GoogleCloudVisionV1p4beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    vertices: typing.List[GoogleCloudVisionV1p4beta1Vertex]
    normalizedVertices: typing.List[GoogleCloudVisionV1p4beta1NormalizedVertex]

class GoogleCloudVisionV1p2beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p2beta1Property(typing_extensions.TypedDict, total=False):
    uint64Value: str
    value: str
    name: str

class GoogleCloudVisionV1p2beta1Symbol(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    text: str

class Property(typing_extensions.TypedDict, total=False):
    value: str
    uint64Value: str
    name: str

class GoogleCloudVisionV1p2beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    value: str
    key: str
