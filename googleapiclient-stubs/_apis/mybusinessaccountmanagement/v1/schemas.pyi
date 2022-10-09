import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceptInvitationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountName: str
    accountNumber: str
    name: str
    organizationInfo: OrganizationInfo
    permissionLevel: typing_extensions.Literal[
        "PERMISSION_LEVEL_UNSPECIFIED", "OWNER_LEVEL", "MEMBER_LEVEL"
    ]
    primaryOwner: str
    role: typing_extensions.Literal[
        "ACCOUNT_ROLE_UNSPECIFIED", "PRIMARY_OWNER", "OWNER", "MANAGER", "SITE_MANAGER"
    ]
    type: typing_extensions.Literal[
        "ACCOUNT_TYPE_UNSPECIFIED",
        "PERSONAL",
        "LOCATION_GROUP",
        "USER_GROUP",
        "ORGANIZATION",
    ]
    verificationState: typing_extensions.Literal[
        "VERIFICATION_STATE_UNSPECIFIED",
        "VERIFIED",
        "UNVERIFIED",
        "VERIFICATION_REQUESTED",
    ]
    vettedState: typing_extensions.Literal[
        "VETTED_STATE_UNSPECIFIED", "NOT_VETTED", "VETTED", "INVALID"
    ]

@typing.type_check_only
class Admin(typing_extensions.TypedDict, total=False):
    account: str
    admin: str
    name: str
    pendingInvitation: bool
    role: typing_extensions.Literal[
        "ADMIN_ROLE_UNSPECIFIED", "PRIMARY_OWNER", "OWNER", "MANAGER", "SITE_MANAGER"
    ]

@typing.type_check_only
class DeclineInvitationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Invitation(typing_extensions.TypedDict, total=False):
    name: str
    role: typing_extensions.Literal[
        "ADMIN_ROLE_UNSPECIFIED", "PRIMARY_OWNER", "OWNER", "MANAGER", "SITE_MANAGER"
    ]
    targetAccount: Account
    targetLocation: TargetLocation
    targetType: typing_extensions.Literal[
        "TARGET_TYPE_UNSPECIFIED", "ACCOUNTS_ONLY", "LOCATIONS_ONLY"
    ]

@typing.type_check_only
class ListAccountAdminsResponse(typing_extensions.TypedDict, total=False):
    accountAdmins: _list[Admin]

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListInvitationsResponse(typing_extensions.TypedDict, total=False):
    invitations: _list[Invitation]

@typing.type_check_only
class ListLocationAdminsResponse(typing_extensions.TypedDict, total=False):
    admins: _list[Admin]

@typing.type_check_only
class OrganizationInfo(typing_extensions.TypedDict, total=False):
    address: PostalAddress
    phoneNumber: str
    registeredDomain: str

@typing.type_check_only
class PostalAddress(typing_extensions.TypedDict, total=False):
    addressLines: _list[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: _list[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class TargetLocation(typing_extensions.TypedDict, total=False):
    address: str
    locationName: str

@typing.type_check_only
class TransferLocationRequest(typing_extensions.TypedDict, total=False):
    destinationAccount: str
