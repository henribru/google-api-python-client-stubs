import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudKMSResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class KeyRingsResource(googleapiclient.discovery.Resource):
                class CryptoKeysResource(googleapiclient.discovery.Resource):
                    class CryptoKeyVersionsResource(googleapiclient.discovery.Resource):
                        def asymmetricSign(
                            self,
                            *,
                            name: str,
                            body: AsymmetricSignRequest = ...,
                            **kwargs: typing.Any
                        ) -> AsymmetricSignResponseHttpRequest: ...
                        def restore(
                            self,
                            *,
                            name: str,
                            body: RestoreCryptoKeyVersionRequest = ...,
                            **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            filter: str = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "CRYPTO_KEY_VERSION_VIEW_UNSPECIFIED", "FULL"
                            ] = ...,
                            orderBy: str = ...,
                            **kwargs: typing.Any
                        ) -> ListCryptoKeyVersionsResponseHttpRequest: ...
                        def asymmetricDecrypt(
                            self,
                            *,
                            name: str,
                            body: AsymmetricDecryptRequest = ...,
                            **kwargs: typing.Any
                        ) -> AsymmetricDecryptResponseHttpRequest: ...
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
                        def patch(
                            self,
                            *,
                            name: str,
                            body: CryptoKeyVersion = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> CryptoKeyVersionHttpRequest: ...
                    def encrypt(
                        self,
                        *,
                        name: str,
                        body: EncryptRequest = ...,
                        **kwargs: typing.Any
                    ) -> EncryptResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: CryptoKey = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def updatePrimaryVersion(
                        self,
                        *,
                        name: str,
                        body: UpdateCryptoKeyPrimaryVersionRequest = ...,
                        **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        filter: str = ...,
                        versionView: typing_extensions.Literal[
                            "CRYPTO_KEY_VERSION_VIEW_UNSPECIFIED", "FULL"
                        ] = ...,
                        orderBy: str = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCryptoKeysResponseHttpRequest: ...
                    def decrypt(
                        self,
                        *,
                        name: str,
                        body: DecryptRequest = ...,
                        **kwargs: typing.Any
                    ) -> DecryptResponseHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
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
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CryptoKey = ...,
                        skipInitialVersionCreation: bool = ...,
                        cryptoKeyId: str = ...,
                        **kwargs: typing.Any
                    ) -> CryptoKeyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def cryptoKeyVersions(self) -> CryptoKeyVersionsResource: ...
                class ImportJobsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ImportJobHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        orderBy: str = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> ListImportJobsResponseHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ImportJob = ...,
                        importJobId: str = ...,
                        **kwargs: typing.Any
                    ) -> ImportJobHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> KeyRingHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: KeyRing = ...,
                    keyRingId: str = ...,
                    **kwargs: typing.Any
                ) -> KeyRingHttpRequest: ...
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
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListKeyRingsResponseHttpRequest: ...
                def cryptoKeys(self) -> CryptoKeysResource: ...
                def importJobs(self) -> ImportJobsResource: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def keyRings(self) -> KeyRingsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class CryptoKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CryptoKey: ...

class AsymmetricDecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AsymmetricDecryptResponse: ...

class ListImportJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListImportJobsResponse: ...

class EncryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EncryptResponse: ...

class CryptoKeyVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CryptoKeyVersion: ...

class AsymmetricSignResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AsymmetricSignResponse: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class ListCryptoKeyVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCryptoKeyVersionsResponse: ...

class ImportJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImportJob: ...

class KeyRingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> KeyRing: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class DecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DecryptResponse: ...

class ListKeyRingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListKeyRingsResponse: ...

class ListCryptoKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCryptoKeysResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class PublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublicKey: ...
