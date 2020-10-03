import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class VaultResource(googleapiclient.discovery.Resource):
    class MattersResource(googleapiclient.discovery.Resource):
        class ExportsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                matterId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListExportsResponseHttpRequest: ...
            def delete(
                self, *, matterId: str, exportId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, matterId: str, exportId: str, **kwargs: typing.Any
            ) -> ExportHttpRequest: ...
            def create(
                self, *, matterId: str, body: Export = ..., **kwargs: typing.Any
            ) -> ExportHttpRequest: ...
        class SavedQueriesResource(googleapiclient.discovery.Resource):
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
            def create(
                self, *, matterId: str, body: SavedQuery = ..., **kwargs: typing.Any
            ) -> SavedQueryHttpRequest: ...
        class HoldsResource(googleapiclient.discovery.Resource):
            class AccountsResource(googleapiclient.discovery.Resource):
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
                def create(
                    self,
                    *,
                    matterId: str,
                    holdId: str,
                    body: HeldAccount = ...,
                    **kwargs: typing.Any
                ) -> HeldAccountHttpRequest: ...
            def delete(
                self, *, matterId: str, holdId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                matterId: str,
                view: typing_extensions.Literal[
                    "HOLD_VIEW_UNSPECIFIED", "BASIC_HOLD", "FULL_HOLD"
                ] = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListHoldsResponseHttpRequest: ...
            def addHeldAccounts(
                self,
                *,
                matterId: str,
                holdId: str,
                body: AddHeldAccountsRequest = ...,
                **kwargs: typing.Any
            ) -> AddHeldAccountsResponseHttpRequest: ...
            def update(
                self,
                *,
                matterId: str,
                holdId: str,
                body: Hold = ...,
                **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
            def create(
                self, *, matterId: str, body: Hold = ..., **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
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
            def removeHeldAccounts(
                self,
                *,
                matterId: str,
                holdId: str,
                body: RemoveHeldAccountsRequest = ...,
                **kwargs: typing.Any
            ) -> RemoveHeldAccountsResponseHttpRequest: ...
            def accounts(self) -> AccountsResource: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            pageSize: int = ...,
            state: typing_extensions.Literal[
                "STATE_UNSPECIFIED", "OPEN", "CLOSED", "DELETED"
            ] = ...,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> ListMattersResponseHttpRequest: ...
        def update(
            self, *, matterId: str, body: Matter = ..., **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def undelete(
            self,
            *,
            matterId: str,
            body: UndeleteMatterRequest = ...,
            **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def create(
            self, *, body: Matter = ..., **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def reopen(
            self,
            *,
            matterId: str,
            body: ReopenMatterRequest = ...,
            **kwargs: typing.Any
        ) -> ReopenMatterResponseHttpRequest: ...
        def addPermissions(
            self,
            *,
            matterId: str,
            body: AddMatterPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> MatterPermissionHttpRequest: ...
        def close(self, *, matterId: str, body: CloseMatterRequest = ..., **kwargs: typing.Any) -> CloseMatterResponseHttpRequest: ...  # type: ignore
        def get(
            self,
            *,
            matterId: str,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def removePermissions(
            self,
            *,
            matterId: str,
            body: RemoveMatterPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(
            self, *, matterId: str, **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def exports(self) -> ExportsResource: ...
        def savedQueries(self) -> SavedQueriesResource: ...
        def holds(self) -> HoldsResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
    def matters(self) -> MattersResource: ...
    def operations(self) -> OperationsResource: ...

class ExportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Export: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListMattersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMattersResponse: ...

class SavedQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SavedQuery: ...

class ListHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListHeldAccountsResponse: ...

class ListSavedQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSavedQueriesResponse: ...

class AddHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AddHeldAccountsResponse: ...

class ListHoldsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListHoldsResponse: ...

class MatterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Matter: ...

class RemoveHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RemoveHeldAccountsResponse: ...

class ReopenMatterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReopenMatterResponse: ...

class HoldHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Hold: ...

class MatterPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MatterPermission: ...

class CloseMatterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CloseMatterResponse: ...

class HeldAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HeldAccount: ...

class ListExportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListExportsResponse: ...
