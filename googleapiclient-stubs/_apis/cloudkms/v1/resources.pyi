import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudKMSResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        def getAutokeyConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> AutokeyConfigHttpRequest: ...
        def updateAutokeyConfig(
            self,
            *,
            name: str,
            body: AutokeyConfig = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> AutokeyConfigHttpRequest: ...

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
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class EkmConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EkmConnection = ...,
                    ekmConnectionId: str = ...,
                    **kwargs: typing.Any,
                ) -> EkmConnectionHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EkmConnectionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> EkmConnectionHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def verifyConnectivity(
                    self, *, name: str, **kwargs: typing.Any
                ) -> VerifyConnectivityResponseHttpRequest: ...

            @typing.type_check_only
            class KeyHandlesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: KeyHandle = ...,
                    keyHandleId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> KeyHandleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListKeyHandlesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListKeyHandlesResponseHttpRequest,
                    previous_response: ListKeyHandlesResponse,
                ) -> ListKeyHandlesResponseHttpRequest | None: ...

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
                            **kwargs: typing.Any,
                        ) -> AsymmetricDecryptResponseHttpRequest: ...
                        def asymmetricSign(
                            self,
                            *,
                            name: str,
                            body: AsymmetricSignRequest = ...,
                            **kwargs: typing.Any,
                        ) -> AsymmetricSignResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CryptoKeyVersion = ...,
                            **kwargs: typing.Any,
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def destroy(
                            self,
                            *,
                            name: str,
                            body: DestroyCryptoKeyVersionRequest = ...,
                            **kwargs: typing.Any,
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
                            **kwargs: typing.Any,
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
                            **kwargs: typing.Any,
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
                            **kwargs: typing.Any,
                        ) -> MacSignResponseHttpRequest: ...
                        def macVerify(
                            self,
                            *,
                            name: str,
                            body: MacVerifyRequest = ...,
                            **kwargs: typing.Any,
                        ) -> MacVerifyResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: CryptoKeyVersion = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def rawDecrypt(
                            self,
                            *,
                            name: str,
                            body: RawDecryptRequest = ...,
                            **kwargs: typing.Any,
                        ) -> RawDecryptResponseHttpRequest: ...
                        def rawEncrypt(
                            self,
                            *,
                            name: str,
                            body: RawEncryptRequest = ...,
                            **kwargs: typing.Any,
                        ) -> RawEncryptResponseHttpRequest: ...
                        def restore(
                            self,
                            *,
                            name: str,
                            body: RestoreCryptoKeyVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> CryptoKeyVersionHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: CryptoKey = ...,
                        cryptoKeyId: str = ...,
                        skipInitialVersionCreation: bool = ...,
                        **kwargs: typing.Any,
                    ) -> CryptoKeyHttpRequest: ...
                    def decrypt(
                        self,
                        *,
                        name: str,
                        body: DecryptRequest = ...,
                        **kwargs: typing.Any,
                    ) -> DecryptResponseHttpRequest: ...
                    def encrypt(
                        self,
                        *,
                        name: str,
                        body: EncryptRequest = ...,
                        **kwargs: typing.Any,
                    ) -> EncryptResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> CryptoKeyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def updatePrimaryVersion(
                        self,
                        *,
                        name: str,
                        body: UpdateCryptoKeyPrimaryVersionRequest = ...,
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> ImportJobHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ImportJobHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: KeyRing = ...,
                    keyRingId: str = ...,
                    **kwargs: typing.Any,
                ) -> KeyRingHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> KeyRingHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def cryptoKeys(self) -> CryptoKeysResource: ...
                def importJobs(self) -> ImportJobsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            def generateRandomBytes(
                self,
                *,
                location: str,
                body: GenerateRandomBytesRequest = ...,
                **kwargs: typing.Any,
            ) -> GenerateRandomBytesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getEkmConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> EkmConfigHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def updateEkmConfig(
                self,
                *,
                name: str,
                body: EkmConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> EkmConfigHttpRequest: ...
            def ekmConfig(self) -> EkmConfigResource: ...
            def ekmConnections(self) -> EkmConnectionsResource: ...
            def keyHandles(self) -> KeyHandlesResource: ...
            def keyRings(self) -> KeyRingsResource: ...
            def operations(self) -> OperationsResource: ...

        def showEffectiveAutokeyConfig(
            self, *, parent: str, **kwargs: typing.Any
        ) -> ShowEffectiveAutokeyConfigResponseHttpRequest: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def folders(self) -> FoldersResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AsymmetricDecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AsymmetricDecryptResponse: ...

@typing.type_check_only
class AsymmetricSignResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AsymmetricSignResponse: ...

@typing.type_check_only
class AutokeyConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutokeyConfig: ...

@typing.type_check_only
class CryptoKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CryptoKey: ...

@typing.type_check_only
class CryptoKeyVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CryptoKeyVersion: ...

@typing.type_check_only
class DecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DecryptResponse: ...

@typing.type_check_only
class EkmConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EkmConfig: ...

@typing.type_check_only
class EkmConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EkmConnection: ...

@typing.type_check_only
class EncryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EncryptResponse: ...

@typing.type_check_only
class GenerateRandomBytesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateRandomBytesResponse: ...

@typing.type_check_only
class ImportJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ImportJob: ...

@typing.type_check_only
class KeyHandleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> KeyHandle: ...

@typing.type_check_only
class KeyRingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> KeyRing: ...

@typing.type_check_only
class ListCryptoKeyVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCryptoKeyVersionsResponse: ...

@typing.type_check_only
class ListCryptoKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCryptoKeysResponse: ...

@typing.type_check_only
class ListEkmConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEkmConnectionsResponse: ...

@typing.type_check_only
class ListImportJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListImportJobsResponse: ...

@typing.type_check_only
class ListKeyHandlesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListKeyHandlesResponse: ...

@typing.type_check_only
class ListKeyRingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListKeyRingsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class MacSignResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MacSignResponse: ...

@typing.type_check_only
class MacVerifyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MacVerifyResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class PublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PublicKey: ...

@typing.type_check_only
class RawDecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RawDecryptResponse: ...

@typing.type_check_only
class RawEncryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RawEncryptResponse: ...

@typing.type_check_only
class ShowEffectiveAutokeyConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShowEffectiveAutokeyConfigResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class VerifyConnectivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VerifyConnectivityResponse: ...
