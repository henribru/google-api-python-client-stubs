import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1AndroidDeliveryData(
    typing_extensions.TypedDict, total=False
):
    analyticsLabel: str
    appId: str
    data: GoogleFirebaseFcmDataV1beta1Data
    date: GoogleTypeDate

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1Data(typing_extensions.TypedDict, total=False):
    countMessagesAccepted: str
    deliveryPerformancePercents: GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercents
    messageInsightPercents: GoogleFirebaseFcmDataV1beta1MessageInsightPercents
    messageOutcomePercents: GoogleFirebaseFcmDataV1beta1MessageOutcomePercents

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercents(
    typing_extensions.TypedDict, total=False
):
    delayedDeviceDoze: float
    delayedDeviceOffline: float
    delayedMessageThrottled: float
    delayedUserStopped: float
    deliveredNoDelay: float

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponse(
    typing_extensions.TypedDict, total=False
):
    androidDeliveryData: _list[GoogleFirebaseFcmDataV1beta1AndroidDeliveryData]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1MessageInsightPercents(
    typing_extensions.TypedDict, total=False
):
    priorityLowered: float

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1MessageOutcomePercents(
    typing_extensions.TypedDict, total=False
):
    delivered: float
    droppedAppForceStopped: float
    droppedDeviceInactive: float
    droppedTooManyPendingMessages: float
    pending: float

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int
