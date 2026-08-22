import typing

_list = list

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    approvals: _list[Approval]
    createTime: str
    inputProperties: dict[str, typing.Any]
    name: str
    provider: str
    resellerParentBillingAccount: str
    state: typing.Literal[
        "ACCOUNT_STATE_UNSPECIFIED", "ACCOUNT_ACTIVATION_REQUESTED", "ACCOUNT_ACTIVE"
    ]
    updateTime: str

@typing.type_check_only
class Approval(typing.TypedDict, total=False):
    name: str
    reason: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED"]
    updateTime: str

@typing.type_check_only
class ApproveAccountRequest(typing.TypedDict, total=False):
    approvalName: str
    properties: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class ApproveEntitlementPlanChangeRequest(typing.TypedDict, total=False):
    pendingPlanName: str

@typing.type_check_only
class ApproveEntitlementRequest(typing.TypedDict, total=False):
    entitlementMigrated: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class Consumer(typing.TypedDict, total=False):
    project: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Entitlement(typing.TypedDict, total=False):
    account: str
    cancellationReason: str
    consumers: _list[Consumer]
    createTime: str
    entitlementBenefitIds: _list[str]
    inputProperties: dict[str, typing.Any]
    messageToUser: str
    name: str
    newOfferEndTime: str
    newOfferStartTime: str
    newPendingOffer: str
    newPendingOfferDuration: str
    newPendingPlan: str
    offer: str
    offerDuration: str
    offerEndTime: str
    orderId: str
    plan: str
    product: str
    productExternalName: str
    provider: str
    quoteExternalName: str
    state: typing.Literal[
        "ENTITLEMENT_STATE_UNSPECIFIED",
        "ENTITLEMENT_ACTIVATION_REQUESTED",
        "ENTITLEMENT_ACTIVE",
        "ENTITLEMENT_PENDING_CANCELLATION",
        "ENTITLEMENT_CANCELLED",
        "ENTITLEMENT_PENDING_PLAN_CHANGE",
        "ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL",
        "ENTITLEMENT_SUSPENDED",
    ]
    subscriptionEndTime: str
    updateTime: str
    usageReportingId: str

@typing.type_check_only
class ListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListEntitlementsResponse(typing.TypedDict, total=False):
    entitlements: _list[Entitlement]
    nextPageToken: str

@typing.type_check_only
class RejectAccountRequest(typing.TypedDict, total=False):
    approvalName: str
    reason: str

@typing.type_check_only
class RejectEntitlementPlanChangeRequest(typing.TypedDict, total=False):
    pendingPlanName: str
    reason: str

@typing.type_check_only
class RejectEntitlementRequest(typing.TypedDict, total=False):
    reason: str

@typing.type_check_only
class ResetAccountRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SuspendEntitlementRequest(typing.TypedDict, total=False):
    reason: str
