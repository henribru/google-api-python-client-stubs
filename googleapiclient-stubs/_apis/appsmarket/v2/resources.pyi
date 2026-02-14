import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GSuiteMarketplaceAPIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomerLicenseResource(googleapiclient.discovery.Resource):
        def get(
            self, *, applicationId: str, customerId: str, **kwargs: typing.Any
        ) -> CustomerLicenseHttpRequest: ...

    @typing.type_check_only
    class UserLicenseResource(googleapiclient.discovery.Resource):
        def get(
            self, *, applicationId: str, userId: str, **kwargs: typing.Any
        ) -> UserLicenseHttpRequest: ...

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
    def customerLicense(self) -> CustomerLicenseResource: ...
    def userLicense(self) -> UserLicenseResource: ...

@typing.type_check_only
class CustomerLicenseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomerLicense: ...

@typing.type_check_only
class UserLicenseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserLicense: ...
