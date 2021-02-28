import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class PeopleServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ContactGroupsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MembersResource(googleapiclient.discovery.Resource):
            def modify(
                self,
                *,
                resourceName: str,
                body: ModifyContactGroupMembersRequest = ...,
                **kwargs: typing.Any
            ) -> ModifyContactGroupMembersResponseHttpRequest: ...
        def batchGet(
            self,
            *,
            groupFields: str = ...,
            maxMembers: int = ...,
            resourceNames: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> BatchGetContactGroupsResponseHttpRequest: ...
        def create(
            self, *, body: CreateContactGroupRequest = ..., **kwargs: typing.Any
        ) -> ContactGroupHttpRequest: ...
        def delete(
            self, *, resourceName: str, deleteContacts: bool = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            resourceName: str,
            groupFields: str = ...,
            maxMembers: int = ...,
            **kwargs: typing.Any
        ) -> ContactGroupHttpRequest: ...
        def list(
            self,
            *,
            groupFields: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ListContactGroupsResponseHttpRequest: ...
        def update(
            self,
            *,
            resourceName: str,
            body: UpdateContactGroupRequest = ...,
            **kwargs: typing.Any
        ) -> ContactGroupHttpRequest: ...
        def members(self) -> MembersResource: ...
    @typing.type_check_only
    class OtherContactsResource(googleapiclient.discovery.Resource):
        def copyOtherContactToMyContactsGroup(
            self,
            *,
            resourceName: str,
            body: CopyOtherContactToMyContactsGroupRequest = ...,
            **kwargs: typing.Any
        ) -> PersonHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            readMask: str = ...,
            requestSyncToken: bool = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOtherContactsResponseHttpRequest: ...
        def search(
            self,
            *,
            pageSize: int = ...,
            query: str = ...,
            readMask: str = ...,
            **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
    @typing.type_check_only
    class PeopleResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConnectionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                resourceName: str,
                pageSize: int = ...,
                pageToken: str = ...,
                personFields: str = ...,
                requestMask_includeField: str = ...,
                requestSyncToken: bool = ...,
                sortOrder: typing_extensions.Literal[
                    "LAST_MODIFIED_ASCENDING",
                    "LAST_MODIFIED_DESCENDING",
                    "FIRST_NAME_ASCENDING",
                    "LAST_NAME_ASCENDING",
                ] = ...,
                sources: typing.Union[
                    typing_extensions.Literal[
                        "READ_SOURCE_TYPE_UNSPECIFIED",
                        "READ_SOURCE_TYPE_PROFILE",
                        "READ_SOURCE_TYPE_CONTACT",
                        "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "READ_SOURCE_TYPE_UNSPECIFIED",
                            "READ_SOURCE_TYPE_PROFILE",
                            "READ_SOURCE_TYPE_CONTACT",
                            "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                        ]
                    ],
                ] = ...,
                syncToken: str = ...,
                **kwargs: typing.Any
            ) -> ListConnectionsResponseHttpRequest: ...
        def createContact(
            self,
            *,
            body: Person = ...,
            personFields: str = ...,
            sources: typing.Union[
                typing_extensions.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "READ_SOURCE_TYPE_UNSPECIFIED",
                        "READ_SOURCE_TYPE_PROFILE",
                        "READ_SOURCE_TYPE_CONTACT",
                        "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> PersonHttpRequest: ...
        def deleteContact(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def deleteContactPhoto(
            self,
            *,
            resourceName: str,
            personFields: str = ...,
            sources: typing.Union[
                typing_extensions.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "READ_SOURCE_TYPE_UNSPECIFIED",
                        "READ_SOURCE_TYPE_PROFILE",
                        "READ_SOURCE_TYPE_CONTACT",
                        "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> DeleteContactPhotoResponseHttpRequest: ...
        def get(
            self,
            *,
            resourceName: str,
            personFields: str = ...,
            requestMask_includeField: str = ...,
            sources: typing.Union[
                typing_extensions.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "READ_SOURCE_TYPE_UNSPECIFIED",
                        "READ_SOURCE_TYPE_PROFILE",
                        "READ_SOURCE_TYPE_CONTACT",
                        "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> PersonHttpRequest: ...
        def getBatchGet(
            self,
            *,
            personFields: str = ...,
            requestMask_includeField: str = ...,
            resourceNames: typing.Union[str, typing.List[str]] = ...,
            sources: typing.Union[
                typing_extensions.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "READ_SOURCE_TYPE_UNSPECIFIED",
                        "READ_SOURCE_TYPE_PROFILE",
                        "READ_SOURCE_TYPE_CONTACT",
                        "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> GetPeopleResponseHttpRequest: ...
        def listDirectoryPeople(
            self,
            *,
            mergeSources: typing.Union[
                typing_extensions.Literal[
                    "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                        "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
                    ]
                ],
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            readMask: str = ...,
            requestSyncToken: bool = ...,
            sources: typing.Union[
                typing_extensions.Literal[
                    "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                        "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                        "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
                    ]
                ],
            ] = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ListDirectoryPeopleResponseHttpRequest: ...
        def searchContacts(
            self,
            *,
            pageSize: int = ...,
            query: str = ...,
            readMask: str = ...,
            **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
        def searchDirectoryPeople(
            self,
            *,
            mergeSources: typing.Union[
                typing_extensions.Literal[
                    "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                        "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
                    ]
                ],
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            readMask: str = ...,
            sources: typing.Union[
                typing_extensions.Literal[
                    "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                        "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                        "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> SearchDirectoryPeopleResponseHttpRequest: ...
        def updateContact(
            self,
            *,
            resourceName: str,
            body: Person = ...,
            personFields: str = ...,
            sources: typing.Union[
                typing_extensions.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "READ_SOURCE_TYPE_UNSPECIFIED",
                        "READ_SOURCE_TYPE_PROFILE",
                        "READ_SOURCE_TYPE_CONTACT",
                        "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    ]
                ],
            ] = ...,
            updatePersonFields: str = ...,
            **kwargs: typing.Any
        ) -> PersonHttpRequest: ...
        def updateContactPhoto(
            self,
            *,
            resourceName: str,
            body: UpdateContactPhotoRequest = ...,
            **kwargs: typing.Any
        ) -> UpdateContactPhotoResponseHttpRequest: ...
        def connections(self) -> ConnectionsResource: ...
    def contactGroups(self) -> ContactGroupsResource: ...
    def otherContacts(self) -> OtherContactsResource: ...
    def people(self) -> PeopleResource: ...

@typing.type_check_only
class BatchGetContactGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchGetContactGroupsResponse: ...

@typing.type_check_only
class ContactGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ContactGroup: ...

@typing.type_check_only
class DeleteContactPhotoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DeleteContactPhotoResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetPeopleResponse: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListContactGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListContactGroupsResponse: ...

@typing.type_check_only
class ListDirectoryPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListDirectoryPeopleResponse: ...

@typing.type_check_only
class ListOtherContactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListOtherContactsResponse: ...

@typing.type_check_only
class ModifyContactGroupMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ModifyContactGroupMembersResponse: ...

@typing.type_check_only
class PersonHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Person: ...

@typing.type_check_only
class SearchDirectoryPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchDirectoryPeopleResponse: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchResponse: ...

@typing.type_check_only
class UpdateContactPhotoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UpdateContactPhotoResponse: ...
