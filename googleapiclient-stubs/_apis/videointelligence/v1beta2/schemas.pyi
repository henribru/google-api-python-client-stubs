import typing

import typing_extensions

class GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p3beta1_Entity]
    version: str
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelSegment]
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelFrame]

class GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1beta2_NormalizedVertex]

class GoogleCloudVideointelligenceV1_Track(typing_extensions.TypedDict, total=False):
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    timestampedObjects: typing.List[GoogleCloudVideointelligenceV1_TimestampedObject]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextFrame]

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame]
    trackId: str
    version: str
    confidence: float
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    trackId: str
    entity: GoogleCloudVideointelligenceV1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1_ObjectTrackingFrame]
    version: str
    confidence: float

class GoogleCloudVideointelligenceV1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1beta2_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    point: GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex
    confidence: float

class GoogleCloudVideointelligenceV1beta2_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1beta2_NormalizedVertex
    name: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_TextFrame]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    entity: GoogleCloudVideointelligenceV1beta2_Entity

class GoogleCloudVideointelligenceV1p1beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextSegment]
    text: str

class GoogleCloudVideointelligenceV1p1beta1_Track(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_TimestampedObject
    ]

class GoogleCloudVideointelligenceV1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1_TextSegment]

class GoogleCloudVideointelligenceV1beta2_TextDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str
    languageHints: typing.List[str]

class GoogleCloudVideointelligenceV1p2beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    annotationResultsUri: str
    annotationResults: GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults

class GoogleCloudVideointelligenceV1p2beta1_Track(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    confidence: float
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_TimestampedObject
    ]

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    left: float
    top: float
    bottom: float
    right: float

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    left: float
    bottom: float
    right: float
    top: float

class GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    value: str
    name: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1p1beta1_WordInfo]

class GoogleCloudVideointelligenceV1p3beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity

class GoogleCloudVideointelligenceV1p3beta1_Track(
    typing_extensions.TypedDict, total=False
):
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_TimestampedObject
    ]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]

class GoogleCloudVideointelligenceV1beta2_ExplicitContentDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    point: GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex

class GoogleCloudVideointelligenceV1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    point: GoogleCloudVideointelligenceV1_NormalizedVertex
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1_WordInfo(typing_extensions.TypedDict, total=False):
    endTime: str
    speakerTag: int
    word: str
    startTime: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    thumbnail: str
    version: str

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription
    ]
    inputUri: str
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextAnnotation]
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    error: GoogleRpc_Status
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    celebrityRecognitionAnnotations: GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]

class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float
    trackId: str
    version: str
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame]

class GoogleCloudVideointelligenceV1p2beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextSegment]
    version: str

class GoogleCloudVideointelligenceV1beta2_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    languageCode: str
    entityId: str

class GoogleCloudVideointelligenceV1p1beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]

class GoogleCloudVideointelligenceV1beta2_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_TextSegment]
    version: str

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    progressPercent: int
    startTime: str
    updateTime: str
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
    ]

class GoogleCloudVideointelligenceV1p2beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

class GoogleCloudVideointelligenceV1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1_DetectedLandmark]
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1_Entity(typing_extensions.TypedDict, total=False):
    entityId: str
    description: str
    languageCode: str

class GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    trackId: str
    version: str
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1_NormalizedVertex]

class GoogleCloudVideointelligenceV1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextSegment]

class GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    value: str

class GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack(
    typing_extensions.TypedDict, total=False
):
    celebrities: typing.List[GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity]
    faceTrack: GoogleCloudVideointelligenceV1p3beta1_Track

class GoogleLongrunning_Operation(typing_extensions.TypedDict, total=False):
    error: GoogleRpc_Status
    done: bool
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    updateTime: str
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
    ]
    inputUri: str
    progressPercent: int

class GoogleRpc_Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    explicitAnnotation: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextAnnotation]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    inputUri: str
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    error: GoogleRpc_Status
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]

class GoogleCloudVideointelligenceV1p1beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    speakerTag: int
    endTime: str
    word: str
    startTime: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1beta2_WordInfo]

class GoogleCloudVideointelligenceV1p3beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    description: str
    entityId: str

class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1beta2_ShotChangeDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p3beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    speakerTag: int
    word: str
    startTime: str
    confidence: float
    endTime: str

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
    ]
    inputUri: str
    updateTime: str
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    progressPercent: int

class GoogleCloudVideointelligenceV1p3beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    right: float
    top: float
    left: float

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

class GoogleCloudVideointelligenceV1beta2_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    celebrity: GoogleCloudVideointelligenceV1p3beta1_Celebrity

class GoogleCloudVideointelligenceV1p2beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    word: str
    endTime: str
    confidence: float
    startTime: str
    speakerTag: int

class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame]

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

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p1beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextFrame]

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

class GoogleCloudVideointelligenceV1p3beta1_Celebrity(
    typing_extensions.TypedDict, total=False
):
    name: str
    displayName: str
    description: str

class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    pornographyLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]

class GoogleCloudVideointelligenceV1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str
    confidence: float

class GoogleCloudVideointelligenceV1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    shotLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    inputUri: str
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation
    ]
    frameLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    explicitAnnotation: GoogleCloudVideointelligenceV1_ExplicitContentAnnotation
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1_TextAnnotation]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1_SpeechTranscription
    ]

class GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p1beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelSegment]
    version: str

class GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]

class GoogleCloudVideointelligenceV1p2beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    value: str
    name: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]

class GoogleCloudVideointelligenceV1p2beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    landmarks: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    timeOffset: str

class GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1_WordInfo]

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionConfig(
    typing_extensions.TypedDict, total=False
):
    speechContexts: typing.List[GoogleCloudVideointelligenceV1beta2_SpeechContext]
    enableAutomaticPunctuation: bool
    maxAlternatives: int
    enableWordConfidence: bool
    audioTracks: typing.List[int]
    enableSpeakerDiarization: bool
    diarizationSpeakerCount: int
    filterProfanity: bool
    languageCode: str

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoRequest(
    typing_extensions.TypedDict, total=False
):
    inputContent: str
    inputUri: str
    videoContext: GoogleCloudVideointelligenceV1beta2_VideoContext
    locationId: str
    features: typing.List[str]
    outputUri: str

class GoogleCloudVideointelligenceV1p1beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

class GoogleCloudVideointelligenceV1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1_LabelSegment]
    version: str
    entity: GoogleCloudVideointelligenceV1_Entity

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
    updateTime: str
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    inputUri: str
    progressPercent: int
    startTime: str

class GoogleCloudVideointelligenceV1beta2_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1beta2_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1beta2_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    explicitAnnotation: GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    error: GoogleRpc_Status
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_TextAnnotation]

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    trackId: str
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame]
    version: str
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    entity: GoogleCloudVideointelligenceV1beta2_Entity

class GoogleCloudVideointelligenceV1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    right: float
    top: float
    left: float
    bottom: float

class GoogleCloudVideointelligenceV1p3beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p3beta1_WordInfo]

class GoogleCloudVideointelligenceV1beta2_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    version: str
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1beta2_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_LabelSegment]
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_LabelFrame]

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    startTime: str
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "LABEL_DETECTION",
        "SHOT_CHANGE_DETECTION",
        "EXPLICIT_CONTENT_DETECTION",
        "SPEECH_TRANSCRIPTION",
        "TEXT_DETECTION",
        "OBJECT_TRACKING",
        "LOGO_RECOGNITION",
    ]
    inputUri: str

class GoogleCloudVideointelligenceV1p1beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_TextFrame]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1beta2_SpeechContext(
    typing_extensions.TypedDict, total=False
):
    phrases: typing.List[str]

class GoogleCloudVideointelligenceV1beta2_LabelDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    videoConfidenceThreshold: float
    frameConfidenceThreshold: float
    labelDetectionMode: typing_extensions.Literal[
        "LABEL_DETECTION_MODE_UNSPECIFIED",
        "SHOT_MODE",
        "FRAME_MODE",
        "SHOT_AND_FRAME_MODE",
    ]
    stationaryCamera: bool
    model: str

class GoogleCloudVideointelligenceV1p1beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1beta2_VideoContext(
    typing_extensions.TypedDict, total=False
):
    explicitContentDetectionConfig: GoogleCloudVideointelligenceV1beta2_ExplicitContentDetectionConfig
    speechTranscriptionConfig: GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionConfig
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    shotChangeDetectionConfig: GoogleCloudVideointelligenceV1beta2_ShotChangeDetectionConfig
    labelDetectionConfig: GoogleCloudVideointelligenceV1beta2_LabelDetectionConfig
    objectTrackingConfig: GoogleCloudVideointelligenceV1beta2_ObjectTrackingConfig
    textDetectionConfig: GoogleCloudVideointelligenceV1beta2_TextDetectionConfig

class GoogleCloudVideointelligenceV1beta2_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    top: float
    right: float
    left: float

class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    pornographyLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]

class GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]

class GoogleCloudVideointelligenceV1p2beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1beta2_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1beta2_TimestampedObject
    ]

class GoogleCloudVideointelligenceV1p2beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1beta2_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    inputUri: str
    error: GoogleRpc_Status
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextAnnotation]

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    version: str

class GoogleCloudVideointelligenceV1beta2_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    confidence: float
    startTime: str
    speakerTag: int
    word: str

class GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p2beta1_WordInfo]
    transcript: str

class GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p2beta1_Entity]
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelFrame]
    version: str

class GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    labelAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]

class GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    celebrityTracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack]

class GoogleCloudVideointelligenceV1beta2_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str
