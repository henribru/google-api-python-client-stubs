import typing

import typing_extensions

class DriveFolder(typing_extensions.TypedDict, total=False):
    title: str
    id: str
    alternateLink: str

class Assignment(typing_extensions.TypedDict, total=False):
    studentWorkFolder: DriveFolder

class ListStudentSubmissionsResponse(typing_extensions.TypedDict, total=False):
    studentSubmissions: typing.List[StudentSubmission]
    nextPageToken: str

class ReturnStudentSubmissionRequest(typing_extensions.TypedDict, total=False): ...

class ListGuardianInvitationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    guardianInvitations: typing.List[GuardianInvitation]

class CourseRosterChangesInfo(typing_extensions.TypedDict, total=False):
    courseId: str

class StateHistory(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATED",
        "TURNED_IN",
        "RETURNED",
        "RECLAIMED_BY_STUDENT",
        "STUDENT_EDITED_AFTER_TURN_IN",
    ]
    stateTimestamp: str
    actorUserId: str

class ListStudentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    students: typing.List[Student]

class Feed(typing_extensions.TypedDict, total=False):
    feedType: typing_extensions.Literal[
        "FEED_TYPE_UNSPECIFIED",
        "DOMAIN_ROSTER_CHANGES",
        "COURSE_ROSTER_CHANGES",
        "COURSE_WORK_CHANGES",
    ]
    courseRosterChangesInfo: CourseRosterChangesInfo
    courseWorkChangesInfo: CourseWorkChangesInfo

class ListCourseWorkResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    courseWork: typing.List[CourseWork]

class Guardian(typing_extensions.TypedDict, total=False):
    invitedEmailAddress: str
    guardianProfile: UserProfile
    guardianId: str
    studentId: str

class Announcement(typing_extensions.TypedDict, total=False):
    updateTime: str
    creatorUserId: str
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    courseId: str
    state: typing_extensions.Literal[
        "ANNOUNCEMENT_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    materials: typing.List[Material]
    id: str
    scheduledTime: str
    creationTime: str
    alternateLink: str
    individualStudentsOptions: IndividualStudentsOptions
    text: str

class ModifyAttachmentsRequest(typing_extensions.TypedDict, total=False):
    addAttachments: typing.List[Attachment]

class ModifyCourseWorkAssigneesRequest(typing_extensions.TypedDict, total=False):
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    modifyIndividualStudentsOptions: ModifyIndividualStudentsOptions

class CourseWorkChangesInfo(typing_extensions.TypedDict, total=False):
    courseId: str

class StudentSubmission(typing_extensions.TypedDict, total=False):
    courseId: str
    associatedWithDeveloper: bool
    multipleChoiceSubmission: MultipleChoiceSubmission
    shortAnswerSubmission: ShortAnswerSubmission
    alternateLink: str
    courseWorkId: str
    state: typing_extensions.Literal[
        "SUBMISSION_STATE_UNSPECIFIED",
        "NEW",
        "CREATED",
        "TURNED_IN",
        "RETURNED",
        "RECLAIMED_BY_STUDENT",
    ]
    courseWorkType: typing_extensions.Literal[
        "COURSE_WORK_TYPE_UNSPECIFIED",
        "ASSIGNMENT",
        "SHORT_ANSWER_QUESTION",
        "MULTIPLE_CHOICE_QUESTION",
    ]
    updateTime: str
    draftGrade: float
    late: bool
    userId: str
    assignedGrade: float
    id: str
    creationTime: str
    assignmentSubmission: AssignmentSubmission
    submissionHistory: typing.List[SubmissionHistory]

class UserProfile(typing_extensions.TypedDict, total=False):
    id: str
    photoUrl: str
    name: Name
    permissions: typing.List[GlobalPermission]
    emailAddress: str
    verifiedTeacher: bool

class ModifyIndividualStudentsOptions(typing_extensions.TypedDict, total=False):
    addStudentIds: typing.List[str]
    removeStudentIds: typing.List[str]

class Material(typing_extensions.TypedDict, total=False):
    youtubeVideo: YouTubeVideo
    driveFile: SharedDriveFile
    form: Form
    link: Link

class TimeOfDay(typing_extensions.TypedDict, total=False):
    seconds: int
    nanos: int
    hours: int
    minutes: int

class GuardianInvitation(typing_extensions.TypedDict, total=False):
    creationTime: str
    studentId: str
    invitedEmailAddress: str
    invitationId: str
    state: typing_extensions.Literal[
        "GUARDIAN_INVITATION_STATE_UNSPECIFIED", "PENDING", "COMPLETE"
    ]

class ListAnnouncementsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    announcements: typing.List[Announcement]

class CourseWork(typing_extensions.TypedDict, total=False):
    id: str
    description: str
    title: str
    topicId: str
    submissionModificationMode: typing_extensions.Literal[
        "SUBMISSION_MODIFICATION_MODE_UNSPECIFIED",
        "MODIFIABLE_UNTIL_TURNED_IN",
        "MODIFIABLE",
    ]
    dueTime: TimeOfDay
    courseId: str
    state: typing_extensions.Literal[
        "COURSE_WORK_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    associatedWithDeveloper: bool
    individualStudentsOptions: IndividualStudentsOptions
    dueDate: Date
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    creationTime: str
    workType: typing_extensions.Literal[
        "COURSE_WORK_TYPE_UNSPECIFIED",
        "ASSIGNMENT",
        "SHORT_ANSWER_QUESTION",
        "MULTIPLE_CHOICE_QUESTION",
    ]
    alternateLink: str
    updateTime: str
    assignment: Assignment
    creatorUserId: str
    materials: typing.List[Material]
    maxPoints: float
    scheduledTime: str
    multipleChoiceQuestion: MultipleChoiceQuestion

class Student(typing_extensions.TypedDict, total=False):
    studentWorkFolder: DriveFolder
    courseId: str
    profile: UserProfile
    userId: str

class GlobalPermission(typing_extensions.TypedDict, total=False):
    permission: typing_extensions.Literal["PERMISSION_UNSPECIFIED", "CREATE_COURSE"]

class Empty(typing_extensions.TypedDict, total=False): ...

class Attachment(typing_extensions.TypedDict, total=False):
    youTubeVideo: YouTubeVideo
    form: Form
    driveFile: DriveFile
    link: Link

class ShortAnswerSubmission(typing_extensions.TypedDict, total=False):
    answer: str

class TurnInStudentSubmissionRequest(typing_extensions.TypedDict, total=False): ...

class CourseWorkMaterial(typing_extensions.TypedDict, total=False):
    courseId: str
    topicId: str
    id: str
    title: str
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    materials: typing.List[Material]
    description: str
    creatorUserId: str
    individualStudentsOptions: IndividualStudentsOptions
    updateTime: str
    state: typing_extensions.Literal[
        "COURSEWORK_MATERIAL_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    alternateLink: str
    creationTime: str
    scheduledTime: str

class ListCoursesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    courses: typing.List[Course]

class Invitation(typing_extensions.TypedDict, total=False):
    role: typing_extensions.Literal[
        "COURSE_ROLE_UNSPECIFIED", "STUDENT", "TEACHER", "OWNER"
    ]
    id: str
    userId: str
    courseId: str

class Registration(typing_extensions.TypedDict, total=False):
    expiryTime: str
    registrationId: str
    feed: Feed
    cloudPubsubTopic: CloudPubsubTopic

class SharedDriveFile(typing_extensions.TypedDict, total=False):
    driveFile: DriveFile
    shareMode: typing_extensions.Literal[
        "UNKNOWN_SHARE_MODE", "VIEW", "EDIT", "STUDENT_COPY"
    ]

class ListGuardiansResponse(typing_extensions.TypedDict, total=False):
    guardians: typing.List[Guardian]
    nextPageToken: str

class Link(typing_extensions.TypedDict, total=False):
    title: str
    thumbnailUrl: str
    url: str

class CourseAlias(typing_extensions.TypedDict, total=False):
    alias: str

class CloudPubsubTopic(typing_extensions.TypedDict, total=False):
    topicName: str

class ListInvitationsResponse(typing_extensions.TypedDict, total=False):
    invitations: typing.List[Invitation]
    nextPageToken: str

class Name(typing_extensions.TypedDict, total=False):
    familyName: str
    fullName: str
    givenName: str

class GradeHistory(typing_extensions.TypedDict, total=False):
    pointsEarned: float
    actorUserId: str
    maxPoints: float
    gradeTimestamp: str
    gradeChangeType: typing_extensions.Literal[
        "UNKNOWN_GRADE_CHANGE_TYPE",
        "DRAFT_GRADE_POINTS_EARNED_CHANGE",
        "ASSIGNED_GRADE_POINTS_EARNED_CHANGE",
        "MAX_POINTS_CHANGE",
    ]

class MultipleChoiceSubmission(typing_extensions.TypedDict, total=False):
    answer: str

class ListTeachersResponse(typing_extensions.TypedDict, total=False):
    teachers: typing.List[Teacher]
    nextPageToken: str

class AssignmentSubmission(typing_extensions.TypedDict, total=False):
    attachments: typing.List[Attachment]

class IndividualStudentsOptions(typing_extensions.TypedDict, total=False):
    studentIds: typing.List[str]

class DriveFile(typing_extensions.TypedDict, total=False):
    thumbnailUrl: str
    title: str
    id: str
    alternateLink: str

class Teacher(typing_extensions.TypedDict, total=False):
    profile: UserProfile
    userId: str
    courseId: str

class ModifyAnnouncementAssigneesRequest(typing_extensions.TypedDict, total=False):
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    modifyIndividualStudentsOptions: ModifyIndividualStudentsOptions

class Form(typing_extensions.TypedDict, total=False):
    thumbnailUrl: str
    title: str
    formUrl: str
    responseUrl: str

class Topic(typing_extensions.TypedDict, total=False):
    name: str
    topicId: str
    updateTime: str
    courseId: str

class MultipleChoiceQuestion(typing_extensions.TypedDict, total=False):
    choices: typing.List[str]

class SubmissionHistory(typing_extensions.TypedDict, total=False):
    gradeHistory: GradeHistory
    stateHistory: StateHistory

class ReclaimStudentSubmissionRequest(typing_extensions.TypedDict, total=False): ...

class Date(typing_extensions.TypedDict, total=False):
    month: int
    day: int
    year: int

class ListTopicResponse(typing_extensions.TypedDict, total=False):
    topic: typing.List[Topic]
    nextPageToken: str

class ListCourseAliasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    aliases: typing.List[CourseAlias]

class CourseMaterial(typing_extensions.TypedDict, total=False):
    form: Form
    driveFile: DriveFile
    youTubeVideo: YouTubeVideo
    link: Link

class ListCourseWorkMaterialResponse(typing_extensions.TypedDict, total=False):
    courseWorkMaterial: typing.List[CourseWorkMaterial]
    nextPageToken: str

class Course(typing_extensions.TypedDict, total=False):
    section: str
    courseMaterialSets: typing.List[CourseMaterialSet]
    description: str
    room: str
    courseState: typing_extensions.Literal[
        "COURSE_STATE_UNSPECIFIED",
        "ACTIVE",
        "ARCHIVED",
        "PROVISIONED",
        "DECLINED",
        "SUSPENDED",
    ]
    courseGroupEmail: str
    ownerId: str
    alternateLink: str
    calendarId: str
    guardiansEnabled: bool
    updateTime: str
    id: str
    enrollmentCode: str
    creationTime: str
    descriptionHeading: str
    name: str
    teacherGroupEmail: str
    teacherFolder: DriveFolder

class CourseMaterialSet(typing_extensions.TypedDict, total=False):
    materials: typing.List[CourseMaterial]
    title: str

class YouTubeVideo(typing_extensions.TypedDict, total=False):
    title: str
    thumbnailUrl: str
    id: str
    alternateLink: str
