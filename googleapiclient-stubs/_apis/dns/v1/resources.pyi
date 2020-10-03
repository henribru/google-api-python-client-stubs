import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DnsResource(googleapiclient.discovery.Resource):
    class ManagedZoneOperationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            pageToken: str = ...,
            sortBy: typing_extensions.Literal["startTime", "id"] = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> ManagedZoneOperationsListResponseHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            operation: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ManagedZonesResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            project: str,
            managedZone: str,
            body: ManagedZone = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ManagedZoneHttpRequest: ...
        def create(
            self,
            *,
            project: str,
            body: ManagedZone = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ManagedZoneHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            managedZone: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int = ...,
            dnsName: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ManagedZonesListResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            managedZone: str,
            body: ManagedZone = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, clientOperationId: str = ..., **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
    class ResourceRecordSetsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            pageToken: str = ...,
            maxResults: int = ...,
            name: str = ...,
            type: str = ...,
            **kwargs: typing.Any
        ) -> ResourceRecordSetsListResponseHttpRequest: ...
    class PoliciesResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            project: str,
            policy: str,
            body: Policy = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PoliciesPatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            policy: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            project: str,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> PoliciesListResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            policy: str,
            body: Policy = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PoliciesUpdateResponseHttpRequest: ...
        def create(
            self,
            *,
            project: str,
            body: Policy = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            policy: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
    class ChangesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            changeId: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ChangeHttpRequest: ...
        def create(
            self,
            *,
            project: str,
            managedZone: str,
            body: Change = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ChangeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            pageToken: str = ...,
            maxResults: int = ...,
            sortBy: typing_extensions.Literal["changeSequence"] = ...,
            sortOrder: str = ...,
            **kwargs: typing.Any
        ) -> ChangesListResponseHttpRequest: ...
    class DnsKeysResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            digestType: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> DnsKeysListResponseHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            dnsKeyId: str,
            clientOperationId: str = ...,
            digestType: str = ...,
            **kwargs: typing.Any
        ) -> DnsKeyHttpRequest: ...
    def managedZoneOperations(self) -> ManagedZoneOperationsResource: ...
    def managedZones(self) -> ManagedZonesResource: ...
    def projects(self) -> ProjectsResource: ...
    def resourceRecordSets(self) -> ResourceRecordSetsResource: ...
    def policies(self) -> PoliciesResource: ...
    def changes(self) -> ChangesResource: ...
    def dnsKeys(self) -> DnsKeysResource: ...

class ChangesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChangesListResponse: ...

class PoliciesPatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PoliciesPatchResponse: ...

class ManagedZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManagedZone: ...

class ResourceRecordSetsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourceRecordSetsListResponse: ...

class DnsKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DnsKey: ...

class PoliciesUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PoliciesUpdateResponse: ...

class DnsKeysListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DnsKeysListResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Project: ...

class ManagedZoneOperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManagedZoneOperationsListResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class PoliciesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PoliciesListResponse: ...

class ManagedZonesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManagedZonesListResponse: ...

class ChangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Change: ...
