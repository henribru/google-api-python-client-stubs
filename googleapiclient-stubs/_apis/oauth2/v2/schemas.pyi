import typing

import typing_extensions

_list = list

@typing.type_check_only
class Tokeninfo(typing_extensions.TypedDict, total=False):
    audience: str
    email: str
    expires_in: int
    issued_to: str
    scope: str
    user_id: str
    verified_email: bool

@typing.type_check_only
class Userinfo(typing_extensions.TypedDict, total=False):
    email: str
    family_name: str
    gender: str
    given_name: str
    hd: str
    id: str
    link: str
    locale: str
    name: str
    picture: str
    verified_email: bool
