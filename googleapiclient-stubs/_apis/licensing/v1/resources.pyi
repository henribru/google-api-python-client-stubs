import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class LicensingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LicenseAssignmentsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, productId: str, skuId: str, userId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, productId: str, skuId: str, userId: str, **kwargs: typing.Any
        ) -> LicenseAssignmentHttpRequest: ...
        def insert(
            self,
            *,
            productId: str,
            skuId: str,
            body: LicenseAssignmentInsert = ...,
            **kwargs: typing.Any
        ) -> LicenseAssignmentHttpRequest: ...
        def listForProduct(
            self,
            *,
            productId: str,
            customerId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LicenseAssignmentListHttpRequest: ...
        def listForProductAndSku(
            self,
            *,
            productId: str,
            skuId: str,
            customerId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LicenseAssignmentListHttpRequest: ...
        def patch(
            self,
            *,
            productId: str,
            skuId: str,
            userId: str,
            body: LicenseAssignment = ...,
            **kwargs: typing.Any
        ) -> LicenseAssignmentHttpRequest: ...
        def update(
            self,
            *,
            productId: str,
            skuId: str,
            userId: str,
            body: LicenseAssignment = ...,
            **kwargs: typing.Any
        ) -> LicenseAssignmentHttpRequest: ...
    def licenseAssignments(self) -> LicenseAssignmentsResource: ...

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
class LicenseAssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LicenseAssignment: ...

@typing.type_check_only
class LicenseAssignmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LicenseAssignmentList: ...
