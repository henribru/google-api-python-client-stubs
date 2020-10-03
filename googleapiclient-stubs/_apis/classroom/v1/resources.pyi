import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ClassroomResource(googleapiclient.discovery.Resource):
    class CoursesResource(googleapiclient.discovery.Resource):
        class CourseWorkResource(googleapiclient.discovery.Resource):
            class StudentSubmissionsResource(googleapiclient.discovery.Resource):
                def turnIn(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: TurnInStudentSubmissionRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    late: typing_extensions.Literal[
                        "LATE_VALUES_UNSPECIFIED", "LATE_ONLY", "NOT_LATE_ONLY"
                    ] = ...,
                    pageSize: int = ...,
                    states: typing.Union[
                        typing_extensions.Literal[
                            "SUBMISSION_STATE_UNSPECIFIED",
                            "NEW",
                            "CREATED",
                            "TURNED_IN",
                            "RETURNED",
                            "RECLAIMED_BY_STUDENT",
                        ],
                        typing.List[
                            typing_extensions.Literal[
                                "SUBMISSION_STATE_UNSPECIFIED",
                                "NEW",
                                "CREATED",
                                "TURNED_IN",
                                "RETURNED",
                                "RECLAIMED_BY_STUDENT",
                            ]
                        ],
                    ] = ...,
                    pageToken: str = ...,
                    userId: str = ...,
                    **kwargs: typing.Any
                ) -> ListStudentSubmissionsResponseHttpRequest: ...
                def return_(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: ReturnStudentSubmissionRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def reclaim(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: ReclaimStudentSubmissionRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    **kwargs: typing.Any
                ) -> StudentSubmissionHttpRequest: ...
                def patch(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: StudentSubmission = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> StudentSubmissionHttpRequest: ...
                def modifyAttachments(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: ModifyAttachmentsRequest = ...,
                    **kwargs: typing.Any
                ) -> StudentSubmissionHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> CourseWorkHttpRequest: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: CourseWork = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> CourseWorkHttpRequest: ...
            def create(
                self, *, courseId: str, body: CourseWork = ..., **kwargs: typing.Any
            ) -> CourseWorkHttpRequest: ...
            def modifyAssignees(
                self,
                *,
                courseId: str,
                id: str,
                body: ModifyCourseWorkAssigneesRequest = ...,
                **kwargs: typing.Any
            ) -> CourseWorkHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                courseWorkStates: typing.Union[
                    typing_extensions.Literal[
                        "COURSE_WORK_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "COURSE_WORK_STATE_UNSPECIFIED",
                            "PUBLISHED",
                            "DRAFT",
                            "DELETED",
                        ]
                    ],
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                orderBy: str = ...,
                **kwargs: typing.Any
            ) -> ListCourseWorkResponseHttpRequest: ...
            def studentSubmissions(self) -> StudentSubmissionsResource: ...
        class TeachersResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTeachersResponseHttpRequest: ...
            def create(
                self, *, courseId: str, body: Teacher = ..., **kwargs: typing.Any
            ) -> TeacherHttpRequest: ...
            def get(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> TeacherHttpRequest: ...
        class CourseWorkMaterialsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                courseId: str,
                pageSize: int = ...,
                courseWorkMaterialStates: typing.Union[
                    typing_extensions.Literal[
                        "COURSEWORK_MATERIAL_STATE_UNSPECIFIED",
                        "PUBLISHED",
                        "DRAFT",
                        "DELETED",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "COURSEWORK_MATERIAL_STATE_UNSPECIFIED",
                            "PUBLISHED",
                            "DRAFT",
                            "DELETED",
                        ]
                    ],
                ] = ...,
                pageToken: str = ...,
                materialDriveId: str = ...,
                orderBy: str = ...,
                materialLink: str = ...,
                **kwargs: typing.Any
            ) -> ListCourseWorkMaterialResponseHttpRequest: ...
            def create(
                self,
                *,
                courseId: str,
                body: CourseWorkMaterial = ...,
                **kwargs: typing.Any
            ) -> CourseWorkMaterialHttpRequest: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: CourseWorkMaterial = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> CourseWorkMaterialHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> CourseWorkMaterialHttpRequest: ...
        class AliasesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, courseId: str, alias: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListCourseAliasesResponseHttpRequest: ...
            def create(
                self, *, courseId: str, body: CourseAlias = ..., **kwargs: typing.Any
            ) -> CourseAliasHttpRequest: ...
        class AnnouncementsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> AnnouncementHttpRequest: ...
            def modifyAssignees(
                self,
                *,
                courseId: str,
                id: str,
                body: ModifyAnnouncementAssigneesRequest = ...,
                **kwargs: typing.Any
            ) -> AnnouncementHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageSize: int = ...,
                orderBy: str = ...,
                pageToken: str = ...,
                announcementStates: typing.Union[
                    typing_extensions.Literal[
                        "ANNOUNCEMENT_STATE_UNSPECIFIED",
                        "PUBLISHED",
                        "DRAFT",
                        "DELETED",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "ANNOUNCEMENT_STATE_UNSPECIFIED",
                            "PUBLISHED",
                            "DRAFT",
                            "DELETED",
                        ]
                    ],
                ] = ...,
                **kwargs: typing.Any
            ) -> ListAnnouncementsResponseHttpRequest: ...
            def create(
                self, *, courseId: str, body: Announcement = ..., **kwargs: typing.Any
            ) -> AnnouncementHttpRequest: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: Announcement = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AnnouncementHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class TopicsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: Topic = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListTopicResponseHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, courseId: str, body: Topic = ..., **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
        class StudentsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                courseId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListStudentsResponseHttpRequest: ...
            def get(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> StudentHttpRequest: ...
            def create(
                self,
                *,
                courseId: str,
                body: Student = ...,
                enrollmentCode: str = ...,
                **kwargs: typing.Any
            ) -> StudentHttpRequest: ...
            def delete(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        def get(self, *, id: str, **kwargs: typing.Any) -> CourseHttpRequest: ...
        def update(
            self, *, id: str, body: Course = ..., **kwargs: typing.Any
        ) -> CourseHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            courseStates: typing.Union[
                typing_extensions.Literal[
                    "COURSE_STATE_UNSPECIFIED",
                    "ACTIVE",
                    "ARCHIVED",
                    "PROVISIONED",
                    "DECLINED",
                    "SUSPENDED",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "COURSE_STATE_UNSPECIFIED",
                        "ACTIVE",
                        "ARCHIVED",
                        "PROVISIONED",
                        "DECLINED",
                        "SUSPENDED",
                    ]
                ],
            ] = ...,
            pageToken: str = ...,
            studentId: str = ...,
            teacherId: str = ...,
            **kwargs: typing.Any
        ) -> ListCoursesResponseHttpRequest: ...
        def patch(
            self,
            *,
            id: str,
            body: Course = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> CourseHttpRequest: ...
        def create(
            self, *, body: Course = ..., **kwargs: typing.Any
        ) -> CourseHttpRequest: ...
        def delete(self, *, id: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def courseWork(self) -> CourseWorkResource: ...
        def teachers(self) -> TeachersResource: ...
        def courseWorkMaterials(self) -> CourseWorkMaterialsResource: ...
        def aliases(self) -> AliasesResource: ...
        def announcements(self) -> AnnouncementsResource: ...
        def topics(self) -> TopicsResource: ...
        def students(self) -> StudentsResource: ...
    class InvitationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            userId: str = ...,
            pageToken: str = ...,
            courseId: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListInvitationsResponseHttpRequest: ...
        def create(
            self, *, body: Invitation = ..., **kwargs: typing.Any
        ) -> InvitationHttpRequest: ...
        def delete(self, *, id: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, id: str, **kwargs: typing.Any) -> InvitationHttpRequest: ...
        def accept(self, *, id: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
    class UserProfilesResource(googleapiclient.discovery.Resource):
        class GuardiansResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, studentId: str, guardianId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                studentId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                invitedEmailAddress: str = ...,
                **kwargs: typing.Any
            ) -> ListGuardiansResponseHttpRequest: ...
            def get(
                self, *, studentId: str, guardianId: str, **kwargs: typing.Any
            ) -> GuardianHttpRequest: ...
        class GuardianInvitationsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                studentId: str,
                body: GuardianInvitation = ...,
                **kwargs: typing.Any
            ) -> GuardianInvitationHttpRequest: ...
            def patch(
                self,
                *,
                studentId: str,
                invitationId: str,
                body: GuardianInvitation = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GuardianInvitationHttpRequest: ...
            def list(
                self,
                *,
                studentId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                states: typing.Union[
                    typing_extensions.Literal[
                        "GUARDIAN_INVITATION_STATE_UNSPECIFIED", "PENDING", "COMPLETE"
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "GUARDIAN_INVITATION_STATE_UNSPECIFIED",
                            "PENDING",
                            "COMPLETE",
                        ]
                    ],
                ] = ...,
                invitedEmailAddress: str = ...,
                **kwargs: typing.Any
            ) -> ListGuardianInvitationsResponseHttpRequest: ...
            def get(
                self, *, studentId: str, invitationId: str, **kwargs: typing.Any
            ) -> GuardianInvitationHttpRequest: ...
        def get(
            self, *, userId: str, **kwargs: typing.Any
        ) -> UserProfileHttpRequest: ...
        def guardians(self) -> GuardiansResource: ...
        def guardianInvitations(self) -> GuardianInvitationsResource: ...
    class RegistrationsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, registrationId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self, *, body: Registration = ..., **kwargs: typing.Any
        ) -> RegistrationHttpRequest: ...
    def courses(self) -> CoursesResource: ...
    def invitations(self) -> InvitationsResource: ...
    def userProfiles(self) -> UserProfilesResource: ...
    def registrations(self) -> RegistrationsResource: ...

class ListCoursesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCoursesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class CourseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Course: ...

class UserProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserProfile: ...

class StudentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Student: ...

class ListStudentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListStudentsResponse: ...

class ListCourseWorkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCourseWorkResponse: ...

class ListStudentSubmissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListStudentSubmissionsResponse: ...

class TeacherHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Teacher: ...

class CourseWorkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CourseWork: ...

class ListTeachersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTeachersResponse: ...

class ListTopicResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTopicResponse: ...

class InvitationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Invitation: ...

class CourseAliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CourseAlias: ...

class StudentSubmissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> StudentSubmission: ...

class RegistrationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Registration: ...

class ListCourseAliasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCourseAliasesResponse: ...

class ListGuardianInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGuardianInvitationsResponse: ...

class AnnouncementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Announcement: ...

class CourseWorkMaterialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CourseWorkMaterial: ...

class GuardianHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Guardian: ...

class ListAnnouncementsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAnnouncementsResponse: ...

class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Topic: ...

class GuardianInvitationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GuardianInvitation: ...

class ListInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListInvitationsResponse: ...

class ListGuardiansResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGuardiansResponse: ...

class ListCourseWorkMaterialResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCourseWorkMaterialResponse: ...
