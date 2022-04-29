import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class VaultResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class MattersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ExportsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, matterId: str, body: Export = ..., **kwargs: typing.Any
            ) -> ExportHttpRequest: ...
            def delete(
                self, *, matterId: str, exportId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, matterId: str, exportId: str, **kwargs: typing.Any
            ) -> ExportHttpRequest: ...
            def list(
                self,
                *,
                matterId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListExportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListExportsResponseHttpRequest,
                previous_response: ListExportsResponse,
            ) -> ListExportsResponseHttpRequest | None: ...

        @typing.type_check_only
        class HoldsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AccountsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    matterId: str,
                    holdId: str,
                    body: HeldAccount = ...,
                    **kwargs: typing.Any
                ) -> HeldAccountHttpRequest: ...
                def delete(
                    self,
                    *,
                    matterId: str,
                    holdId: str,
                    accountId: str,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self, *, matterId: str, holdId: str, **kwargs: typing.Any
                ) -> ListHeldAccountsResponseHttpRequest: ...

            def addHeldAccounts(
                self,
                *,
                matterId: str,
                holdId: str,
                body: AddHeldAccountsRequest = ...,
                **kwargs: typing.Any
            ) -> AddHeldAccountsResponseHttpRequest: ...
            def create(
                self, *, matterId: str, body: Hold = ..., **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
            def delete(
                self, *, matterId: str, holdId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                matterId: str,
                holdId: str,
                view: typing_extensions.Literal[
                    "HOLD_VIEW_UNSPECIFIED", "BASIC_HOLD", "FULL_HOLD"
                ] = ...,
                **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
            def list(
                self,
                *,
                matterId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "HOLD_VIEW_UNSPECIFIED", "BASIC_HOLD", "FULL_HOLD"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListHoldsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListHoldsResponseHttpRequest,
                previous_response: ListHoldsResponse,
            ) -> ListHoldsResponseHttpRequest | None: ...
            def removeHeldAccounts(
                self,
                *,
                matterId: str,
                holdId: str,
                body: RemoveHeldAccountsRequest = ...,
                **kwargs: typing.Any
            ) -> RemoveHeldAccountsResponseHttpRequest: ...
            def update(
                self,
                *,
                matterId: str,
                holdId: str,
                body: Hold = ...,
                **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
            def accounts(self) -> AccountsResource: ...

        @typing.type_check_only
        class SavedQueriesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, matterId: str, body: SavedQuery = ..., **kwargs: typing.Any
            ) -> SavedQueryHttpRequest: ...
            def delete(
                self, *, matterId: str, savedQueryId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, matterId: str, savedQueryId: str, **kwargs: typing.Any
            ) -> SavedQueryHttpRequest: ...
            def list(
                self,
                *,
                matterId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSavedQueriesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSavedQueriesResponseHttpRequest,
                previous_response: ListSavedQueriesResponse,
            ) -> ListSavedQueriesResponseHttpRequest | None: ...

        def addPermissions(
            self,
            *,
            matterId: str,
            body: AddMatterPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> MatterPermissionHttpRequest: ...
        def close(self, *, matterId: str, body: CloseMatterRequest = ..., **kwargs: typing.Any) -> CloseMatterResponseHttpRequest: ...  # type: ignore
        def count(
            self,
            *,
            matterId: str,
            body: CountArtifactsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def create(
            self, *, body: Matter = ..., **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def delete(
            self, *, matterId: str, **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def get(
            self,
            *,
            matterId: str,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            state: typing_extensions.Literal[
                "STATE_UNSPECIFIED", "OPEN", "CLOSED", "DELETED"
            ] = ...,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> ListMattersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListMattersResponseHttpRequest,
            previous_response: ListMattersResponse,
        ) -> ListMattersResponseHttpRequest | None: ...
        def removePermissions(
            self,
            *,
            matterId: str,
            body: RemoveMatterPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def reopen(
            self,
            *,
            matterId: str,
            body: ReopenMatterRequest = ...,
            **kwargs: typing.Any
        ) -> ReopenMatterResponseHttpRequest: ...
        def undelete(
            self,
            *,
            matterId: str,
            body: UndeleteMatterRequest = ...,
            **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def update(
            self, *, matterId: str, body: Matter = ..., **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def exports(self) -> ExportsResource: ...
        def holds(self) -> HoldsResource: ...
        def savedQueries(self) -> SavedQueriesResource: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOperationsResponseHttpRequest,
            previous_response: ListOperationsResponse,
        ) -> ListOperationsResponseHttpRequest | None: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def matters(self) -> MattersResource: ...
    def operations(self) -> OperationsResource: ...

@typing.type_check_only
class AddHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AddHeldAccountsResponse: ...

@typing.type_check_only
class CloseMatterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CloseMatterResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ExportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Export: ...

@typing.type_check_only
class HeldAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HeldAccount: ...

@typing.type_check_only
class HoldHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Hold: ...

@typing.type_check_only
class ListExportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListExportsResponse: ...

@typing.type_check_only
class ListHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListHeldAccountsResponse: ...

@typing.type_check_only
class ListHoldsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListHoldsResponse: ...

@typing.type_check_only
class ListMattersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMattersResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListSavedQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSavedQueriesResponse: ...

@typing.type_check_only
class MatterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Matter: ...

@typing.type_check_only
class MatterPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MatterPermission: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class RemoveHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RemoveHeldAccountsResponse: ...

@typing.type_check_only
class ReopenMatterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReopenMatterResponse: ...

@typing.type_check_only
class SavedQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SavedQuery: ...
