import typing

_list = list

@typing.type_check_only
class AddOnAttachment(typing.TypedDict, total=False):
    copyHistory: _list[CopyHistory]
    courseId: str
    dueDate: Date
    dueTime: TimeOfDay
    id: str
    itemId: str
    maxPoints: float
    postId: str
    studentViewUri: EmbedUri
    studentWorkReviewUri: EmbedUri
    teacherViewUri: EmbedUri
    title: str

@typing.type_check_only
class AddOnAttachmentStudentSubmission(typing.TypedDict, total=False):
    courseWorkSubmissionId: str
    id: str
    pointsEarned: float
    postSubmissionState: typing.Literal[
        "SUBMISSION_STATE_UNSPECIFIED",
        "NEW",
        "CREATED",
        "TURNED_IN",
        "RETURNED",
        "RECLAIMED_BY_STUDENT",
    ]
    userId: str

@typing.type_check_only
class AddOnContext(typing.TypedDict, total=False):
    courseId: str
    itemId: str
    postId: str
    studentContext: StudentContext
    supportsStudentWork: bool
    teacherContext: TeacherContext

@typing.type_check_only
class Announcement(typing.TypedDict, total=False):
    alternateLink: str
    assigneeMode: typing.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    courseId: str
    creationTime: str
    creatorUserId: str
    id: str
    individualStudentsOptions: IndividualStudentsOptions
    materials: _list[Material]
    scheduledTime: str
    state: typing.Literal[
        "ANNOUNCEMENT_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    text: str
    updateTime: str

@typing.type_check_only
class Assignment(typing.TypedDict, total=False):
    studentWorkFolder: DriveFolder

@typing.type_check_only
class AssignmentSubmission(typing.TypedDict, total=False):
    attachments: _list[Attachment]

@typing.type_check_only
class Attachment(typing.TypedDict, total=False):
    driveFile: DriveFile
    form: Form
    link: Link
    youTubeVideo: YouTubeVideo

@typing.type_check_only
class CloudPubsubTopic(typing.TypedDict, total=False):
    topicName: str

@typing.type_check_only
class CopyHistory(typing.TypedDict, total=False):
    attachmentId: str
    courseId: str
    itemId: str
    postId: str

@typing.type_check_only
class Course(typing.TypedDict, total=False):
    alternateLink: str
    calendarId: str
    courseGroupEmail: str
    courseMaterialSets: _list[CourseMaterialSet]
    courseState: typing.Literal[
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
    levels: str
    name: str
    ownerId: str
    room: str
    section: str
    subject: str
    teacherFolder: DriveFolder
    teacherGroupEmail: str
    updateTime: str

@typing.type_check_only
class CourseAlias(typing.TypedDict, total=False):
    alias: str

@typing.type_check_only
class CourseMaterial(typing.TypedDict, total=False):
    driveFile: DriveFile
    form: Form
    link: Link
    youTubeVideo: YouTubeVideo

@typing.type_check_only
class CourseMaterialSet(typing.TypedDict, total=False):
    materials: _list[CourseMaterial]
    title: str

@typing.type_check_only
class CourseRosterChangesInfo(typing.TypedDict, total=False):
    courseId: str

@typing.type_check_only
class CourseWork(typing.TypedDict, total=False):
    alternateLink: str
    assigneeMode: typing.Literal[
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
    gradingPeriodId: str
    id: str
    individualStudentsOptions: IndividualStudentsOptions
    materials: _list[Material]
    maxPoints: float
    multipleChoiceQuestion: MultipleChoiceQuestion
    scheduledTime: str
    state: typing.Literal[
        "COURSE_WORK_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    submissionModificationMode: typing.Literal[
        "SUBMISSION_MODIFICATION_MODE_UNSPECIFIED",
        "MODIFIABLE_UNTIL_TURNED_IN",
        "MODIFIABLE",
    ]
    title: str
    topicId: str
    updateTime: str
    workType: typing.Literal[
        "COURSE_WORK_TYPE_UNSPECIFIED",
        "ASSIGNMENT",
        "SHORT_ANSWER_QUESTION",
        "MULTIPLE_CHOICE_QUESTION",
    ]

@typing.type_check_only
class CourseWorkChangesInfo(typing.TypedDict, total=False):
    courseId: str

@typing.type_check_only
class CourseWorkMaterial(typing.TypedDict, total=False):
    alternateLink: str
    assigneeMode: typing.Literal[
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
    state: typing.Literal[
        "COURSEWORK_MATERIAL_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
    ]
    title: str
    topicId: str
    updateTime: str

@typing.type_check_only
class Criterion(typing.TypedDict, total=False):
    description: str
    id: str
    levels: _list[Level]
    title: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DriveFile(typing.TypedDict, total=False):
    alternateLink: str
    id: str
    thumbnailUrl: str
    title: str

@typing.type_check_only
class DriveFolder(typing.TypedDict, total=False):
    alternateLink: str
    id: str
    title: str

@typing.type_check_only
class EmbedUri(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Feed(typing.TypedDict, total=False):
    courseRosterChangesInfo: CourseRosterChangesInfo
    courseWorkChangesInfo: CourseWorkChangesInfo
    feedType: typing.Literal[
        "FEED_TYPE_UNSPECIFIED",
        "DOMAIN_ROSTER_CHANGES",
        "COURSE_ROSTER_CHANGES",
        "COURSE_WORK_CHANGES",
    ]

@typing.type_check_only
class Form(typing.TypedDict, total=False):
    formUrl: str
    responseUrl: str
    thumbnailUrl: str
    title: str

@typing.type_check_only
class GeminiGem(typing.TypedDict, total=False):
    id: str
    title: str
    url: str

@typing.type_check_only
class GlobalPermission(typing.TypedDict, total=False):
    permission: typing.Literal["PERMISSION_UNSPECIFIED", "CREATE_COURSE"]

@typing.type_check_only
class GradeCategory(typing.TypedDict, total=False):
    defaultGradeDenominator: int
    id: str
    name: str
    weight: int

@typing.type_check_only
class GradeHistory(typing.TypedDict, total=False):
    actorUserId: str
    gradeChangeType: typing.Literal[
        "UNKNOWN_GRADE_CHANGE_TYPE",
        "DRAFT_GRADE_POINTS_EARNED_CHANGE",
        "ASSIGNED_GRADE_POINTS_EARNED_CHANGE",
        "MAX_POINTS_CHANGE",
    ]
    gradeTimestamp: str
    maxPoints: float
    pointsEarned: float

@typing.type_check_only
class GradebookSettings(typing.TypedDict, total=False):
    calculationType: typing.Literal[
        "CALCULATION_TYPE_UNSPECIFIED", "TOTAL_POINTS", "WEIGHTED_CATEGORIES"
    ]
    displaySetting: typing.Literal[
        "DISPLAY_SETTING_UNSPECIFIED",
        "SHOW_OVERALL_GRADE",
        "HIDE_OVERALL_GRADE",
        "SHOW_TEACHERS_ONLY",
    ]
    gradeCategories: _list[GradeCategory]

@typing.type_check_only
class GradingPeriod(typing.TypedDict, total=False):
    endDate: Date
    id: str
    startDate: Date
    title: str

@typing.type_check_only
class GradingPeriodSettings(typing.TypedDict, total=False):
    applyToExistingCoursework: bool
    gradingPeriods: _list[GradingPeriod]

@typing.type_check_only
class Guardian(typing.TypedDict, total=False):
    guardianId: str
    guardianProfile: UserProfile
    invitedEmailAddress: str
    studentId: str

@typing.type_check_only
class GuardianInvitation(typing.TypedDict, total=False):
    creationTime: str
    invitationId: str
    invitedEmailAddress: str
    state: typing.Literal[
        "GUARDIAN_INVITATION_STATE_UNSPECIFIED", "PENDING", "COMPLETE"
    ]
    studentId: str

@typing.type_check_only
class IndividualStudentsOptions(typing.TypedDict, total=False):
    studentIds: _list[str]

@typing.type_check_only
class Invitation(typing.TypedDict, total=False):
    courseId: str
    id: str
    role: typing.Literal["COURSE_ROLE_UNSPECIFIED", "STUDENT", "TEACHER", "OWNER"]
    userId: str

@typing.type_check_only
class Level(typing.TypedDict, total=False):
    description: str
    id: str
    points: float
    title: str

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    thumbnailUrl: str
    title: str
    url: str

@typing.type_check_only
class ListAddOnAttachmentsResponse(typing.TypedDict, total=False):
    addOnAttachments: _list[AddOnAttachment]
    nextPageToken: str

@typing.type_check_only
class ListAnnouncementsResponse(typing.TypedDict, total=False):
    announcements: _list[Announcement]
    nextPageToken: str

@typing.type_check_only
class ListCourseAliasesResponse(typing.TypedDict, total=False):
    aliases: _list[CourseAlias]
    nextPageToken: str

@typing.type_check_only
class ListCourseWorkMaterialResponse(typing.TypedDict, total=False):
    courseWorkMaterial: _list[CourseWorkMaterial]
    nextPageToken: str

@typing.type_check_only
class ListCourseWorkResponse(typing.TypedDict, total=False):
    courseWork: _list[CourseWork]
    nextPageToken: str

@typing.type_check_only
class ListCoursesResponse(typing.TypedDict, total=False):
    courses: _list[Course]
    nextPageToken: str

@typing.type_check_only
class ListGuardianInvitationsResponse(typing.TypedDict, total=False):
    guardianInvitations: _list[GuardianInvitation]
    nextPageToken: str

@typing.type_check_only
class ListGuardiansResponse(typing.TypedDict, total=False):
    guardians: _list[Guardian]
    nextPageToken: str

@typing.type_check_only
class ListInvitationsResponse(typing.TypedDict, total=False):
    invitations: _list[Invitation]
    nextPageToken: str

@typing.type_check_only
class ListRubricsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rubrics: _list[Rubric]

@typing.type_check_only
class ListStudentGroupMembersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    studentGroupMembers: _list[StudentGroupMember]

@typing.type_check_only
class ListStudentGroupsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    studentGroups: _list[StudentGroup]

@typing.type_check_only
class ListStudentSubmissionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    studentSubmissions: _list[StudentSubmission]

@typing.type_check_only
class ListStudentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    students: _list[Student]

@typing.type_check_only
class ListTeachersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    teachers: _list[Teacher]

@typing.type_check_only
class ListTopicResponse(typing.TypedDict, total=False):
    nextPageToken: str
    topic: _list[Topic]

@typing.type_check_only
class Material(typing.TypedDict, total=False):
    driveFile: SharedDriveFile
    form: Form
    gem: GeminiGem
    link: Link
    notebook: NotebookLmNotebook
    youtubeVideo: YouTubeVideo

@typing.type_check_only
class ModifyAnnouncementAssigneesRequest(typing.TypedDict, total=False):
    assigneeMode: typing.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    modifyIndividualStudentsOptions: ModifyIndividualStudentsOptions

@typing.type_check_only
class ModifyAttachmentsRequest(typing.TypedDict, total=False):
    addAttachments: _list[Attachment]

@typing.type_check_only
class ModifyCourseWorkAssigneesRequest(typing.TypedDict, total=False):
    assigneeMode: typing.Literal[
        "ASSIGNEE_MODE_UNSPECIFIED", "ALL_STUDENTS", "INDIVIDUAL_STUDENTS"
    ]
    modifyIndividualStudentsOptions: ModifyIndividualStudentsOptions

@typing.type_check_only
class ModifyIndividualStudentsOptions(typing.TypedDict, total=False):
    addStudentIds: _list[str]
    removeStudentIds: _list[str]

@typing.type_check_only
class MultipleChoiceQuestion(typing.TypedDict, total=False):
    choices: _list[str]

@typing.type_check_only
class MultipleChoiceSubmission(typing.TypedDict, total=False):
    answer: str

@typing.type_check_only
class Name(typing.TypedDict, total=False):
    familyName: str
    fullName: str
    givenName: str

@typing.type_check_only
class NotebookLmNotebook(typing.TypedDict, total=False):
    id: str
    title: str
    url: str

@typing.type_check_only
class ReclaimStudentSubmissionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Registration(typing.TypedDict, total=False):
    cloudPubsubTopic: CloudPubsubTopic
    expiryTime: str
    feed: Feed
    registrationId: str

@typing.type_check_only
class ReturnStudentSubmissionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Rubric(typing.TypedDict, total=False):
    courseId: str
    courseWorkId: str
    creationTime: str
    criteria: _list[Criterion]
    id: str
    sourceSpreadsheetId: str
    updateTime: str

@typing.type_check_only
class RubricGrade(typing.TypedDict, total=False):
    criterionId: str
    levelId: str
    points: float

@typing.type_check_only
class SharedDriveFile(typing.TypedDict, total=False):
    driveFile: DriveFile
    shareMode: typing.Literal["UNKNOWN_SHARE_MODE", "VIEW", "EDIT", "STUDENT_COPY"]

@typing.type_check_only
class ShortAnswerSubmission(typing.TypedDict, total=False):
    answer: str

@typing.type_check_only
class StateHistory(typing.TypedDict, total=False):
    actorUserId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATED",
        "TURNED_IN",
        "RETURNED",
        "RECLAIMED_BY_STUDENT",
        "STUDENT_EDITED_AFTER_TURN_IN",
    ]
    stateTimestamp: str

@typing.type_check_only
class Student(typing.TypedDict, total=False):
    courseId: str
    profile: UserProfile
    studentWorkFolder: DriveFolder
    userId: str

@typing.type_check_only
class StudentContext(typing.TypedDict, total=False):
    submissionId: str

@typing.type_check_only
class StudentGroup(typing.TypedDict, total=False):
    courseId: str
    id: str
    title: str

@typing.type_check_only
class StudentGroupMember(typing.TypedDict, total=False):
    courseId: str
    studentGroupId: str
    userId: str

@typing.type_check_only
class StudentSubmission(typing.TypedDict, total=False):
    alternateLink: str
    assignedGrade: float
    assignedRubricGrades: dict[str, typing.Any]
    assignmentSubmission: AssignmentSubmission
    associatedWithDeveloper: bool
    courseId: str
    courseWorkId: str
    courseWorkType: typing.Literal[
        "COURSE_WORK_TYPE_UNSPECIFIED",
        "ASSIGNMENT",
        "SHORT_ANSWER_QUESTION",
        "MULTIPLE_CHOICE_QUESTION",
    ]
    creationTime: str
    draftGrade: float
    draftRubricGrades: dict[str, typing.Any]
    id: str
    late: bool
    multipleChoiceSubmission: MultipleChoiceSubmission
    shortAnswerSubmission: ShortAnswerSubmission
    state: typing.Literal[
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
class SubmissionHistory(typing.TypedDict, total=False):
    gradeHistory: GradeHistory
    stateHistory: StateHistory

@typing.type_check_only
class Teacher(typing.TypedDict, total=False):
    courseId: str
    profile: UserProfile
    userId: str

@typing.type_check_only
class TeacherContext(typing.TypedDict, total=False): ...

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class Topic(typing.TypedDict, total=False):
    courseId: str
    name: str
    topicId: str
    updateTime: str

@typing.type_check_only
class TurnInStudentSubmissionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UserProfile(typing.TypedDict, total=False):
    emailAddress: str
    id: str
    name: Name
    permissions: _list[GlobalPermission]
    photoUrl: str
    verifiedTeacher: bool

@typing.type_check_only
class YouTubeVideo(typing.TypedDict, total=False):
    alternateLink: str
    id: str
    thumbnailUrl: str
    title: str
