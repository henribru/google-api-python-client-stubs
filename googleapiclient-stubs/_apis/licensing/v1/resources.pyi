import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class LicensingResource(googleapiclient.discovery.Resource):
    class LicenseAssignmentsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            productId: str,
            skuId: str,
            body: LicenseAssignmentInsert = ...,
            **kwargs: typing.Any
        ) -> LicenseAssignmentHttpRequest: ...
        def get(
            self, *, productId: str, skuId: str, userId: str, **kwargs: typing.Any
        ) -> LicenseAssignmentHttpRequest: ...
        def delete(
            self, *, productId: str, skuId: str, userId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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
    def licenseAssignments(self) -> LicenseAssignmentsResource: ...

class LicenseAssignmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LicenseAssignmentList: ...

class LicenseAssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LicenseAssignment: ...
