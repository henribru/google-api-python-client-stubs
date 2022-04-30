import typing

import typing_extensions

_list = list

@typing.type_check_only
class Announcement(typing_extensions.TypedDict, total=False):
    alternateLink: str
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    courseId: str
    creationTime: str
    creatorUserId: str
    id: str
    individualStudentsOptions: IndividualStudentsOptions
    materials: _list[Material]
    scheduledTime: str
    state: typing_extensions.Literal[
        "ANNOUNCEMENT_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    text: str
    updateTime: str

@typing.type_check_only
class Assignment(typing_extensions.TypedDict, total=False):
    studentWorkFolder: DriveFolder

@typing.type_check_only
class AssignmentSubmission(typing_extensions.TypedDict, total=False):
    attachments: _list[Attachment]

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    driveFile: DriveFile
    form: Form
    link: Link
    youTubeVideo: YouTubeVideo

@typing.type_check_only
class CloudPubsubTopic(typing_extensions.TypedDict, total=False):
    topicName: str

@typing.type_check_only
class Course(typing_extensions.TypedDict, total=False):
    alternateLink: str
    calendarId: str
    courseGroupEmail: str
    courseMaterialSets: _list[CourseMaterialSet]
    courseState: typing_extensions.Literal[
        "COURSE_STATE_UNSPECIFIED",
        "ACTIVE",
        "ARCHIVED",
        "PROVISIONED",
        "DECLINED",
        "SUSPENDED",
    ]
    creationTime: str
    description: str
    descriptionHeading: str
    enrollmentCode: str
    gradebookSettings: GradebookSettings
    guardiansEnabled: bool
    id: str
    name: str
    ownerId: str
    room: str
    section: str
    teacherFolder: DriveFolder
    teacherGroupEmail: str
    updateTime: str

@typing.type_check_only
class CourseAlias(typing_extensions.TypedDict, total=False):
    alias: str

@typing.type_check_only
class CourseMaterial(typing_extensions.TypedDict, total=False):
    driveFile: DriveFile
    form: Form
    link: Link
    youTubeVideo: YouTubeVideo

@typing.type_check_only
class CourseMaterialSet(typing_extensions.TypedDict, total=False):
    materials: _list[CourseMaterial]
    title: str

@typing.type_check_only
class CourseRosterChangesInfo(typing_extensions.TypedDict, total=False):
    courseId: str

@typing.type_check_only
class CourseWork(typing_extensions.TypedDict, total=False):
    alternateLink: str
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    assignment: Assignment
    associatedWithDeveloper: bool
    courseId: str
    creationTime: str
    creatorUserId: str
    description: str
    dueDate: Date
    dueTime: TimeOfDay
    gradeCategory: GradeCategory
    id: str
    individualStudentsOptions: IndividualStudentsOptions
    materials: _list[Material]
    maxPoints: float
    multipleChoiceQuestion: MultipleChoiceQuestion
    scheduledTime: str
    state: typing_extensions.Literal[
        "COURSE_WORK_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    submissionModificationMode: typing_extensions.Literal[
        "SUBMISSION_MODIFICATION_MODE_UNSPECIFIED",
        "MODIFIABLE_UNTIL_TURNED_IN",
        "MODIFIABLE",
    ]
    title: str
    topicId: str
    updateTime: str
    workType: typing_extensions.Literal[
        "COURSE_WORK_TYPE_UNSPECIFIED",
        "ASSIGNMENT",
        "SHORT_ANSWER_QUESTION",
        "MULTIPLE_CHOICE_QUESTION",
    ]

@typing.type_check_only
class CourseWorkChangesInfo(typing_extensions.TypedDict, total=False):
    courseId: str

@typing.type_check_only
class CourseWorkMaterial(typing_extensions.TypedDict, total=False):
    alternateLink: str
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    courseId: str
    creationTime: str
    creatorUserId: str
    description: str
    id: str
    individualStudentsOptions: IndividualStudentsOptions
    materials: _list[Material]
    scheduledTime: str
    state: typing_extensions.Literal[
        "COURSEWORK_MATERIAL_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    title: str
    topicId: str
    updateTime: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DriveFile(typing_extensions.TypedDict, total=False):
    alternateLink: str
    id: str
    thumbnailUrl: str
    title: str

@typing.type_check_only
class DriveFolder(typing_extensions.TypedDict, total=False):
    alternateLink: str
    id: str
    title: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Feed(typing_extensions.TypedDict, total=False):
    courseRosterChangesInfo: CourseRosterChangesInfo
    courseWorkChangesInfo: CourseWorkChangesInfo
    feedType: typing_extensions.Literal[
        "FEED_TYPE_UNSPECIFIED",
        "DOMAIN_ROSTER_CHANGES",
        "COURSE_ROSTER_CHANGES",
        "COURSE_WORK_CHANGES",
    ]

@typing.type_check_only
class Form(typing_extensions.TypedDict, total=False):
    formUrl: str
    responseUrl: str
    thumbnailUrl: str
    title: str

@typing.type_check_only
class GlobalPermission(typing_extensions.TypedDict, total=False):
    permission: typing_extensions.Literal["PERMISSION_UNSPECIFIED", "CREATE_COURSE"]

@typing.type_check_only
class GradeCategory(typing_extensions.TypedDict, total=False):
    defaultGradeDenominator: int
    id: str
    name: str
    weight: int

@typing.type_check_only
class GradeHistory(typing_extensions.TypedDict, total=False):
    actorUserId: str
    gradeChangeType: typing_extensions.Literal[
        "UNKNOWN_GRADE_CHANGE_TYPE",
        "DRAFT_GRADE_POINTS_EARNED_CHANGE",
        "ASSIGNED_GRADE_POINTS_EARNED_CHANGE",
        "MAX_POINTS_CHANGE",
    ]
    gradeTimestamp: str
    maxPoints: float
    pointsEarned: float

@typing.type_check_only
class GradebookSettings(typing_extensions.TypedDict, total=False):
    calculationType: typing_extensions.Literal[
        "CALCULATION_TYPE_UNSPECIFIED", "TOTAL_POINTS", "WEIGHTED_CATEGORIES"
    ]
    displaySetting: typing_extensions.Literal[
        "DISPLAY_SETTING_UNSPECIFIED",
        "SHOW_OVERALL_GRADE",
        "HIDE_OVERALL_GRADE",
        "SHOW_TEACHERS_ONLY",
    ]
    gradeCategories: _list[GradeCategory]

@typing.type_check_only
class Guardian(typing_extensions.TypedDict, total=False):
    guardianId: str
    guardianProfile: UserProfile
    invitedEmailAddress: str
    studentId: str

@typing.type_check_only
class GuardianInvitation(typing_extensions.TypedDict, total=False):
    creationTime: str
    invitationId: str
    invitedEmailAddress: str
    state: typing_extensions.Literal[
        "GUARDIAN_INVITATION_STATE_UNSPECIFIED", "PENDING", "COMPLETE"
    ]
    studentId: str

@typing.type_check_only
class IndividualStudentsOptions(typing_extensions.TypedDict, total=False):
    studentIds: _list[str]

@typing.type_check_only
class Invitation(typing_extensions.TypedDict, total=False):
    courseId: str
    id: str
    role: typing_extensions.Literal[
        "COURSE_ROLE_UNSPECIFIED", "STUDENT", "TEACHER", "OWNER"
    ]
    userId: str

@typing.type_check_only
class Link(typing_extensions.TypedDict, total=False):
    thumbnailUrl: str
    title: str
    url: str

@typing.type_check_only
class ListAnnouncementsResponse(typing_extensions.TypedDict, total=False):
    announcements: _list[Announcement]
    nextPageToken: str

@typing.type_check_only
class ListCourseAliasesResponse(typing_extensions.TypedDict, total=False):
    aliases: _list[CourseAlias]
    nextPageToken: str

@typing.type_check_only
class ListCourseWorkMaterialResponse(typing_extensions.TypedDict, total=False):
    courseWorkMaterial: _list[CourseWorkMaterial]
    nextPageToken: str

@typing.type_check_only
class ListCourseWorkResponse(typing_extensions.TypedDict, total=False):
    courseWork: _list[CourseWork]
    nextPageToken: str

@typing.type_check_only
class ListCoursesResponse(typing_extensions.TypedDict, total=False):
    courses: _list[Course]
    nextPageToken: str

@typing.type_check_only
class ListGuardianInvitationsResponse(typing_extensions.TypedDict, total=False):
    guardianInvitations: _list[GuardianInvitation]
    nextPageToken: str

@typing.type_check_only
class ListGuardiansResponse(typing_extensions.TypedDict, total=False):
    guardians: _list[Guardian]
    nextPageToken: str

@typing.type_check_only
class ListInvitationsResponse(typing_extensions.TypedDict, total=False):
    invitations: _list[Invitation]
    nextPageToken: str

@typing.type_check_only
class ListStudentSubmissionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    studentSubmissions: _list[StudentSubmission]

@typing.type_check_only
class ListStudentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    students: _list[Student]

@typing.type_check_only
class ListTeachersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    teachers: _list[Teacher]

@typing.type_check_only
class ListTopicResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topic: _list[Topic]

@typing.type_check_only
class Material(typing_extensions.TypedDict, total=False):
    driveFile: SharedDriveFile
    form: Form
    link: Link
    youtubeVideo: YouTubeVideo

@typing.type_check_only
class ModifyAnnouncementAssigneesRequest(typing_extensions.TypedDict, total=False):
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    modifyIndividualStudentsOptions: ModifyIndividualStudentsOptions

@typing.type_check_only
class ModifyAttachmentsRequest(typing_extensions.TypedDict, total=False):
    addAttachments: _list[Attachment]

@typing.type_check_only
class ModifyCourseWorkAssigneesRequest(typing_extensions.TypedDict, total=False):
    assigneeMode: typing_extensions.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    modifyIndividualStudentsOptions: ModifyIndividualStudentsOptions

@typing.type_check_only
class ModifyIndividualStudentsOptions(typing_extensions.TypedDict, total=False):
    addStudentIds: _list[str]
    removeStudentIds: _list[str]

@typing.type_check_only
class MultipleChoiceQuestion(typing_extensions.TypedDict, total=False):
    choices: _list[str]

@typing.type_check_only
class MultipleChoiceSubmission(typing_extensions.TypedDict, total=False):
    answer: str

@typing.type_check_only
class Name(typing_extensions.TypedDict, total=False):
    familyName: str
    fullName: str
    givenName: str

@typing.type_check_only
class ReclaimStudentSubmissionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Registration(typing_extensions.TypedDict, total=False):
    cloudPubsubTopic: CloudPubsubTopic
    expiryTime: str
    feed: Feed
    registrationId: str

@typing.type_check_only
class ReturnStudentSubmissionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SharedDriveFile(typing_extensions.TypedDict, total=False):
    driveFile: DriveFile
    shareMode: typing_extensions.Literal[
        "UNKNOWN_SHARE_MODE", "VIEW", "EDIT", "STUDENT_COPY"
    ]

@typing.type_check_only
class ShortAnswerSubmission(typing_extensions.TypedDict, total=False):
    answer: str

@typing.type_check_only
class StateHistory(typing_extensions.TypedDict, total=False):
    actorUserId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATED",
        "TURNED_IN",
        "RETURNED",
        "RECLAIMED_BY_STUDENT",
        "STUDENT_EDITED_AFTER_TURN_IN",
    ]
    stateTimestamp: str

@typing.type_check_only
class Student(typing_extensions.TypedDict, total=False):
    courseId: str
    profile: UserProfile
    studentWorkFolder: DriveFolder
    userId: str

@typing.type_check_only
class StudentSubmission(typing_extensions.TypedDict, total=False):
    alternateLink: str
    assignedGrade: float
    assignmentSubmission: AssignmentSubmission
    associatedWithDeveloper: bool
    courseId: str
    courseWorkId: str
    courseWorkType: typing_extensions.Literal[
        "COURSE_WORK_TYPE_UNSPECIFIED",
        "ASSIGNMENT",
        "SHORT_ANSWER_QUESTION",
        "MULTIPLE_CHOICE_QUESTION",
    ]
    creationTime: str
    draftGrade: float
    id: str
    late: bool
    multipleChoiceSubmission: MultipleChoiceSubmission
    shortAnswerSubmission: ShortAnswerSubmission
    state: typing_extensions.Literal[
        "SUBMISSION_STATE_UNSPECIFIED",
        "NEW",
        "CREATED",
        "TURNED_IN",
        "RETURNED",
        "RECLAIMED_BY_STUDENT",
    ]
    submissionHistory: _list[SubmissionHistory]
    updateTime: str
    userId: str

@typing.type_check_only
class SubmissionHistory(typing_extensions.TypedDict, total=False):
    gradeHistory: GradeHistory
    stateHistory: StateHistory

@typing.type_check_only
class Teacher(typing_extensions.TypedDict, total=False):
    courseId: str
    profile: UserProfile
    userId: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    courseId: str
    name: str
    topicId: str
    updateTime: str

@typing.type_check_only
class TurnInStudentSubmissionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UserProfile(typing_extensions.TypedDict, total=False):
    emailAddress: str
    id: str
    name: Name
    permissions: _list[GlobalPermission]
    photoUrl: str
    verifiedTeacher: bool

@typing.type_check_only
class YouTubeVideo(typing_extensions.TypedDict, total=False):
    alternateLink: str
    id: str
    thumbnailUrl: str
    title: str
