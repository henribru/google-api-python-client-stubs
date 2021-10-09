import typing

import typing_extensions

_list = list

@typing.type_check_only
class CreateProfileRequest(typing_extensions.TypedDict, total=False):
    deployment: Deployment
    profileType: _list[str]

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    projectId: str
    target: str

@typing.type_check_only
class Profile(typing_extensions.TypedDict, total=False):
    deployment: Deployment
    duration: str
    labels: dict[str, typing.Any]
    name: str
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
