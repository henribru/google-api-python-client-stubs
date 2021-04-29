import typing

import typing_extensions

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    approvals: typing.List[Approval]
    createTime: str
    inputProperties: typing.Dict[str, typing.Any]
    name: str
    provider: str
    state: typing_extensions.Literal[
        "ACCOUNT_STATE_UNSPECIFIED", "ACCOUNT_ACTIVATION_REQUESTED", "ACCOUNT_ACTIVE"
    ]
    updateTime: str

@typing.type_check_only
class Approval(typing_extensions.TypedDict, total=False):
    name: str
    reason: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED"
    ]
    updateTime: str

@typing.type_check_only
class ApproveAccountRequest(typing_extensions.TypedDict, total=False):
    approvalName: str
    properties: typing.Dict[str, typing.Any]
    reason: str

@typing.type_check_only
class ApproveEntitlementPlanChangeRequest(typing_extensions.TypedDict, total=False):
    pendingPlanName: str

@typing.type_check_only
class ApproveEntitlementRequest(typing_extensions.TypedDict, total=False):
    properties: typing.Dict[str, typing.Any]

@typing.type_check_only
class Consumer(typing_extensions.TypedDict, total=False):
    project: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entitlement(typing_extensions.TypedDict, total=False):
    account: str
    consumers: typing.List[Consumer]
    createTime: str
    inputProperties: typing.Dict[str, typing.Any]
    messageToUser: str
    name: str
    newPendingOffer: str
    newPendingPlan: str
    offer: str
    offerEndTime: str
    plan: str
    product: str
    productExternalName: str
    provider: str
    quoteExternalName: str
    state: typing_extensions.Literal[
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
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: typing.List[Account]
    nextPageToken: str

@typing.type_check_only
class ListEntitlementsResponse(typing_extensions.TypedDict, total=False):
    entitlements: typing.List[Entitlement]
    nextPageToken: str

@typing.type_check_only
class RejectAccountRequest(typing_extensions.TypedDict, total=False):
    approvalName: str
    reason: str

@typing.type_check_only
class RejectEntitlementPlanChangeRequest(typing_extensions.TypedDict, total=False):
    pendingPlanName: str
    reason: str

@typing.type_check_only
class RejectEntitlementRequest(typing_extensions.TypedDict, total=False):
    reason: str

@typing.type_check_only
class ResetAccountRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SuspendEntitlementRequest(typing_extensions.TypedDict, total=False):
    reason: str
