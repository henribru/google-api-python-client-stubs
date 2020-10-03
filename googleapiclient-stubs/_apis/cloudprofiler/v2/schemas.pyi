import typing

import typing_extensions

class Profile(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    duration: str
    deployment: Deployment
    profileBytes: str
    profileType: typing_extensions.Literal[
        "PROFILE_TYPE_UNSPECIFIED",
        "CPU",
        "WALL",
        "HEAP",
        "THREADS",
        "CONTENTION",
        "PEAK_HEAP",
        "HEAP_ALLOC",
    ]
    name: str

class CreateProfileRequest(typing_extensions.TypedDict, total=False):
    profileType: typing.List[str]
    deployment: Deployment

class Deployment(typing_extensions.TypedDict, total=False):
    target: str
    projectId: str
    labels: typing.Dict[str, typing.Any]
