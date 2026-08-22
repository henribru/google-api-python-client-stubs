import typing

_list = list

@typing.type_check_only
class ActiveConference(typing.TypedDict, total=False):
    conferenceRecord: str

@typing.type_check_only
class AnonymousUser(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class ArtifactConfig(typing.TypedDict, total=False):
    recordingConfig: RecordingConfig
    smartNotesConfig: SmartNotesConfig
    transcriptionConfig: TranscriptionConfig

@typing.type_check_only
class ConferenceRecord(typing.TypedDict, total=False):
    endTime: str
    expireTime: str
    name: str
    space: str
    startTime: str

@typing.type_check_only
class DocsDestination(typing.TypedDict, total=False):
    document: str
    exportUri: str

@typing.type_check_only
class DriveDestination(typing.TypedDict, total=False):
    exportUri: str
    file: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EndActiveConferenceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GatewaySipAccess(typing.TypedDict, total=False):
    sipAccessCode: str
    uri: str

@typing.type_check_only
class ListConferenceRecordsResponse(typing.TypedDict, total=False):
    conferenceRecords: _list[ConferenceRecord]
    nextPageToken: str

@typing.type_check_only
class ListParticipantSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    participantSessions: _list[ParticipantSession]

@typing.type_check_only
class ListParticipantsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    participants: _list[Participant]
    totalSize: int

@typing.type_check_only
class ListRecordingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    recordings: _list[Recording]

@typing.type_check_only
class ListSmartNotesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    smartNotes: _list[SmartNote]

@typing.type_check_only
class ListTranscriptEntriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    transcriptEntries: _list[TranscriptEntry]

@typing.type_check_only
class ListTranscriptsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    transcripts: _list[Transcript]

@typing.type_check_only
class ModerationRestrictions(typing.TypedDict, total=False):
    chatRestriction: typing.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED", "HOSTS_ONLY", "NO_RESTRICTION"
    ]
    defaultJoinAsViewerType: typing.Literal[
        "DEFAULT_JOIN_AS_VIEWER_TYPE_UNSPECIFIED", "ON", "OFF"
    ]
    presentRestriction: typing.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED", "HOSTS_ONLY", "NO_RESTRICTION"
    ]
    reactionRestriction: typing.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED", "HOSTS_ONLY", "NO_RESTRICTION"
    ]

@typing.type_check_only
class Participant(typing.TypedDict, total=False):
    anonymousUser: AnonymousUser
    earliestStartTime: str
    latestEndTime: str
    name: str
    phoneUser: PhoneUser
    signedinUser: SignedinUser

@typing.type_check_only
class ParticipantSession(typing.TypedDict, total=False):
    endTime: str
    name: str
    startTime: str

@typing.type_check_only
class PhoneAccess(typing.TypedDict, total=False):
    languageCode: str
    phoneNumber: str
    pin: str
    regionCode: str

@typing.type_check_only
class PhoneUser(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Recording(typing.TypedDict, total=False):
    driveDestination: DriveDestination
    endTime: str
    name: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "STARTED", "ENDED", "FILE_GENERATED"]

@typing.type_check_only
class RecordingConfig(typing.TypedDict, total=False):
    autoRecordingGeneration: typing.Literal[
        "AUTO_GENERATION_TYPE_UNSPECIFIED", "ON", "OFF"
    ]

@typing.type_check_only
class SignedinUser(typing.TypedDict, total=False):
    displayName: str
    user: str

@typing.type_check_only
class SmartNote(typing.TypedDict, total=False):
    docsDestination: DocsDestination
    endTime: str
    name: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "STARTED", "ENDED", "FILE_GENERATED"]

@typing.type_check_only
class SmartNotesConfig(typing.TypedDict, total=False):
    autoSmartNotesGeneration: typing.Literal[
        "AUTO_GENERATION_TYPE_UNSPECIFIED", "ON", "OFF"
    ]

@typing.type_check_only
class Space(typing.TypedDict, total=False):
    activeConference: ActiveConference
    config: SpaceConfig
    gatewaySipAccess: _list[GatewaySipAccess]
    meetingCode: str
    meetingUri: str
    name: str
    phoneAccess: _list[PhoneAccess]

@typing.type_check_only
class SpaceConfig(typing.TypedDict, total=False):
    accessType: typing.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "OPEN", "TRUSTED", "RESTRICTED"
    ]
    artifactConfig: ArtifactConfig
    attendanceReportGenerationType: typing.Literal[
        "ATTENDANCE_REPORT_GENERATION_TYPE_UNSPECIFIED",
        "GENERATE_REPORT",
        "DO_NOT_GENERATE",
    ]
    entryPointAccess: typing.Literal[
        "ENTRY_POINT_ACCESS_UNSPECIFIED", "ALL", "CREATOR_APP_ONLY"
    ]
    moderation: typing.Literal["MODERATION_UNSPECIFIED", "OFF", "ON"]
    moderationRestrictions: ModerationRestrictions

@typing.type_check_only
class Transcript(typing.TypedDict, total=False):
    docsDestination: DocsDestination
    endTime: str
    name: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "STARTED", "ENDED", "FILE_GENERATED"]

@typing.type_check_only
class TranscriptEntry(typing.TypedDict, total=False):
    endTime: str
    languageCode: str
    name: str
    participant: str
    startTime: str
    text: str

@typing.type_check_only
class TranscriptionConfig(typing.TypedDict, total=False):
    autoTranscriptionGeneration: typing.Literal[
        "AUTO_GENERATION_TYPE_UNSPECIFIED", "ON", "OFF"
    ]
