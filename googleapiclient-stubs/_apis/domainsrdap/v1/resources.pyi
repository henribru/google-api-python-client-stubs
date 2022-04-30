import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DomainsRDAPResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AutnumResource(googleapiclient.discovery.Resource):
        def get(
            self, *, autnumId: str, **kwargs: typing.Any
        ) -> RdapResponseHttpRequest: ...

    @typing.type_check_only
    class DomainResource(googleapiclient.discovery.Resource):
        def get(
            self, *, domainName: str, **kwargs: typing.Any
        ) -> HttpBodyHttpRequest: ...

    @typing.type_check_only
    class EntityResource(googleapiclient.discovery.Resource):
        def get(
            self, *, entityId: str, **kwargs: typing.Any
        ) -> RdapResponseHttpRequest: ...

    @typing.type_check_only
    class IpResource(googleapiclient.discovery.Resource):
        def get(
            self, *, ipId: str, ipId1: str, **kwargs: typing.Any
        ) -> RdapResponseHttpRequest: ...

    @typing.type_check_only
    class NameserverResource(googleapiclient.discovery.Resource):
        def get(
            self, *, nameserverId: str, **kwargs: typing.Any
        ) -> RdapResponseHttpRequest: ...

    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def getDomains(self, **kwargs: typing.Any) -> RdapResponseHttpRequest: ...
        def getEntities(self, **kwargs: typing.Any) -> RdapResponseHttpRequest: ...
        def getHelp(self, **kwargs: typing.Any) -> HttpBodyHttpRequest: ...
        def getIp(self, **kwargs: typing.Any) -> HttpBodyHttpRequest: ...
        def getNameservers(self, **kwargs: typing.Any) -> RdapResponseHttpRequest: ...

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
    def autnum(self) -> AutnumResource: ...
    def domain(self) -> DomainResource: ...
    def entity(self) -> EntityResource: ...
    def ip(self) -> IpResource: ...
    def nameserver(self) -> NameserverResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpBody: ...

@typing.type_check_only
class RdapResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RdapResponse: ...
