import typing

_list = list

@typing.type_check_only
class AcceptInvitationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    accountName: str
    accountNumber: str
    name: str
    organizationInfo: OrganizationInfo
    permissionLevel: typing.Literal[
        "PERMISSION_LEVEL_UNSPECIFIED", "OWNER_LEVEL", "MEMBER_LEVEL"
    ]
    primaryOwner: str
    role: typing.Literal[
        "ACCOUNT_ROLE_UNSPECIFIED", "PRIMARY_OWNER", "OWNER", "MANAGER", "SITE_MANAGER"
    ]
    type: typing.Literal[
        "ACCOUNT_TYPE_UNSPECIFIED",
        "PERSONAL",
        "LOCATION_GROUP",
        "USER_GROUP",
        "ORGANIZATION",
    ]
    verificationState: typing.Literal[
        "VERIFICATION_STATE_UNSPECIFIED",
        "VERIFIED",
        "UNVERIFIED",
        "VERIFICATION_REQUESTED",
    ]
    vettedState: typing.Literal[
        "VETTED_STATE_UNSPECIFIED", "NOT_VETTED", "VETTED", "INVALID"
    ]

@typing.type_check_only
class Admin(typing.TypedDict, total=False):
    account: str
    admin: str
    name: str
    pendingInvitation: bool
    role: typing.Literal[
        "ADMIN_ROLE_UNSPECIFIED", "PRIMARY_OWNER", "OWNER", "MANAGER", "SITE_MANAGER"
    ]

@typing.type_check_only
class DeclineInvitationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Invitation(typing.TypedDict, total=False):
    name: str
    role: typing.Literal[
        "ADMIN_ROLE_UNSPECIFIED", "PRIMARY_OWNER", "OWNER", "MANAGER", "SITE_MANAGER"
    ]
    targetAccount: Account
    targetLocation: TargetLocation
    targetType: typing.Literal[
        "TARGET_TYPE_UNSPECIFIED", "ACCOUNTS_ONLY", "LOCATIONS_ONLY"
    ]

@typing.type_check_only
class ListAccountAdminsResponse(typing.TypedDict, total=False):
    accountAdmins: _list[Admin]

@typing.type_check_only
class ListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListInvitationsResponse(typing.TypedDict, total=False):
    invitations: _list[Invitation]

@typing.type_check_only
class ListLocationAdminsResponse(typing.TypedDict, total=False):
    admins: _list[Admin]

@typing.type_check_only
class OrganizationInfo(typing.TypedDict, total=False):
    address: PostalAddress
    phoneNumber: str
    registeredDomain: str

@typing.type_check_only
class PostalAddress(typing.TypedDict, total=False):
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
class TargetLocation(typing.TypedDict, total=False):
    address: str
    locationName: str
    placeId: str

@typing.type_check_only
class TransferLocationRequest(typing.TypedDict, total=False):
    destinationAccount: str
