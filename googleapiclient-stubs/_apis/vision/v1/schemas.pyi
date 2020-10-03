import typing

import typing_extensions

class GoogleCloudVisionV1p1beta1CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    importanceFraction: float

class FaceAnnotation(typing_extensions.TypedDict, total=False):
    landmarks: typing.List[Landmark]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    fdBoundingPoly: BoundingPoly
    boundingPoly: BoundingPoly
    tiltAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    rollAngle: float
    panAngle: float

class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p4beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class DetectedLanguage(typing_extensions.TypedDict, total=False):
    languageCode: str
    confidence: float

class InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    mimeType: str
    gcsSource: GcsSource

class GoogleCloudVisionV1p1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p4beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    boundingPolys: typing.List[GoogleCloudVisionV1p4beta1BoundingPoly]
    name: str
    uri: str

class GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    languageCode: str
    mid: str
    score: float
    name: str

class GoogleCloudVisionV1p2beta1Paragraph(typing_extensions.TypedDict, total=False):
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    words: typing.List[GoogleCloudVisionV1p2beta1Word]

class GoogleCloudVisionV1p3beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class GoogleCloudVisionV1p2beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudVisionV1p2beta1ImageAnnotationContext
    fullTextAnnotation: GoogleCloudVisionV1p2beta1TextAnnotation
    safeSearchAnnotation: GoogleCloudVisionV1p2beta1SafeSearchAnnotation
    faceAnnotations: typing.List[GoogleCloudVisionV1p2beta1FaceAnnotation]
    logoAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    error: Status
    textAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p2beta1WebDetection
    labelAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p2beta1ProductSearchResults
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation
    ]
    imagePropertiesAnnotation: GoogleCloudVisionV1p2beta1ImageProperties
    cropHintsAnnotation: GoogleCloudVisionV1p2beta1CropHintsAnnotation

class GoogleCloudVisionV1p2beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage
    ]
    detectedBreak: GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak

class GoogleCloudVisionV1p2beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    topicality: float
    confidence: float
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    score: float
    properties: typing.List[GoogleCloudVisionV1p2beta1Property]
    mid: str
    locale: str
    description: str
    locations: typing.List[GoogleCloudVisionV1p2beta1LocationInfo]

class GoogleCloudVisionV1p4beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    score: float
    image: str
    product: GoogleCloudVisionV1p4beta1Product

class GoogleCloudVisionV1p3beta1InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudVisionV1p3beta1GcsSource
    mimeType: str
    content: str

class GoogleCloudVisionV1p4beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    submitTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    endTime: str

class GoogleCloudVisionV1p4beta1FaceRecognitionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    celebrity: GoogleCloudVisionV1p4beta1Celebrity

class GoogleCloudVisionV1p3beta1Word(typing_extensions.TypedDict, total=False):
    confidence: float
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    symbols: typing.List[GoogleCloudVisionV1p3beta1Symbol]

class AddProductToProductSetRequest(typing_extensions.TypedDict, total=False):
    product: str

class GoogleCloudVisionV1p2beta1Word(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    symbols: typing.List[GoogleCloudVisionV1p2beta1Symbol]
    confidence: float

class GoogleCloudVisionV1p1beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str
    createTime: str

class GoogleCloudVisionV1p1beta1WebDetection(typing_extensions.TypedDict, total=False):
    fullMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebLabel]
    webEntities: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebEntity]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebPage]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]

class GoogleCloudVisionV1p1beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    landmarks: typing.List[GoogleCloudVisionV1p1beta1FaceAnnotationLandmark]
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    rollAngle: float
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    panAngle: float

class ImageAnnotationContext(typing_extensions.TypedDict, total=False):
    pageNumber: int
    uri: str

class GoogleCloudVisionV1p1beta1Block(typing_extensions.TypedDict, total=False):
    paragraphs: typing.List[GoogleCloudVisionV1p1beta1Paragraph]
    confidence: float
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly

class GoogleCloudVisionV1p3beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p3beta1ColorInfo]

class LatLongRect(typing_extensions.TypedDict, total=False):
    maxLatLng: LatLng
    minLatLng: LatLng

class GoogleCloudVisionV1p2beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p1beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: typing.List[GoogleCloudVisionV1p1beta1Page]
    text: str

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination
    batchSize: int

class GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    score: float
    name: str
    mid: str

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

class GoogleCloudVisionV1p4beta1Celebrity(typing_extensions.TypedDict, total=False):
    name: str
    description: str
    displayName: str

class BatchAnnotateImagesResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AnnotateImageResponse]

class GoogleCloudVisionV1p4beta1Symbol(typing_extensions.TypedDict, total=False):
    text: str
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty

class GoogleCloudVisionV1p4beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult
    ]
    indexTime: str

class BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[NormalizedVertex]
    vertices: typing.List[Vertex]

class GoogleCloudVisionV1p2beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class GoogleCloudVisionV1p2beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class CropHintsParams(typing_extensions.TypedDict, total=False):
    aspectRatios: typing.List[float]

class GoogleCloudVisionV1p2beta1FaceAnnotationLandmark(
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
    position: GoogleCloudVisionV1p2beta1Position

class BatchOperationMetadata(typing_extensions.TypedDict, total=False):
    submitTime: str
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]

class AnnotateFileResponse(typing_extensions.TypedDict, total=False):
    inputConfig: InputConfig
    totalPages: int
    responses: typing.List[AnnotateImageResponse]
    error: Status

class GoogleCloudVisionV1p2beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p2beta1GcsDestination

class ListProductsResponse(typing_extensions.TypedDict, total=False):
    products: typing.List[Product]
    nextPageToken: str

class GoogleCloudVisionV1p4beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    responses: typing.List[GoogleCloudVisionV1p4beta1AnnotateImageResponse]
    inputConfig: GoogleCloudVisionV1p4beta1InputConfig
    totalPages: int

class NormalizedVertex(typing_extensions.TypedDict, total=False):
    y: float
    x: float

class GoogleCloudVisionV1p3beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    statuses: typing.List[Status]
    referenceImages: typing.List[GoogleCloudVisionV1p3beta1ReferenceImage]

class Color(typing_extensions.TypedDict, total=False):
    green: float
    alpha: float
    red: float
    blue: float

class ReferenceImage(typing_extensions.TypedDict, total=False):
    boundingPolys: typing.List[BoundingPoly]
    uri: str
    name: str

class PurgeProductsRequest(typing_extensions.TypedDict, total=False):
    productSetPurgeConfig: ProductSetPurgeConfig
    force: bool
    deleteOrphanProducts: bool

class BatchAnnotateImagesRequest(typing_extensions.TypedDict, total=False):
    parent: str
    requests: typing.List[AnnotateImageRequest]

class ObjectAnnotation(typing_extensions.TypedDict, total=False):
    name: str
    languageCode: str
    score: float
    mid: str

class Page(typing_extensions.TypedDict, total=False):
    confidence: float
    property: TextProperty
    width: int
    blocks: typing.List[Block]
    height: int

class AsyncAnnotateFileResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class GoogleCloudVisionV1p4beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p4beta1CropHint]

class AsyncBatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p4beta1CropHint(typing_extensions.TypedDict, total=False):
    importanceFraction: float
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float

class ProductSetPurgeConfig(typing_extensions.TypedDict, total=False):
    productSetId: str

class GoogleCloudVisionV1p3beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p1beta1Symbol(typing_extensions.TypedDict, total=False):
    text: str
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    confidence: float

class GoogleCloudVisionV1p3beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    panAngle: float
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarks: typing.List[GoogleCloudVisionV1p3beta1FaceAnnotationLandmark]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    rollAngle: float
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    detectionConfidence: float

class GoogleCloudVisionV1p1beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p1beta1ColorInfo]

class GoogleCloudVisionV1p4beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p4beta1ColorInfo]

class GoogleCloudVisionV1p1beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    score: float
    entityId: str
    description: str

class GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    score: float
    name: str
    mid: str

class Result(typing_extensions.TypedDict, total=False):
    image: str
    score: float
    product: Product

class GoogleCloudVisionV1p3beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[GoogleCloudVisionV1p3beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudVisionV1p3beta1Vertex]

class GoogleCloudVisionV1p3beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p3beta1CropHint]

class GoogleCloudVisionV1p2beta1WebDetection(typing_extensions.TypedDict, total=False):
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebPage]
    webEntities: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebEntity]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebLabel]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]

class ImageProperties(typing_extensions.TypedDict, total=False):
    dominantColors: DominantColorsAnnotation

class GoogleCloudVisionV1p4beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p2beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p3beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    score: float
    fullMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    pageTitle: str
    url: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]

class Position(typing_extensions.TypedDict, total=False):
    z: float
    x: float
    y: float

class GoogleCloudVisionV1p4beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p3beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    product: GoogleCloudVisionV1p3beta1Product
    score: float

class GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

class GoogleCloudVisionV1p4beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p4beta1DominantColorsAnnotation

class GoogleCloudVisionV1p1beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVisionV1p4beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig

class GoogleCloudVisionV1p1beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult
    ]
    indexTime: str
    results: typing.List[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]

class Word(typing_extensions.TypedDict, total=False):
    property: TextProperty
    symbols: typing.List[Symbol]
    boundingBox: BoundingPoly
    confidence: float

class GoogleCloudVisionV1p4beta1Property(typing_extensions.TypedDict, total=False):
    value: str
    uint64Value: str
    name: str

class ImportProductSetsRequest(typing_extensions.TypedDict, total=False):
    inputConfig: ImportProductSetsInputConfig

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class ListProductsInProductSetResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: typing.List[Product]

class GoogleCloudVisionV1p3beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

class ImageContext(typing_extensions.TypedDict, total=False):
    languageHints: typing.List[str]
    webDetectionParams: WebDetectionParams
    productSearchParams: ProductSearchParams
    cropHintsParams: CropHintsParams
    latLongRect: LatLongRect

class GoogleCloudVisionV1p3beta1Symbol(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    text: str

class GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation
    ]

class TextAnnotation(typing_extensions.TypedDict, total=False):
    text: str
    pages: typing.List[Page]

class GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation
    ]
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    results: typing.List[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p4beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p1beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    y: float
    z: float

class EntityAnnotation(typing_extensions.TypedDict, total=False):
    locations: typing.List[LocationInfo]
    description: str
    locale: str
    confidence: float
    topicality: float
    mid: str
    score: float
    properties: typing.List[Property]
    boundingPoly: BoundingPoly

class GoogleCloudVisionV1p4beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    done: bool
    name: str
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudVisionV1p4beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]

class ProductSearchResults(typing_extensions.TypedDict, total=False):
    results: typing.List[Result]
    productGroupedResults: typing.List[GroupedResult]
    indexTime: str

class GoogleCloudVisionV1p4beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[GoogleCloudVisionV1p4beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudVisionV1p4beta1Vertex]

class CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingPoly: BoundingPoly
    importanceFraction: float

class ImageSource(typing_extensions.TypedDict, total=False):
    imageUri: str
    gcsImageUri: str

class GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

class ListReferenceImagesResponse(typing_extensions.TypedDict, total=False):
    referenceImages: typing.List[ReferenceImage]
    pageSize: int
    nextPageToken: str

class GoogleCloudVisionV1p4beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    score: float
    confidence: float
    mid: str
    topicality: float
    locale: str
    description: str
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    properties: typing.List[GoogleCloudVisionV1p4beta1Property]
    locations: typing.List[GoogleCloudVisionV1p4beta1LocationInfo]

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

class GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]
    isPrefix: bool

class GoogleCloudVisionV1p2beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p3beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVisionV1p1beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

class GoogleCloudVisionV1p2beta1InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudVisionV1p2beta1GcsSource
    mimeType: str
    content: str

class GoogleCloudVisionV1p2beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    inputConfig: GoogleCloudVisionV1p2beta1InputConfig
    responses: typing.List[GoogleCloudVisionV1p2beta1AnnotateImageResponse]
    totalPages: int

class GoogleCloudVisionV1p3beta1Paragraph(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    confidence: float
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    words: typing.List[GoogleCloudVisionV1p3beta1Word]

class AnnotateImageResponse(typing_extensions.TypedDict, total=False):
    safeSearchAnnotation: SafeSearchAnnotation
    imagePropertiesAnnotation: ImageProperties
    webDetection: WebDetection
    cropHintsAnnotation: CropHintsAnnotation
    landmarkAnnotations: typing.List[EntityAnnotation]
    textAnnotations: typing.List[EntityAnnotation]
    fullTextAnnotation: TextAnnotation
    context: ImageAnnotationContext
    labelAnnotations: typing.List[EntityAnnotation]
    productSearchResults: ProductSearchResults
    error: Status
    localizedObjectAnnotations: typing.List[LocalizedObjectAnnotation]
    logoAnnotations: typing.List[EntityAnnotation]
    faceAnnotations: typing.List[FaceAnnotation]

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

class GoogleCloudVisionV1p3beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    submitTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    endTime: str

class AnnotateFileRequest(typing_extensions.TypedDict, total=False):
    inputConfig: InputConfig
    pages: typing.List[int]
    imageContext: ImageContext
    features: typing.List[Feature]

class GoogleCloudVisionV1p3beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    textAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p3beta1TextAnnotation
    cropHintsAnnotation: GoogleCloudVisionV1p3beta1CropHintsAnnotation
    error: Status
    webDetection: GoogleCloudVisionV1p3beta1WebDetection
    logoAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p3beta1ProductSearchResults
    safeSearchAnnotation: GoogleCloudVisionV1p3beta1SafeSearchAnnotation
    labelAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation
    ]
    context: GoogleCloudVisionV1p3beta1ImageAnnotationContext
    faceAnnotations: typing.List[GoogleCloudVisionV1p3beta1FaceAnnotation]
    imagePropertiesAnnotation: GoogleCloudVisionV1p3beta1ImageProperties

class AsyncBatchAnnotateImagesResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    mid: str
    score: float
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    languageCode: str
    name: str

class GoogleCloudVisionV1p2beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    pageTitle: str
    score: float
    partialMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    url: str
    fullMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]

class TextProperty(typing_extensions.TypedDict, total=False):
    detectedBreak: DetectedBreak
    detectedLanguages: typing.List[DetectedLanguage]

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

class GoogleCloudVisionV1p1beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    locations: typing.List[GoogleCloudVisionV1p1beta1LocationInfo]
    score: float
    topicality: float
    locale: str
    description: str
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    properties: typing.List[GoogleCloudVisionV1p1beta1Property]
    confidence: float
    mid: str

class AsyncBatchAnnotateFilesRequest(typing_extensions.TypedDict, total=False):
    requests: typing.List[AsyncAnnotateFileRequest]
    parent: str

class GoogleCloudVisionV1p2beta1Page(typing_extensions.TypedDict, total=False):
    height: int
    blocks: typing.List[GoogleCloudVisionV1p2beta1Block]
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    confidence: float
    width: int

class GoogleCloudVisionV1p3beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p2beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    fdBoundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    rollAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    landmarks: typing.List[GoogleCloudVisionV1p2beta1FaceAnnotationLandmark]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    panAngle: float
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly

class GoogleCloudVisionV1p3beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    pixelFraction: float
    score: float

class GoogleCloudVisionV1p1beta1OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudVisionV1p1beta1GcsDestination
    batchSize: int

class GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    mid: str
    name: str
    languageCode: str
    score: float

class Block(typing_extensions.TypedDict, total=False):
    paragraphs: typing.List[Paragraph]
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    property: TextProperty
    confidence: float
    boundingBox: BoundingPoly

class GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    score: float
    name: str
    mid: str

class GoogleCloudVisionV1p3beta1OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudVisionV1p3beta1GcsDestination
    batchSize: int

class GoogleCloudVisionV1p3beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: typing.List[GoogleCloudVisionV1p3beta1Page]
    text: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class GoogleCloudVisionV1p2beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

class GoogleCloudVisionV1p4beta1Word(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    symbols: typing.List[GoogleCloudVisionV1p4beta1Symbol]
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float

class GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p2beta1OutputConfig

class GoogleCloudVisionV1p3beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p3beta1WebDetection(typing_extensions.TypedDict, total=False):
    bestGuessLabels: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebLabel]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebPage]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    webEntities: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebEntity]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]

class GoogleCloudVisionV1p3beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    properties: typing.List[GoogleCloudVisionV1p3beta1Property]
    mid: str
    topicality: float
    score: float
    confidence: float
    description: str
    locations: typing.List[GoogleCloudVisionV1p3beta1LocationInfo]
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    locale: str

class Feature(typing_extensions.TypedDict, total=False):
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
    maxResults: int

class GoogleCloudVisionV1p1beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p1beta1CropHint]

class GoogleCloudVisionV1p2beta1Property(typing_extensions.TypedDict, total=False):
    uint64Value: str
    name: str
    value: str

class GoogleCloudVisionV1p2beta1Position(typing_extensions.TypedDict, total=False):
    x: float
    z: float
    y: float

class GoogleCloudVisionV1p1beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    score: float
    pageTitle: str
    fullMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    url: str

class GoogleCloudVisionV1p4beta1ColorInfo(typing_extensions.TypedDict, total=False):
    pixelFraction: float
    color: Color
    score: float

class GoogleCloudVisionV1p2beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    pages: typing.List[GoogleCloudVisionV1p2beta1Page]

class GoogleCloudVisionV1p4beta1Position(typing_extensions.TypedDict, total=False):
    y: float
    z: float
    x: float

class SafeSearchAnnotation(typing_extensions.TypedDict, total=False):
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p1beta1Page(typing_extensions.TypedDict, total=False):
    blocks: typing.List[GoogleCloudVisionV1p1beta1Block]
    height: int
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    confidence: float
    width: int

class GoogleCloudVisionV1p4beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage
    ]
    detectedBreak: GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak

class GoogleCloudVisionV1p4beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class RemoveProductFromProductSetRequest(typing_extensions.TypedDict, total=False):
    product: str

class GoogleCloudVisionV1p3beta1Page(typing_extensions.TypedDict, total=False):
    blocks: typing.List[GoogleCloudVisionV1p3beta1Block]
    height: int
    width: int
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    confidence: float

class GoogleCloudVisionV1p1beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

class GoogleCloudVisionV1p2beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    score: float
    description: str

class GoogleCloudVisionV1p3beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    score: float

class KeyValue(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class GoogleCloudVisionV1p1beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float

class GoogleCloudVisionV1p4beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

class AsyncBatchAnnotateImagesRequest(typing_extensions.TypedDict, total=False):
    parent: str
    outputConfig: OutputConfig
    requests: typing.List[AnnotateImageRequest]

class GoogleCloudVisionV1p1beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

class GoogleCloudVisionV1p1beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p1beta1DominantColorsAnnotation

class GoogleCloudVisionV1p3beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class GoogleCloudVisionV1p2beta1Product(typing_extensions.TypedDict, total=False):
    displayName: str
    productCategory: str
    productLabels: typing.List[GoogleCloudVisionV1p2beta1ProductKeyValue]
    name: str
    description: str

class GoogleCloudVisionV1p4beta1WebDetection(typing_extensions.TypedDict, total=False):
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebPage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebLabel]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    webEntities: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebEntity]

class GoogleCloudVisionV1p4beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    pages: typing.List[GoogleCloudVisionV1p4beta1Page]

class GoogleCloudVisionV1p1beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p3beta1Property(typing_extensions.TypedDict, total=False):
    uint64Value: str
    name: str
    value: str

class GoogleCloudVisionV1p1beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    vertices: typing.List[GoogleCloudVisionV1p1beta1Vertex]
    normalizedVertices: typing.List[GoogleCloudVisionV1p1beta1NormalizedVertex]

class GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p4beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float

class BatchAnnotateFilesRequest(typing_extensions.TypedDict, total=False):
    requests: typing.List[AnnotateFileRequest]
    parent: str

class GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p4beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    cropHintsAnnotation: GoogleCloudVisionV1p4beta1CropHintsAnnotation
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    error: Status
    productSearchResults: GoogleCloudVisionV1p4beta1ProductSearchResults
    faceAnnotations: typing.List[GoogleCloudVisionV1p4beta1FaceAnnotation]
    safeSearchAnnotation: GoogleCloudVisionV1p4beta1SafeSearchAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p4beta1ImageProperties
    logoAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p4beta1WebDetection
    textAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p4beta1TextAnnotation
    labelAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    context: GoogleCloudVisionV1p4beta1ImageAnnotationContext
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation
    ]

class GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    score: float
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    mid: str
    languageCode: str
    name: str

class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p4beta1Page(typing_extensions.TypedDict, total=False):
    width: int
    height: int
    blocks: typing.List[GoogleCloudVisionV1p4beta1Block]
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    confidence: float

class GoogleCloudVisionV1p3beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p3beta1DominantColorsAnnotation

class Property(typing_extensions.TypedDict, total=False):
    value: str
    name: str
    uint64Value: str

class GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    mid: str
    score: float
    name: str

class GoogleCloudVisionV1p2beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[GoogleCloudVisionV1p2beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudVisionV1p2beta1Vertex]

class WebDetection(typing_extensions.TypedDict, total=False):
    pagesWithMatchingImages: typing.List[WebPage]
    bestGuessLabels: typing.List[WebLabel]
    visuallySimilarImages: typing.List[WebImage]
    fullMatchingImages: typing.List[WebImage]
    webEntities: typing.List[WebEntity]
    partialMatchingImages: typing.List[WebImage]

class GoogleCloudVisionV1p3beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    uri: str
    name: str
    boundingPolys: typing.List[GoogleCloudVisionV1p3beta1BoundingPoly]

class GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p4beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float
    pageTitle: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]

class GoogleCloudVisionV1p1beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p3beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

class GoogleCloudVisionV1p2beta1Block(typing_extensions.TypedDict, total=False):
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    paragraphs: typing.List[GoogleCloudVisionV1p2beta1Paragraph]

class GoogleCloudVisionV1p2beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p2beta1ColorInfo]

class Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

class GoogleCloudVisionV1p3beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class ImportProductSetsGcsSource(typing_extensions.TypedDict, total=False):
    csvFileUri: str

class GoogleCloudVisionV1p1beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class GoogleCloudVisionV1p4beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p4beta1GcsDestination

class ProductSearchParams(typing_extensions.TypedDict, total=False):
    productCategories: typing.List[str]
    filter: str
    productSet: str
    boundingPoly: BoundingPoly

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p4beta1AnnotateFileResponse]

class GoogleCloudVisionV1p3beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class CropHintsAnnotation(typing_extensions.TypedDict, total=False):
    cropHints: typing.List[CropHint]

class DetectedBreak(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]
    isPrefix: bool

class ProductSet(typing_extensions.TypedDict, total=False):
    displayName: str
    indexTime: str
    name: str
    indexError: Status

class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p2beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    label: str

class GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation
    ]
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    results: typing.List[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]

class LocalizedObjectAnnotation(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    boundingPoly: BoundingPoly
    score: float
    mid: str

class DominantColorsAnnotation(typing_extensions.TypedDict, total=False):
    colors: typing.List[ColorInfo]

class GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p4beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    referenceImages: typing.List[GoogleCloudVisionV1p4beta1ReferenceImage]
    statuses: typing.List[Status]

class GroupedResult(typing_extensions.TypedDict, total=False):
    results: typing.List[Result]
    boundingPoly: BoundingPoly
    objectAnnotations: typing.List[ObjectAnnotation]

class Product(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    productLabels: typing.List[KeyValue]
    displayName: str
    productCategory: str

class GoogleCloudVisionV1p2beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult
    ]
    indexTime: str

class ListProductSetsResponse(typing_extensions.TypedDict, total=False):
    productSets: typing.List[ProductSet]
    nextPageToken: str

class GoogleCloudVisionV1p3beta1Block(typing_extensions.TypedDict, total=False):
    paragraphs: typing.List[GoogleCloudVisionV1p3beta1Paragraph]
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float

class GoogleCloudVisionV1p1beta1InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudVisionV1p1beta1GcsSource
    content: str
    mimeType: str

class GoogleCloudVisionV1p2beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

class GoogleCloudVisionV1p2beta1CropHint(typing_extensions.TypedDict, total=False):
    importanceFraction: float
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float

class GoogleCloudVisionV1p3beta1Product(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    description: str
    productLabels: typing.List[GoogleCloudVisionV1p3beta1ProductKeyValue]
    productCategory: str

class GoogleCloudVisionV1p2beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p2beta1DominantColorsAnnotation

class GoogleCloudVisionV1p2beta1ColorInfo(typing_extensions.TypedDict, total=False):
    score: float
    pixelFraction: float
    color: Color

class GoogleCloudVisionV1p1beta1ColorInfo(typing_extensions.TypedDict, total=False):
    color: Color
    score: float
    pixelFraction: float

class WebDetectionParams(typing_extensions.TypedDict, total=False):
    includeGeoResults: bool

class WebPage(typing_extensions.TypedDict, total=False):
    url: str
    score: float
    partialMatchingImages: typing.List[WebImage]
    fullMatchingImages: typing.List[WebImage]
    pageTitle: str

class GoogleCloudVisionV1p1beta1Word(typing_extensions.TypedDict, total=False):
    confidence: float
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    symbols: typing.List[GoogleCloudVisionV1p1beta1Symbol]

class GoogleCloudVisionV1p2beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p2beta1CropHint]

class GoogleCloudVisionV1p3beta1CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    importanceFraction: float
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly

class GoogleCloudVisionV1p2beta1Symbol(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    text: str

class GoogleCloudVisionV1p3beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    totalPages: int
    responses: typing.List[GoogleCloudVisionV1p3beta1AnnotateImageResponse]
    error: Status
    inputConfig: GoogleCloudVisionV1p3beta1InputConfig

class Image(typing_extensions.TypedDict, total=False):
    source: ImageSource
    content: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ColorInfo(typing_extensions.TypedDict, total=False):
    score: float
    pixelFraction: float
    color: Color

class WebLabel(typing_extensions.TypedDict, total=False):
    languageCode: str
    label: str

class GoogleCloudVisionV1p2beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float

class GoogleCloudVisionV1p3beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult
    ]
    indexTime: str

class GoogleCloudVisionV1p2beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class AnnotateImageRequest(typing_extensions.TypedDict, total=False):
    features: typing.List[Feature]
    image: Image
    imageContext: ImageContext

class ImportProductSetsInputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: ImportProductSetsGcsSource

class GoogleCloudVisionV1p4beta1Block(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    paragraphs: typing.List[GoogleCloudVisionV1p4beta1Paragraph]
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]

class WebEntity(typing_extensions.TypedDict, total=False):
    entityId: str
    score: float
    description: str

class Symbol(typing_extensions.TypedDict, total=False):
    property: TextProperty
    confidence: float
    boundingBox: BoundingPoly
    text: str

class WebImage(typing_extensions.TypedDict, total=False):
    score: float
    url: str

class Paragraph(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingBox: BoundingPoly
    words: typing.List[Word]
    property: TextProperty

class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]

class GoogleCloudVisionV1p4beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    score: float
    entityId: str

class GoogleCloudVisionV1p1beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    score: float
    product: GoogleCloudVisionV1p1beta1Product
    image: str

class ImportProductSetsResponse(typing_extensions.TypedDict, total=False):
    referenceImages: typing.List[ReferenceImage]
    statuses: typing.List[Status]

class LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p2beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    product: GoogleCloudVisionV1p2beta1Product
    score: float

class GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]
    isPrefix: bool

class GoogleCloudVisionV1p3beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p4beta1Product(typing_extensions.TypedDict, total=False):
    productCategory: str
    name: str
    description: str
    displayName: str
    productLabels: typing.List[GoogleCloudVisionV1p4beta1ProductKeyValue]

class GoogleCloudVisionV1p1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p3beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    createTime: str
    updateTime: str

class GoogleCloudVisionV1p4beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class BatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AnnotateFileResponse]

class GoogleCloudVisionV1p1beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    labelAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    context: GoogleCloudVisionV1p1beta1ImageAnnotationContext
    textAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    imagePropertiesAnnotation: GoogleCloudVisionV1p1beta1ImageProperties
    logoAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    cropHintsAnnotation: GoogleCloudVisionV1p1beta1CropHintsAnnotation
    safeSearchAnnotation: GoogleCloudVisionV1p1beta1SafeSearchAnnotation
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    error: Status
    webDetection: GoogleCloudVisionV1p1beta1WebDetection
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation
    ]
    productSearchResults: GoogleCloudVisionV1p1beta1ProductSearchResults
    faceAnnotations: typing.List[GoogleCloudVisionV1p1beta1FaceAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p1beta1TextAnnotation

class GoogleCloudVisionV1p4beta1Paragraph(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    confidence: float
    words: typing.List[GoogleCloudVisionV1p4beta1Word]
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly

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

class GoogleCloudVisionV1p1beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    responses: typing.List[GoogleCloudVisionV1p1beta1AnnotateImageResponse]
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig
    totalPages: int

class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p1beta1Paragraph(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    words: typing.List[GoogleCloudVisionV1p1beta1Word]
    confidence: float
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly

class GoogleCloudVisionV1p3beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    label: str

class GoogleCloudVisionV1p4beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    recognitionResult: typing.List[GoogleCloudVisionV1p4beta1FaceRecognitionResult]
    panAngle: float
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    landmarks: typing.List[GoogleCloudVisionV1p4beta1FaceAnnotationLandmark]
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    landmarkingConfidence: float
    rollAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p4beta1InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudVisionV1p4beta1GcsSource
    mimeType: str
    content: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    results: typing.List[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation
    ]

class GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p3beta1OutputConfig

class GoogleCloudVisionV1p1beta1Product(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    productLabels: typing.List[GoogleCloudVisionV1p1beta1ProductKeyValue]
    description: str
    productCategory: str

class GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

class AsyncAnnotateFileRequest(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig
    features: typing.List[Feature]
    inputConfig: InputConfig
    imageContext: ImageContext

class GoogleCloudVisionV1p2beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class GoogleCloudVisionV1p1beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng
