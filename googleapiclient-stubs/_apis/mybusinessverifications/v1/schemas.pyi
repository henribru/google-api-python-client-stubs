import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddressVerificationData(typing_extensions.TypedDict, total=False):
    address: PostalAddress
    business: str
    expectedDeliveryDaysRegion: int

@typing.type_check_only
class CompleteVerificationRequest(typing_extensions.TypedDict, total=False):
    pin: str

@typing.type_check_only
class CompleteVerificationResponse(typing_extensions.TypedDict, total=False):
    verification: Verification

@typing.type_check_only
class ComplyWithGuidelines(typing_extensions.TypedDict, total=False):
    recommendationReason: typing_extensions.Literal[
        "RECOMMENDATION_REASON_UNSPECIFIED",
        "BUSINESS_LOCATION_SUSPENDED",
        "BUSINESS_LOCATION_DISABLED",
    ]

@typing.type_check_only
class EmailVerificationData(typing_extensions.TypedDict, total=False):
    domain: str
    isUserNameEditable: bool
    user: str

@typing.type_check_only
class FetchVerificationOptionsRequest(typing_extensions.TypedDict, total=False):
    context: ServiceBusinessContext
    languageCode: str

@typing.type_check_only
class FetchVerificationOptionsResponse(typing_extensions.TypedDict, total=False):
    options: _list[VerificationOption]

@typing.type_check_only
class GenerateVerificationTokenRequest(typing_extensions.TypedDict, total=False):
    location: Location

@typing.type_check_only
class GenerateVerificationTokenResponse(typing_extensions.TypedDict, total=False):
    token: VerificationToken

@typing.type_check_only
class ListVerificationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    verifications: _list[Verification]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    address: PostalAddress
    name: str
    primaryCategoryId: str
    primaryPhone: str
    websiteUri: str

@typing.type_check_only
class PostalAddress(typing_extensions.TypedDict, total=False):
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
class ResolveOwnershipConflict(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ServiceBusinessContext(typing_extensions.TypedDict, total=False):
    address: PostalAddress

@typing.type_check_only
class Verification(typing_extensions.TypedDict, total=False):
    createTime: str
    method: typing_extensions.Literal[
        "VERIFICATION_METHOD_UNSPECIFIED",
        "ADDRESS",
        "EMAIL",
        "PHONE_CALL",
        "SMS",
        "AUTO",
        "VETTED_PARTNER",
    ]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COMPLETED", "FAILED"
    ]

@typing.type_check_only
class VerificationOption(typing_extensions.TypedDict, total=False):
    addressData: AddressVerificationData
    emailData: EmailVerificationData
    phoneNumber: str
    verificationMethod: typing_extensions.Literal[
        "VERIFICATION_METHOD_UNSPECIFIED",
        "ADDRESS",
        "EMAIL",
        "PHONE_CALL",
        "SMS",
        "AUTO",
        "VETTED_PARTNER",
    ]

@typing.type_check_only
class VerificationToken(typing_extensions.TypedDict, total=False):
    tokenString: str

@typing.type_check_only
class Verify(typing_extensions.TypedDict, total=False):
    hasPendingVerification: bool

@typing.type_check_only
class VerifyLocationRequest(typing_extensions.TypedDict, total=False):
    context: ServiceBusinessContext
    emailAddress: str
    languageCode: str
    mailerContact: str
    method: typing_extensions.Literal[
        "VERIFICATION_METHOD_UNSPECIFIED",
        "ADDRESS",
        "EMAIL",
        "PHONE_CALL",
        "SMS",
        "AUTO",
        "VETTED_PARTNER",
    ]
    phoneNumber: str
    token: VerificationToken

@typing.type_check_only
class VerifyLocationResponse(typing_extensions.TypedDict, total=False):
    verification: Verification

@typing.type_check_only
class VoiceOfMerchantState(typing_extensions.TypedDict, total=False):
    complyWithGuidelines: ComplyWithGuidelines
    hasBusinessAuthority: bool
    hasVoiceOfMerchant: bool
    resolveOwnershipConflict: ResolveOwnershipConflict
    verify: Verify
    waitForVoiceOfMerchant: WaitForVoiceOfMerchant

@typing.type_check_only
class WaitForVoiceOfMerchant(typing_extensions.TypedDict, total=False): ...
