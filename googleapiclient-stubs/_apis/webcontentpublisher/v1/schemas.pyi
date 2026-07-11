import typing

import typing_extensions

_list = list

@typing.type_check_only
class CheckFreeAccessResponse(typing_extensions.TypedDict, total=False):
    isAllowed: bool

@typing.type_check_only
class ContentPolicyStatus(typing_extensions.TypedDict, total=False):
    policyInfoUrl: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "OK",
        "VIOLATION_GRACE_PERIOD",
        "VIOLATION_ACTIVE",
        "ORGANIZATION_VIOLATION_GRACE_PERIOD",
        "ORGANIZATION_VIOLATION_ACTIVE",
        "ORGANIZATION_VIOLATION_ACTIVE_IMMEDIATE",
    ]

@typing.type_check_only
class Cta(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    newsletterConfig: NewsletterConfig
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "DRAFT", "ACTIVE"]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "NEWSLETTER_SIGNUP"]

@typing.type_check_only
class DomainProperty(typing_extensions.TypedDict, total=False):
    ownershipVerified: bool
    url: str

@typing.type_check_only
class ListCtasResponse(typing_extensions.TypedDict, total=False):
    ctas: _list[Cta]
    nextPageToken: str

@typing.type_check_only
class ListPublicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    publications: _list[Publication]

@typing.type_check_only
class NewsletterConfig(typing_extensions.TypedDict, total=False):
    customConsentText: str
    customMessage: str
    nameRequired: bool
    title: str

@typing.type_check_only
class Publication(typing_extensions.TypedDict, total=False):
    additionalDomains: _list[DomainProperty]
    contentPolicyStatus: ContentPolicyStatus
    displayName: str
    languageCode: str
    name: str
    onboardingState: typing_extensions.Literal[
        "ONBOARDING_STATE_UNSPECIFIED",
        "ACTION_REQUIRED",
        "PENDING_VERIFICATION",
        "COMPLETE",
    ]
    organizationId: str
    paymentOption: typing_extensions.Literal[
        "PAYMENT_OPTION_UNSPECIFIED", "NONE", "SUBSCRIPTIONS", "CONTRIBUTIONS"
    ]
    primaryDomain: DomainProperty
    products: _list[str]
    publicationId: str
    publicationPrivacyPolicyUrl: str
    publicationTosUrl: str
    regionCode: str
    rrmProduct: RrmProduct
    slProduct: SlProduct

@typing.type_check_only
class RrmProduct(typing_extensions.TypedDict, total=False):
    enabled: bool
    productTosUrl: str
    tosAcceptance: TosAcceptance

@typing.type_check_only
class SlProduct(typing_extensions.TypedDict, total=False):
    enabled: bool
    gcpProjectNumber: str

@typing.type_check_only
class TosAcceptance(typing_extensions.TypedDict, total=False):
    signer: str
    signerTitle: str
    userAccepted: bool
