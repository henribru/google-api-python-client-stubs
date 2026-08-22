import typing

_list = list

@typing.type_check_only
class GoogleCloudVideointelligenceV1_AnnotateVideoProgress(
    typing.TypedDict, total=False
):
    annotationProgress: _list[GoogleCloudVideointelligenceV1_VideoAnnotationProgress]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_AnnotateVideoResponse(
    typing.TypedDict, total=False
):
    annotationResults: _list[GoogleCloudVideointelligenceV1_VideoAnnotationResults]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_DetectedAttribute(typing.TypedDict, total=False):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_DetectedLandmark(typing.TypedDict, total=False):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1_Entity(typing.TypedDict, total=False):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ExplicitContentAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ExplicitContentFrame(
    typing.TypedDict, total=False
):
    pornographyLikelihood: typing.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ExportToOutputUriStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    status: GoogleRpc_Status

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceAnnotation(typing.TypedDict, total=False):
    frames: _list[GoogleCloudVideointelligenceV1_FaceFrame]
    segments: _list[GoogleCloudVideointelligenceV1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceDetectionAnnotation(
    typing.TypedDict, total=False
):
    thumbnail: str
    tracks: _list[GoogleCloudVideointelligenceV1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceFrame(typing.TypedDict, total=False):
    normalizedBoundingBoxes: _list[GoogleCloudVideointelligenceV1_NormalizedBoundingBox]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_FaceSegment(typing.TypedDict, total=False):
    segment: GoogleCloudVideointelligenceV1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LabelAnnotation(typing.TypedDict, total=False):
    categoryEntities: _list[GoogleCloudVideointelligenceV1_Entity]
    entity: GoogleCloudVideointelligenceV1_Entity
    frames: _list[GoogleCloudVideointelligenceV1_LabelFrame]
    segments: _list[GoogleCloudVideointelligenceV1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LabelFrame(typing.TypedDict, total=False):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LabelSegment(typing.TypedDict, total=False):
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation(
    typing.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1_Entity
    segments: _list[GoogleCloudVideointelligenceV1_VideoSegment]
    tracks: _list[GoogleCloudVideointelligenceV1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_NormalizedBoundingBox(
    typing.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1_NormalizedBoundingPoly(
    typing.TypedDict, total=False
):
    vertices: _list[GoogleCloudVideointelligenceV1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_NormalizedVertex(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation(
    typing.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1_Entity
    frames: _list[GoogleCloudVideointelligenceV1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_ObjectTrackingFrame(typing.TypedDict, total=False):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_PersonDetectionAnnotation(
    typing.TypedDict, total=False
):
    tracks: _list[GoogleCloudVideointelligenceV1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative(
    typing.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: _list[GoogleCloudVideointelligenceV1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_SpeechTranscription(typing.TypedDict, total=False):
    alternatives: _list[GoogleCloudVideointelligenceV1_SpeechRecognitionAlternative]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TextAnnotation(typing.TypedDict, total=False):
    segments: _list[GoogleCloudVideointelligenceV1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TextFrame(typing.TypedDict, total=False):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TextSegment(typing.TypedDict, total=False):
    confidence: float
    frames: _list[GoogleCloudVideointelligenceV1_TextFrame]
    segment: GoogleCloudVideointelligenceV1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1_TimestampedObject(typing.TypedDict, total=False):
    attributes: _list[GoogleCloudVideointelligenceV1_DetectedAttribute]
    landmarks: _list[GoogleCloudVideointelligenceV1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_Track(typing.TypedDict, total=False):
    attributes: _list[GoogleCloudVideointelligenceV1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    timestampedObjects: _list[GoogleCloudVideointelligenceV1_TimestampedObject]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_VideoAnnotationProgress(
    typing.TypedDict, total=False
):
    exportStatus: GoogleCloudVideointelligenceV1_ExportToOutputUriStatus
    feature: typing.Literal[
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
    typing.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1_ExplicitContentAnnotation
    faceAnnotations: _list[GoogleCloudVideointelligenceV1_FaceAnnotation]
    faceDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: _list[GoogleCloudVideointelligenceV1_LabelAnnotation]
    inputUri: str
    logoRecognitionAnnotations: _list[
        GoogleCloudVideointelligenceV1_LogoRecognitionAnnotation
    ]
    objectAnnotations: _list[GoogleCloudVideointelligenceV1_ObjectTrackingAnnotation]
    personDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1_VideoSegment
    segmentLabelAnnotations: _list[GoogleCloudVideointelligenceV1_LabelAnnotation]
    segmentPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1_LabelAnnotation
    ]
    shotAnnotations: _list[GoogleCloudVideointelligenceV1_VideoSegment]
    shotLabelAnnotations: _list[GoogleCloudVideointelligenceV1_LabelAnnotation]
    shotPresenceLabelAnnotations: _list[GoogleCloudVideointelligenceV1_LabelAnnotation]
    speechTranscriptions: _list[GoogleCloudVideointelligenceV1_SpeechTranscription]
    textAnnotations: _list[GoogleCloudVideointelligenceV1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1_VideoSegment(typing.TypedDict, total=False):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1_WordInfo(typing.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerLabel: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgress(
    typing.TypedDict, total=False
):
    annotationProgress: _list[
        GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_AnnotateVideoRequest(
    typing.TypedDict, total=False
):
    features: _list[
        typing.Literal[
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
    ]
    inputContent: str
    inputUri: str
    locationId: str
    outputUri: str
    videoContext: GoogleCloudVideointelligenceV1beta2_VideoContext

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponse(
    typing.TypedDict, total=False
):
    annotationResults: _list[GoogleCloudVideointelligenceV1beta2_VideoAnnotationResults]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_DetectedAttribute(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_DetectedLandmark(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1beta2_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_Entity(typing.TypedDict, total=False):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ExplicitContentDetectionConfig(
    typing.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ExplicitContentFrame(
    typing.TypedDict, total=False
):
    pornographyLikelihood: typing.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ExportToOutputUriStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    status: GoogleRpc_Status

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceAnnotation(typing.TypedDict, total=False):
    frames: _list[GoogleCloudVideointelligenceV1beta2_FaceFrame]
    segments: _list[GoogleCloudVideointelligenceV1beta2_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotation(
    typing.TypedDict, total=False
):
    thumbnail: str
    tracks: _list[GoogleCloudVideointelligenceV1beta2_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceDetectionConfig(
    typing.TypedDict, total=False
):
    includeAttributes: bool
    includeBoundingBoxes: bool
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceFrame(typing.TypedDict, total=False):
    normalizedBoundingBoxes: _list[
        GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_FaceSegment(typing.TypedDict, total=False):
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LabelAnnotation(
    typing.TypedDict, total=False
):
    categoryEntities: _list[GoogleCloudVideointelligenceV1beta2_Entity]
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    frames: _list[GoogleCloudVideointelligenceV1beta2_LabelFrame]
    segments: _list[GoogleCloudVideointelligenceV1beta2_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LabelDetectionConfig(
    typing.TypedDict, total=False
):
    frameConfidenceThreshold: float
    labelDetectionMode: typing.Literal[
        "LABEL_DETECTION_MODE_UNSPECIFIED",
        "SHOT_MODE",
        "FRAME_MODE",
        "SHOT_AND_FRAME_MODE",
    ]
    model: str
    stationaryCamera: bool
    videoConfidenceThreshold: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LabelFrame(typing.TypedDict, total=False):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LabelSegment(typing.TypedDict, total=False):
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation(
    typing.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    segments: _list[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    tracks: _list[GoogleCloudVideointelligenceV1beta2_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox(
    typing.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly(
    typing.TypedDict, total=False
):
    vertices: _list[GoogleCloudVideointelligenceV1beta2_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_NormalizedVertex(
    typing.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation(
    typing.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1beta2_Entity
    frames: _list[GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ObjectTrackingConfig(
    typing.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrame(
    typing.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotation(
    typing.TypedDict, total=False
):
    tracks: _list[GoogleCloudVideointelligenceV1beta2_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_PersonDetectionConfig(
    typing.TypedDict, total=False
):
    includeAttributes: bool
    includeBoundingBoxes: bool
    includePoseLandmarks: bool

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_ShotChangeDetectionConfig(
    typing.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_SpeechContext(typing.TypedDict, total=False):
    phrases: _list[str]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative(
    typing.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: _list[GoogleCloudVideointelligenceV1beta2_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_SpeechTranscription(
    typing.TypedDict, total=False
):
    alternatives: _list[
        GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionConfig(
    typing.TypedDict, total=False
):
    audioOutputUriPrefix: str
    audioTracks: _list[int]
    diarizationSpeakerCount: int
    enableAutomaticPunctuation: bool
    enableSpeakerDiarization: bool
    enableWordConfidence: bool
    filterProfanity: bool
    languageCode: str
    maxAlternatives: int
    speechContexts: _list[GoogleCloudVideointelligenceV1beta2_SpeechContext]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TextAnnotation(typing.TypedDict, total=False):
    segments: _list[GoogleCloudVideointelligenceV1beta2_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TextDetectionConfig(
    typing.TypedDict, total=False
):
    languageHints: _list[str]
    model: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TextFrame(typing.TypedDict, total=False):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TextSegment(typing.TypedDict, total=False):
    confidence: float
    frames: _list[GoogleCloudVideointelligenceV1beta2_TextFrame]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_TimestampedObject(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    landmarks: _list[GoogleCloudVideointelligenceV1beta2_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_Track(typing.TypedDict, total=False):
    attributes: _list[GoogleCloudVideointelligenceV1beta2_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    timestampedObjects: _list[GoogleCloudVideointelligenceV1beta2_TimestampedObject]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgress(
    typing.TypedDict, total=False
):
    exportStatus: GoogleCloudVideointelligenceV1beta2_ExportToOutputUriStatus
    feature: typing.Literal[
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
    typing.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotation
    faceAnnotations: _list[GoogleCloudVideointelligenceV1beta2_FaceAnnotation]
    faceDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: _list[GoogleCloudVideointelligenceV1beta2_LabelAnnotation]
    inputUri: str
    logoRecognitionAnnotations: _list[
        GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotation
    ]
    objectAnnotations: _list[
        GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1beta2_VideoSegment
    segmentLabelAnnotations: _list[GoogleCloudVideointelligenceV1beta2_LabelAnnotation]
    segmentPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    shotAnnotations: _list[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    shotLabelAnnotations: _list[GoogleCloudVideointelligenceV1beta2_LabelAnnotation]
    shotPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1beta2_LabelAnnotation
    ]
    speechTranscriptions: _list[GoogleCloudVideointelligenceV1beta2_SpeechTranscription]
    textAnnotations: _list[GoogleCloudVideointelligenceV1beta2_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_VideoContext(typing.TypedDict, total=False):
    explicitContentDetectionConfig: (
        GoogleCloudVideointelligenceV1beta2_ExplicitContentDetectionConfig
    )
    faceDetectionConfig: GoogleCloudVideointelligenceV1beta2_FaceDetectionConfig
    labelDetectionConfig: GoogleCloudVideointelligenceV1beta2_LabelDetectionConfig
    objectTrackingConfig: GoogleCloudVideointelligenceV1beta2_ObjectTrackingConfig
    personDetectionConfig: GoogleCloudVideointelligenceV1beta2_PersonDetectionConfig
    segments: _list[GoogleCloudVideointelligenceV1beta2_VideoSegment]
    shotChangeDetectionConfig: (
        GoogleCloudVideointelligenceV1beta2_ShotChangeDetectionConfig
    )
    speechTranscriptionConfig: (
        GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionConfig
    )
    textDetectionConfig: GoogleCloudVideointelligenceV1beta2_TextDetectionConfig

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_VideoSegment(typing.TypedDict, total=False):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1beta2_WordInfo(typing.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerLabel: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgress(
    typing.TypedDict, total=False
):
    annotationProgress: _list[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponse(
    typing.TypedDict, total=False
):
    annotationResults: _list[
        GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_Entity(typing.TypedDict, total=False):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrame(
    typing.TypedDict, total=False
):
    pornographyLikelihood: typing.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ExportToOutputUriStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    status: GoogleRpc_Status

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1p1beta1_FaceFrame]
    segments: _list[GoogleCloudVideointelligenceV1p1beta1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotation(
    typing.TypedDict, total=False
):
    thumbnail: str
    tracks: _list[GoogleCloudVideointelligenceV1p1beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceFrame(typing.TypedDict, total=False):
    normalizedBoundingBoxes: _list[
        GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_FaceSegment(typing.TypedDict, total=False):
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation(
    typing.TypedDict, total=False
):
    categoryEntities: _list[GoogleCloudVideointelligenceV1p1beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    frames: _list[GoogleCloudVideointelligenceV1p1beta1_LabelFrame]
    segments: _list[GoogleCloudVideointelligenceV1p1beta1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LabelFrame(typing.TypedDict, total=False):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LabelSegment(typing.TypedDict, total=False):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation(
    typing.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    segments: _list[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    tracks: _list[GoogleCloudVideointelligenceV1p1beta1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox(
    typing.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly(
    typing.TypedDict, total=False
):
    vertices: _list[GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_NormalizedVertex(
    typing.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation(
    typing.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1p1beta1_Entity
    frames: _list[GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrame(
    typing.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotation(
    typing.TypedDict, total=False
):
    tracks: _list[GoogleCloudVideointelligenceV1p1beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative(
    typing.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: _list[GoogleCloudVideointelligenceV1p1beta1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription(
    typing.TypedDict, total=False
):
    alternatives: _list[
        GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TextAnnotation(
    typing.TypedDict, total=False
):
    segments: _list[GoogleCloudVideointelligenceV1p1beta1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TextFrame(typing.TypedDict, total=False):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TextSegment(typing.TypedDict, total=False):
    confidence: float
    frames: _list[GoogleCloudVideointelligenceV1p1beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_TimestampedObject(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    landmarks: _list[GoogleCloudVideointelligenceV1p1beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_Track(typing.TypedDict, total=False):
    attributes: _list[GoogleCloudVideointelligenceV1p1beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    timestampedObjects: _list[GoogleCloudVideointelligenceV1p1beta1_TimestampedObject]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgress(
    typing.TypedDict, total=False
):
    exportStatus: GoogleCloudVideointelligenceV1p1beta1_ExportToOutputUriStatus
    feature: typing.Literal[
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
    typing.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotation
    faceAnnotations: _list[GoogleCloudVideointelligenceV1p1beta1_FaceAnnotation]
    faceDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: _list[GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation]
    inputUri: str
    logoRecognitionAnnotations: _list[
        GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotation
    ]
    objectAnnotations: _list[
        GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p1beta1_VideoSegment
    segmentLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    shotAnnotations: _list[GoogleCloudVideointelligenceV1p1beta1_VideoSegment]
    shotLabelAnnotations: _list[GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation]
    shotPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p1beta1_LabelAnnotation
    ]
    speechTranscriptions: _list[
        GoogleCloudVideointelligenceV1p1beta1_SpeechTranscription
    ]
    textAnnotations: _list[GoogleCloudVideointelligenceV1p1beta1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_VideoSegment(typing.TypedDict, total=False):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p1beta1_WordInfo(typing.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerLabel: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgress(
    typing.TypedDict, total=False
):
    annotationProgress: _list[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponse(
    typing.TypedDict, total=False
):
    annotationResults: _list[
        GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_Entity(typing.TypedDict, total=False):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrame(
    typing.TypedDict, total=False
):
    pornographyLikelihood: typing.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ExportToOutputUriStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    status: GoogleRpc_Status

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1p2beta1_FaceFrame]
    segments: _list[GoogleCloudVideointelligenceV1p2beta1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotation(
    typing.TypedDict, total=False
):
    thumbnail: str
    tracks: _list[GoogleCloudVideointelligenceV1p2beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceFrame(typing.TypedDict, total=False):
    normalizedBoundingBoxes: _list[
        GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_FaceSegment(typing.TypedDict, total=False):
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation(
    typing.TypedDict, total=False
):
    categoryEntities: _list[GoogleCloudVideointelligenceV1p2beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: _list[GoogleCloudVideointelligenceV1p2beta1_LabelFrame]
    segments: _list[GoogleCloudVideointelligenceV1p2beta1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LabelFrame(typing.TypedDict, total=False):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LabelSegment(typing.TypedDict, total=False):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation(
    typing.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    segments: _list[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    tracks: _list[GoogleCloudVideointelligenceV1p2beta1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox(
    typing.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly(
    typing.TypedDict, total=False
):
    vertices: _list[GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_NormalizedVertex(
    typing.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation(
    typing.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1p2beta1_Entity
    frames: _list[GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrame(
    typing.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotation(
    typing.TypedDict, total=False
):
    tracks: _list[GoogleCloudVideointelligenceV1p2beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative(
    typing.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: _list[GoogleCloudVideointelligenceV1p2beta1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription(
    typing.TypedDict, total=False
):
    alternatives: _list[
        GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TextAnnotation(
    typing.TypedDict, total=False
):
    segments: _list[GoogleCloudVideointelligenceV1p2beta1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TextFrame(typing.TypedDict, total=False):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TextSegment(typing.TypedDict, total=False):
    confidence: float
    frames: _list[GoogleCloudVideointelligenceV1p2beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_TimestampedObject(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    landmarks: _list[GoogleCloudVideointelligenceV1p2beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_Track(typing.TypedDict, total=False):
    attributes: _list[GoogleCloudVideointelligenceV1p2beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    timestampedObjects: _list[GoogleCloudVideointelligenceV1p2beta1_TimestampedObject]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgress(
    typing.TypedDict, total=False
):
    exportStatus: GoogleCloudVideointelligenceV1p2beta1_ExportToOutputUriStatus
    feature: typing.Literal[
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
    typing.TypedDict, total=False
):
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotation
    faceAnnotations: _list[GoogleCloudVideointelligenceV1p2beta1_FaceAnnotation]
    faceDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: _list[GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation]
    inputUri: str
    logoRecognitionAnnotations: _list[
        GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotation
    ]
    objectAnnotations: _list[
        GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p2beta1_VideoSegment
    segmentLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    shotAnnotations: _list[GoogleCloudVideointelligenceV1p2beta1_VideoSegment]
    shotLabelAnnotations: _list[GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation]
    shotPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p2beta1_LabelAnnotation
    ]
    speechTranscriptions: _list[
        GoogleCloudVideointelligenceV1p2beta1_SpeechTranscription
    ]
    textAnnotations: _list[GoogleCloudVideointelligenceV1p2beta1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_VideoSegment(typing.TypedDict, total=False):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p2beta1_WordInfo(typing.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerLabel: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgress(
    typing.TypedDict, total=False
):
    annotationProgress: _list[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponse(
    typing.TypedDict, total=False
):
    annotationResults: _list[
        GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResults
    ]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_Celebrity(typing.TypedDict, total=False):
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation(
    typing.TypedDict, total=False
):
    celebrityTracks: _list[GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_CelebrityTrack(
    typing.TypedDict, total=False
):
    celebrities: _list[GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity]
    faceTrack: GoogleCloudVideointelligenceV1p3beta1_Track

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    value: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark(
    typing.TypedDict, total=False
):
    confidence: float
    name: str
    point: GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_Entity(typing.TypedDict, total=False):
    description: str
    entityId: str
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrame(
    typing.TypedDict, total=False
):
    pornographyLikelihood: typing.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ExportToOutputUriStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    status: GoogleRpc_Status

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceAnnotation(
    typing.TypedDict, total=False
):
    frames: _list[GoogleCloudVideointelligenceV1p3beta1_FaceFrame]
    segments: _list[GoogleCloudVideointelligenceV1p3beta1_FaceSegment]
    thumbnail: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation(
    typing.TypedDict, total=False
):
    thumbnail: str
    tracks: _list[GoogleCloudVideointelligenceV1p3beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceFrame(typing.TypedDict, total=False):
    normalizedBoundingBoxes: _list[
        GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    ]
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_FaceSegment(typing.TypedDict, total=False):
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation(
    typing.TypedDict, total=False
):
    categoryEntities: _list[GoogleCloudVideointelligenceV1p3beta1_Entity]
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    frames: _list[GoogleCloudVideointelligenceV1p3beta1_LabelFrame]
    segments: _list[GoogleCloudVideointelligenceV1p3beta1_LabelSegment]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LabelFrame(typing.TypedDict, total=False):
    confidence: float
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LabelSegment(typing.TypedDict, total=False):
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation(
    typing.TypedDict, total=False
):
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    segments: _list[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    tracks: _list[GoogleCloudVideointelligenceV1p3beta1_Track]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox(
    typing.TypedDict, total=False
):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly(
    typing.TypedDict, total=False
):
    vertices: _list[GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_NormalizedVertex(
    typing.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation(
    typing.TypedDict, total=False
):
    confidence: float
    entity: GoogleCloudVideointelligenceV1p3beta1_Entity
    frames: _list[GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    trackId: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrame(
    typing.TypedDict, total=False
):
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation(
    typing.TypedDict, total=False
):
    tracks: _list[GoogleCloudVideointelligenceV1p3beta1_Track]
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrity(
    typing.TypedDict, total=False
):
    celebrity: GoogleCloudVideointelligenceV1p3beta1_Celebrity
    confidence: float

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative(
    typing.TypedDict, total=False
):
    confidence: float
    transcript: str
    words: _list[GoogleCloudVideointelligenceV1p3beta1_WordInfo]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription(
    typing.TypedDict, total=False
):
    alternatives: _list[
        GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternative
    ]
    languageCode: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponse(
    typing.TypedDict, total=False
):
    annotationResults: (
        GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults
    )
    annotationResultsUri: str
    error: GoogleRpc_Status

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResults(
    typing.TypedDict, total=False
):
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    frameTimestamp: str
    labelAnnotations: _list[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    objectAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    shotAnnotations: _list[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TextAnnotation(
    typing.TypedDict, total=False
):
    segments: _list[GoogleCloudVideointelligenceV1p3beta1_TextSegment]
    text: str
    version: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TextFrame(typing.TypedDict, total=False):
    rotatedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TextSegment(typing.TypedDict, total=False):
    confidence: float
    frames: _list[GoogleCloudVideointelligenceV1p3beta1_TextFrame]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_TimestampedObject(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    landmarks: _list[GoogleCloudVideointelligenceV1p3beta1_DetectedLandmark]
    normalizedBoundingBox: GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBox
    timeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_Track(typing.TypedDict, total=False):
    attributes: _list[GoogleCloudVideointelligenceV1p3beta1_DetectedAttribute]
    confidence: float
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    timestampedObjects: _list[GoogleCloudVideointelligenceV1p3beta1_TimestampedObject]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgress(
    typing.TypedDict, total=False
):
    exportStatus: GoogleCloudVideointelligenceV1p3beta1_ExportToOutputUriStatus
    feature: typing.Literal[
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
    typing.TypedDict, total=False
):
    celebrityRecognitionAnnotations: (
        GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotation
    )
    error: GoogleRpc_Status
    explicitAnnotation: GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotation
    faceAnnotations: _list[GoogleCloudVideointelligenceV1p3beta1_FaceAnnotation]
    faceDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotation
    ]
    frameLabelAnnotations: _list[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    inputUri: str
    logoRecognitionAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotation
    ]
    objectAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotation
    ]
    personDetectionAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotation
    ]
    segment: GoogleCloudVideointelligenceV1p3beta1_VideoSegment
    segmentLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    segmentPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    shotAnnotations: _list[GoogleCloudVideointelligenceV1p3beta1_VideoSegment]
    shotLabelAnnotations: _list[GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation]
    shotPresenceLabelAnnotations: _list[
        GoogleCloudVideointelligenceV1p3beta1_LabelAnnotation
    ]
    speechTranscriptions: _list[
        GoogleCloudVideointelligenceV1p3beta1_SpeechTranscription
    ]
    textAnnotations: _list[GoogleCloudVideointelligenceV1p3beta1_TextAnnotation]

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_VideoSegment(typing.TypedDict, total=False):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudVideointelligenceV1p3beta1_WordInfo(typing.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerLabel: str
    speakerTag: int
    startTime: str
    word: str

@typing.type_check_only
class GoogleLongrunning_Operation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpc_Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpc_Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
