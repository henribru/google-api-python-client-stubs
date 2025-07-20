import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActiveConference(typing_extensions.TypedDict, total=False):
    conferenceRecord: str

@typing.type_check_only
class AnonymousUser(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class ArtifactConfig(typing_extensions.TypedDict, total=False):
    recordingConfig: RecordingConfig
    smartNotesConfig: SmartNotesConfig
    transcriptionConfig: TranscriptionConfig

@typing.type_check_only
class ConferenceRecord(typing_extensions.TypedDict, total=False):
    endTime: str
    expireTime: str
    name: str
    space: str
    startTime: str

@typing.type_check_only
class DocsDestination(typing_extensions.TypedDict, total=False):
    document: str
    exportUri: str

@typing.type_check_only
class DriveDestination(typing_extensions.TypedDict, total=False):
    exportUri: str
    file: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EndActiveConferenceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListConferenceRecordsResponse(typing_extensions.TypedDict, total=False):
    conferenceRecords: _list[ConferenceRecord]
    nextPageToken: str

@typing.type_check_only
class ListParticipantSessionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    participantSessions: _list[ParticipantSession]

@typing.type_check_only
class ListParticipantsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    participants: _list[Participant]
    totalSize: int

@typing.type_check_only
class ListRecordingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    recordings: _list[Recording]

@typing.type_check_only
class ListTranscriptEntriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transcriptEntries: _list[TranscriptEntry]

@typing.type_check_only
class ListTranscriptsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transcripts: _list[Transcript]

@typing.type_check_only
class ModerationRestrictions(typing_extensions.TypedDict, total=False):
    chatRestriction: typing_extensions.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED", "HOSTS_ONLY", "NO_RESTRICTION"
    ]
    defaultJoinAsViewerType: typing_extensions.Literal[
        "DEFAULT_JOIN_AS_VIEWER_TYPE_UNSPECIFIED", "ON", "OFF"
    ]
    presentRestriction: typing_extensions.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED", "HOSTS_ONLY", "NO_RESTRICTION"
    ]
    reactionRestriction: typing_extensions.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED", "HOSTS_ONLY", "NO_RESTRICTION"
    ]

@typing.type_check_only
class Participant(typing_extensions.TypedDict, total=False):
    anonymousUser: AnonymousUser
    earliestStartTime: str
    latestEndTime: str
    name: str
    phoneUser: PhoneUser
    signedinUser: SignedinUser

@typing.type_check_only
class ParticipantSession(typing_extensions.TypedDict, total=False):
    endTime: str
    name: str
    startTime: str

@typing.type_check_only
class PhoneUser(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Recording(typing_extensions.TypedDict, total=False):
    driveDestination: DriveDestination
    endTime: str
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STARTED", "ENDED", "FILE_GENERATED"
    ]

@typing.type_check_only
class RecordingConfig(typing_extensions.TypedDict, total=False):
    autoRecordingGeneration: typing_extensions.Literal[
        "AUTO_GENERATION_TYPE_UNSPECIFIED", "ON", "OFF"
    ]

@typing.type_check_only
class SignedinUser(typing_extensions.TypedDict, total=False):
    displayName: str
    user: str

@typing.type_check_only
class SmartNotesConfig(typing_extensions.TypedDict, total=False):
    autoSmartNotesGeneration: typing_extensions.Literal[
        "AUTO_GENERATION_TYPE_UNSPECIFIED", "ON", "OFF"
    ]

@typing.type_check_only
class Space(typing_extensions.TypedDict, total=False):
    activeConference: ActiveConference
    config: SpaceConfig
    meetingCode: str
    meetingUri: str
    name: str

@typing.type_check_only
class SpaceConfig(typing_extensions.TypedDict, total=False):
    accessType: typing_extensions.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "OPEN", "TRUSTED", "RESTRICTED"
    ]
    artifactConfig: ArtifactConfig
    attendanceReportGenerationType: typing_extensions.Literal[
        "ATTENDANCE_REPORT_GENERATION_TYPE_UNSPECIFIED",
        "GENERATE_REPORT",
        "DO_NOT_GENERATE",
    ]
    entryPointAccess: typing_extensions.Literal[
        "ENTRY_POINT_ACCESS_UNSPECIFIED", "ALL", "CREATOR_APP_ONLY"
    ]
    moderation: typing_extensions.Literal["MODERATION_UNSPECIFIED", "OFF", "ON"]
    moderationRestrictions: ModerationRestrictions

@typing.type_check_only
class Transcript(typing_extensions.TypedDict, total=False):
    docsDestination: DocsDestination
    endTime: str
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STARTED", "ENDED", "FILE_GENERATED"
    ]

@typing.type_check_only
class TranscriptEntry(typing_extensions.TypedDict, total=False):
    endTime: str
    languageCode: str
    name: str
    participant: str
    startTime: str
    text: str

@typing.type_check_only
class TranscriptionConfig(typing_extensions.TypedDict, total=False):
    autoTranscriptionGeneration: typing_extensions.Literal[
        "AUTO_GENERATION_TYPE_UNSPECIFIED", "ON", "OFF"
    ]
