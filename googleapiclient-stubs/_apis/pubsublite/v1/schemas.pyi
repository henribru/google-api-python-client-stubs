import typing

import typing_extensions

class Topic(typing_extensions.TypedDict, total=False):
    partitionConfig: PartitionConfig
    name: str
    retentionConfig: RetentionConfig

class ComputeMessageStatsRequest(typing_extensions.TypedDict, total=False):
    endCursor: Cursor
    startCursor: Cursor
    partition: str

class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    subscriptions: typing.List[str]
    nextPageToken: str

class RetentionConfig(typing_extensions.TypedDict, total=False):
    perPartitionBytes: str
    period: str

class TopicPartitions(typing_extensions.TypedDict, total=False):
    partitionCount: str

class ListPartitionCursorsResponse(typing_extensions.TypedDict, total=False):
    partitionCursors: typing.List[PartitionCursor]
    nextPageToken: str

class PartitionCursor(typing_extensions.TypedDict, total=False):
    cursor: Cursor
    partition: str

class Empty(typing_extensions.TypedDict, total=False): ...

class PartitionConfig(typing_extensions.TypedDict, total=False):
    count: str
    scale: int
    capacity: Capacity

class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: typing.List[Subscription]

class Subscription(typing_extensions.TypedDict, total=False):
    name: str
    deliveryConfig: DeliveryConfig
    topic: str

class Capacity(typing_extensions.TypedDict, total=False):
    publishMibPerSec: int
    subscribeMibPerSec: int

class DeliveryConfig(typing_extensions.TypedDict, total=False):
    deliveryRequirement: typing_extensions.Literal[
        "DELIVERY_REQUIREMENT_UNSPECIFIED",
        "DELIVER_IMMEDIATELY",
        "DELIVER_AFTER_STORED",
    ]

class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    topics: typing.List[Topic]
    nextPageToken: str

class ComputeMessageStatsResponse(typing_extensions.TypedDict, total=False):
    minimumPublishTime: str
    messageBytes: str
    minimumEventTime: str
    messageCount: str

class Cursor(typing_extensions.TypedDict, total=False):
    offset: str
