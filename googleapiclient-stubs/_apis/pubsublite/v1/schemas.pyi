import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Capacity(typing_extensions.TypedDict, total=False):
    publishMibPerSec: int
    subscribeMibPerSec: int

@typing.type_check_only
class CommitCursorRequest(typing_extensions.TypedDict, total=False):
    cursor: Cursor
    partition: str

@typing.type_check_only
class CommitCursorResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ComputeHeadCursorRequest(typing_extensions.TypedDict, total=False):
    partition: str

@typing.type_check_only
class ComputeHeadCursorResponse(typing_extensions.TypedDict, total=False):
    headCursor: Cursor

@typing.type_check_only
class ComputeMessageStatsRequest(typing_extensions.TypedDict, total=False):
    endCursor: Cursor
    partition: str
    startCursor: Cursor

@typing.type_check_only
class ComputeMessageStatsResponse(typing_extensions.TypedDict, total=False):
    messageBytes: str
    messageCount: str
    minimumEventTime: str
    minimumPublishTime: str

@typing.type_check_only
class ComputeTimeCursorRequest(typing_extensions.TypedDict, total=False):
    partition: str
    target: TimeTarget

@typing.type_check_only
class ComputeTimeCursorResponse(typing_extensions.TypedDict, total=False):
    cursor: Cursor

@typing.type_check_only
class Cursor(typing_extensions.TypedDict, total=False):
    offset: str

@typing.type_check_only
class DeliveryConfig(typing_extensions.TypedDict, total=False):
    deliveryRequirement: typing_extensions.Literal[
        "DELIVERY_REQUIREMENT_UNSPECIFIED",
        "DELIVER_IMMEDIATELY",
        "DELIVER_AFTER_STORED",
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListPartitionCursorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partitionCursors: _list[PartitionCursor]

@typing.type_check_only
class ListReservationTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topics: _list[str]

@typing.type_check_only
class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[str]

@typing.type_check_only
class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    target: str
    verb: str

@typing.type_check_only
class PartitionConfig(typing_extensions.TypedDict, total=False):
    capacity: Capacity
    count: str
    scale: int

@typing.type_check_only
class PartitionCursor(typing_extensions.TypedDict, total=False):
    cursor: Cursor
    partition: str

@typing.type_check_only
class Reservation(typing_extensions.TypedDict, total=False):
    name: str
    throughputCapacity: str

@typing.type_check_only
class ReservationConfig(typing_extensions.TypedDict, total=False):
    throughputReservation: str

@typing.type_check_only
class RetentionConfig(typing_extensions.TypedDict, total=False):
    perPartitionBytes: str
    period: str

@typing.type_check_only
class SeekSubscriptionRequest(typing_extensions.TypedDict, total=False):
    namedTarget: typing_extensions.Literal["NAMED_TARGET_UNSPECIFIED", "TAIL", "HEAD"]
    timeTarget: TimeTarget

@typing.type_check_only
class SeekSubscriptionResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    deliveryConfig: DeliveryConfig
    name: str
    topic: str

@typing.type_check_only
class TimeTarget(typing_extensions.TypedDict, total=False):
    eventTime: str
    publishTime: str

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    name: str
    partitionConfig: PartitionConfig
    reservationConfig: ReservationConfig
    retentionConfig: RetentionConfig

@typing.type_check_only
class TopicPartitions(typing_extensions.TypedDict, total=False):
    partitionCount: str
