import typing

import typing_extensions

class GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    score: float
    languageCode: str
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    name: str
    mid: str

class GoogleCloudVisionV1p3beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource
    mimeType: str
    content: str

class GoogleCloudVisionV1p2beta1Block(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    paragraphs: typing.List[GoogleCloudVisionV1p2beta1Paragraph]
    confidence: float

class GoogleCloudVisionV1p3beta1Symbol(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    text: str
    confidence: float
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly

class GoogleCloudVisionV1p1beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class GoogleCloudVisionV1p2beta1Property(typing_extensions.TypedDict, total=False):
    uint64Value: str
    name: str
    value: str

class GoogleCloudVisionV1p4beta1Position(typing_extensions.TypedDict, total=False):
    z: float
    y: float
    x: float

class GoogleCloudVisionV1p2beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    label: str

class GoogleCloudVisionV1p1beta1BatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p1beta1AnnotateFileResponse]

class GoogleCloudVisionV1p3beta1WebDetection(typing_extensions.TypedDict, total=False):
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebLabel]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebPage]
    webEntities: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebEntity]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]

class GoogleCloudVisionV1p3beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    uint64Value: str

class DetectedLanguage(typing_extensions.TypedDict, total=False):
    confidence: float
    languageCode: str

class GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

class Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class GoogleCloudVisionV1p3beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    pages: typing.List[GoogleCloudVisionV1p3beta1Page]

class GoogleCloudVisionV1p1beta1Image(typing_extensions.TypedDict, total=False):
    source: GoogleCloudVisionV1p1beta1ImageSource
    content: str

class GoogleCloudVisionV1p4beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p1beta1InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudVisionV1p1beta1GcsSource
    content: str
    mimeType: str

class WebLabel(typing_extensions.TypedDict, total=False):
    languageCode: str
    label: str

class GoogleCloudVisionV1p1beta1BatchAnnotateImagesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p1beta1AnnotateImageResponse]

class GoogleCloudVisionV1p4beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    referenceImages: typing.List[GoogleCloudVisionV1p4beta1ReferenceImage]
    statuses: typing.List[Status]

class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateImagesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleCloudVisionV1p1beta1AnnotateImageRequest]
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig
    parent: str

class GoogleCloudVisionV1p1beta1ProductSearchParams(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    productSet: str
    productCategories: typing.List[str]
    filter: str

class GoogleCloudVisionV1p1beta1Product(typing_extensions.TypedDict, total=False):
    description: str
    productLabels: typing.List[GoogleCloudVisionV1p1beta1ProductKeyValue]
    name: str
    displayName: str
    productCategory: str

class GoogleCloudVisionV1p4beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    createTime: str
    updateTime: str

class GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p2beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p1beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    description: str
    score: float

class GoogleCloudVisionV1p2beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p1beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    fullTextAnnotation: GoogleCloudVisionV1p1beta1TextAnnotation
    labelAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p1beta1ProductSearchResults
    faceAnnotations: typing.List[GoogleCloudVisionV1p1beta1FaceAnnotation]
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    webDetection: GoogleCloudVisionV1p1beta1WebDetection
    cropHintsAnnotation: GoogleCloudVisionV1p1beta1CropHintsAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p1beta1ImageProperties
    context: GoogleCloudVisionV1p1beta1ImageAnnotationContext
    logoAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    textAnnotations: typing.List[GoogleCloudVisionV1p1beta1EntityAnnotation]
    safeSearchAnnotation: GoogleCloudVisionV1p1beta1SafeSearchAnnotation
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation
    ]
    error: Status

class GoogleCloudVisionV1p1beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVisionV1p1beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    name: str
    mid: str
    languageCode: str
    score: float

class GoogleCloudVisionV1p4beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

class GoogleCloudVisionV1p4beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    fdBoundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    panAngle: float
    landmarks: typing.List[GoogleCloudVisionV1p4beta1FaceAnnotationLandmark]
    rollAngle: float
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    recognitionResult: typing.List[GoogleCloudVisionV1p4beta1FaceRecognitionResult]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float

class GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]
    isPrefix: bool

class GoogleCloudVisionV1p1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p1beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p4beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    violence: typing_extensions.Literal[
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
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p3beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult
    ]
    results: typing.List[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]
    indexTime: str

class GoogleCloudVisionV1p4beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p4beta1GcsDestination

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class GoogleCloudVisionV1p4beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p4beta1DominantColorsAnnotation

class GoogleCloudVisionV1p3beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

class GoogleCloudVisionV1p4beta1Product(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    description: str
    productCategory: str
    productLabels: typing.List[GoogleCloudVisionV1p4beta1ProductKeyValue]

class GoogleCloudVisionV1p2beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    url: str
    fullMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    pageTitle: str
    score: float

class GoogleCloudVisionV1p2beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    spoof: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    adult: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    medical: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class ImportProductSetsResponse(typing_extensions.TypedDict, total=False):
    statuses: typing.List[Status]
    referenceImages: typing.List[ReferenceImage]

class TextProperty(typing_extensions.TypedDict, total=False):
    detectedLanguages: typing.List[DetectedLanguage]
    detectedBreak: DetectedBreak

class WebDetection(typing_extensions.TypedDict, total=False):
    pagesWithMatchingImages: typing.List[WebPage]
    visuallySimilarImages: typing.List[WebImage]
    bestGuessLabels: typing.List[WebLabel]
    partialMatchingImages: typing.List[WebImage]
    webEntities: typing.List[WebEntity]
    fullMatchingImages: typing.List[WebImage]

class GoogleCloudVisionV1p3beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p3beta1CropHint]

class GoogleCloudVisionV1p3beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    properties: typing.List[GoogleCloudVisionV1p3beta1Property]
    score: float
    description: str
    locale: str
    mid: str
    confidence: float
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    locations: typing.List[GoogleCloudVisionV1p3beta1LocationInfo]
    topicality: float

class GoogleCloudVisionV1p4beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    pages: typing.List[GoogleCloudVisionV1p4beta1Page]

class GoogleCloudVisionV1p1beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    pages: typing.List[GoogleCloudVisionV1p1beta1Page]
    text: str

class GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    name: str
    score: float
    mid: str

class GoogleCloudVisionV1p1beta1WebDetection(typing_extensions.TypedDict, total=False):
    fullMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    webEntities: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebEntity]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebLabel]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebPage]

class GoogleCloudVisionV1p2beta1Product(typing_extensions.TypedDict, total=False):
    productCategory: str
    displayName: str
    description: str
    productLabels: typing.List[GoogleCloudVisionV1p2beta1ProductKeyValue]
    name: str

class GoogleCloudVisionV1p3beta1OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudVisionV1p3beta1GcsDestination
    batchSize: int

class GoogleCloudVisionV1p1beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    image: str
    score: float
    product: GoogleCloudVisionV1p1beta1Product

class GoogleCloudVisionV1p2beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GoogleCloudVisionV1p2beta1GcsSource
    mimeType: str

class GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p2beta1OutputConfig

class EntityAnnotation(typing_extensions.TypedDict, total=False):
    mid: str
    properties: typing.List[Property]
    score: float
    confidence: float
    boundingPoly: BoundingPoly
    description: str
    locale: str
    locations: typing.List[LocationInfo]
    topicality: float

class AsyncAnnotateFileResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation
    ]

class GoogleCloudVisionV1p1beta1AsyncAnnotateFileRequest(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig
    imageContext: GoogleCloudVisionV1p1beta1ImageContext
    features: typing.List[GoogleCloudVisionV1p1beta1Feature]
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig

class GoogleCloudVisionV1p1beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

class GoogleCloudVisionV1p3beta1Page(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    height: int
    blocks: typing.List[GoogleCloudVisionV1p3beta1Block]
    confidence: float
    width: int

class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleCloudVisionV1p1beta1AsyncAnnotateFileRequest]
    parent: str

class GoogleCloudVisionV1p2beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    product: GoogleCloudVisionV1p2beta1Product
    image: str
    score: float

class GoogleCloudVisionV1p3beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    labelAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p3beta1ProductSearchResults
    cropHintsAnnotation: GoogleCloudVisionV1p3beta1CropHintsAnnotation
    logoAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    imagePropertiesAnnotation: GoogleCloudVisionV1p3beta1ImageProperties
    fullTextAnnotation: GoogleCloudVisionV1p3beta1TextAnnotation
    context: GoogleCloudVisionV1p3beta1ImageAnnotationContext
    faceAnnotations: typing.List[GoogleCloudVisionV1p3beta1FaceAnnotation]
    textAnnotations: typing.List[GoogleCloudVisionV1p3beta1EntityAnnotation]
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p3beta1LocalizedObjectAnnotation
    ]
    error: Status
    webDetection: GoogleCloudVisionV1p3beta1WebDetection
    safeSearchAnnotation: GoogleCloudVisionV1p3beta1SafeSearchAnnotation

class GoogleCloudVisionV1p4beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p4beta1ColorInfo]

class GoogleCloudVisionV1p1beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    fullMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]
    pageTitle: str
    score: float
    url: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p1beta1WebDetectionWebImage]

class GoogleCloudVisionV1p1beta1BatchAnnotateImagesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    requests: typing.List[GoogleCloudVisionV1p1beta1AnnotateImageRequest]

class GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    score: float
    name: str
    languageCode: str
    mid: str

class GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    confidence: float

class GoogleCloudVisionV1p1beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p3beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    score: float
    entityId: str

class TextAnnotation(typing_extensions.TypedDict, total=False):
    pages: typing.List[Page]
    text: str

class GoogleCloudVisionV1p1beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig
    totalPages: int
    error: Status
    responses: typing.List[GoogleCloudVisionV1p1beta1AnnotateImageResponse]

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

class GoogleCloudVisionV1p2beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    textAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    productSearchResults: GoogleCloudVisionV1p2beta1ProductSearchResults
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation
    ]
    labelAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    fullTextAnnotation: GoogleCloudVisionV1p2beta1TextAnnotation
    imagePropertiesAnnotation: GoogleCloudVisionV1p2beta1ImageProperties
    logoAnnotations: typing.List[GoogleCloudVisionV1p2beta1EntityAnnotation]
    cropHintsAnnotation: GoogleCloudVisionV1p2beta1CropHintsAnnotation
    safeSearchAnnotation: GoogleCloudVisionV1p2beta1SafeSearchAnnotation
    webDetection: GoogleCloudVisionV1p2beta1WebDetection
    faceAnnotations: typing.List[GoogleCloudVisionV1p2beta1FaceAnnotation]
    context: GoogleCloudVisionV1p2beta1ImageAnnotationContext
    error: Status

class AsyncBatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AsyncAnnotateFileResponse]

class ColorInfo(typing_extensions.TypedDict, total=False):
    score: float
    pixelFraction: float
    color: Color

class GoogleCloudVisionV1p2beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class Product(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    description: str
    productLabels: typing.List[KeyValue]
    productCategory: str

class GoogleCloudVisionV1p1beta1Word(typing_extensions.TypedDict, total=False):
    symbols: typing.List[GoogleCloudVisionV1p1beta1Symbol]
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    confidence: float
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly

class GoogleCloudVisionV1p1beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p1beta1GcsDestination

class Color(typing_extensions.TypedDict, total=False):
    blue: float
    red: float
    alpha: float
    green: float

class GoogleCloudVisionV1p1beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    racy: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
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

class GoogleCloudVisionV1p3beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    importanceFraction: float
    boundingPoly: BoundingPoly

class GoogleCloudVisionV1p1beta1CropHint(typing_extensions.TypedDict, total=False):
    importanceFraction: float
    confidence: float
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly

class GoogleCloudVisionV1p4beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: Status
    totalPages: int
    inputConfig: GoogleCloudVisionV1p4beta1InputConfig
    responses: typing.List[GoogleCloudVisionV1p4beta1AnnotateImageResponse]

class GoogleCloudVisionV1p3beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    mid: str
    name: str
    languageCode: str
    score: float

class GoogleCloudVisionV1p4beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    fullMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    score: float
    pageTitle: str
    url: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]

class GoogleCloudVisionV1p2beta1Position(typing_extensions.TypedDict, total=False):
    z: float
    x: float
    y: float

class GoogleCloudVisionV1p2beta1TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    pages: typing.List[GoogleCloudVisionV1p2beta1Page]

class GoogleCloudVisionV1p1beta1ColorInfo(typing_extensions.TypedDict, total=False):
    pixelFraction: float
    score: float
    color: Color

class GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p3beta1OutputConfig

class GoogleCloudVisionV1p3beta1ImportProductSetsResponse(
    typing_extensions.TypedDict, total=False
):
    referenceImages: typing.List[GoogleCloudVisionV1p3beta1ReferenceImage]
    statuses: typing.List[Status]

class WebEntity(typing_extensions.TypedDict, total=False):
    description: str
    score: float
    entityId: str

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

class GoogleCloudVisionV1p3beta1Paragraph(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    confidence: float
    words: typing.List[GoogleCloudVisionV1p3beta1Word]
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly

class Paragraph(typing_extensions.TypedDict, total=False):
    property: TextProperty
    boundingBox: BoundingPoly
    confidence: float
    words: typing.List[Word]

class GoogleCloudVisionV1p4beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    boundingPolys: typing.List[GoogleCloudVisionV1p4beta1BoundingPoly]
    uri: str
    name: str

class Block(typing_extensions.TypedDict, total=False):
    boundingBox: BoundingPoly
    property: TextProperty
    confidence: float
    paragraphs: typing.List[Paragraph]
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]

class GoogleCloudVisionV1p4beta1Page(typing_extensions.TypedDict, total=False):
    blocks: typing.List[GoogleCloudVisionV1p4beta1Block]
    width: int
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    confidence: float
    height: int

class GoogleCloudVisionV1p2beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]

class GoogleCloudVisionV1p4beta1ColorInfo(typing_extensions.TypedDict, total=False):
    score: float
    pixelFraction: float
    color: Color

class Page(typing_extensions.TypedDict, total=False):
    confidence: float
    height: int
    property: TextProperty
    blocks: typing.List[Block]
    width: int

class GoogleCloudVisionV1p3beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

class GoogleCloudVisionV1p2beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult
    ]
    indexTime: str
    results: typing.List[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p2beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p2beta1AnnotateImageResponse]
    totalPages: int
    error: Status
    inputConfig: GoogleCloudVisionV1p2beta1InputConfig

class ProductSearchResults(typing_extensions.TypedDict, total=False):
    productGroupedResults: typing.List[GroupedResult]
    indexTime: str
    results: typing.List[Result]

class GoogleCloudVisionV1p3beta1InputConfig(typing_extensions.TypedDict, total=False):
    mimeType: str
    gcsSource: GoogleCloudVisionV1p3beta1GcsSource
    content: str

class GoogleCloudVisionV1p2beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GcsDestination

class GoogleCloudVisionV1p3beta1Word(typing_extensions.TypedDict, total=False):
    symbols: typing.List[GoogleCloudVisionV1p3beta1Symbol]
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float

class GoogleCloudVisionV1p1beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p1beta1ColorInfo]

class GoogleCloudVisionV1p1beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    locations: typing.List[GoogleCloudVisionV1p1beta1LocationInfo]
    locale: str
    mid: str
    confidence: float
    description: str
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    properties: typing.List[GoogleCloudVisionV1p1beta1Property]
    score: float
    topicality: float

class FaceAnnotation(typing_extensions.TypedDict, total=False):
    boundingPoly: BoundingPoly
    detectionConfidence: float
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    panAngle: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarks: typing.List[Landmark]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: BoundingPoly
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    rollAngle: float
    landmarkingConfidence: float

class GoogleCloudVisionV1p3beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

class GoogleCloudVisionV1p1beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

class GoogleCloudVisionV1p2beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    topicality: float
    confidence: float
    locations: typing.List[GoogleCloudVisionV1p2beta1LocationInfo]
    properties: typing.List[GoogleCloudVisionV1p2beta1Property]
    description: str
    locale: str
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    mid: str
    score: float

class GoogleCloudVisionV1p1beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    score: float
    url: str

class LocalizedObjectAnnotation(typing_extensions.TypedDict, total=False):
    name: str
    languageCode: str
    mid: str
    boundingPoly: BoundingPoly
    score: float

class GoogleCloudVisionV1p4beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

class CropHintsAnnotation(typing_extensions.TypedDict, total=False):
    cropHints: typing.List[CropHint]

class GoogleCloudVisionV1p2beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p2beta1CropHint]

class LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p2beta1OutputConfig(typing_extensions.TypedDict, total=False):
    batchSize: int
    gcsDestination: GoogleCloudVisionV1p2beta1GcsDestination

class GoogleCloudVisionV1p2beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[GoogleCloudVisionV1p2beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudVisionV1p2beta1Vertex]

class ObjectAnnotation(typing_extensions.TypedDict, total=False):
    mid: str
    name: str
    score: float
    languageCode: str

class GoogleCloudVisionV1p1beta1AnnotateFileRequest(
    typing_extensions.TypedDict, total=False
):
    pages: typing.List[int]
    inputConfig: GoogleCloudVisionV1p1beta1InputConfig
    imageContext: GoogleCloudVisionV1p1beta1ImageContext
    features: typing.List[GoogleCloudVisionV1p1beta1Feature]

class GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation
    ]
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    results: typing.List[GoogleCloudVisionV1p3beta1ProductSearchResultsResult]

class GoogleCloudVisionV1p4beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    uri: str

class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse]

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

class KeyValue(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class GoogleCloudVisionV1p4beta1CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    importanceFraction: float
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly

class GoogleCloudVisionV1p1beta1Block(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    paragraphs: typing.List[GoogleCloudVisionV1p1beta1Paragraph]
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    confidence: float

class AnnotateFileResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AnnotateImageResponse]
    error: Status
    inputConfig: InputConfig
    totalPages: int

class GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p2beta1WebDetection(typing_extensions.TypedDict, total=False):
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebPage]
    webEntities: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebEntity]
    bestGuessLabels: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebLabel]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p2beta1WebDetectionWebImage]

class ImageProperties(typing_extensions.TypedDict, total=False):
    dominantColors: DominantColorsAnnotation

class DominantColorsAnnotation(typing_extensions.TypedDict, total=False):
    colors: typing.List[ColorInfo]

class GoogleCloudVisionV1p2beta1Page(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    width: int
    blocks: typing.List[GoogleCloudVisionV1p2beta1Block]
    confidence: float
    height: int

class GoogleCloudVisionV1p1beta1BatchAnnotateFilesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleCloudVisionV1p1beta1AnnotateFileRequest]
    parent: str

class GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p4beta1FaceRecognitionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    celebrity: GoogleCloudVisionV1p4beta1Celebrity

class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p3beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p3beta1ColorInfo]

class WebPage(typing_extensions.TypedDict, total=False):
    url: str
    partialMatchingImages: typing.List[WebImage]
    fullMatchingImages: typing.List[WebImage]
    score: float
    pageTitle: str

class GoogleCloudVisionV1p4beta1AnnotateImageResponse(
    typing_extensions.TypedDict, total=False
):
    textAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    imagePropertiesAnnotation: GoogleCloudVisionV1p4beta1ImageProperties
    fullTextAnnotation: GoogleCloudVisionV1p4beta1TextAnnotation
    safeSearchAnnotation: GoogleCloudVisionV1p4beta1SafeSearchAnnotation
    localizedObjectAnnotations: typing.List[
        GoogleCloudVisionV1p4beta1LocalizedObjectAnnotation
    ]
    context: GoogleCloudVisionV1p4beta1ImageAnnotationContext
    webDetection: GoogleCloudVisionV1p4beta1WebDetection
    cropHintsAnnotation: GoogleCloudVisionV1p4beta1CropHintsAnnotation
    error: Status
    productSearchResults: GoogleCloudVisionV1p4beta1ProductSearchResults
    landmarkAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    faceAnnotations: typing.List[GoogleCloudVisionV1p4beta1FaceAnnotation]
    logoAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]
    labelAnnotations: typing.List[GoogleCloudVisionV1p4beta1EntityAnnotation]

class GoogleCloudVisionV1p3beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVisionV1p3beta1FaceAnnotationLandmark]
    detectionConfidence: float
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    fdBoundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    landmarkingConfidence: float
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    rollAngle: float
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    panAngle: float
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p4beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    vertices: typing.List[GoogleCloudVisionV1p4beta1Vertex]
    normalizedVertices: typing.List[GoogleCloudVisionV1p4beta1NormalizedVertex]

class AsyncBatchAnnotateImagesResponse(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class GoogleCloudVisionV1p2beta1LocalizedObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    mid: str
    score: float
    name: str
    languageCode: str

class GoogleCloudVisionV1p3beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p3beta1DominantColorsAnnotation

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

class GoogleCloudVisionV1p2beta1ColorInfo(typing_extensions.TypedDict, total=False):
    pixelFraction: float
    score: float
    color: Color

class GoogleCloudVisionV1p4beta1EntityAnnotation(
    typing_extensions.TypedDict, total=False
):
    description: str
    topicality: float
    confidence: float
    locale: str
    score: float
    mid: str
    locations: typing.List[GoogleCloudVisionV1p4beta1LocationInfo]
    properties: typing.List[GoogleCloudVisionV1p4beta1Property]
    boundingPoly: GoogleCloudVisionV1p4beta1BoundingPoly

class GoogleCloudVisionV1p3beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguage
    ]
    detectedBreak: GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreak

class GoogleCloudVisionV1p1beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str
    createTime: str

class GoogleCloudVisionV1p1beta1ImageContext(typing_extensions.TypedDict, total=False):
    cropHintsParams: GoogleCloudVisionV1p1beta1CropHintsParams
    productSearchParams: GoogleCloudVisionV1p1beta1ProductSearchParams
    webDetectionParams: GoogleCloudVisionV1p1beta1WebDetectionParams
    languageHints: typing.List[str]
    latLongRect: GoogleCloudVisionV1p1beta1LatLongRect

class AnnotateImageResponse(typing_extensions.TypedDict, total=False):
    error: Status
    faceAnnotations: typing.List[FaceAnnotation]
    safeSearchAnnotation: SafeSearchAnnotation
    localizedObjectAnnotations: typing.List[LocalizedObjectAnnotation]
    textAnnotations: typing.List[EntityAnnotation]
    labelAnnotations: typing.List[EntityAnnotation]
    cropHintsAnnotation: CropHintsAnnotation
    webDetection: WebDetection
    logoAnnotations: typing.List[EntityAnnotation]
    context: ImageAnnotationContext
    fullTextAnnotation: TextAnnotation
    landmarkAnnotations: typing.List[EntityAnnotation]
    productSearchResults: ProductSearchResults
    imagePropertiesAnnotation: ImageProperties

class GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p3beta1ReferenceImage(
    typing_extensions.TypedDict, total=False
):
    uri: str
    boundingPolys: typing.List[GoogleCloudVisionV1p3beta1BoundingPoly]
    name: str

class BatchOperationMetadata(typing_extensions.TypedDict, total=False):
    submitTime: str
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]

class DetectedBreak(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]
    isPrefix: bool

class GoogleCloudVisionV1p1beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p1beta1CropHint]

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

class GoogleCloudVisionV1p3beta1CropHint(typing_extensions.TypedDict, total=False):
    confidence: float
    boundingPoly: GoogleCloudVisionV1p3beta1BoundingPoly
    importanceFraction: float

class GoogleCloudVisionV1p3beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p4beta1Block(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    paragraphs: typing.List[GoogleCloudVisionV1p4beta1Paragraph]
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    confidence: float
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty

class GoogleCloudVisionV1p4beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

class GoogleCloudVisionV1p1beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    landmarks: typing.List[GoogleCloudVisionV1p1beta1FaceAnnotationLandmark]
    rollAngle: float
    tiltAngle: float
    detectionConfidence: float
    panAngle: float
    fdBoundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    landmarkingConfidence: float

class GoogleCloudVisionV1p3beta1ColorInfo(typing_extensions.TypedDict, total=False):
    score: float
    pixelFraction: float
    color: Color

class GoogleCloudVisionV1p2beta1WebDetectionWebImage(
    typing_extensions.TypedDict, total=False
):
    url: str
    score: float

class GoogleCloudVisionV1p4beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p3beta1AnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p3beta1AnnotateImageResponse]
    totalPages: int
    error: Status
    inputConfig: GoogleCloudVisionV1p3beta1InputConfig

class GoogleCloudVisionV1p3beta1SafeSearchAnnotation(
    typing_extensions.TypedDict, total=False
):
    violence: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
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

class GoogleCloudVisionV1p4beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]
    submitTime: str

class GoogleCloudVisionV1p2beta1FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    joyLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    surpriseLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    tiltAngle: float
    rollAngle: float
    fdBoundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    landmarkingConfidence: float
    landmarks: typing.List[GoogleCloudVisionV1p2beta1FaceAnnotationLandmark]
    underExposedLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    sorrowLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    headwearLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    detectionConfidence: float
    panAngle: float
    blurredLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    angerLikelihood: typing_extensions.Literal[
        "UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY"
    ]

class GoogleCloudVisionV1p2beta1ImageAnnotationContext(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p4beta1Symbol(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    text: str

class GoogleCloudVisionV1p4beta1Celebrity(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    displayName: str

class GoogleCloudVisionV1p4beta1WebDetection(typing_extensions.TypedDict, total=False):
    bestGuessLabels: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebLabel]
    webEntities: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebEntity]
    fullMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    partialMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]
    pagesWithMatchingImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebPage]
    visuallySimilarImages: typing.List[GoogleCloudVisionV1p4beta1WebDetectionWebImage]

class GoogleCloudVisionV1p3beta1Position(typing_extensions.TypedDict, total=False):
    z: float
    x: float
    y: float

class GoogleCloudVisionV1p3beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudVisionV1p3beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    product: GoogleCloudVisionV1p3beta1Product
    image: str
    score: float

class GoogleCloudVisionV1p2beta1Paragraph(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    words: typing.List[GoogleCloudVisionV1p2beta1Word]
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    confidence: float

class GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p2beta1ProductSearchResultsResult]
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation
    ]

class GoogleCloudVisionV1p1beta1Page(typing_extensions.TypedDict, total=False):
    width: int
    confidence: float
    blocks: typing.List[GoogleCloudVisionV1p1beta1Block]
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    height: int

class BatchAnnotateFilesResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AnnotateFileResponse]

class BoundingPoly(typing_extensions.TypedDict, total=False):
    normalizedVertices: typing.List[NormalizedVertex]
    vertices: typing.List[Vertex]

class GoogleCloudVisionV1p1beta1AnnotateImageRequest(
    typing_extensions.TypedDict, total=False
):
    imageContext: GoogleCloudVisionV1p1beta1ImageContext
    features: typing.List[GoogleCloudVisionV1p1beta1Feature]
    image: GoogleCloudVisionV1p1beta1Image

class GoogleCloudVisionV1p1beta1Paragraph(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    confidence: float
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    words: typing.List[GoogleCloudVisionV1p1beta1Word]

class GoogleCloudVisionV1p4beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

class GoogleCloudVisionV1p4beta1CropHintsAnnotation(
    typing_extensions.TypedDict, total=False
):
    cropHints: typing.List[GoogleCloudVisionV1p4beta1CropHint]

class GoogleCloudVisionV1p4beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]
    indexTime: str
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult
    ]

class GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse]

class GoogleCloudVisionV1p2beta1ProductKeyValue(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

class GoogleCloudVisionV1p4beta1LocationInfo(typing_extensions.TypedDict, total=False):
    latLng: LatLng

class GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    mid: str
    languageCode: str
    score: float
    name: str

class GoogleCloudVisionV1p1beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

class GoogleCloudVisionV1p4beta1InputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GoogleCloudVisionV1p4beta1GcsSource
    mimeType: str

class GoogleCloudVisionV1p3beta1WebDetectionWebLabel(
    typing_extensions.TypedDict, total=False
):
    label: str
    languageCode: str

class GoogleCloudVisionV1p1beta1ImageSource(typing_extensions.TypedDict, total=False):
    gcsImageUri: str
    imageUri: str

class GoogleCloudVisionV1p1beta1Symbol(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p1beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p1beta1BoundingPoly
    text: str
    confidence: float

class GoogleCloudVisionV1p3beta1BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    submitTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "SUCCESSFUL", "FAILED", "CANCELLED"
    ]

class GoogleCloudVisionV1p1beta1WebDetectionParams(
    typing_extensions.TypedDict, total=False
):
    includeGeoResults: bool

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

class GoogleCloudVisionV1p4beta1Paragraph(typing_extensions.TypedDict, total=False):
    words: typing.List[GoogleCloudVisionV1p4beta1Word]
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    confidence: float
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly

class GoogleCloudVisionV1p2beta1Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class Result(typing_extensions.TypedDict, total=False):
    product: Product
    image: str
    score: float

class ImageAnnotationContext(typing_extensions.TypedDict, total=False):
    uri: str
    pageNumber: int

class GoogleCloudVisionV1p1beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p1beta1DominantColorsAnnotation

class GoogleCloudVisionV1p2beta1ImageProperties(
    typing_extensions.TypedDict, total=False
):
    dominantColors: GoogleCloudVisionV1p2beta1DominantColorsAnnotation

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

class GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p1beta1OutputConfig

class GoogleCloudVisionV1p1beta1LatLongRect(typing_extensions.TypedDict, total=False):
    minLatLng: LatLng
    maxLatLng: LatLng

class GroupedResult(typing_extensions.TypedDict, total=False):
    boundingPoly: BoundingPoly
    objectAnnotations: typing.List[ObjectAnnotation]
    results: typing.List[Result]

class ReferenceImage(typing_extensions.TypedDict, total=False):
    uri: str
    boundingPolys: typing.List[BoundingPoly]
    name: str

class Word(typing_extensions.TypedDict, total=False):
    property: TextProperty
    symbols: typing.List[Symbol]
    confidence: float
    boundingBox: BoundingPoly

class GoogleCloudVisionV1p1beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    vertices: typing.List[GoogleCloudVisionV1p1beta1Vertex]
    normalizedVertices: typing.List[GoogleCloudVisionV1p1beta1NormalizedVertex]

class GoogleCloudVisionV1p2beta1Word(typing_extensions.TypedDict, total=False):
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty
    symbols: typing.List[GoogleCloudVisionV1p2beta1Symbol]

class GoogleCloudVisionV1p3beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

class GoogleCloudVisionV1p3beta1Product(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    description: str
    productCategory: str
    productLabels: typing.List[GoogleCloudVisionV1p3beta1ProductKeyValue]

class NormalizedVertex(typing_extensions.TypedDict, total=False):
    x: float
    y: float

class GoogleCloudVisionV1p1beta1Position(typing_extensions.TypedDict, total=False):
    z: float
    x: float
    y: float

class GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]
    objectAnnotations: typing.List[
        GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotation
    ]
    boundingPoly: GoogleCloudVisionV1p1beta1BoundingPoly

class GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudVisionV1p4beta1OutputConfig

class GoogleCloudVisionV1p4beta1Word(typing_extensions.TypedDict, total=False):
    property: GoogleCloudVisionV1p4beta1TextAnnotationTextProperty
    boundingBox: GoogleCloudVisionV1p4beta1BoundingPoly
    confidence: float
    symbols: typing.List[GoogleCloudVisionV1p4beta1Symbol]

class GoogleCloudVisionV1p1beta1Property(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    uint64Value: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]

class GoogleCloudVisionV1p3beta1WebDetectionWebPage(
    typing_extensions.TypedDict, total=False
):
    pageTitle: str
    partialMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]
    url: str
    score: float
    fullMatchingImages: typing.List[GoogleCloudVisionV1p3beta1WebDetectionWebImage]

class GoogleCloudVisionV1p4beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class Position(typing_extensions.TypedDict, total=False):
    y: float
    z: float
    x: float

class GoogleCloudVisionV1p3beta1Block(typing_extensions.TypedDict, total=False):
    blockType: typing_extensions.Literal[
        "UNKNOWN", "TEXT", "TABLE", "PICTURE", "RULER", "BARCODE"
    ]
    boundingBox: GoogleCloudVisionV1p3beta1BoundingPoly
    confidence: float
    property: GoogleCloudVisionV1p3beta1TextAnnotationTextProperty
    paragraphs: typing.List[GoogleCloudVisionV1p3beta1Paragraph]

class GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudVisionV1p4beta1AnnotateFileResponse]

class GoogleCloudVisionV1p3beta1BoundingPoly(typing_extensions.TypedDict, total=False):
    vertices: typing.List[GoogleCloudVisionV1p3beta1Vertex]
    normalizedVertices: typing.List[GoogleCloudVisionV1p3beta1NormalizedVertex]

class GoogleCloudVisionV1p1beta1CropHintsParams(
    typing_extensions.TypedDict, total=False
):
    aspectRatios: typing.List[float]

class Property(typing_extensions.TypedDict, total=False):
    name: str
    uint64Value: str
    value: str

class GoogleCloudVisionV1p2beta1DominantColorsAnnotation(
    typing_extensions.TypedDict, total=False
):
    colors: typing.List[GoogleCloudVisionV1p2beta1ColorInfo]

class GoogleCloudVisionV1p2beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p4beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    score: float
    entityId: str
    description: str

class GoogleCloudVisionV1p4beta1ProductSearchResultsResult(
    typing_extensions.TypedDict, total=False
):
    product: GoogleCloudVisionV1p4beta1Product
    score: float
    image: str

class GoogleCloudVisionV1p4beta1TextAnnotationTextProperty(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguage
    ]

class GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotation(
    typing_extensions.TypedDict, total=False
):
    score: float
    mid: str
    languageCode: str
    name: str

class Symbol(typing_extensions.TypedDict, total=False):
    text: str
    boundingBox: BoundingPoly
    property: TextProperty
    confidence: float

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleCloudVisionV1p4beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    isPrefix: bool
    type: typing_extensions.Literal[
        "UNKNOWN", "SPACE", "SURE_SPACE", "EOL_SURE_SPACE", "HYPHEN", "LINE_BREAK"
    ]

class GoogleCloudVisionV1p2beta1CropHint(typing_extensions.TypedDict, total=False):
    boundingPoly: GoogleCloudVisionV1p2beta1BoundingPoly
    importanceFraction: float
    confidence: float

class GoogleCloudVisionV1p2beta1Symbol(typing_extensions.TypedDict, total=False):
    text: str
    confidence: float
    boundingBox: GoogleCloudVisionV1p2beta1BoundingPoly
    property: GoogleCloudVisionV1p2beta1TextAnnotationTextProperty

class GoogleCloudVisionV1p1beta1ProductSearchResults(
    typing_extensions.TypedDict, total=False
):
    indexTime: str
    results: typing.List[GoogleCloudVisionV1p1beta1ProductSearchResultsResult]
    productGroupedResults: typing.List[
        GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResult
    ]

class WebImage(typing_extensions.TypedDict, total=False):
    url: str
    score: float

class GoogleCloudVisionV1p2beta1WebDetectionWebEntity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    score: float

class OperationMetadata(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    createTime: str
    updateTime: str
