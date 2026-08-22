import typing

_list = list

@typing.type_check_only
class Address(typing.TypedDict, total=False):
    city: str
    country: str
    countryCode: str
    extendedAddress: str
    formattedType: str
    formattedValue: str
    metadata: FieldMetadata
    poBox: str
    postalCode: str
    region: str
    streetAddress: str
    type: str

@typing.type_check_only
class AgeRangeType(typing.TypedDict, total=False):
    ageRange: typing.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "LESS_THAN_EIGHTEEN",
        "EIGHTEEN_TO_TWENTY",
        "TWENTY_ONE_OR_OLDER",
    ]
    metadata: FieldMetadata

@typing.type_check_only
class BatchCreateContactsRequest(typing.TypedDict, total=False):
    contacts: _list[ContactToCreate]
    readMask: str
    sources: _list[
        typing.Literal[
            "READ_SOURCE_TYPE_UNSPECIFIED",
            "READ_SOURCE_TYPE_PROFILE",
            "READ_SOURCE_TYPE_CONTACT",
            "READ_SOURCE_TYPE_DOMAIN_CONTACT",
            "READ_SOURCE_TYPE_OTHER_CONTACT",
        ]
    ]

@typing.type_check_only
class BatchCreateContactsResponse(typing.TypedDict, total=False):
    createdPeople: _list[PersonResponse]

@typing.type_check_only
class BatchDeleteContactsRequest(typing.TypedDict, total=False):
    resourceNames: _list[str]

@typing.type_check_only
class BatchGetContactGroupsResponse(typing.TypedDict, total=False):
    responses: _list[ContactGroupResponse]

@typing.type_check_only
class BatchUpdateContactsRequest(typing.TypedDict, total=False):
    contacts: dict[str, typing.Any]
    readMask: str
    sources: _list[
        typing.Literal[
            "READ_SOURCE_TYPE_UNSPECIFIED",
            "READ_SOURCE_TYPE_PROFILE",
            "READ_SOURCE_TYPE_CONTACT",
            "READ_SOURCE_TYPE_DOMAIN_CONTACT",
            "READ_SOURCE_TYPE_OTHER_CONTACT",
        ]
    ]
    updateMask: str

@typing.type_check_only
class BatchUpdateContactsResponse(typing.TypedDict, total=False):
    updateResult: dict[str, typing.Any]

@typing.type_check_only
class Biography(typing.TypedDict, total=False):
    contentType: typing.Literal["CONTENT_TYPE_UNSPECIFIED", "TEXT_PLAIN", "TEXT_HTML"]
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Birthday(typing.TypedDict, total=False):
    date: Date
    metadata: FieldMetadata
    text: str

@typing.type_check_only
class BraggingRights(typing.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class CalendarUrl(typing.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    url: str

@typing.type_check_only
class ClientData(typing.TypedDict, total=False):
    key: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class ContactGroup(typing.TypedDict, total=False):
    clientData: _list[GroupClientData]
    etag: str
    formattedName: str
    groupType: typing.Literal[
        "GROUP_TYPE_UNSPECIFIED", "USER_CONTACT_GROUP", "SYSTEM_CONTACT_GROUP"
    ]
    memberCount: int
    memberResourceNames: _list[str]
    metadata: ContactGroupMetadata
    name: str
    resourceName: str

@typing.type_check_only
class ContactGroupMembership(typing.TypedDict, total=False):
    contactGroupId: str
    contactGroupResourceName: str

@typing.type_check_only
class ContactGroupMetadata(typing.TypedDict, total=False):
    deleted: bool
    updateTime: str

@typing.type_check_only
class ContactGroupResponse(typing.TypedDict, total=False):
    contactGroup: ContactGroup
    requestedResourceName: str
    status: Status

@typing.type_check_only
class ContactToCreate(typing.TypedDict, total=False):
    contactPerson: Person

@typing.type_check_only
class CopyOtherContactToMyContactsGroupRequest(typing.TypedDict, total=False):
    copyMask: str
    readMask: str
    sources: _list[
        typing.Literal[
            "READ_SOURCE_TYPE_UNSPECIFIED",
            "READ_SOURCE_TYPE_PROFILE",
            "READ_SOURCE_TYPE_CONTACT",
            "READ_SOURCE_TYPE_DOMAIN_CONTACT",
            "READ_SOURCE_TYPE_OTHER_CONTACT",
        ]
    ]

@typing.type_check_only
class CoverPhoto(typing.TypedDict, total=False):
    default: bool
    metadata: FieldMetadata
    url: str

@typing.type_check_only
class CreateContactGroupRequest(typing.TypedDict, total=False):
    contactGroup: ContactGroup
    readGroupFields: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeleteContactPhotoResponse(typing.TypedDict, total=False):
    person: Person

@typing.type_check_only
class DomainMembership(typing.TypedDict, total=False):
    inViewerDomain: bool

@typing.type_check_only
class EmailAddress(typing.TypedDict, total=False):
    displayName: str
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing.TypedDict, total=False):
    date: Date
    formattedType: str
    metadata: FieldMetadata
    type: str

@typing.type_check_only
class ExternalId(typing.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class FieldMetadata(typing.TypedDict, total=False):
    primary: bool
    source: Source
    sourcePrimary: bool
    verified: bool

@typing.type_check_only
class FileAs(typing.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Gender(typing.TypedDict, total=False):
    addressMeAs: str
    formattedValue: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class GetPeopleResponse(typing.TypedDict, total=False):
    responses: _list[PersonResponse]

@typing.type_check_only
class GroupClientData(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ImClient(typing.TypedDict, total=False):
    formattedProtocol: str
    formattedType: str
    metadata: FieldMetadata
    protocol: str
    type: str
    username: str

@typing.type_check_only
class Interest(typing.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class ListConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[Person]
    nextPageToken: str
    nextSyncToken: str
    totalItems: int
    totalPeople: int

@typing.type_check_only
class ListContactGroupsResponse(typing.TypedDict, total=False):
    contactGroups: _list[ContactGroup]
    nextPageToken: str
    nextSyncToken: str
    totalItems: int

@typing.type_check_only
class ListDirectoryPeopleResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nextSyncToken: str
    people: _list[Person]

@typing.type_check_only
class ListOtherContactsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nextSyncToken: str
    otherContacts: _list[Person]
    totalSize: int

@typing.type_check_only
class Locale(typing.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    buildingId: str
    current: bool
    deskCode: str
    floor: str
    floorSection: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Membership(typing.TypedDict, total=False):
    contactGroupMembership: ContactGroupMembership
    domainMembership: DomainMembership
    metadata: FieldMetadata

@typing.type_check_only
class MiscKeyword(typing.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "OUTLOOK_BILLING_INFORMATION",
        "OUTLOOK_DIRECTORY_SERVER",
        "OUTLOOK_KEYWORD",
        "OUTLOOK_MILEAGE",
        "OUTLOOK_PRIORITY",
        "OUTLOOK_SENSITIVITY",
        "OUTLOOK_SUBJECT",
        "OUTLOOK_USER",
        "HOME",
        "WORK",
        "OTHER",
    ]
    value: str

@typing.type_check_only
class ModifyContactGroupMembersRequest(typing.TypedDict, total=False):
    resourceNamesToAdd: _list[str]
    resourceNamesToRemove: _list[str]

@typing.type_check_only
class ModifyContactGroupMembersResponse(typing.TypedDict, total=False):
    canNotRemoveLastContactGroupResourceNames: _list[str]
    notFoundResourceNames: _list[str]

@typing.type_check_only
class Name(typing.TypedDict, total=False):
    displayName: str
    displayNameLastFirst: str
    familyName: str
    givenName: str
    honorificPrefix: str
    honorificSuffix: str
    metadata: FieldMetadata
    middleName: str
    phoneticFamilyName: str
    phoneticFullName: str
    phoneticGivenName: str
    phoneticHonorificPrefix: str
    phoneticHonorificSuffix: str
    phoneticMiddleName: str
    unstructuredName: str

@typing.type_check_only
class Nickname(typing.TypedDict, total=False):
    metadata: FieldMetadata
    type: typing.Literal[
        "DEFAULT",
        "MAIDEN_NAME",
        "INITIALS",
        "GPLUS",
        "OTHER_NAME",
        "ALTERNATE_NAME",
        "SHORT_NAME",
    ]
    value: str

@typing.type_check_only
class Occupation(typing.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Organization(typing.TypedDict, total=False):
    costCenter: str
    current: bool
    department: str
    domain: str
    endDate: Date
    formattedType: str
    fullTimeEquivalentMillipercent: int
    jobDescription: str
    location: str
    metadata: FieldMetadata
    name: str
    phoneticName: str
    startDate: Date
    symbol: str
    title: str
    type: str

@typing.type_check_only
class Person(typing.TypedDict, total=False):
    addresses: _list[Address]
    ageRange: typing.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "LESS_THAN_EIGHTEEN",
        "EIGHTEEN_TO_TWENTY",
        "TWENTY_ONE_OR_OLDER",
    ]
    ageRanges: _list[AgeRangeType]
    biographies: _list[Biography]
    birthdays: _list[Birthday]
    braggingRights: _list[BraggingRights]
    calendarUrls: _list[CalendarUrl]
    clientData: _list[ClientData]
    coverPhotos: _list[CoverPhoto]
    emailAddresses: _list[EmailAddress]
    etag: str
    events: _list[Event]
    externalIds: _list[ExternalId]
    fileAses: _list[FileAs]
    genders: _list[Gender]
    imClients: _list[ImClient]
    interests: _list[Interest]
    locales: _list[Locale]
    locations: _list[Location]
    memberships: _list[Membership]
    metadata: PersonMetadata
    miscKeywords: _list[MiscKeyword]
    names: _list[Name]
    nicknames: _list[Nickname]
    occupations: _list[Occupation]
    organizations: _list[Organization]
    phoneNumbers: _list[PhoneNumber]
    photos: _list[Photo]
    relations: _list[Relation]
    relationshipInterests: _list[RelationshipInterest]
    relationshipStatuses: _list[RelationshipStatus]
    residences: _list[Residence]
    resourceName: str
    sipAddresses: _list[SipAddress]
    skills: _list[Skill]
    taglines: _list[Tagline]
    urls: _list[Url]
    userDefined: _list[UserDefined]

@typing.type_check_only
class PersonMetadata(typing.TypedDict, total=False):
    deleted: bool
    linkedPeopleResourceNames: _list[str]
    objectType: typing.Literal["OBJECT_TYPE_UNSPECIFIED", "PERSON", "PAGE"]
    previousResourceNames: _list[str]
    sources: _list[Source]

@typing.type_check_only
class PersonResponse(typing.TypedDict, total=False):
    httpStatusCode: int
    person: Person
    requestedResourceName: str
    status: Status

@typing.type_check_only
class PhoneNumber(typing.TypedDict, total=False):
    canonicalForm: str
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Photo(typing.TypedDict, total=False):
    default: bool
    metadata: FieldMetadata
    url: str

@typing.type_check_only
class ProfileMetadata(typing.TypedDict, total=False):
    objectType: typing.Literal["OBJECT_TYPE_UNSPECIFIED", "PERSON", "PAGE"]
    userTypes: _list[
        typing.Literal[
            "USER_TYPE_UNKNOWN", "GOOGLE_USER", "GPLUS_USER", "GOOGLE_APPS_USER"
        ]
    ]

@typing.type_check_only
class Relation(typing.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    person: str
    type: str

@typing.type_check_only
class RelationshipInterest(typing.TypedDict, total=False):
    formattedValue: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class RelationshipStatus(typing.TypedDict, total=False):
    formattedValue: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Residence(typing.TypedDict, total=False):
    current: bool
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class SearchDirectoryPeopleResponse(typing.TypedDict, total=False):
    nextPageToken: str
    people: _list[Person]
    totalSize: int

@typing.type_check_only
class SearchResponse(typing.TypedDict, total=False):
    results: _list[SearchResult]

@typing.type_check_only
class SearchResult(typing.TypedDict, total=False):
    person: Person

@typing.type_check_only
class SipAddress(typing.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Skill(typing.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    etag: str
    id: str
    profileMetadata: ProfileMetadata
    type: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED",
        "ACCOUNT",
        "PROFILE",
        "DOMAIN_PROFILE",
        "CONTACT",
        "OTHER_CONTACT",
        "DOMAIN_CONTACT",
    ]
    updateTime: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Tagline(typing.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class UpdateContactGroupRequest(typing.TypedDict, total=False):
    contactGroup: ContactGroup
    readGroupFields: str
    updateGroupFields: str

@typing.type_check_only
class UpdateContactPhotoRequest(typing.TypedDict, total=False):
    personFields: str
    photoBytes: str
    sources: _list[
        typing.Literal[
            "READ_SOURCE_TYPE_UNSPECIFIED",
            "READ_SOURCE_TYPE_PROFILE",
            "READ_SOURCE_TYPE_CONTACT",
            "READ_SOURCE_TYPE_DOMAIN_CONTACT",
            "READ_SOURCE_TYPE_OTHER_CONTACT",
        ]
    ]

@typing.type_check_only
class UpdateContactPhotoResponse(typing.TypedDict, total=False):
    person: Person

@typing.type_check_only
class Url(typing.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class UserDefined(typing.TypedDict, total=False):
    key: str
    metadata: FieldMetadata
    value: str
