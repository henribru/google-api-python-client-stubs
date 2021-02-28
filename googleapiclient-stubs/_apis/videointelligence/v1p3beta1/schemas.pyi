import typing

import typing_extensions
@typing.type_check_only
class GoogleCloudVideointelligenceV1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1_Entity(typing_extensions.TypedDict, total=False):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ExplicitContentFrame(
    typing_extensions.TypedDict, total=False
):
    pornographyLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_FaceFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBoxes: typing.List[
        GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1_Entity]
    entity: GoogleCloudVideointelligenceV1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1_LabelFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1_TextFrame]
    segment: GoogleCloudVideointelligenceV1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_Track(typing_extensions.TypedDict, total=False):
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    timestampedObjects: typing.List[GoogleCloudVideointelligenceV1_TimestampedObject]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "FACE_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
        "PERSON_DETECTION",
    ]
    inputUri: str
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    startTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1_ExplicitContentAnnotation
    faceAnnotations: typing.List[GoogleCloudVideointelligenceV1_FaceAnnotation]
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    inputUri: str
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    segmentLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    shotLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_WordInfo(typing_extensions.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1beta2_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame(
    typing_extensions.TypedDict, total=False
):
    pornographyLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_FaceFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBoxes: typing.List[
        GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1beta2_Entity]
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_LabelFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1beta2_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1beta2_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_TextFrame]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1beta2_TimestampedObject
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "FACE_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
        "PERSON_DETECTION",
    ]
    inputUri: str
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    startTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation
    faceAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_FaceAnnotation]
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    inputUri: str
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_WordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame(
    typing_extensions.TypedDict, total=False
):
    pornographyLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_FaceFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBoxes: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p1beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1p1beta1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_TimestampedObject
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "FACE_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
        "PERSON_DETECTION",
    ]
    inputUri: str
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    startTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation
    faceAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_FaceAnnotation]
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    inputUri: str
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame(
    typing_extensions.TypedDict, total=False
):
    pornographyLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_FaceFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBoxes: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p2beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1p2beta1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_TimestampedObject
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "FACE_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
        "PERSON_DETECTION",
    ]
    inputUri: str
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    startTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation
    faceAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_FaceAnnotation]
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    inputUri: str
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoRequest(
    typing_extensions.TypedDict, total=False
):
    features: typing.List[str]
    inputContent: str
    inputUri: str
    locationId: str
    outputUri: str
    videoContext: GoogleCloudVideointelligenceV1p3beta1_VideoContext

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_Celebrity(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    celebrityTracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack(
    typing_extensions.TypedDict, total=False
):
    celebrities: typing.List[GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity]
    faceTrack: GoogleCloudVideointelligenceV1p3beta1_Track

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame(
    typing_extensions.TypedDict, total=False
):
    pornographyLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_FaceFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    includeAttributes: bool
    includeBoundingBoxes: bool
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBoxes: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p3beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelFrame]
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LabelDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    frameConfidenceThreshold: float
    labelDetectionMode: typing_extensions.Literal[
        "LABEL_DETECTION_MODE_UNSPECIFIED",
        "SHOT_MODE",
        "FRAME_MODE",
        "SHOT_AND_FRAME_MODE",
    ]
    model: str
    stationaryCamera: bool
    videoConfidenceThreshold: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    includeAttributes: bool
    includeBoundingBoxes: bool
    includePoseLandmarks: bool

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity(
    typing_extensions.TypedDict, total=False
):
    celebrity: GoogleCloudVideointelligenceV1p3beta1_Celebrity
    confidence: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ShotChangeDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_SpeechContext(
    typing_extensions.TypedDict, total=False
):
    phrases: typing.List[str]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1p3beta1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionConfig(
    typing_extensions.TypedDict, total=False
):
    audioTracks: typing.List[int]
    diarizationSpeakerCount: int
    enableAutomaticPunctuation: bool
    enableSpeakerDiarization: bool
    enableWordConfidence: bool
    filterProfanity: bool
    languageCode: str
    maxAlternatives: int
    speechContexts: typing.List[GoogleCloudVideointelligenceV1p3beta1_SpeechContext]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults
    annotationResultsUri: str
    error: GoogleRpc_Status

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    frameTimestamp: str
    labelAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TextDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    languageHints: typing.List[str]
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_TimestampedObject
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "FACE_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
        "CELEBRITY_RECOGNITION",
        "PERSON_DETECTION",
    ]
    inputUri: str
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    startTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    celebrityRecognitionAnnotations: GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    faceAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_FaceAnnotation]
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    inputUri: str
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_VideoContext(
    typing_extensions.TypedDict, total=False
):
    explicitContentDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentDetectionConfig
    faceDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_FaceDetectionConfig
    labelDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_LabelDetectionConfig
    objectTrackingConfig: GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingConfig
    personDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_PersonDetectionConfig
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    shotChangeDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_ShotChangeDetectionConfig
    speechTranscriptionConfig: GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionConfig
    textDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_TextDetectionConfig

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleLongrunning_Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpc_Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleRpc_Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
