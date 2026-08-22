import typing

_list = list

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Capacity(typing.TypedDict, total=False):
    publishMibPerSec: int
    subscribeMibPerSec: int

@typing.type_check_only
class CommitCursorRequest(typing.TypedDict, total=False):
    cursor: Cursor
    partition: str

@typing.type_check_only
class CommitCursorResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ComputeHeadCursorRequest(typing.TypedDict, total=False):
    partition: str

@typing.type_check_only
class ComputeHeadCursorResponse(typing.TypedDict, total=False):
    headCursor: Cursor

@typing.type_check_only
class ComputeMessageStatsRequest(typing.TypedDict, total=False):
    endCursor: Cursor
    partition: str
    startCursor: Cursor

@typing.type_check_only
class ComputeMessageStatsResponse(typing.TypedDict, total=False):
    messageBytes: str
    messageCount: str
    minimumEventTime: str
    minimumPublishTime: str

@typing.type_check_only
class ComputeTimeCursorRequest(typing.TypedDict, total=False):
    partition: str
    target: TimeTarget

@typing.type_check_only
class ComputeTimeCursorResponse(typing.TypedDict, total=False):
    cursor: Cursor

@typing.type_check_only
class Cursor(typing.TypedDict, total=False):
    offset: str

@typing.type_check_only
class DeliveryConfig(typing.TypedDict, total=False):
    deliveryRequirement: typing.Literal[
        "DELIVERY_REQUIREMENT_UNSPECIFIED",
        "DELIVER_IMMEDIATELY",
        "DELIVER_AFTER_STORED",
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportConfig(typing.TypedDict, total=False):
    currentState: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "PAUSED", "PERMISSION_DENIED", "NOT_FOUND"
    ]
    deadLetterTopic: str
    desiredState: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "PAUSED", "PERMISSION_DENIED", "NOT_FOUND"
    ]
    pubsubConfig: PubSubConfig

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPartitionCursorsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    partitionCursors: _list[PartitionCursor]

@typing.type_check_only
class ListReservationTopicsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    topics: _list[str]

@typing.type_check_only
class ListReservationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class ListSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[str]

@typing.type_check_only
class ListTopicsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    target: str
    verb: str

@typing.type_check_only
class PartitionConfig(typing.TypedDict, total=False):
    capacity: Capacity
    count: str
    scale: int

@typing.type_check_only
class PartitionCursor(typing.TypedDict, total=False):
    cursor: Cursor
    partition: str

@typing.type_check_only
class PubSubConfig(typing.TypedDict, total=False):
    topic: str

@typing.type_check_only
class Reservation(typing.TypedDict, total=False):
    name: str
    throughputCapacity: str

@typing.type_check_only
class ReservationConfig(typing.TypedDict, total=False):
    throughputReservation: str

@typing.type_check_only
class RetentionConfig(typing.TypedDict, total=False):
    perPartitionBytes: str
    period: str

@typing.type_check_only
class SeekSubscriptionRequest(typing.TypedDict, total=False):
    namedTarget: typing.Literal["NAMED_TARGET_UNSPECIFIED", "TAIL", "HEAD"]
    timeTarget: TimeTarget

@typing.type_check_only
class SeekSubscriptionResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    deliveryConfig: DeliveryConfig
    exportConfig: ExportConfig
    name: str
    topic: str

@typing.type_check_only
class TimeTarget(typing.TypedDict, total=False):
    eventTime: str
    publishTime: str

@typing.type_check_only
class Topic(typing.TypedDict, total=False):
    name: str
    partitionConfig: PartitionConfig
    reservationConfig: ReservationConfig
    retentionConfig: RetentionConfig

@typing.type_check_only
class TopicPartitions(typing.TypedDict, total=False):
    partitionCount: str
