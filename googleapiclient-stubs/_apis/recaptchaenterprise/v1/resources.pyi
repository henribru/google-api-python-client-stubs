import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class RecaptchaEnterpriseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssessmentsResource(googleapiclient.discovery.Resource):
            def annotate(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseHttpRequest
            ): ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudRecaptchaenterpriseV1Assessment = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1AssessmentHttpRequest: ...

        @typing.type_check_only
        class FirewallpoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudRecaptchaenterpriseV1FirewallPolicy = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1FirewallPolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1FirewallPolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseHttpRequest
            ): ...
            def list_next(
                self,
                previous_request: GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseHttpRequest,
                previous_response: GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponse,
            ) -> (
                GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1FirewallPolicy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1FirewallPolicyHttpRequest: ...
            def reorder(
                self,
                *,
                parent: str,
                body: GoogleCloudRecaptchaenterpriseV1ReorderFirewallPoliciesRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1ReorderFirewallPoliciesResponseHttpRequest: ...

        @typing.type_check_only
        class KeysResource(googleapiclient.discovery.Resource):
            def addIpOverride(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1AddIpOverrideRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1AddIpOverrideResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudRecaptchaenterpriseV1Key = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
            def getMetrics(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1MetricsHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest,
                previous_response: GoogleCloudRecaptchaenterpriseV1ListKeysResponse,
            ) -> GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest | None: ...
            def listIpOverrides(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1ListIpOverridesResponseHttpRequest: ...
            def listIpOverrides_next(
                self,
                previous_request: GoogleCloudRecaptchaenterpriseV1ListIpOverridesResponseHttpRequest,
                previous_response: GoogleCloudRecaptchaenterpriseV1ListIpOverridesResponse,
            ) -> (
                GoogleCloudRecaptchaenterpriseV1ListIpOverridesResponseHttpRequest
                | None
            ): ...
            def migrate(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1MigrateKeyRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1Key = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
            def removeIpOverride(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1RemoveIpOverrideRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudRecaptchaenterpriseV1RemoveIpOverrideResponseHttpRequest
            ): ...
            def retrieveLegacySecretKey(
                self, *, key: str, **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseHttpRequest: ...

        @typing.type_check_only
        class RelatedaccountgroupmembershipsResource(
            googleapiclient.discovery.Resource
        ):
            def search(
                self,
                *,
                project: str,
                body: GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseHttpRequest: ...
            def search_next(
                self,
                previous_request: GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseHttpRequest,
                previous_response: GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponse,
            ) -> (
                GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class RelatedaccountgroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MembershipsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseHttpRequest,
                    previous_response: GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponse,
                ) -> (
                    GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseHttpRequest
                    | None
                ): ...

            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseHttpRequest,
                previous_response: GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponse,
            ) -> (
                GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseHttpRequest
                | None
            ): ...
            def memberships(self) -> MembershipsResource: ...

        def assessments(self) -> AssessmentsResource: ...
        def firewallpolicies(self) -> FirewallpoliciesResource: ...
        def keys(self) -> KeysResource: ...
        def relatedaccountgroupmemberships(
            self,
        ) -> RelatedaccountgroupmembershipsResource: ...
        def relatedaccountgroups(self) -> RelatedaccountgroupsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AddIpOverrideResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1AddIpOverrideResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AssessmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1Assessment: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallPolicyHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1FirewallPolicy: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1KeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1Key: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListIpOverridesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1ListIpOverridesResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1ListKeysResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1MetricsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1Metrics: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RemoveIpOverrideResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1RemoveIpOverrideResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ReorderFirewallPoliciesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1ReorderFirewallPoliciesResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponse
    ): ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
