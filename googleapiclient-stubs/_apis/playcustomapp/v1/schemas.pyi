import typing

import typing_extensions

_list = list

@typing.type_check_only
class CustomApp(typing_extensions.TypedDict, total=False):
    languageCode: str
    organizations: _list[Organization]
    packageName: str
    title: str

@typing.type_check_only
class Organization(typing_extensions.TypedDict, total=False):
    organizationId: str
    organizationName: str
