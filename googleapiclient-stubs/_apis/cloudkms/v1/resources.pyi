import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudKMSResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
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
            def keyRings(self) -> KeyRingsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AsymmetricDecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AsymmetricDecryptResponse: ...

@typing.type_check_only
class AsymmetricSignResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AsymmetricSignResponse: ...

@typing.type_check_only
class CryptoKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CryptoKey: ...

@typing.type_check_only
class CryptoKeyVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CryptoKeyVersion: ...

@typing.type_check_only
class DecryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DecryptResponse: ...

@typing.type_check_only
class EncryptResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> EncryptResponse: ...

@typing.type_check_only
class ImportJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ImportJob: ...

@typing.type_check_only
class KeyRingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> KeyRing: ...

@typing.type_check_only
class ListCryptoKeyVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCryptoKeyVersionsResponse: ...

@typing.type_check_only
class ListCryptoKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCryptoKeysResponse: ...

@typing.type_check_only
class ListImportJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListImportJobsResponse: ...

@typing.type_check_only
class ListKeyRingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListKeyRingsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class PublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PublicKey: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
