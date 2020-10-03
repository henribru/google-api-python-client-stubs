import typing

import typing_extensions

class GoogleCloudVideointelligenceV1p1beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]
    entity: GoogleCloudVideointelligenceV1_Entity

class GoogleCloudVideointelligenceV1beta2_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_TextFrame]
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1_ExplicitContentFrame(
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

class GoogleCloudVideointelligenceV1p3beta1_ShotChangeDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    frameLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    shotLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    error: GoogleRpc_Status
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1_SpeechTranscription
    ]
    segmentLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1_ExplicitContentAnnotation
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1_TextAnnotation]
    inputUri: str
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    segment: GoogleCloudVideointelligenceV1_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark]

class GoogleCloudVideointelligenceV1p3beta1_Track(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_TimestampedObject
    ]
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame]
    confidence: float
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    version: str
    trackId: str
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextFrame]

class GoogleCloudVideointelligenceV1p1beta1_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_TimestampedObject
    ]

class GoogleCloudVideointelligenceV1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1_TextSegment]
    text: str
    version: str

class GoogleCloudVideointelligenceV1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    value: str

class GoogleCloudVideointelligenceV1p3beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextSegment]
    version: str
    text: str

class GoogleCloudVideointelligenceV1p3beta1_TextDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    languageHints: typing.List[str]
    model: str

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
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
    startTime: str

class GoogleCloudVideointelligenceV1p3beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark]

class GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    point: GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex
    name: str

class GoogleCloudVideointelligenceV1p3beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    entityId: str
    description: str

class GoogleCloudVideointelligenceV1_Track(typing_extensions.TypedDict, total=False):
    timestampedObjects: typing.List[GoogleCloudVideointelligenceV1_TimestampedObject]
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    segment: GoogleCloudVideointelligenceV1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame(
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

class GoogleCloudVideointelligenceV1beta2_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_TextSegment]

class GoogleCloudVideointelligenceV1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1_LabelSegment]
    version: str
    entity: GoogleCloudVideointelligenceV1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1_LabelFrame]

class GoogleCloudVideointelligenceV1p3beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    labelAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]

class GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p1beta1_WordInfo]

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    progressPercent: int
    startTime: str
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    inputUri: str
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
    updateTime: str

class GoogleCloudVideointelligenceV1beta2_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedLandmark]
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    word: str
    confidence: float
    speakerTag: int

class GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p3beta1_Celebrity(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    description: str

class GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack(
    typing_extensions.TypedDict, total=False
):
    celebrities: typing.List[GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity]
    faceTrack: GoogleCloudVideointelligenceV1p3beta1_Track

class GoogleCloudVideointelligenceV1p1beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    point: GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex

class GoogleCloudVideointelligenceV1p2beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly

class GoogleLongrunning_Operation(typing_extensions.TypedDict, total=False):
    done: bool
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: GoogleRpc_Status

class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    version: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]

class GoogleCloudVideointelligenceV1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    top: float
    left: float
    bottom: float
    right: float

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str
    confidence: float

class GoogleCloudVideointelligenceV1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1p1beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    description: str
    languageCode: str

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    right: float
    top: float
    left: float

class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionConfig(
    typing_extensions.TypedDict, total=False
):
    enableAutomaticPunctuation: bool
    audioTracks: typing.List[int]
    speechContexts: typing.List[GoogleCloudVideointelligenceV1p3beta1_SpeechContext]
    diarizationSpeakerCount: int
    enableSpeakerDiarization: bool
    filterProfanity: bool
    maxAlternatives: int
    languageCode: str
    enableWordConfidence: bool

class GoogleCloudVideointelligenceV1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1_NormalizedVertex
    name: str
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    value: str
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults
    ]

class GoogleRpc_Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class GoogleCloudVideointelligenceV1beta2_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

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

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    left: float
    top: float
    right: float
    bottom: float

class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame]
    confidence: float
    trackId: str
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    version: str

class GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    point: GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex
    confidence: float

class GoogleCloudVideointelligenceV1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    entity: GoogleCloudVideointelligenceV1_Entity
    trackId: str
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1_ObjectTrackingFrame]

class GoogleCloudVideointelligenceV1p3beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1beta2_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    point: GoogleCloudVideointelligenceV1beta2_NormalizedVertex

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    trackId: str
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame]
    version: str
    confidence: float

class GoogleCloudVideointelligenceV1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p3beta1_VideoContext(
    typing_extensions.TypedDict, total=False
):
    speechTranscriptionConfig: GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionConfig
    objectTrackingConfig: GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingConfig
    explicitContentDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentDetectionConfig
    shotChangeDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_ShotChangeDetectionConfig
    personDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_PersonDetectionConfig
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    faceDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_FaceDetectionConfig
    labelDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_LabelDetectionConfig
    textDetectionConfig: GoogleCloudVideointelligenceV1p3beta1_TextDetectionConfig

class GoogleCloudVideointelligenceV1p2beta1_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_TimestampedObject
    ]
    confidence: float

class GoogleCloudVideointelligenceV1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1_WordInfo]
    confidence: float
    transcript: str

class GoogleCloudVideointelligenceV1p1beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextFrame]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p2beta1_Entity]
    version: str

class GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p2beta1_WordInfo]
    transcript: str

class GoogleCloudVideointelligenceV1p3beta1_SpeechContext(
    typing_extensions.TypedDict, total=False
):
    phrases: typing.List[str]

class GoogleCloudVideointelligenceV1p3beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    annotationResultsUri: str
    annotationResults: GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults

class GoogleCloudVideointelligenceV1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    inputUri: str
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
    startTime: str
    updateTime: str

class GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    right: float
    left: float
    top: float
    bottom: float

class GoogleCloudVideointelligenceV1p2beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    word: str
    startTime: str
    speakerTag: int
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    top: float
    right: float
    left: float
    bottom: float

class GoogleCloudVideointelligenceV1beta2_Track(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1beta2_TimestampedObject
    ]
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1beta2_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    includeAttributes: bool
    includeBoundingBoxes: bool
    model: str

class GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame(
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

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p1beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelSegment]
    version: str
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity

class GoogleCloudVideointelligenceV1_Entity(typing_extensions.TypedDict, total=False):
    entityId: str
    description: str
    languageCode: str

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p3beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelFrame]
    version: str

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1beta2_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_LabelSegment]
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1beta2_Entity]
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    version: str

class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1_WordInfo(typing_extensions.TypedDict, total=False):
    confidence: float
    word: str
    startTime: str
    endTime: str
    speakerTag: int

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    inputUri: str
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextAnnotation]

class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    progressPercent: int
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
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    startTime: str

class GoogleCloudVideointelligenceV1p2beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    description: str
    entityId: str

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    value: str
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    celebrity: GoogleCloudVideointelligenceV1p3beta1_Celebrity

class GoogleCloudVideointelligenceV1beta2_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextAnnotation]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    inputUri: str
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    celebrityRecognitionAnnotations: GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation
    ]
    error: GoogleRpc_Status

class GoogleCloudVideointelligenceV1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1beta2_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_LabelDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    stationaryCamera: bool
    frameConfidenceThreshold: float
    model: str
    videoConfidenceThreshold: float
    labelDetectionMode: typing_extensions.Literal[
        "LABEL_DETECTION_MODE_UNSPECIFIED",
        "SHOT_MODE",
        "FRAME_MODE",
        "SHOT_AND_FRAME_MODE",
    ]

class GoogleCloudVideointelligenceV1p2beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity

class GoogleCloudVideointelligenceV1beta2_WordInfo(
    typing_extensions.TypedDict, total=False
):
    word: str
    confidence: float
    speakerTag: int
    endTime: str
    startTime: str

class GoogleCloudVideointelligenceV1beta2_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p3beta1_WordInfo]

class GoogleCloudVideointelligenceV1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_TextFrame]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    celebrityTracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack]

class GoogleCloudVideointelligenceV1p2beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextSegment]
    version: str

class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    includeAttributes: bool
    includeBoundingBoxes: bool
    includePoseLandmarks: bool

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

class GoogleCloudVideointelligenceV1p1beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation
    ]
    inputUri: str
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation
    ]
    error: GoogleRpc_Status
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextAnnotation]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]

class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    version: str

class GoogleCloudVideointelligenceV1p1beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    trackId: str
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    version: str

class GoogleCloudVideointelligenceV1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    updateTime: str
    startTime: str
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
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
    progressPercent: int

class GoogleCloudVideointelligenceV1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p2beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark]
    timeOffset: str
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_TextAnnotation]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechTranscription
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    inputUri: str
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    error: GoogleRpc_Status
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation
    ]

class GoogleCloudVideointelligenceV1p1beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    speakerTag: int
    endTime: str
    startTime: str
    word: str
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextSegment]
    version: str

class GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1beta2_WordInfo]
    transcript: str

class GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoRequest(
    typing_extensions.TypedDict, total=False
):
    features: typing.List[str]
    inputUri: str
    locationId: str
    videoContext: GoogleCloudVideointelligenceV1p3beta1_VideoContext
    outputUri: str
    inputContent: str

class GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]

class GoogleCloudVideointelligenceV1p3beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

class GoogleCloudVideointelligenceV1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVideointelligenceV1_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
