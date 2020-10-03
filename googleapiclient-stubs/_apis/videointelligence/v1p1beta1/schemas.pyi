import typing

import typing_extensions

class GoogleCloudVideointelligenceV1p2beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextSegment]

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_Track(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_TimestampedObject
    ]
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_ShotChangeDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p1beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    languageCode: str
    entityId: str

class GoogleCloudVideointelligenceV1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1_SpeechTranscription
    ]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    shotLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    segmentLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation
    ]
    frameLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1_ExplicitContentAnnotation
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1_TextAnnotation]
    error: GoogleRpc_Status
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]

class GoogleCloudVideointelligenceV1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_Track(
    typing_extensions.TypedDict, total=False
):
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_TimestampedObject
    ]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    version: str
    confidence: float
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    trackId: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame]

class GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    celebrityTracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack]
    version: str

class GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p2beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelFrame]

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox

class GoogleLongrunning_Operation(typing_extensions.TypedDict, total=False):
    error: GoogleRpc_Status
    name: str
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    done: bool

class GoogleCloudVideointelligenceV1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    right: float
    top: float
    left: float
    bottom: float

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame]
    version: str
    confidence: float
    trackId: str

class GoogleCloudVideointelligenceV1beta2_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1beta2_NormalizedVertex
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1p2beta1_Track(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_TimestampedObject
    ]

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p1beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextSegment]
    text: str

class GoogleCloudVideointelligenceV1p3beta1_Celebrity(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    description: str

class GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1p3beta1_WordInfo]

class GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p1beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelSegment]
    version: str
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelFrame]

class GoogleCloudVideointelligenceV1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_VideoContext(
    typing_extensions.TypedDict, total=False
):
    speechTranscriptionConfig: GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionConfig
    textDetectionConfig: GoogleCloudVideointelligenceV1p1beta1_TextDetectionConfig
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    explicitContentDetectionConfig: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentDetectionConfig
    labelDetectionConfig: GoogleCloudVideointelligenceV1p1beta1_LabelDetectionConfig
    objectTrackingConfig: GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingConfig
    shotChangeDetectionConfig: GoogleCloudVideointelligenceV1p1beta1_ShotChangeDetectionConfig

class GoogleCloudVideointelligenceV1p2beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextFrame]

class GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack(
    typing_extensions.TypedDict, total=False
):
    celebrities: typing.List[GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity]
    faceTrack: GoogleCloudVideointelligenceV1p3beta1_Track

class GoogleCloudVideointelligenceV1p1beta1_LabelDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    videoConfidenceThreshold: float
    stationaryCamera: bool
    model: str
    labelDetectionMode: typing_extensions.Literal[
        "LABEL_DETECTION_MODE_UNSPECIFIED",
        "SHOT_MODE",
        "FRAME_MODE",
        "SHOT_AND_FRAME_MODE",
    ]
    frameConfidenceThreshold: float

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
    startTime: str
    progressPercent: int
    updateTime: str
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    inputUri: str

class GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity

class GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex

class GoogleCloudVideointelligenceV1beta2_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_LabelSegment]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1beta2_Entity]
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_LabelFrame]

class GoogleCloudVideointelligenceV1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

class GoogleCloudVideointelligenceV1p3beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1p1beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame]
    version: str
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    confidence: float
    trackId: str

class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoRequest(
    typing_extensions.TypedDict, total=False
):
    outputUri: str
    features: typing.List[str]
    inputUri: str
    locationId: str
    inputContent: str
    videoContext: GoogleCloudVideointelligenceV1p1beta1_VideoContext

class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1p3beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]

class GoogleCloudVideointelligenceV1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1_NormalizedVertex]

class GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1_Entity

class GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1_ObjectTrackingFrame]
    trackId: str
    entity: GoogleCloudVideointelligenceV1_Entity
    segment: GoogleCloudVideointelligenceV1_VideoSegment

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

class GoogleRpc_Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class GoogleCloudVideointelligenceV1p1beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    value: str

class GoogleCloudVideointelligenceV1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1_TextSegment]

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

class GoogleCloudVideointelligenceV1p3beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1_Entity

class GoogleCloudVideointelligenceV1p3beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    inputUri: str
    error: GoogleRpc_Status
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextAnnotation]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation
    ]

class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1beta2_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    thumbnail: str

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    entityId: str
    description: str

class GoogleCloudVideointelligenceV1p1beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
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
    updateTime: str
    progressPercent: int
    startTime: str

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1beta2_WordInfo]
    transcript: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    word: str
    confidence: float
    speakerTag: int
    startTime: str

class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]

class GoogleCloudVideointelligenceV1p2beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    landmarks: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation
    ]
    error: GoogleRpc_Status
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    inputUri: str
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    explicitAnnotation: GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_TextAnnotation]

class GoogleCloudVideointelligenceV1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1_TextFrame]

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
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
    startTime: str
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    inputUri: str
    progressPercent: int

class GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    annotationResultsUri: str
    annotationResults: GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults

class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionConfig(
    typing_extensions.TypedDict, total=False
):
    enableWordConfidence: bool
    maxAlternatives: int
    speechContexts: typing.List[GoogleCloudVideointelligenceV1p1beta1_SpeechContext]
    filterProfanity: bool
    enableSpeakerDiarization: bool
    enableAutomaticPunctuation: bool
    diarizationSpeakerCount: int
    audioTracks: typing.List[int]
    languageCode: str

class GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]

class GoogleCloudVideointelligenceV1beta2_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p3beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextSegment]
    version: str
    text: str

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1beta2_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    entityId: str
    languageCode: str

class GoogleCloudVideointelligenceV1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    inputUri: str
    updateTime: str
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    progressPercent: int
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

class GoogleCloudVideointelligenceV1_WordInfo(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str
    word: str
    confidence: float
    speakerTag: int

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

class GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelFrame]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p3beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelSegment]

class GoogleCloudVideointelligenceV1p2beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p2beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1beta2_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    value: str
    name: str

class GoogleCloudVideointelligenceV1beta2_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_TextSegment]
    version: str

class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]

class GoogleCloudVideointelligenceV1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    left: float
    right: float
    bottom: float
    top: float

class GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    point: GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex
    name: str

class GoogleCloudVideointelligenceV1beta2_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    explicitAnnotation: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription
    ]
    inputUri: str
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    error: GoogleRpc_Status
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextAnnotation]

class GoogleCloudVideointelligenceV1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1beta2_NormalizedVertex]

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame]
    trackId: str
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    version: str
    confidence: float
    entity: GoogleCloudVideointelligenceV1beta2_Entity

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
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
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    progressPercent: int
    inputUri: str
    updateTime: str
    startTime: str

class GoogleCloudVideointelligenceV1p3beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    word: str
    startTime: str
    speakerTag: int
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    celebrity: GoogleCloudVideointelligenceV1p3beta1_Celebrity

class GoogleCloudVideointelligenceV1_Track(typing_extensions.TypedDict, total=False):
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    timestampedObjects: typing.List[GoogleCloudVideointelligenceV1_TimestampedObject]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1beta2_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p2beta1_WordInfo]

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    right: float
    left: float
    top: float
    bottom: float

class GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    right: float
    left: float
    top: float

class GoogleCloudVideointelligenceV1p2beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    speakerTag: int
    confidence: float
    startTime: str
    word: str

class GoogleCloudVideointelligenceV1p2beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    landmarks: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]

class GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1_WordInfo]
    transcript: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_Entity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    description: str
    languageCode: str

class GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1p1beta1_WordInfo]
    transcript: str
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_SpeechContext(
    typing_extensions.TypedDict, total=False
):
    phrases: typing.List[str]

class GoogleCloudVideointelligenceV1p1beta1_TextDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str
    languageHints: typing.List[str]

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

class GoogleCloudVideointelligenceV1p1beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1_NormalizedVertex

class GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity

class GoogleCloudVideointelligenceV1beta2_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    labelAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]

class GoogleCloudVideointelligenceV1p1beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    error: GoogleRpc_Status
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation
    ]
    inputUri: str
    celebrityRecognitionAnnotations: GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation
    ]

class GoogleCloudVideointelligenceV1_Entity(typing_extensions.TypedDict, total=False):
    entityId: str
    languageCode: str
    description: str

class GoogleCloudVideointelligenceV1p1beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    word: str
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str

class GoogleCloudVideointelligenceV1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

class GoogleCloudVideointelligenceV1beta2_Track(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1beta2_TimestampedObject
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextFrame]
    confidence: float

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    left: float
    bottom: float
    top: float
    right: float

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1beta2_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_TextFrame]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex
    confidence: float
    name: str

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

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults
    ]
