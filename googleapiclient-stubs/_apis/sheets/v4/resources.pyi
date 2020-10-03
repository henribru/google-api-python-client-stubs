import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SheetsResource(googleapiclient.discovery.Resource):
    class SpreadsheetsResource(googleapiclient.discovery.Resource):
        class SheetsResource(googleapiclient.discovery.Resource):
            def copyTo(
                self,
                *,
                spreadsheetId: str,
                sheetId: int,
                body: CopySheetToAnotherSpreadsheetRequest = ...,
                **kwargs: typing.Any
            ) -> SheetPropertiesHttpRequest: ...
        class DeveloperMetadataResource(googleapiclient.discovery.Resource):
            def search(
                self,
                *,
                spreadsheetId: str,
                body: SearchDeveloperMetadataRequest = ...,
                **kwargs: typing.Any
            ) -> SearchDeveloperMetadataResponseHttpRequest: ...
            def get(
                self, *, spreadsheetId: str, metadataId: int, **kwargs: typing.Any
            ) -> DeveloperMetadataHttpRequest: ...
        class ValuesResource(googleapiclient.discovery.Resource):
            def batchUpdateByDataFilter(
                self,
                *,
                spreadsheetId: str,
                body: BatchUpdateValuesByDataFilterRequest = ...,
                **kwargs: typing.Any
            ) -> BatchUpdateValuesByDataFilterResponseHttpRequest: ...
            def batchClearByDataFilter(
                self,
                *,
                spreadsheetId: str,
                body: BatchClearValuesByDataFilterRequest = ...,
                **kwargs: typing.Any
            ) -> BatchClearValuesByDataFilterResponseHttpRequest: ...
            def batchGetByDataFilter(
                self,
                *,
                spreadsheetId: str,
                body: BatchGetValuesByDataFilterRequest = ...,
                **kwargs: typing.Any
            ) -> BatchGetValuesByDataFilterResponseHttpRequest: ...
            def batchClear(
                self,
                *,
                spreadsheetId: str,
                body: BatchClearValuesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchClearValuesResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                spreadsheetId: str,
                body: BatchUpdateValuesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchUpdateValuesResponseHttpRequest: ...
            def append(
                self,
                *,
                spreadsheetId: str,
                range: str,
                body: ValueRange = ...,
                responseValueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                includeValuesInResponse: bool = ...,
                responseDateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                insertDataOption: typing_extensions.Literal[
                    "OVERWRITE", "INSERT_ROWS"
                ] = ...,
                valueInputOption: typing_extensions.Literal[
                    "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
                ] = ...,
                **kwargs: typing.Any
            ) -> AppendValuesResponseHttpRequest: ...
            def get(
                self,
                *,
                spreadsheetId: str,
                range: str,
                majorDimension: typing_extensions.Literal[
                    "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
                ] = ...,
                valueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                dateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                **kwargs: typing.Any
            ) -> ValueRangeHttpRequest: ...
            def batchGet(
                self,
                *,
                spreadsheetId: str,
                ranges: typing.Union[str, typing.List[str]] = ...,
                valueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                majorDimension: typing_extensions.Literal[
                    "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
                ] = ...,
                dateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                **kwargs: typing.Any
            ) -> BatchGetValuesResponseHttpRequest: ...
            def update(
                self,
                *,
                spreadsheetId: str,
                range: str,
                body: ValueRange = ...,
                responseValueRenderOption: typing_extensions.Literal[
                    "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
                ] = ...,
                responseDateTimeRenderOption: typing_extensions.Literal[
                    "SERIAL_NUMBER", "FORMATTED_STRING"
                ] = ...,
                valueInputOption: typing_extensions.Literal[
                    "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
                ] = ...,
                includeValuesInResponse: bool = ...,
                **kwargs: typing.Any
            ) -> UpdateValuesResponseHttpRequest: ...
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
            ranges: typing.Union[str, typing.List[str]] = ...,
            includeGridData: bool = ...,
            **kwargs: typing.Any
        ) -> SpreadsheetHttpRequest: ...
        def create(
            self, *, body: Spreadsheet = ..., **kwargs: typing.Any
        ) -> SpreadsheetHttpRequest: ...
        def getByDataFilter(
            self,
            *,
            spreadsheetId: str,
            body: GetSpreadsheetByDataFilterRequest = ...,
            **kwargs: typing.Any
        ) -> SpreadsheetHttpRequest: ...
        def batchUpdate(
            self,
            *,
            spreadsheetId: str,
            body: BatchUpdateSpreadsheetRequest = ...,
            **kwargs: typing.Any
        ) -> BatchUpdateSpreadsheetResponseHttpRequest: ...
        def sheets(self) -> SheetsResource: ...
        def developerMetadata(self) -> DeveloperMetadataResource: ...
        def values(self) -> ValuesResource: ...
    def spreadsheets(self) -> SpreadsheetsResource: ...

class BatchUpdateValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdateValuesResponse: ...

class DeveloperMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeveloperMetadata: ...

class AppendValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AppendValuesResponse: ...

class SheetPropertiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SheetProperties: ...

class SearchDeveloperMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchDeveloperMetadataResponse: ...

class BatchClearValuesByDataFilterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchClearValuesByDataFilterResponse: ...

class BatchUpdateValuesByDataFilterResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdateValuesByDataFilterResponse: ...

class UpdateValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UpdateValuesResponse: ...

class BatchUpdateSpreadsheetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdateSpreadsheetResponse: ...

class ValueRangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ValueRange: ...

class BatchClearValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchClearValuesResponse: ...

class SpreadsheetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Spreadsheet: ...

class ClearValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClearValuesResponse: ...

class BatchGetValuesByDataFilterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetValuesByDataFilterResponse: ...

class BatchGetValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetValuesResponse: ...
