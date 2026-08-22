import typing

_list = list

@typing.type_check_only
class PackageRegistrationStatus(typing.TypedDict, total=False):
    certificateFingerprint: str
    name: str
    state: typing.Literal[
        "REGISTRATION_STATE_UNSPECIFIED",
        "REGISTERED",
        "NOT_REGISTERED",
        "REGISTERED_WITH_ANOTHER_CERTIFICATE_FINGERPRINT",
    ]
