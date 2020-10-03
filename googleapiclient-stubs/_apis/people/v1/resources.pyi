import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PeopleServiceResource(googleapiclient.discovery.Resource):
    class OtherContactsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            syncToken: str = ...,
            requestSyncToken: bool = ...,
            pageSize: int = ...,
            readMask: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOtherContactsResponseHttpRequest: ...
        def copyOtherContactToMyContactsGroup(
            self,
            *,
            resourceName: str,
            body: CopyOtherContactToMyContactsGroupRequest = ...,
            **kwargs: typing.Any
        ) -> PersonHttpRequest: ...
    class PeopleResource(googleapiclient.discovery.Resource):
        class ConnectionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                resourceName: str,
                personFields: str = ...,
                pageSize: int = ...,
                syncToken: str = ...,
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
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListConnectionsResponseHttpRequest: ...
        def updateContactPhoto(
            self,
            *,
            resourceName: str,
            body: UpdateContactPhotoRequest = ...,
            **kwargs: typing.Any
        ) -> UpdateContactPhotoResponseHttpRequest: ...
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
        def createContact(
            self,
            *,
            body: Person = ...,
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
            personFields: str = ...,
            **kwargs: typing.Any
        ) -> PersonHttpRequest: ...
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
        def deleteContact(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def listDirectoryPeople(
            self,
            *,
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
            pageSize: int = ...,
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
            readMask: str = ...,
            syncToken: str = ...,
            requestSyncToken: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListDirectoryPeopleResponseHttpRequest: ...
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
            pageToken: str = ...,
            query: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> SearchDirectoryPeopleResponseHttpRequest: ...
        def deleteContactPhoto(
            self,
            *,
            resourceName: str,
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
            personFields: str = ...,
            **kwargs: typing.Any
        ) -> DeleteContactPhotoResponseHttpRequest: ...
        def getBatchGet(
            self,
            *,
            requestMask_includeField: str = ...,
            personFields: str = ...,
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
        def connections(self) -> ConnectionsResource: ...
    class ContactGroupsResource(googleapiclient.discovery.Resource):
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
            maxMembers: int = ...,
            resourceNames: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> BatchGetContactGroupsResponseHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ListContactGroupsResponseHttpRequest: ...
        def get(
            self, *, resourceName: str, maxMembers: int = ..., **kwargs: typing.Any
        ) -> ContactGroupHttpRequest: ...
        def create(
            self, *, body: CreateContactGroupRequest = ..., **kwargs: typing.Any
        ) -> ContactGroupHttpRequest: ...
        def update(
            self,
            *,
            resourceName: str,
            body: UpdateContactGroupRequest = ...,
            **kwargs: typing.Any
        ) -> ContactGroupHttpRequest: ...
        def delete(
            self, *, resourceName: str, deleteContacts: bool = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def members(self) -> MembersResource: ...
    def otherContacts(self) -> OtherContactsResource: ...
    def people(self) -> PeopleResource: ...
    def contactGroups(self) -> ContactGroupsResource: ...

class BatchGetContactGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetContactGroupsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ContactGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ContactGroup: ...

class UpdateContactPhotoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UpdateContactPhotoResponse: ...

class PersonHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Person: ...

class SearchDirectoryPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchDirectoryPeopleResponse: ...

class ListOtherContactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOtherContactsResponse: ...

class ListDirectoryPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDirectoryPeopleResponse: ...

class ModifyContactGroupMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ModifyContactGroupMembersResponse: ...

class GetPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetPeopleResponse: ...

class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConnectionsResponse: ...

class ListContactGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListContactGroupsResponse: ...

class DeleteContactPhotoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeleteContactPhotoResponse: ...
