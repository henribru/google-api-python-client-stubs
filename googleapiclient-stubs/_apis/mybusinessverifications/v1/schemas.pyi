import typing

_list = list

@typing.type_check_only
class AddressVerificationData(typing.TypedDict, total=False):
    address: PostalAddress
    business: str
    expectedDeliveryDaysRegion: int

@typing.type_check_only
class CompleteVerificationRequest(typing.TypedDict, total=False):
    pin: str

@typing.type_check_only
class CompleteVerificationResponse(typing.TypedDict, total=False):
    verification: Verification

@typing.type_check_only
class ComplyWithGuidelines(typing.TypedDict, total=False):
    recommendationReason: typing.Literal[
        "RECOMMENDATION_REASON_UNSPECIFIED",
        "BUSINESS_LOCATION_SUSPENDED",
        "BUSINESS_LOCATION_DISABLED",
    ]

@typing.type_check_only
class EmailVerificationData(typing.TypedDict, total=False):
    domain: str
    isUserNameEditable: bool
    user: str

@typing.type_check_only
class FetchVerificationOptionsRequest(typing.TypedDict, total=False):
    context: ServiceBusinessContext
    languageCode: str

@typing.type_check_only
class FetchVerificationOptionsResponse(typing.TypedDict, total=False):
    options: _list[VerificationOption]

@typing.type_check_only
class GenerateInstantVerificationTokenRequest(typing.TypedDict, total=False):
    locationId: str

@typing.type_check_only
class GenerateInstantVerificationTokenResponse(typing.TypedDict, total=False):
    instantVerificationToken: str
    result: typing.Literal["RESULT_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class ListVerificationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    verifications: _list[Verification]

@typing.type_check_only
class PostalAddress(typing.TypedDict, total=False):
    addressLines: _list[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: _list[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class ResolveOwnershipConflict(typing.TypedDict, total=False): ...

@typing.type_check_only
class ServiceBusinessContext(typing.TypedDict, total=False):
    address: PostalAddress

@typing.type_check_only
class Verification(typing.TypedDict, total=False):
    announcement: str
    createTime: str
    method: typing.Literal[
        "VERIFICATION_METHOD_UNSPECIFIED",
        "ADDRESS",
        "EMAIL",
        "PHONE_CALL",
        "SMS",
        "AUTO",
        "TRUSTED_PARTNER",
    ]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "COMPLETED", "FAILED"]

@typing.type_check_only
class VerificationOption(typing.TypedDict, total=False):
    addressData: AddressVerificationData
    announcement: str
    emailData: EmailVerificationData
    phoneNumber: str
    verificationMethod: typing.Literal[
        "VERIFICATION_METHOD_UNSPECIFIED",
        "ADDRESS",
        "EMAIL",
        "PHONE_CALL",
        "SMS",
        "AUTO",
        "TRUSTED_PARTNER",
    ]

@typing.type_check_only
class VerificationToken(typing.TypedDict, total=False):
    tokenString: str

@typing.type_check_only
class Verify(typing.TypedDict, total=False):
    hasPendingVerification: bool

@typing.type_check_only
class VerifyLocationRequest(typing.TypedDict, total=False):
    context: ServiceBusinessContext
    emailAddress: str
    languageCode: str
    mailerContact: str
    method: typing.Literal[
        "VERIFICATION_METHOD_UNSPECIFIED",
        "ADDRESS",
        "EMAIL",
        "PHONE_CALL",
        "SMS",
        "AUTO",
        "TRUSTED_PARTNER",
    ]
    phoneNumber: str
    token: VerificationToken
    trustedPartnerToken: str

@typing.type_check_only
class VerifyLocationResponse(typing.TypedDict, total=False):
    verification: Verification

@typing.type_check_only
class VoiceOfMerchantState(typing.TypedDict, total=False):
    complyWithGuidelines: ComplyWithGuidelines
    hasBusinessAuthority: bool
    hasVoiceOfMerchant: bool
    resolveOwnershipConflict: ResolveOwnershipConflict
    verify: Verify
    waitForVoiceOfMerchant: WaitForVoiceOfMerchant

@typing.type_check_only
class WaitForVoiceOfMerchant(typing.TypedDict, total=False): ...
