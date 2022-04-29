import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SheetsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class SpreadsheetsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeveloperMetadataResource(googleapiclient.discovery.Resource):
            def get(
                self, *, spreadsheetId: str, metadataId: int, **kwargs: typing.Any
            ) -> DeveloperMetadataHttpRequest: ...
            def search(
                self,
                *,
                spreadsheetId: str,
                body: SearchDeveloperMetadataRequest = ...,
                **kwargs: typing.Any
            ) -> SearchDeveloperMetadataResponseHttpRequest: ...

        @typing.type_check_only
        class SheetsResource(googleapiclient.discovery.Resource):
            def copyTo(
                self,
                *,
                spreadsheetId: str,
                sheetId: int,
                body: CopySheetToAnotherSpreadsheetRequest = ...,
                **kwargs: typing.Any
            ) -> SheetPropertiesHttpRequest: ...

        @typing.type_check_only
        class ValuesResource(googleapiclient.discovery.Resource):
            def append(
                self,
                *,
                spreadsheetId: str,
                range: str,
                body: ValueRange = ...,
                includeValuesInResponse: bool = ...,
                insertDataOption: typing_extensions.Literal[
                    "OVERWRITE", "INSERT_ROWS"
                ] = ...,
                responseDateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                responseValueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                valueInputOption: typing_extensions.Literal[
                    "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
                ] = ...,
                **kwargs: typing.Any
            ) -> AppendValuesResponseHttpRequest: ...
            def batchClear(
                self,
                *,
                spreadsheetId: str,
                body: BatchClearValuesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchClearValuesResponseHttpRequest: ...
            def batchClearByDataFilter(
                self,
                *,
                spreadsheetId: str,
                body: BatchClearValuesByDataFilterRequest = ...,
                **kwargs: typing.Any
            ) -> BatchClearValuesByDataFilterResponseHttpRequest: ...
            def batchGet(
                self,
                *,
                spreadsheetId: str,
                dateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                majorDimension: typing_extensions.Literal[
                    "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
                ] = ...,
                ranges: str | _list[str] = ...,
                valueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                **kwargs: typing.Any
            ) -> BatchGetValuesResponseHttpRequest: ...
            def batchGetByDataFilter(
                self,
                *,
                spreadsheetId: str,
                body: BatchGetValuesByDataFilterRequest = ...,
                **kwargs: typing.Any
            ) -> BatchGetValuesByDataFilterResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                spreadsheetId: str,
                body: BatchUpdateValuesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchUpdateValuesResponseHttpRequest: ...
            def batchUpdateByDataFilter(
                self,
                *,
                spreadsheetId: str,
                body: BatchUpdateValuesByDataFilterRequest = ...,
                **kwargs: typing.Any
            ) -> BatchUpdateValuesByDataFilterResponseHttpRequest: ...
            def clear(
                self,
                *,
                spreadsheetId: str,
                range: str,
                body: ClearValuesRequest = ...,
                **kwargs: typing.Any
            ) -> ClearValuesResponseHttpRequest: ...
            def get(
                self,
                *,
                spreadsheetId: str,
                range: str,
                dateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                majorDimension: typing_extensions.Literal[
                    "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
                ] = ...,
                valueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                **kwargs: typing.Any
            ) -> ValueRangeHttpRequest: ...
            def update(
                self,
                *,
                spreadsheetId: str,
                range: str,
                body: ValueRange = ...,
                includeValuesInResponse: bool = ...,
                responseDateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                responseValueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                valueInputOption: typing_extensions.Literal[
                    "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
                ] = ...,
                **kwargs: typing.Any
            ) -> UpdateValuesResponseHttpRequest: ...

        def batchUpdate(
            self,
            *,
            spreadsheetId: str,
            body: BatchUpdateSpreadsheetRequest = ...,
            **kwargs: typing.Any
        ) -> BatchUpdateSpreadsheetResponseHttpRequest: ...
        def create(
            self, *, body: Spreadsheet = ..., **kwargs: typing.Any
        ) -> SpreadsheetHttpRequest: ...
        def get(
            self,
            *,
            spreadsheetId: str,
            includeGridData: bool = ...,
            ranges: str | _list[str] = ...,
            **kwargs: typing.Any
        ) -> SpreadsheetHttpRequest: ...
        def getByDataFilter(
            self,
            *,
            spreadsheetId: str,
            body: GetSpreadsheetByDataFilterRequest = ...,
            **kwargs: typing.Any
        ) -> SpreadsheetHttpRequest: ...
        def developerMetadata(self) -> DeveloperMetadataResource: ...
        def sheets(self) -> SheetsResource: ...
        def values(self) -> ValuesResource: ...

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
    def spreadsheets(self) -> SpreadsheetsResource: ...

@typing.type_check_only
class AppendValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AppendValuesResponse: ...

@typing.type_check_only
class BatchClearValuesByDataFilterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchClearValuesByDataFilterResponse: ...

@typing.type_check_only
class BatchClearValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchClearValuesResponse: ...

@typing.type_check_only
class BatchGetValuesByDataFilterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchGetValuesByDataFilterResponse: ...

@typing.type_check_only
class BatchGetValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchGetValuesResponse: ...

@typing.type_check_only
class BatchUpdateSpreadsheetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchUpdateSpreadsheetResponse: ...

@typing.type_check_only
class BatchUpdateValuesByDataFilterResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchUpdateValuesByDataFilterResponse: ...

@typing.type_check_only
class BatchUpdateValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchUpdateValuesResponse: ...

@typing.type_check_only
class ClearValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClearValuesResponse: ...

@typing.type_check_only
class DeveloperMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeveloperMetadata: ...

@typing.type_check_only
class SearchDeveloperMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchDeveloperMetadataResponse: ...

@typing.type_check_only
class SheetPropertiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SheetProperties: ...

@typing.type_check_only
class SpreadsheetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Spreadsheet: ...

@typing.type_check_only
class UpdateValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UpdateValuesResponse: ...

@typing.type_check_only
class ValueRangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ValueRange: ...
