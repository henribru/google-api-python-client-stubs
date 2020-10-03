import typing

import typing_extensions

class Subscription(typing_extensions.TypedDict, total=False):
    renewalSettings: RenewalSettings
    status: str
    customerDomain: str
    billingMethod: str
    transferInfo: typing.Dict[str, typing.Any]
    suspensionReasons: typing.List[str]
    plan: typing.Dict[str, typing.Any]
    skuName: str
    kind: str
    seats: Seats
    trialSettings: typing.Dict[str, typing.Any]
    purchaseOrderId: str
    skuId: str
    subscriptionId: str
    resourceUiUrl: str
    creationTime: str
    customerId: str
    dealCode: str

class ResellernotifyGetwatchdetailsResponse(typing_extensions.TypedDict, total=False):
    serviceAccountEmailAddresses: typing.List[str]
    topicName: str

class RenewalSettings(typing_extensions.TypedDict, total=False):
    renewalType: str
    kind: str

class Customer(typing_extensions.TypedDict, total=False):
    customerDomain: str
    customerDomainVerified: bool
    phoneNumber: str
    postalAddress: Address
    alternateEmail: str
    kind: str
    customerId: str
    resourceUiUrl: str

class ChangePlanRequest(typing_extensions.TypedDict, total=False):
    dealCode: str
    planName: str
    kind: str
    seats: Seats
    purchaseOrderId: str

class ResellernotifyResource(typing_extensions.TypedDict, total=False):
    topicName: str

class Subscriptions(typing_extensions.TypedDict, total=False):
    subscriptions: typing.List[Subscription]
    nextPageToken: str
    kind: str

class Address(typing_extensions.TypedDict, total=False):
    addressLine2: str
    kind: str
    addressLine1: str
    locality: str
    region: str
    contactName: str
    addressLine3: str
    countryCode: str
    organizationName: str
    postalCode: str

class Seats(typing_extensions.TypedDict, total=False):
    licensedNumberOfSeats: int
    kind: str
    numberOfSeats: int
    maximumNumberOfSeats: int
