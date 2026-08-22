import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

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
                body: ModifyContactGroupMembersRequest,
                **kwargs: typing.Any,
            ) -> ModifyContactGroupMembersResponseHttpRequest: ...

        def batchGet(
            self,
            *,
            groupFields: str | None = ...,
            maxMembers: int | None = ...,
            resourceNames: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> BatchGetContactGroupsResponseHttpRequest: ...
        def create(
            self, *, body: CreateContactGroupRequest, **kwargs: typing.Any
        ) -> ContactGroupHttpRequest: ...
        def delete(
            self,
            *,
            resourceName: str,
            deleteContacts: bool | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            resourceName: str,
            groupFields: str | None = ...,
            maxMembers: int | None = ...,
            **kwargs: typing.Any,
        ) -> ContactGroupHttpRequest: ...
        def list(
            self,
            *,
            groupFields: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListContactGroupsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListContactGroupsResponseHttpRequest,
            previous_response: ListContactGroupsResponse,
        ) -> ListContactGroupsResponseHttpRequest | None: ...
        def update(
            self,
            *,
            resourceName: str,
            body: UpdateContactGroupRequest,
            **kwargs: typing.Any,
        ) -> ContactGroupHttpRequest: ...
        def members(self) -> MembersResource: ...

    @typing.type_check_only
    class OtherContactsResource(googleapiclient.discovery.Resource):
        def copyOtherContactToMyContactsGroup(
            self,
            *,
            resourceName: str,
            body: CopyOtherContactToMyContactsGroupRequest,
            **kwargs: typing.Any,
        ) -> PersonHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            readMask: str | None = ...,
            requestSyncToken: bool | None = ...,
            sources: typing.Literal[
                "READ_SOURCE_TYPE_UNSPECIFIED",
                "READ_SOURCE_TYPE_PROFILE",
                "READ_SOURCE_TYPE_CONTACT",
                "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                "READ_SOURCE_TYPE_OTHER_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
            ]
            | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListOtherContactsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOtherContactsResponseHttpRequest,
            previous_response: ListOtherContactsResponse,
        ) -> ListOtherContactsResponseHttpRequest | None: ...
        def search(
            self,
            *,
            pageSize: int | None = ...,
            query: str | None = ...,
            readMask: str | None = ...,
            **kwargs: typing.Any,
        ) -> SearchResponseHttpRequest: ...

    @typing.type_check_only
    class PeopleResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConnectionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                resourceName: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                personFields: str | None = ...,
                requestMask_includeField: str | None = ...,
                requestSyncToken: bool | None = ...,
                sortOrder: typing.Literal[
                    "LAST_MODIFIED_ASCENDING",
                    "LAST_MODIFIED_DESCENDING",
                    "FIRST_NAME_ASCENDING",
                    "LAST_NAME_ASCENDING",
                ]
                | None = ...,
                sources: typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
                | _list[
                    typing.Literal[
                        "READ_SOURCE_TYPE_UNSPECIFIED",
                        "READ_SOURCE_TYPE_PROFILE",
                        "READ_SOURCE_TYPE_CONTACT",
                        "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                        "READ_SOURCE_TYPE_OTHER_CONTACT",
                    ]
                ]
                | None = ...,
                syncToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListConnectionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListConnectionsResponseHttpRequest,
                previous_response: ListConnectionsResponse,
            ) -> ListConnectionsResponseHttpRequest | None: ...

        def batchCreateContacts(
            self, *, body: BatchCreateContactsRequest, **kwargs: typing.Any
        ) -> BatchCreateContactsResponseHttpRequest: ...
        def batchDeleteContacts(
            self, *, body: BatchDeleteContactsRequest, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def batchUpdateContacts(
            self, *, body: BatchUpdateContactsRequest, **kwargs: typing.Any
        ) -> BatchUpdateContactsResponseHttpRequest: ...
        def createContact(
            self,
            *,
            body: Person,
            personFields: str | None = ...,
            sources: typing.Literal[
                "READ_SOURCE_TYPE_UNSPECIFIED",
                "READ_SOURCE_TYPE_PROFILE",
                "READ_SOURCE_TYPE_CONTACT",
                "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                "READ_SOURCE_TYPE_OTHER_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PersonHttpRequest: ...
        def deleteContact(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def deleteContactPhoto(
            self,
            *,
            resourceName: str,
            personFields: str | None = ...,
            sources: typing.Literal[
                "READ_SOURCE_TYPE_UNSPECIFIED",
                "READ_SOURCE_TYPE_PROFILE",
                "READ_SOURCE_TYPE_CONTACT",
                "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                "READ_SOURCE_TYPE_OTHER_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> DeleteContactPhotoResponseHttpRequest: ...
        def get(
            self,
            *,
            resourceName: str,
            personFields: str | None = ...,
            requestMask_includeField: str | None = ...,
            sources: typing.Literal[
                "READ_SOURCE_TYPE_UNSPECIFIED",
                "READ_SOURCE_TYPE_PROFILE",
                "READ_SOURCE_TYPE_CONTACT",
                "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                "READ_SOURCE_TYPE_OTHER_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PersonHttpRequest: ...
        def getBatchGet(
            self,
            *,
            personFields: str | None = ...,
            requestMask_includeField: str | None = ...,
            resourceNames: str | _list[str] | None = ...,
            sources: typing.Literal[
                "READ_SOURCE_TYPE_UNSPECIFIED",
                "READ_SOURCE_TYPE_PROFILE",
                "READ_SOURCE_TYPE_CONTACT",
                "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                "READ_SOURCE_TYPE_OTHER_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> GetPeopleResponseHttpRequest: ...
        def listDirectoryPeople(
            self,
            *,
            mergeSources: typing.Literal[
                "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
                ]
            ]
            | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            readMask: str | None = ...,
            requestSyncToken: bool | None = ...,
            sources: typing.Literal[
                "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
            ]
            | _list[
                typing.Literal[
                    "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
                ]
            ]
            | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListDirectoryPeopleResponseHttpRequest: ...
        def listDirectoryPeople_next(
            self,
            previous_request: ListDirectoryPeopleResponseHttpRequest,
            previous_response: ListDirectoryPeopleResponse,
        ) -> ListDirectoryPeopleResponseHttpRequest | None: ...
        def searchContacts(
            self,
            *,
            pageSize: int | None = ...,
            query: str | None = ...,
            readMask: str | None = ...,
            sources: typing.Literal[
                "READ_SOURCE_TYPE_UNSPECIFIED",
                "READ_SOURCE_TYPE_PROFILE",
                "READ_SOURCE_TYPE_CONTACT",
                "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                "READ_SOURCE_TYPE_OTHER_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> SearchResponseHttpRequest: ...
        def searchDirectoryPeople(
            self,
            *,
            mergeSources: typing.Literal[
                "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "DIRECTORY_MERGE_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_MERGE_SOURCE_TYPE_CONTACT",
                ]
            ]
            | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            query: str | None = ...,
            readMask: str | None = ...,
            sources: typing.Literal[
                "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
            ]
            | _list[
                typing.Literal[
                    "DIRECTORY_SOURCE_TYPE_UNSPECIFIED",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_CONTACT",
                    "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE",
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> SearchDirectoryPeopleResponseHttpRequest: ...
        def searchDirectoryPeople_next(
            self,
            previous_request: SearchDirectoryPeopleResponseHttpRequest,
            previous_response: SearchDirectoryPeopleResponse,
        ) -> SearchDirectoryPeopleResponseHttpRequest | None: ...
        def updateContact(
            self,
            *,
            resourceName: str,
            body: Person,
            personFields: str | None = ...,
            sources: typing.Literal[
                "READ_SOURCE_TYPE_UNSPECIFIED",
                "READ_SOURCE_TYPE_PROFILE",
                "READ_SOURCE_TYPE_CONTACT",
                "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                "READ_SOURCE_TYPE_OTHER_CONTACT",
            ]
            | _list[
                typing.Literal[
                    "READ_SOURCE_TYPE_UNSPECIFIED",
                    "READ_SOURCE_TYPE_PROFILE",
                    "READ_SOURCE_TYPE_CONTACT",
                    "READ_SOURCE_TYPE_DOMAIN_CONTACT",
                    "READ_SOURCE_TYPE_OTHER_CONTACT",
                ]
            ]
            | None = ...,
            updatePersonFields: str | None = ...,
            **kwargs: typing.Any,
        ) -> PersonHttpRequest: ...
        def updateContactPhoto(
            self,
            *,
            resourceName: str,
            body: UpdateContactPhotoRequest,
            **kwargs: typing.Any,
        ) -> UpdateContactPhotoResponseHttpRequest: ...
        def connections(self) -> ConnectionsResource: ...

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
    def contactGroups(self) -> ContactGroupsResource: ...
    def otherContacts(self) -> OtherContactsResource: ...
    def people(self) -> PeopleResource: ...

@typing.type_check_only
class BatchCreateContactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchCreateContactsResponse: ...

@typing.type_check_only
class BatchGetContactGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetContactGroupsResponse: ...

@typing.type_check_only
class BatchUpdateContactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateContactsResponse: ...

@typing.type_check_only
class ContactGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ContactGroup: ...

@typing.type_check_only
class DeleteContactPhotoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeleteContactPhotoResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GetPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetPeopleResponse: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListContactGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListContactGroupsResponse: ...

@typing.type_check_only
class ListDirectoryPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDirectoryPeopleResponse: ...

@typing.type_check_only
class ListOtherContactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOtherContactsResponse: ...

@typing.type_check_only
class ModifyContactGroupMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ModifyContactGroupMembersResponse: ...

@typing.type_check_only
class PersonHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Person: ...

@typing.type_check_only
class SearchDirectoryPeopleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchDirectoryPeopleResponse: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchResponse: ...

@typing.type_check_only
class UpdateContactPhotoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UpdateContactPhotoResponse: ...
