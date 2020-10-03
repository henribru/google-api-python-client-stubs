import typing

import typing_extensions

class GoogleCloudVideointelligenceV1p1beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    word: str
    endTime: str
    confidence: float
    startTime: str
    speakerTag: int

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p2beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextSegment]
    text: str
    version: str

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1p1beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    description: str
    languageCode: str

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame]
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    trackId: str
    version: str

class GoogleCloudVideointelligenceV1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    landmarks: typing.List[GoogleCloudVideointelligenceV1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox

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
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    inputUri: str
    updateTime: str
    startTime: str
    progressPercent: int

class GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    point: GoogleCloudVideointelligenceV1_NormalizedVertex

class GoogleCloudVideointelligenceV1p3beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    landmarks: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark]

class GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    trackId: str
    frames: typing.List[GoogleCloudVideointelligenceV1_ObjectTrackingFrame]
    version: str
    entity: GoogleCloudVideointelligenceV1_Entity
    segment: GoogleCloudVideointelligenceV1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1_TextSegment]

class GoogleCloudVideointelligenceV1p3beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p3beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    confidence: float

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

class GoogleCloudVideointelligenceV1p2beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextFrame]
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

class GoogleCloudVideointelligenceV1p1beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1beta2_Entity]
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_LabelFrame]
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_LabelSegment]

class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]
    thumbnail: str
    version: str

class GoogleCloudVideointelligenceV1beta2_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p3beta1_WordInfo]

class GoogleCloudVideointelligenceV1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    segment: GoogleCloudVideointelligenceV1_VideoSegment
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

class GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1beta2_Track]

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    progressPercent: int
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    startTime: str
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

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    progressPercent: int
    startTime: str
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
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_LabelDetectionConfig(
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
    videoConfidenceThreshold: float
    stationaryCamera: bool

class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame]
    trackId: str
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    version: str
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

class GoogleCloudVideointelligenceV1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]

class GoogleCloudVideointelligenceV1p1beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_Track(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_TimestampedObject
    ]
    attributes: typing.List[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]

class GoogleCloudVideointelligenceV1p2beta1_ShotChangeDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p1beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextFrame]

class GoogleCloudVideointelligenceV1p3beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    tracks: typing.List[GoogleCloudVideointelligenceV1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    entity: GoogleCloudVideointelligenceV1_Entity

class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    celebrityRecognitionAnnotations: GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription
    ]
    personDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    faceDetectionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    inputUri: str
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextAnnotation]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation
    ]

class GoogleCloudVideointelligenceV1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    point: GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex
    confidence: float
    name: str

class GoogleCloudVideointelligenceV1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1_TextFrame]

class GoogleCloudVideointelligenceV1p2beta1_SpeechContext(
    typing_extensions.TypedDict, total=False
):
    phrases: typing.List[str]

class GoogleCloudVideointelligenceV1p2beta1_VideoContext(
    typing_extensions.TypedDict, total=False
):
    objectTrackingConfig: GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingConfig
    speechTranscriptionConfig: GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionConfig
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    shotChangeDetectionConfig: GoogleCloudVideointelligenceV1p2beta1_ShotChangeDetectionConfig
    explicitContentDetectionConfig: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentDetectionConfig
    textDetectionConfig: GoogleCloudVideointelligenceV1p2beta1_TextDetectionConfig
    labelDetectionConfig: GoogleCloudVideointelligenceV1p2beta1_LabelDetectionConfig

class GoogleCloudVideointelligenceV1_WordInfo(typing_extensions.TypedDict, total=False):
    word: str
    speakerTag: int
    startTime: str
    endTime: str
    confidence: float

class GoogleRpc_Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class GoogleCloudVideointelligenceV1beta2_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1beta2_TextFrame]
    confidence: float

class GoogleCloudVideointelligenceV1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    point: GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex

class GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelFrame]
    version: str
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelSegment]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p3beta1_Entity]

class GoogleCloudVideointelligenceV1p3beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    word: str
    speakerTag: int
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1p2beta1_WordInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    confidence: float
    speakerTag: int
    word: str

class GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p2beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    languageCode: str
    description: str

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex]

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    confidence: float
    trackId: str
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame]

class GoogleCloudVideointelligenceV1p2beta1_TextDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    languageHints: typing.List[str]
    model: str

class GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudVideointelligenceV1p2beta1_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    landmarks: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]

class GoogleCloudVideointelligenceV1p1beta1_Track(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_TimestampedObject
    ]

class GoogleCloudVideointelligenceV1beta2_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress(
    typing_extensions.TypedDict, total=False
):
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
    inputUri: str
    startTime: str
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    updateTime: str

class GoogleCloudVideointelligenceV1beta2_Entity(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    entityId: str
    description: str

class GoogleCloudVideointelligenceV1p3beta1_TextSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    frames: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextFrame]
    confidence: float

class GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1_WordInfo]
    transcript: str
    confidence: float

class GoogleCloudVideointelligenceV1beta2_NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack(
    typing_extensions.TypedDict, total=False
):
    celebrities: typing.List[GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity]
    faceTrack: GoogleCloudVideointelligenceV1p3beta1_Track

class GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    confidence: float
    value: str

class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    top: float
    right: float
    bottom: float
    left: float

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    top: float
    bottom: float
    right: float
    left: float

class GoogleCloudVideointelligenceV1p2beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p2beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity

class GoogleCloudVideointelligenceV1beta2_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_Entity(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    description: str
    languageCode: str

class GoogleCloudVideointelligenceV1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1beta2_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    tracks: typing.List[GoogleCloudVideointelligenceV1p1beta1_Track]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_Track(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1beta2_TimestampedObject
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

class GoogleCloudVideointelligenceV1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingPoly
    timeOffset: str

class GoogleLongrunning_Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpc_Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

class GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str
    confidence: float

class GoogleCloudVideointelligenceV1p3beta1_Celebrity(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    description: str

class GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    labelAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]

class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative
    ]

class GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    words: typing.List[GoogleCloudVideointelligenceV1beta2_WordInfo]
    confidence: float
    transcript: str

class GoogleCloudVideointelligenceV1beta2_WordInfo(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    word: str
    confidence: float
    speakerTag: int
    endTime: str

class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoRequest(
    typing_extensions.TypedDict, total=False
):
    outputUri: str
    inputUri: str
    locationId: str
    inputContent: str
    videoContext: GoogleCloudVideointelligenceV1p2beta1_VideoContext
    features: typing.List[str]

class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    trackId: str
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame]
    version: str
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    right: float
    top: float
    left: float
    bottom: float

class GoogleCloudVideointelligenceV1beta2_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    point: GoogleCloudVideointelligenceV1beta2_NormalizedVertex
    name: str

class GoogleCloudVideointelligenceV1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1_SpeechTranscription
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1_VideoSegment]
    shotLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1_ExplicitContentAnnotation
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1_TextAnnotation]
    error: GoogleRpc_Status
    frameLabelAnnotations: typing.List[GoogleCloudVideointelligenceV1_LabelAnnotation]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1_VideoSegment

class GoogleCloudVideointelligenceV1p2beta1_Track(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    timestampedObjects: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_TimestampedObject
    ]
    attributes: typing.List[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

class GoogleCloudVideointelligenceV1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame]
    version: str

class GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    celebrityTracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack]

class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1_Entity]
    frames: typing.List[GoogleCloudVideointelligenceV1_LabelFrame]
    entity: GoogleCloudVideointelligenceV1_Entity
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1_LabelSegment]

class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextSegment]
    version: str

class GoogleCloudVideointelligenceV1beta2_SpeechTranscription(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    alternatives: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative
    ]

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

class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    inputUri: str
    error: GoogleRpc_Status
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p2beta1_TextAnnotation]
    explicitAnnotation: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]

class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1p1beta1_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    inputUri: str
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation
    ]
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    error: GoogleRpc_Status
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    explicitAnnotation: GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1beta2_SpeechTranscription
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_TextAnnotation]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation
    ]
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]

class GoogleCloudVideointelligenceV1_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1_NormalizedVertex]

class GoogleCloudVideointelligenceV1_NormalizedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    bottom: float
    right: float
    left: float
    top: float

class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    tracks: typing.List[GoogleCloudVideointelligenceV1p3beta1_Track]

class GoogleCloudVideointelligenceV1_LabelSegment(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment

class GoogleCloudVideointelligenceV1p3beta1_TextFrame(
    typing_extensions.TypedDict, total=False
):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly
    timeOffset: str

class GoogleCloudVideointelligenceV1_Track(typing_extensions.TypedDict, total=False):
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    confidence: float
    attributes: typing.List[GoogleCloudVideointelligenceV1_DetectedAttribute]
    timestampedObjects: typing.List[GoogleCloudVideointelligenceV1_TimestampedObject]

class GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation(
    typing_extensions.TypedDict, total=False
):
    frames: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelFrame]
    categoryEntities: typing.List[GoogleCloudVideointelligenceV1p1beta1_Entity]
    segments: typing.List[GoogleCloudVideointelligenceV1p1beta1_LabelSegment]
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    version: str

class GoogleCloudVideointelligenceV1beta2_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    text: str
    version: str
    segments: typing.List[GoogleCloudVideointelligenceV1beta2_TextSegment]

class GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    timeOffset: str

class GoogleCloudVideointelligenceV1p3beta1_TextAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    text: str
    segments: typing.List[GoogleCloudVideointelligenceV1p3beta1_TextSegment]

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

class GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    transcript: str
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p2beta1_WordInfo]

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

class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation(
    typing_extensions.TypedDict, total=False
):
    version: str
    frames: typing.List[GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame]

class GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

class GoogleCloudVideointelligenceV1beta2_VideoSegment(
    typing_extensions.TypedDict, total=False
):
    startTimeOffset: str
    endTimeOffset: str

class GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark(
    typing_extensions.TypedDict, total=False
):
    name: str
    point: GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex
    confidence: float

class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults(
    typing_extensions.TypedDict, total=False
):
    frameLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    speechTranscriptions: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription
    ]
    shotLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    error: GoogleRpc_Status
    shotPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    segmentLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    objectAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation
    ]
    explicitAnnotation: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation
    logoRecognitionAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation
    ]
    shotAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    inputUri: str
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    segmentPresenceLabelAnnotations: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    textAnnotations: typing.List[GoogleCloudVideointelligenceV1p1beta1_TextAnnotation]

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgress(
    typing_extensions.TypedDict, total=False
):
    annotationProgress: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress
    ]

class GoogleCloudVideointelligenceV1beta2_TimestampedObject(
    typing_extensions.TypedDict, total=False
):
    landmarks: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedLandmark]
    attributes: typing.List[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    timeOffset: str
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox

class GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults
    error: GoogleRpc_Status
    annotationResultsUri: str

class GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    words: typing.List[GoogleCloudVideointelligenceV1p1beta1_WordInfo]
    transcript: str

class GoogleCloudVideointelligenceV1p1beta1_LabelFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    confidence: float

class GoogleCloudVideointelligenceV1_Entity(typing_extensions.TypedDict, total=False):
    entityId: str
    languageCode: str
    description: str

class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    annotationResults: typing.List[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults
    ]

class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudVideointelligenceV1beta2_NormalizedVertex]

class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionConfig(
    typing_extensions.TypedDict, total=False
):
    enableAutomaticPunctuation: bool
    filterProfanity: bool
    speechContexts: typing.List[GoogleCloudVideointelligenceV1p2beta1_SpeechContext]
    maxAlternatives: int
    languageCode: str
    audioTracks: typing.List[int]
    enableSpeakerDiarization: bool
    enableWordConfidence: bool
    diarizationSpeakerCount: int

class GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity(
    typing_extensions.TypedDict, total=False
):
    celebrity: GoogleCloudVideointelligenceV1p3beta1_Celebrity
    confidence: float

class GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    tracks: typing.List[GoogleCloudVideointelligenceV1p2beta1_Track]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
