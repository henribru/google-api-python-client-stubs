from typing import Any

from googleapiclient import errors as errors

EPOCH: Any
CHANNEL_PARAMS: Any
X_GOOG_CHANNEL_ID: str
X_GOOG_MESSAGE_NUMBER: str
X_GOOG_RESOURCE_STATE: str
X_GOOG_RESOURCE_URI: str
X_GOOG_RESOURCE_ID: str

class Notification:
    message_number: Any
    state: Any
    resource_uri: Any
    resource_id: Any
    def __init__(self, message_number, state, resource_uri, resource_id) -> None: ...

class Channel:
    type: Any
    id: Any
    token: Any
    address: Any
    expiration: Any
    params: Any
    resource_id: Any
    resource_uri: Any
    def __init__(
        self,
        type,
        id,
        token,
        address,
        expiration: Any | None = ...,
        params: Any | None = ...,
        resource_id: str = ...,
        resource_uri: str = ...,
    ) -> None: ...
    def body(self): ...
    def update(self, resp) -> None: ...

def notification_from_headers(channel, headers): ...
def new_webhook_channel(
    url, token: Any | None = ..., expiration: Any | None = ..., params: Any | None = ...
): ...
