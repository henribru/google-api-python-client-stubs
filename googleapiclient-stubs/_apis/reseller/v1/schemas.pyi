import typing

import typing_extensions
@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    addressLine3: str
    contactName: str
    countryCode: str
    kind: str
    locality: str
    organizationName: str
    postalCode: str
    region: str

@typing.type_check_only
class ChangePlanRequest(typing_extensions.TypedDict, total=False):
    dealCode: str
    kind: str
    planName: str
    purchaseOrderId: str
    seats: Seats

@typing.type_check_only
class Customer(typing_extensions.TypedDict, total=False):
    alternateEmail: str
    customerDomain: str
    customerDomainVerified: bool
    customerId: str
    kind: str
    phoneNumber: str
    postalAddress: Address
    resourceUiUrl: str

@typing.type_check_only
class RenewalSettings(typing_extensions.TypedDict, total=False):
    kind: str
    renewalType: str

@typing.type_check_only
class ResellernotifyGetwatchdetailsResponse(typing_extensions.TypedDict, total=False):
    serviceAccountEmailAddresses: typing.List[str]
    topicName: str

@typing.type_check_only
class ResellernotifyResource(typing_extensions.TypedDict, total=False):
    topicName: str

@typing.type_check_only
class Seats(typing_extensions.TypedDict, total=False):
    kind: str
    licensedNumberOfSeats: int
    maximumNumberOfSeats: int
    numberOfSeats: int

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    billingMethod: str
    creationTime: str
    customerDomain: str
    customerId: str
    dealCode: str
    kind: str
    plan: typing.Dict[str, typing.Any]
    purchaseOrderId: str
    renewalSettings: RenewalSettings
    resourceUiUrl: str
    seats: Seats
    skuId: str
    skuName: str
    status: str
    subscriptionId: str
    suspensionReasons: typing.List[str]
    transferInfo: typing.Dict[str, typing.Any]
    trialSettings: typing.Dict[str, typing.Any]

@typing.type_check_only
class Subscriptions(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    subscriptions: typing.List[Subscription]
