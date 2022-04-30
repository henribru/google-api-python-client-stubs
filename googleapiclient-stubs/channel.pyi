from _typeshed import Incomplete

from googleapiclient import errors as errors

EPOCH: Incomplete
CHANNEL_PARAMS: Incomplete
X_GOOG_CHANNEL_ID: str
X_GOOG_MESSAGE_NUMBER: str
X_GOOG_RESOURCE_STATE: str
X_GOOG_RESOURCE_URI: str
X_GOOG_RESOURCE_ID: str

class Notification:
    message_number: Incomplete
    state: Incomplete
    resource_uri: Incomplete
    resource_id: Incomplete
    def __init__(self, message_number, state, resource_uri, resource_id) -> None: ...

class Channel:
    type: Incomplete
    id: Incomplete
    token: Incomplete
    address: Incomplete
    expiration: Incomplete
    params: Incomplete
    resource_id: Incomplete
    resource_uri: Incomplete
    def __init__(
        self,
        type,
        id,
        token,
        address,
        expiration: Incomplete | None = ...,
        params: Incomplete | None = ...,
        resource_id: str = ...,
        resource_uri: str = ...,
    ) -> None: ...
    def body(self): ...
    def update(self, resp) -> None: ...

def notification_from_headers(channel, headers): ...
def new_webhook_channel(
    url,
    token: Incomplete | None = ...,
    expiration: Incomplete | None = ...,
    params: Incomplete | None = ...,
): ...
