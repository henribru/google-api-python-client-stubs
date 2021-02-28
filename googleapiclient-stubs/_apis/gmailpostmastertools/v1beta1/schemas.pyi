import typing

import typing_extensions
@typing.type_check_only
class DeliveryError(typing_extensions.TypedDict, total=False):
    errorClass: typing_extensions.Literal[
        "DELIVERY_ERROR_CLASS_UNSPECIFIED", "PERMANENT_ERROR", "TEMPORARY_ERROR"
    ]
    errorRatio: float
    errorType: typing_extensions.Literal[
        "DELIVERY_ERROR_TYPE_UNSPECIFIED",
        "RATE_LIMIT_EXCEEDED",
        "SUSPECTED_SPAM",
        "CONTENT_SPAMMY",
        "BAD_ATTACHMENT",
        "BAD_DMARC_POLICY",
        "LOW_IP_REPUTATION",
        "LOW_DOMAIN_REPUTATION",
        "IP_IN_RBL",
        "DOMAIN_IN_RBL",
        "BAD_PTR_RECORD",
    ]

@typing.type_check_only
class Domain(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    permission: typing_extensions.Literal[
        "PERMISSION_UNSPECIFIED", "OWNER", "READER", "NONE"
    ]

@typing.type_check_only
class FeedbackLoop(typing_extensions.TypedDict, total=False):
    id: str
    spamRatio: float

@typing.type_check_only
class IpReputation(typing_extensions.TypedDict, total=False):
    ipCount: str
    numIps: str
    reputation: typing_extensions.Literal[
        "REPUTATION_CATEGORY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BAD"
    ]
    sampleIps: typing.List[str]

@typing.type_check_only
class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: typing.List[Domain]
    nextPageToken: str

@typing.type_check_only
class ListTrafficStatsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    trafficStats: typing.List[TrafficStats]

@typing.type_check_only
class TrafficStats(typing_extensions.TypedDict, total=False):
    deliveryErrors: typing.List[DeliveryError]
    dkimSuccessRatio: float
    dmarcSuccessRatio: float
    domainReputation: typing_extensions.Literal[
        "REPUTATION_CATEGORY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BAD"
    ]
    inboundEncryptionRatio: float
    ipReputations: typing.List[IpReputation]
    name: str
    outboundEncryptionRatio: float
    spammyFeedbackLoops: typing.List[FeedbackLoop]
    spfSuccessRatio: float
    userReportedSpamRatio: float
