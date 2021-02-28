import typing

import typing_extensions
@typing.type_check_only
class Capacity(typing_extensions.TypedDict, total=False):
    publishMibPerSec: int
    subscribeMibPerSec: int

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
class ListPartitionCursorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partitionCursors: typing.List[PartitionCursor]

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: typing.List[Subscription]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: typing.List[str]

@typing.type_check_only
class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topics: typing.List[Topic]

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
class RetentionConfig(typing_extensions.TypedDict, total=False):
    perPartitionBytes: str
    period: str

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    deliveryConfig: DeliveryConfig
    name: str
    topic: str

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    name: str
    partitionConfig: PartitionConfig
    retentionConfig: RetentionConfig

@typing.type_check_only
class TopicPartitions(typing_extensions.TypedDict, total=False):
    partitionCount: str
