import typing

import typing_extensions

class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    version: str
    id: str

class GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponse(
    typing_extensions.TypedDict, total=False
):
    detailedLeadReports: typing.List[
        GoogleAdsHomeservicesLocalservicesV1DetailedLeadReport
    ]
    nextPageToken: str

class GoogleAdsHomeservicesLocalservicesV1MessageLead(
    typing_extensions.TypedDict, total=False
):
    postalCode: str
    consumerPhoneNumber: str
    jobType: str
    customerName: str

class GoogleAdsHomeservicesLocalservicesV1DetailedLeadReport(
    typing_extensions.TypedDict, total=False
):
    accountId: str
    currencyCode: str
    leadId: str
    geo: str
    businessName: str
    messageLead: GoogleAdsHomeservicesLocalservicesV1MessageLead
    leadPrice: float
    phoneLead: GoogleAdsHomeservicesLocalservicesV1PhoneLead
    leadCreationTimestamp: str
    disputeStatus: str
    chargeStatus: typing_extensions.Literal[
        "CHARGE_STATUS_UNSPECIFIED", "CHARGED", "NOT_CHARGED"
    ]
    leadType: typing_extensions.Literal[
        "LEAD_TYPE_UNSPECIFIED", "MESSAGE", "PHONE_CALL"
    ]
    leadCategory: str
    timezone: GoogleTypeTimeZone
    aggregatorInfo: GoogleAdsHomeservicesLocalservicesV1AggregatorInfo

class GoogleAdsHomeservicesLocalservicesV1AggregatorInfo(
    typing_extensions.TypedDict, total=False
):
    aggregatorProviderId: str

class GoogleAdsHomeservicesLocalservicesV1AccountReport(
    typing_extensions.TypedDict, total=False
):
    currentPeriodPhoneCalls: str
    previousPeriodConnectedPhoneCalls: str
    currencyCode: str
    averageFiveStarRating: float
    currentPeriodConnectedPhoneCalls: str
    phoneLeadResponsiveness: float
    previousPeriodPhoneCalls: str
    totalReview: int
    currentPeriodChargedLeads: str
    previousPeriodTotalCost: float
    businessName: str
    currentPeriodTotalCost: float
    averageWeeklyBudget: float
    previousPeriodChargedLeads: str
    accountId: str

class GoogleAdsHomeservicesLocalservicesV1PhoneLead(
    typing_extensions.TypedDict, total=False
):
    consumerPhoneNumber: str
    chargedCallTimestamp: str
    chargedConnectedCallDurationSeconds: str

class GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    accountReports: typing.List[GoogleAdsHomeservicesLocalservicesV1AccountReport]
