import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudKMSResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EkmConfigResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class EkmConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EkmConnection = ...,
                    ekmConnectionId: str = ...,
                    **kwargs: typing.Any
                ) -> EkmConnectionHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EkmConnectionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListEkmConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEkmConnectionsResponseHttpRequest,
                    previous_response: ListEkmConnectionsResponse,
                ) -> ListEkmConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: EkmConnection = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> EkmConnectionHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class KeyRingsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CryptoKeysResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class CryptoKeyVersionsResource(googleapiclient.discovery.Resource):
                        def asymmetricDecrypt(
                            self,
                            *,
                            name: str,
                            body: AsymmetricDecryptRequest = ...,
                            **kwargs: typing.Any
                        ) -> AsymmetricDecryptResponseHttpRequest: ...
                        def asymmetricSign(
                            self,
                            *,
                            name: str,
                            body: AsymmetricSignRequest = ...,
                            **kwargs: typing.Any
                        ) -> AsymmetricSignResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CryptoKeyVersion = ...,
                            **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def destroy(
                            self,
                            *,
                            name: str,
                            body: DestroyCryptoKeyVersionRequest = ...,
                            **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def getPublicKey(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> PublicKeyHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: ImportCryptoKeyVersionRequest = ...,
                            **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "CRYPTO_KEY_VERSION_VIEW_UNSPECIFIED", "FULL"
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ListCryptoKeyVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListCryptoKeyVersionsResponseHttpRequest,
                            previous_response: ListCryptoKeyVersionsResponse,
                        ) -> ListCryptoKeyVersionsResponseHttpRequest | None: ...
                        def macSign(
                            self,
                            *,
                            name: str,
                            body: MacSignRequest = ...,
                            **kwargs: typing.Any
                        ) -> MacSignResponseHttpRequest: ...
                        def macVerify(
                            self,
                            *,
                            name: str,
                            body: MacVerifyRequest = ...,
                            **kwargs: typing.Any
                        ) -> MacVerifyResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: CryptoKeyVersion = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def restore(
                            self,
                            *,
                            name: str,
                            body: RestoreCryptoKeyVersionRequest = ...,
                            **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: CryptoKey = ...,
                        cryptoKeyId: str = ...,
                        skipInitialVersionCreation: bool = ...,
                        **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def decrypt(
                        self,
                        *,
                        name: str,
                        body: DecryptRequest = ...,
                        **kwargs: typing.Any
                    ) -> DecryptResponseHttpRequest: ...
                    def encrypt(
                        self,
                        *,
                        name: str,
                        body: EncryptRequest = ...,
                        **kwargs: typing.Any
                    ) -> EncryptResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        versionView: typing_extensions.Literal[
                            "CRYPTO_KEY_VERSION_VIEW_UNSPECIFIED", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListCryptoKeysResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListCryptoKeysResponseHttpRequest,
                        previous_response: ListCryptoKeysResponse,
                    ) -> ListCryptoKeysResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: CryptoKey = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def updatePrimaryVersion(
                        self,
                        *,
                        name: str,
                        body: UpdateCryptoKeyPrimaryVersionRequest = ...,
                        **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def cryptoKeyVersions(self) -> CryptoKeyVersionsResource: ...

                @typing.type_check_only
                class ImportJobsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ImportJob = ...,
                        importJobId: str = ...,
                        **kwargs: typing.Any
                    ) -> ImportJobHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ImportJobHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListImportJobsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListImportJobsResponseHttpRequest,
                        previous_response: ListImportJobsResponse,
                    ) -> ListImportJobsResponseHttpRequest | None: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: KeyRing = ...,
                    keyRingId: str = ...,
                    **kwargs: typing.Any
                ) -> KeyRingHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> KeyRingHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListKeyRingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListKeyRingsResponseHttpRequest,
                    previous_response: ListKeyRingsResponse,
                ) -> ListKeyRingsResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def cryptoKeys(self) -> CryptoKeysResource: ...
                def importJobs(self) -> ImportJobsResource: ...

            def generateRandomBytes(
                self,
                *,
                location: str,
                body: GenerateRandomBytesRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateRandomBytesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def ekmConfig(self) -> EkmConfigResource: ...
            def ekmConnections(self) -> EkmConnectionsResource: ...
            def keyRings(self) -> KeyRingsResource: ...

        def locations(self) -> LocationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AsymmetricDecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AsymmetricDecryptResponse: ...

@typing.type_check_only
class AsymmetricSignResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AsymmetricSignResponse: ...

@typing.type_check_only
class CryptoKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CryptoKey: ...

@typing.type_check_only
class CryptoKeyVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CryptoKeyVersion: ...

@typing.type_check_only
class DecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DecryptResponse: ...

@typing.type_check_only
class EkmConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EkmConnection: ...

@typing.type_check_only
class EncryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EncryptResponse: ...

@typing.type_check_only
class GenerateRandomBytesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GenerateRandomBytesResponse: ...

@typing.type_check_only
class ImportJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImportJob: ...

@typing.type_check_only
class KeyRingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> KeyRing: ...

@typing.type_check_only
class ListCryptoKeyVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCryptoKeyVersionsResponse: ...

@typing.type_check_only
class ListCryptoKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCryptoKeysResponse: ...

@typing.type_check_only
class ListEkmConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEkmConnectionsResponse: ...

@typing.type_check_only
class ListImportJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListImportJobsResponse: ...

@typing.type_check_only
class ListKeyRingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListKeyRingsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class MacSignResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MacSignResponse: ...

@typing.type_check_only
class MacVerifyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MacVerifyResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class PublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublicKey: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
