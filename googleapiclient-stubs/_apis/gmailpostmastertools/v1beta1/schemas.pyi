import typing

_list = list

@typing.type_check_only
class DeliveryError(typing.TypedDict, total=False):
    errorClass: typing.Literal[
        "DELIVERY_ERROR_CLASS_UNSPECIFIED", "PERMANENT_ERROR", "TEMPORARY_ERROR"
    ]
    errorRatio: float
    errorType: typing.Literal[
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
class Domain(typing.TypedDict, total=False):
    createTime: str
    name: str
    permission: typing.Literal["PERMISSION_UNSPECIFIED", "OWNER", "READER", "NONE"]

@typing.type_check_only
class FeedbackLoop(typing.TypedDict, total=False):
    id: str
    spamRatio: float

@typing.type_check_only
class IpReputation(typing.TypedDict, total=False):
    ipCount: str
    numIps: str
    reputation: typing.Literal[
        "REPUTATION_CATEGORY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BAD"
    ]
    sampleIps: _list[str]

@typing.type_check_only
class ListDomainsResponse(typing.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str

@typing.type_check_only
class ListTrafficStatsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    trafficStats: _list[TrafficStats]

@typing.type_check_only
class TrafficStats(typing.TypedDict, total=False):
    deliveryErrors: _list[DeliveryError]
    dkimSuccessRatio: float
    dmarcSuccessRatio: float
    domainReputation: typing.Literal[
        "REPUTATION_CATEGORY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BAD"
    ]
    inboundEncryptionRatio: float
    ipReputations: _list[IpReputation]
    name: str
    outboundEncryptionRatio: float
    spammyFeedbackLoops: _list[FeedbackLoop]
    spfSuccessRatio: float
    userReportedSpamRatio: float
    userReportedSpamRatioLowerBound: float
    userReportedSpamRatioUpperBound: float
