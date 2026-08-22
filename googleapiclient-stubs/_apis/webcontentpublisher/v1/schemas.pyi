import typing

_list = list

@typing.type_check_only
class CheckFreeAccessResponse(typing.TypedDict, total=False):
    isAllowed: bool

@typing.type_check_only
class ContentPolicyStatus(typing.TypedDict, total=False):
    policyInfoUrl: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "OK",
        "VIOLATION_GRACE_PERIOD",
        "VIOLATION_ACTIVE",
        "ORGANIZATION_VIOLATION_GRACE_PERIOD",
        "ORGANIZATION_VIOLATION_ACTIVE",
        "ORGANIZATION_VIOLATION_ACTIVE_IMMEDIATE",
    ]

@typing.type_check_only
class Cta(typing.TypedDict, total=False):
    displayName: str
    name: str
    newsletterConfig: NewsletterConfig
    state: typing.Literal["STATE_UNSPECIFIED", "DRAFT", "ACTIVE"]
    type: typing.Literal["TYPE_UNSPECIFIED", "NEWSLETTER_SIGNUP"]

@typing.type_check_only
class DomainProperty(typing.TypedDict, total=False):
    ownershipVerified: bool
    url: str

@typing.type_check_only
class GeneratePlatformSiteTokensRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GeneratePlatformSiteTokensResponse(typing.TypedDict, total=False):
    siteTokens: _list[SiteToken]

@typing.type_check_only
class ListCtasResponse(typing.TypedDict, total=False):
    ctas: _list[Cta]
    nextPageToken: str

@typing.type_check_only
class ListPublicationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    publications: _list[Publication]

@typing.type_check_only
class NewsletterConfig(typing.TypedDict, total=False):
    customConsentText: str
    customMessage: str
    nameRequired: bool
    optInRequired: bool
    title: str

@typing.type_check_only
class Publication(typing.TypedDict, total=False):
    additionalDomains: _list[DomainProperty]
    contentPolicyStatus: ContentPolicyStatus
    displayName: str
    languageCode: str
    name: str
    onboardingState: typing.Literal[
        "ONBOARDING_STATE_UNSPECIFIED",
        "ACTION_REQUIRED",
        "PENDING_VERIFICATION",
        "COMPLETE",
    ]
    organizationId: str
    paymentOption: typing.Literal[
        "PAYMENT_OPTION_UNSPECIFIED", "NONE", "SUBSCRIPTIONS", "CONTRIBUTIONS"
    ]
    primaryDomain: DomainProperty
    products: _list[str]
    publicationId: str
    publicationPrivacyPolicyUrl: str
    publicationTosUrl: str
    publicationType: typing.Literal[
        "PUBLICATION_TYPE_UNSPECIFIED", "FOR_PROFIT", "NON_PROFIT"
    ]
    regionCode: str
    rrmProduct: RrmProduct
    slProduct: SlProduct

@typing.type_check_only
class RrmProduct(typing.TypedDict, total=False):
    enabled: bool
    productTosUrl: str
    tosAcceptance: TosAcceptance

@typing.type_check_only
class SiteToken(typing.TypedDict, total=False):
    domain: str
    token: str

@typing.type_check_only
class SlProduct(typing.TypedDict, total=False):
    enabled: bool
    gcpProjectNumber: str

@typing.type_check_only
class TosAcceptance(typing.TypedDict, total=False):
    emailOptIn: bool
    signer: str
    signerTitle: str
    userAccepted: bool
