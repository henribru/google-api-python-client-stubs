import typing

import typing_extensions

class ListTrafficStatsResponse(typing_extensions.TypedDict, total=False):
    trafficStats: typing.List[TrafficStats]
    nextPageToken: str

class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domains: typing.List[Domain]

class FeedbackLoop(typing_extensions.TypedDict, total=False):
    id: str
    spamRatio: float

class TrafficStats(typing_extensions.TypedDict, total=False):
    domainReputation: typing_extensions.Literal[
        "REPUTATION_CATEGORY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BAD"
    ]
    deliveryErrors: typing.List[DeliveryError]
    dkimSuccessRatio: float
    inboundEncryptionRatio: float
    name: str
    outboundEncryptionRatio: float
    spammyFeedbackLoops: typing.List[FeedbackLoop]
    dmarcSuccessRatio: float
    spfSuccessRatio: float
    userReportedSpamRatio: float
    ipReputations: typing.List[IpReputation]

class Domain(typing_extensions.TypedDict, total=False):
    createTime: str
    permission: typing_extensions.Literal[
        "PERMISSION_UNSPECIFIED", "OWNER", "READER", "NONE"
    ]
    name: str

class DeliveryError(typing_extensions.TypedDict, total=False):
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
    errorClass: typing_extensions.Literal[
        "DELIVERY_ERROR_CLASS_UNSPECIFIED", "PERMANENT_ERROR", "TEMPORARY_ERROR"
    ]
    errorRatio: float

class IpReputation(typing_extensions.TypedDict, total=False):
    reputation: typing_extensions.Literal[
        "REPUTATION_CATEGORY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BAD"
    ]
    numIps: str
    sampleIps: typing.List[str]
