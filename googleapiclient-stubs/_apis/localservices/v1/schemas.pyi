import typing

import typing_extensions
@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1AccountReport(
    typing_extensions.TypedDict, total=False
):
    accountId: str
    aggregatorInfo: GoogleAdsHomeservicesLocalservicesV1AggregatorInfo
    averageFiveStarRating: float
    averageWeeklyBudget: float
    businessName: str
    currencyCode: str
    currentPeriodChargedLeads: str
    currentPeriodConnectedPhoneCalls: str
    currentPeriodPhoneCalls: str
    currentPeriodTotalCost: float
    phoneLeadResponsiveness: float
    previousPeriodChargedLeads: str
    previousPeriodConnectedPhoneCalls: str
    previousPeriodPhoneCalls: str
    previousPeriodTotalCost: float
    totalReview: int

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1AggregatorInfo(
    typing_extensions.TypedDict, total=False
):
    aggregatorProviderId: str

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1DetailedLeadReport(
    typing_extensions.TypedDict, total=False
):
    accountId: str
    aggregatorInfo: GoogleAdsHomeservicesLocalservicesV1AggregatorInfo
    businessName: str
    chargeStatus: typing_extensions.Literal[
        "CHARGE_STATUS_UNSPECIFIED", "CHARGED", "NOT_CHARGED"
    ]
    currencyCode: str
    disputeStatus: str
    geo: str
    leadCategory: str
    leadCreationTimestamp: str
    leadId: str
    leadPrice: float
    leadType: typing_extensions.Literal[
        "LEAD_TYPE_UNSPECIFIED", "MESSAGE", "PHONE_CALL"
    ]
    messageLead: GoogleAdsHomeservicesLocalservicesV1MessageLead
    phoneLead: GoogleAdsHomeservicesLocalservicesV1PhoneLead
    timezone: GoogleTypeTimeZone

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1MessageLead(
    typing_extensions.TypedDict, total=False
):
    consumerPhoneNumber: str
    customerName: str
    jobType: str
    postalCode: str

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1PhoneLead(
    typing_extensions.TypedDict, total=False
):
    chargedCallTimestamp: str
    chargedConnectedCallDurationSeconds: str
    consumerPhoneNumber: str

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponse(
    typing_extensions.TypedDict, total=False
):
    accountReports: typing.List[GoogleAdsHomeservicesLocalservicesV1AccountReport]
    nextPageToken: str

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponse(
    typing_extensions.TypedDict, total=False
):
    detailedLeadReports: typing.List[
        GoogleAdsHomeservicesLocalservicesV1DetailedLeadReport
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str
