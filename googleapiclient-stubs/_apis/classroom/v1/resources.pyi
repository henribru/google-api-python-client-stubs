import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ClassroomResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CoursesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AliasesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, courseId: str, body: CourseAlias = ..., **kwargs: typing.Any
            ) -> CourseAliasHttpRequest: ...
            def delete(
                self, *, courseId: str, alias: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListCourseAliasesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCourseAliasesResponseHttpRequest,
                previous_response: ListCourseAliasesResponse,
            ) -> ListCourseAliasesResponseHttpRequest | None: ...

        @typing.type_check_only
        class AnnouncementsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddOnAttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    body: AddOnAttachment = ...,
                    addOnToken: str = ...,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def delete(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddOnAttachmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAddOnAttachmentsResponseHttpRequest,
                    previous_response: ListAddOnAttachmentsResponse,
                ) -> ListAddOnAttachmentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    body: AddOnAttachment = ...,
                    postId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...

            def create(
                self, *, courseId: str, body: Announcement = ..., **kwargs: typing.Any
            ) -> AnnouncementHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> AnnouncementHttpRequest: ...
            def getAddOnContext(
                self,
                *,
                courseId: str,
                itemId: str,
                addOnToken: str = ...,
                attachmentId: str = ...,
                postId: str = ...,
                **kwargs: typing.Any,
            ) -> AddOnContextHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                announcementStates: typing_extensions.Literal[
                    "ANNOUNCEMENT_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
                ]
                | _list[
                    typing_extensions.Literal[
                        "ANNOUNCEMENT_STATE_UNSPECIFIED",
                        "PUBLISHED",
                        "DRAFT",
                        "DELETED",
                    ]
                ] = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAnnouncementsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAnnouncementsResponseHttpRequest,
                previous_response: ListAnnouncementsResponse,
            ) -> ListAnnouncementsResponseHttpRequest | None: ...
            def modifyAssignees(
                self,
                *,
                courseId: str,
                id: str,
                body: ModifyAnnouncementAssigneesRequest = ...,
                **kwargs: typing.Any,
            ) -> AnnouncementHttpRequest: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: Announcement = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> AnnouncementHttpRequest: ...
            def addOnAttachments(self) -> AddOnAttachmentsResource: ...

        @typing.type_check_only
        class CourseWorkResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddOnAttachmentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class StudentSubmissionsResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        courseId: str,
                        itemId: str,
                        attachmentId: str,
                        submissionId: str,
                        postId: str = ...,
                        **kwargs: typing.Any,
                    ) -> AddOnAttachmentStudentSubmissionHttpRequest: ...
                    def patch(
                        self,
                        *,
                        courseId: str,
                        itemId: str,
                        attachmentId: str,
                        submissionId: str,
                        body: AddOnAttachmentStudentSubmission = ...,
                        postId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> AddOnAttachmentStudentSubmissionHttpRequest: ...

                def create(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    body: AddOnAttachment = ...,
                    addOnToken: str = ...,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def delete(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddOnAttachmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAddOnAttachmentsResponseHttpRequest,
                    previous_response: ListAddOnAttachmentsResponse,
                ) -> ListAddOnAttachmentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    body: AddOnAttachment = ...,
                    postId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def studentSubmissions(self) -> StudentSubmissionsResource: ...

            @typing.type_check_only
            class RubricsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    body: Rubric = ...,
                    **kwargs: typing.Any,
                ) -> RubricHttpRequest: ...
                def delete(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    **kwargs: typing.Any,
                ) -> RubricHttpRequest: ...
                def list(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRubricsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRubricsResponseHttpRequest,
                    previous_response: ListRubricsResponse,
                ) -> ListRubricsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: Rubric = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> RubricHttpRequest: ...

            @typing.type_check_only
            class StudentSubmissionsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    **kwargs: typing.Any,
                ) -> StudentSubmissionHttpRequest: ...
                def list(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    late: typing_extensions.Literal[
                        "LATE_VALUES_UNSPECIFIED", "LATE_ONLY", "NOT_LATE_ONLY"
                    ] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    states: typing_extensions.Literal[
                        "SUBMISSION_STATE_UNSPECIFIED",
                        "NEW",
                        "CREATED",
                        "TURNED_IN",
                        "RETURNED",
                        "RECLAIMED_BY_STUDENT",
                    ]
                    | _list[
                        typing_extensions.Literal[
                            "SUBMISSION_STATE_UNSPECIFIED",
                            "NEW",
                            "CREATED",
                            "TURNED_IN",
                            "RETURNED",
                            "RECLAIMED_BY_STUDENT",
                        ]
                    ] = ...,
                    userId: str = ...,
                    **kwargs: typing.Any,
                ) -> ListStudentSubmissionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListStudentSubmissionsResponseHttpRequest,
                    previous_response: ListStudentSubmissionsResponse,
                ) -> ListStudentSubmissionsResponseHttpRequest | None: ...
                def modifyAttachments(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: ModifyAttachmentsRequest = ...,
                    **kwargs: typing.Any,
                ) -> StudentSubmissionHttpRequest: ...
                def patch(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: StudentSubmission = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> StudentSubmissionHttpRequest: ...
                def reclaim(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: ReclaimStudentSubmissionRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def return_(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: ReturnStudentSubmissionRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def turnIn(
                    self,
                    *,
                    courseId: str,
                    courseWorkId: str,
                    id: str,
                    body: TurnInStudentSubmissionRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...

            def create(
                self, *, courseId: str, body: CourseWork = ..., **kwargs: typing.Any
            ) -> CourseWorkHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> CourseWorkHttpRequest: ...
            def getAddOnContext(
                self,
                *,
                courseId: str,
                itemId: str,
                addOnToken: str = ...,
                attachmentId: str = ...,
                postId: str = ...,
                **kwargs: typing.Any,
            ) -> AddOnContextHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                courseWorkStates: typing_extensions.Literal[
                    "COURSE_WORK_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
                ]
                | _list[
                    typing_extensions.Literal[
                        "COURSE_WORK_STATE_UNSPECIFIED", "PUBLISHED", "DRAFT", "DELETED"
                    ]
                ] = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListCourseWorkResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCourseWorkResponseHttpRequest,
                previous_response: ListCourseWorkResponse,
            ) -> ListCourseWorkResponseHttpRequest | None: ...
            def modifyAssignees(
                self,
                *,
                courseId: str,
                id: str,
                body: ModifyCourseWorkAssigneesRequest = ...,
                **kwargs: typing.Any,
            ) -> CourseWorkHttpRequest: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: CourseWork = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> CourseWorkHttpRequest: ...
            def updateRubric(
                self,
                *,
                courseId: str,
                courseWorkId: str,
                body: Rubric = ...,
                id: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> RubricHttpRequest: ...
            def addOnAttachments(self) -> AddOnAttachmentsResource: ...
            def rubrics(self) -> RubricsResource: ...
            def studentSubmissions(self) -> StudentSubmissionsResource: ...

        @typing.type_check_only
        class CourseWorkMaterialsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddOnAttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    body: AddOnAttachment = ...,
                    addOnToken: str = ...,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def delete(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    postId: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddOnAttachmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAddOnAttachmentsResponseHttpRequest,
                    previous_response: ListAddOnAttachmentsResponse,
                ) -> ListAddOnAttachmentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    courseId: str,
                    itemId: str,
                    attachmentId: str,
                    body: AddOnAttachment = ...,
                    postId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...

            def create(
                self,
                *,
                courseId: str,
                body: CourseWorkMaterial = ...,
                **kwargs: typing.Any,
            ) -> CourseWorkMaterialHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> CourseWorkMaterialHttpRequest: ...
            def getAddOnContext(
                self,
                *,
                courseId: str,
                itemId: str,
                addOnToken: str = ...,
                attachmentId: str = ...,
                postId: str = ...,
                **kwargs: typing.Any,
            ) -> AddOnContextHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                courseWorkMaterialStates: typing_extensions.Literal[
                    "COURSEWORK_MATERIAL_STATE_UNSPECIFIED",
                    "PUBLISHED",
                    "DRAFT",
                    "DELETED",
                ]
                | _list[
                    typing_extensions.Literal[
                        "COURSEWORK_MATERIAL_STATE_UNSPECIFIED",
                        "PUBLISHED",
                        "DRAFT",
                        "DELETED",
                    ]
                ] = ...,
                materialDriveId: str = ...,
                materialLink: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListCourseWorkMaterialResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCourseWorkMaterialResponseHttpRequest,
                previous_response: ListCourseWorkMaterialResponse,
            ) -> ListCourseWorkMaterialResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: CourseWorkMaterial = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> CourseWorkMaterialHttpRequest: ...
            def addOnAttachments(self) -> AddOnAttachmentsResource: ...

        @typing.type_check_only
        class PostsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddOnAttachmentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class StudentSubmissionsResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        courseId: str,
                        postId: str,
                        attachmentId: str,
                        submissionId: str,
                        itemId: str = ...,
                        **kwargs: typing.Any,
                    ) -> AddOnAttachmentStudentSubmissionHttpRequest: ...
                    def patch(
                        self,
                        *,
                        courseId: str,
                        postId: str,
                        attachmentId: str,
                        submissionId: str,
                        body: AddOnAttachmentStudentSubmission = ...,
                        itemId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> AddOnAttachmentStudentSubmissionHttpRequest: ...

                def create(
                    self,
                    *,
                    courseId: str,
                    postId: str,
                    body: AddOnAttachment = ...,
                    addOnToken: str = ...,
                    itemId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def delete(
                    self,
                    *,
                    courseId: str,
                    postId: str,
                    attachmentId: str,
                    itemId: str = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    courseId: str,
                    postId: str,
                    attachmentId: str,
                    itemId: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    courseId: str,
                    postId: str,
                    itemId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddOnAttachmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAddOnAttachmentsResponseHttpRequest,
                    previous_response: ListAddOnAttachmentsResponse,
                ) -> ListAddOnAttachmentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    courseId: str,
                    postId: str,
                    attachmentId: str,
                    body: AddOnAttachment = ...,
                    itemId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> AddOnAttachmentHttpRequest: ...
                def studentSubmissions(self) -> StudentSubmissionsResource: ...

            def getAddOnContext(
                self,
                *,
                courseId: str,
                postId: str,
                addOnToken: str = ...,
                attachmentId: str = ...,
                itemId: str = ...,
                **kwargs: typing.Any,
            ) -> AddOnContextHttpRequest: ...
            def addOnAttachments(self) -> AddOnAttachmentsResource: ...

        @typing.type_check_only
        class StudentsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                courseId: str,
                body: Student = ...,
                enrollmentCode: str = ...,
                **kwargs: typing.Any,
            ) -> StudentHttpRequest: ...
            def delete(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> StudentHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListStudentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListStudentsResponseHttpRequest,
                previous_response: ListStudentsResponse,
            ) -> ListStudentsResponseHttpRequest | None: ...

        @typing.type_check_only
        class TeachersResource(googleapiclient.discovery.Resource):
            def create(
                self, *, courseId: str, body: Teacher = ..., **kwargs: typing.Any
            ) -> TeacherHttpRequest: ...
            def delete(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, userId: str, **kwargs: typing.Any
            ) -> TeacherHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListTeachersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTeachersResponseHttpRequest,
                previous_response: ListTeachersResponse,
            ) -> ListTeachersResponseHttpRequest | None: ...

        @typing.type_check_only
        class TopicsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, courseId: str, body: Topic = ..., **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def delete(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, courseId: str, id: str, **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def list(
                self,
                *,
                courseId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListTopicResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTopicResponseHttpRequest,
                previous_response: ListTopicResponse,
            ) -> ListTopicResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                courseId: str,
                id: str,
                body: Topic = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> TopicHttpRequest: ...

        def create(
            self, *, body: Course = ..., **kwargs: typing.Any
        ) -> CourseHttpRequest: ...
        def delete(self, *, id: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, id: str, **kwargs: typing.Any) -> CourseHttpRequest: ...
        def list(
            self,
            *,
            courseStates: typing_extensions.Literal[
                "COURSE_STATE_UNSPECIFIED",
                "ACTIVE",
                "ARCHIVED",
                "PROVISIONED",
                "DECLINED",
                "SUSPENDED",
            ]
            | _list[
                typing_extensions.Literal[
                    "COURSE_STATE_UNSPECIFIED",
                    "ACTIVE",
                    "ARCHIVED",
                    "PROVISIONED",
                    "DECLINED",
                    "SUSPENDED",
                ]
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            studentId: str = ...,
            teacherId: str = ...,
            **kwargs: typing.Any,
        ) -> ListCoursesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCoursesResponseHttpRequest,
            previous_response: ListCoursesResponse,
        ) -> ListCoursesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            id: str,
            body: Course = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> CourseHttpRequest: ...
        def update(
            self, *, id: str, body: Course = ..., **kwargs: typing.Any
        ) -> CourseHttpRequest: ...
        def aliases(self) -> AliasesResource: ...
        def announcements(self) -> AnnouncementsResource: ...
        def courseWork(self) -> CourseWorkResource: ...
        def courseWorkMaterials(self) -> CourseWorkMaterialsResource: ...
        def posts(self) -> PostsResource: ...
        def students(self) -> StudentsResource: ...
        def teachers(self) -> TeachersResource: ...
        def topics(self) -> TopicsResource: ...

    @typing.type_check_only
    class InvitationsResource(googleapiclient.discovery.Resource):
        def accept(self, *, id: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def create(
            self, *, body: Invitation = ..., **kwargs: typing.Any
        ) -> InvitationHttpRequest: ...
        def delete(self, *, id: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, id: str, **kwargs: typing.Any) -> InvitationHttpRequest: ...
        def list(
            self,
            *,
            courseId: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            userId: str = ...,
            **kwargs: typing.Any,
        ) -> ListInvitationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListInvitationsResponseHttpRequest,
            previous_response: ListInvitationsResponse,
        ) -> ListInvitationsResponseHttpRequest | None: ...

    @typing.type_check_only
    class RegistrationsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Registration = ..., **kwargs: typing.Any
        ) -> RegistrationHttpRequest: ...
        def delete(
            self, *, registrationId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...

    @typing.type_check_only
    class UserProfilesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class GuardianInvitationsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                studentId: str,
                body: GuardianInvitation = ...,
                **kwargs: typing.Any,
            ) -> GuardianInvitationHttpRequest: ...
            def get(
                self, *, studentId: str, invitationId: str, **kwargs: typing.Any
            ) -> GuardianInvitationHttpRequest: ...
            def list(
                self,
                *,
                studentId: str,
                invitedEmailAddress: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                states: typing_extensions.Literal[
                    "GUARDIAN_INVITATION_STATE_UNSPECIFIED", "PENDING", "COMPLETE"
                ]
                | _list[
                    typing_extensions.Literal[
                        "GUARDIAN_INVITATION_STATE_UNSPECIFIED", "PENDING", "COMPLETE"
                    ]
                ] = ...,
                **kwargs: typing.Any,
            ) -> ListGuardianInvitationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListGuardianInvitationsResponseHttpRequest,
                previous_response: ListGuardianInvitationsResponse,
            ) -> ListGuardianInvitationsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                studentId: str,
                invitationId: str,
                body: GuardianInvitation = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GuardianInvitationHttpRequest: ...

        @typing.type_check_only
        class GuardiansResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, studentId: str, guardianId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, studentId: str, guardianId: str, **kwargs: typing.Any
            ) -> GuardianHttpRequest: ...
            def list(
                self,
                *,
                studentId: str,
                invitedEmailAddress: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListGuardiansResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListGuardiansResponseHttpRequest,
                previous_response: ListGuardiansResponse,
            ) -> ListGuardiansResponseHttpRequest | None: ...

        def get(
            self, *, userId: str, **kwargs: typing.Any
        ) -> UserProfileHttpRequest: ...
        def guardianInvitations(self) -> GuardianInvitationsResource: ...
        def guardians(self) -> GuardiansResource: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def courses(self) -> CoursesResource: ...
    def invitations(self) -> InvitationsResource: ...
    def registrations(self) -> RegistrationsResource: ...
    def userProfiles(self) -> UserProfilesResource: ...

@typing.type_check_only
class AddOnAttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AddOnAttachment: ...

@typing.type_check_only
class AddOnAttachmentStudentSubmissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AddOnAttachmentStudentSubmission: ...

@typing.type_check_only
class AddOnContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AddOnContext: ...

@typing.type_check_only
class AnnouncementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Announcement: ...

@typing.type_check_only
class CourseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Course: ...

@typing.type_check_only
class CourseAliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CourseAlias: ...

@typing.type_check_only
class CourseWorkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CourseWork: ...

@typing.type_check_only
class CourseWorkMaterialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CourseWorkMaterial: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GuardianHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Guardian: ...

@typing.type_check_only
class GuardianInvitationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GuardianInvitation: ...

@typing.type_check_only
class InvitationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Invitation: ...

@typing.type_check_only
class ListAddOnAttachmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAddOnAttachmentsResponse: ...

@typing.type_check_only
class ListAnnouncementsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAnnouncementsResponse: ...

@typing.type_check_only
class ListCourseAliasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCourseAliasesResponse: ...

@typing.type_check_only
class ListCourseWorkMaterialResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCourseWorkMaterialResponse: ...

@typing.type_check_only
class ListCourseWorkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCourseWorkResponse: ...

@typing.type_check_only
class ListCoursesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCoursesResponse: ...

@typing.type_check_only
class ListGuardianInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGuardianInvitationsResponse: ...

@typing.type_check_only
class ListGuardiansResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGuardiansResponse: ...

@typing.type_check_only
class ListInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInvitationsResponse: ...

@typing.type_check_only
class ListRubricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRubricsResponse: ...

@typing.type_check_only
class ListStudentSubmissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListStudentSubmissionsResponse: ...

@typing.type_check_only
class ListStudentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListStudentsResponse: ...

@typing.type_check_only
class ListTeachersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTeachersResponse: ...

@typing.type_check_only
class ListTopicResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTopicResponse: ...

@typing.type_check_only
class RegistrationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Registration: ...

@typing.type_check_only
class RubricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Rubric: ...

@typing.type_check_only
class StudentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Student: ...

@typing.type_check_only
class StudentSubmissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StudentSubmission: ...

@typing.type_check_only
class TeacherHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Teacher: ...

@typing.type_check_only
class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Topic: ...

@typing.type_check_only
class UserProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserProfile: ...
