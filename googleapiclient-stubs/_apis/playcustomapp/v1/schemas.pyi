import typing

_list = list

@typing.type_check_only
class CustomApp(typing.TypedDict, total=False):
    languageCode: str
    organizations: _list[Organization]
    packageName: str
    title: str

@typing.type_check_only
class Organization(typing.TypedDict, total=False):
    organizationId: str
    organizationName: str
