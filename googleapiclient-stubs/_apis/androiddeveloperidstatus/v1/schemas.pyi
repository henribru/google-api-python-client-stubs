import typing

import typing_extensions

_list = list

@typing.type_check_only
class PackageRegistrationStatus(typing_extensions.TypedDict, total=False):
    certificateFingerprint: str
    name: str
    state: typing_extensions.Literal[
        "REGISTRATION_STATE_UNSPECIFIED",
        "REGISTERED",
        "NOT_REGISTERED",
        "REGISTERED_WITH_ANOTHER_CERTIFICATE_FINGERPRINT",
    ]
