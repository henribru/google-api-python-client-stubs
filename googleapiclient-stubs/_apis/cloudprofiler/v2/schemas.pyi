import typing

import typing_extensions
@typing.type_check_only
class CreateProfileRequest(typing_extensions.TypedDict, total=False):
    deployment: Deployment
    profileType: typing.List[str]

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    projectId: str
    target: str

@typing.type_check_only
class Profile(typing_extensions.TypedDict, total=False):
    deployment: Deployment
    duration: str
    labels: typing.Dict[str, typing.Any]
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
