import typing

import typing_extensions

class GoogleCloudVideointelligenceV1_WordInfo(typing_extensions.TypedDict, total=False):
    startTime: str
    speakerTag: int
    endTime: str
    word: str
    confidence: float

class GoogleCloudVideointelligenceV1_Entity(typing_extensions.TypedDict, total=False):
    languageCode: str
    entityId: str
    description: str

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p1beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    landmarks: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark]

class GoogleCloudVideointelligenceV1beta2_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1_LabelDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str
    labelDetectionMode: typing_extensions.Literal[
        "LABEL_DETECTION_MODE_UNSPECIFIED",
        "SHOT_MODE",
        "FRAME_MODE",
        "SHOT_AND_FRAME_MODE",
    ]
    frameConfidenceThreshold: float
    videoConfidenceThreshold: float
    stationaryCamera: bool

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    top: float
    bottom: float
    left: float
    right: float

class GoogleCloudVideointelligenceV1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    landmarks: typing.List[GoogleCloudVideointelligenceV1_DetectedLandmark]

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

class GoogleCloudVideointelligenceV1p1beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextFrame]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextAnnotation]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    inputUri: str
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]

class GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity(
    typing_extensions.TypedDict, total=False
):
    celebrity: GoogleCloudVideointelligenceV1p3beta1_Celebrity
    confidence: float

class GoogleCloudVideointelligenceV1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment

class GoogleProtobuf_Empty(typing_extensions.TypedDict, total=False): ...

class GoogleRpc_Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class GoogleCloudVideointelligenceV1_SpeechTranscriptionConfig(
    typing_extensions.TypedDict, total=False
):
    diarizationSpeakerCount: int
    speechContexts: typing.List[GoogleCloudVideointelligenceV1_SpeechContext]
    enableWordConfidence: bool
    enableAutomaticPunctuation: bool
    audioTracks: typing.List[int]
    languageCode: str
    enableSpeakerDiarization: bool
    filterProfanity: bool
    maxAlternatives: int

class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    version: str

class GoogleCloudVideointelligenceV1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    right: float
    bottom: float
    left: float
    top: float

class GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack(
    typing_extensions.TypedDict, total=False
):
    celebrities: typing.List[GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity]
    faceTrack: GoogleCloudVideointelligenceV1p3beta1_Track

class GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1p1beta1_WordInfo]
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
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
    progressPercent: int
    startTime: str
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox

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

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1p2beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    word: str
    speakerTag: int
    startTime: str
    endTime: str

class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation
    ]
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    celebrityRecognitionAnnotations: GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation
    ]
    inputUri: str
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextAnnotation]

class GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]

class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1p3beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1_TextFrame]

class GoogleCloudVideointelligenceV1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p2beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    languageCode: str
    entityId: str

class GoogleCloudVideointelligenceV1beta2_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1_VideoContext(
    typing_extensions.TypedDict, total=False
):
    textDetectionConfig: GoogleCloudVideointelligenceV1_TextDetectionConfig
    labelDetectionConfig: GoogleCloudVideointelligenceV1_LabelDetectionConfig
    shotChangeDetectionConfig: GoogleCloudVideointelligenceV1_ShotChangeDetectionConfig
    segments: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    objectTrackingConfig: GoogleCloudVideointelligenceV1_ObjectTrackingConfig
    speechTranscriptionConfig: GoogleCloudVideointelligenceV1_SpeechTranscriptionConfig
    explicitContentDetectionConfig: GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfig

class GoogleCloudVideointelligenceV1p2beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    landmarks: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark]

class GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]

class GoogleCloudVideointelligenceV1p1beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    confidence: float
    word: str
    speakerTag: int

class GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    value: str
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1p3beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    endTime: str
    confidence: float
    word: str
    speakerTag: int

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
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    updateTime: str
    inputUri: str

class GoogleCloudVideointelligenceV1beta2_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str
    confidence: float

class GoogleCloudVideointelligenceV1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1_TextAnnotation]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1_SpeechTranscription
    ]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1_ExplicitContentAnnotation
    frameLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    inputUri: str
    shotLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    segmentLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]

class GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1p2beta1_WordInfo]
    confidence: float
    transcript: str

class GoogleCloudVideointelligenceV1beta2_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1beta2_NormalizedVertex
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1_Entity]
    frames: typing.List[GoogleCloudVideointelligenceV1_LabelFrame]
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1_Entity

class GoogleCloudVideointelligenceV1p1beta1_Track(
    typing_extensions.TypedDict, total=False
):
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_TimestampedObject
    ]
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    inputUri: str
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
    startTime: str
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextSegment]

class GoogleCloudVideointelligenceV1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    labelAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]

class GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    point: GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex
    confidence: float

class GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    confidence: float
    trackId: str
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame]

class GoogleCloudVideointelligenceV1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative
    ]
    languageCode: str

class GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelSegment]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p1beta1_Entity]
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelFrame]

class GoogleCloudVideointelligenceV1p1beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    languageCode: str
    description: str

class GoogleCloudVideointelligenceV1beta2_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1beta2_TimestampedObject
    ]
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

class GoogleCloudVideointelligenceV1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechTranscription
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation
    ]
    inputUri: str
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    error: GoogleRpc_Status
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_TextAnnotation]

class GoogleCloudVideointelligenceV1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    value: str
    name: str

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]

class GoogleCloudVideointelligenceV1beta2_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_LabelSegment]
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_LabelFrame]
    version: str
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1beta2_Entity]

class GoogleCloudVideointelligenceV1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1_TextSegment]
    text: str

class GoogleCloudVideointelligenceV1beta2_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

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

class GoogleCloudVideointelligenceV1_SpeechContext(
    typing_extensions.TypedDict, total=False
):
    phrases: typing.List[str]

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1beta2_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_Celebrity(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    description: str

class GoogleCloudVideointelligenceV1p2beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_TextFrame]
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    celebrityTracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack]

class GoogleCloudVideointelligenceV1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    point: GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex
    confidence: float

class GoogleLongrunning_CancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudVideointelligenceV1beta2_Entity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    languageCode: str
    description: str

class GoogleCloudVideointelligenceV1beta2_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_TextSegment]

class GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    value: str

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    trackId: str
    version: str
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame]

class GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1p2beta1_Track(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    confidence: float
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_TimestampedObject
    ]

class GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_ObjectTrackingFrame]
    entity: GoogleCloudVideointelligenceV1_Entity
    trackId: str
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    version: str

class GoogleCloudVideointelligenceV1p2beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextFrame]
    confidence: float

class GoogleCloudVideointelligenceV1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1p3beta1_WordInfo]

class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    top: float
    left: float
    right: float
    bottom: float

class GoogleCloudVideointelligenceV1p2beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1p1beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_WordInfo(
    typing_extensions.TypedDict, total=False
):
    word: str
    startTime: str
    speakerTag: int
    confidence: float
    endTime: str

class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p2beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelFrame]
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelSegment]

class GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p3beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1_Track(typing_extensions.TypedDict, total=False):
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    timestampedObjects: typing.List[GoogleCloudVideointelligenceV1_TimestampedObject]
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p3beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelSegment]
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelFrame]

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    inputUri: str
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    error: GoogleRpc_Status
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextAnnotation]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_Track(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_TimestampedObject
    ]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    startTime: str
    inputUri: str
    updateTime: str
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

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpc_Status
    annotationResults: GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults
    annotationResultsUri: str

class GoogleCloudVideointelligenceV1_ObjectTrackingConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

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

class GoogleCloudVideointelligenceV1p3beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextSegment]
    text: str
    version: str

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    trackId: str
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    confidence: float
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

class GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    words: typing.List[GoogleCloudVideointelligenceV1_WordInfo]
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    confidence: float
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame]
    trackId: str
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    version: str

class GoogleLongrunning_ListOperationsResponse(
    typing_extensions.TypedDict, total=False
):
    operations: typing.List[GoogleLongrunning_Operation]
    nextPageToken: str

class GoogleCloudVideointelligenceV1_ShotChangeDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1_AnnotateVideoRequest(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    outputUri: str
    inputContent: str
    locationId: str
    videoContext: GoogleCloudVideointelligenceV1_VideoContext
    features: typing.List[str]

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    left: float
    top: float
    bottom: float
    right: float

class GoogleCloudVideointelligenceV1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1_NormalizedVertex
    name: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    startTime: str
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

class GoogleCloudVideointelligenceV1beta2_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p1beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    description: str
    languageCode: str
    entityId: str

class GoogleLongrunning_Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    error: GoogleRpc_Status
    done: bool
    metadata: typing.Dict[str, typing.Any]
    name: str

class GoogleCloudVideointelligenceV1beta2_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    value: str
    name: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox(
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

class GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p1beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextSegment]

class GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1beta2_WordInfo]
    transcript: str
    confidence: float

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

class GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity

class GoogleCloudVideointelligenceV1p3beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p1beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1_TextDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str
    languageHints: typing.List[str]

class GoogleCloudVideointelligenceV1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly

class GoogleCloudVideointelligenceV1p2beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p3beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float
