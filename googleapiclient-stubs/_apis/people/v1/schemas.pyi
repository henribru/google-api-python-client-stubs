import typing

import typing_extensions

class Organization(typing_extensions.TypedDict, total=False):
    domain: str
    startDate: Date
    phoneticName: str
    formattedType: str
    symbol: str
    jobDescription: str
    current: bool
    endDate: Date
    type: str
    name: str
    title: str
    location: str
    department: str
    metadata: FieldMetadata

class ListDirectoryPeopleResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nextSyncToken: str
    people: typing.List[Person]

class UpdateContactPhotoResponse(typing_extensions.TypedDict, total=False):
    person: Person

class FileAs(typing_extensions.TypedDict, total=False):
    value: str
    metadata: FieldMetadata

class ProfileMetadata(typing_extensions.TypedDict, total=False):
    userTypes: typing.List[str]
    objectType: typing_extensions.Literal["OBJECT_TYPE_UNSPECIFIED", "PERSON", "PAGE"]

class EmailAddress(typing_extensions.TypedDict, total=False):
    value: str
    formattedType: str
    displayName: str
    metadata: FieldMetadata
    type: str

class SipAddress(typing_extensions.TypedDict, total=False):
    formattedType: str
    value: str
    metadata: FieldMetadata
    type: str

class FieldMetadata(typing_extensions.TypedDict, total=False):
    primary: bool
    verified: bool
    source: Source

class Name(typing_extensions.TypedDict, total=False):
    phoneticMiddleName: str
    middleName: str
    givenName: str
    phoneticFullName: str
    displayNameLastFirst: str
    displayName: str
    honorificSuffix: str
    phoneticHonorificPrefix: str
    honorificPrefix: str
    metadata: FieldMetadata
    phoneticGivenName: str
    unstructuredName: str
    phoneticFamilyName: str
    phoneticHonorificSuffix: str
    familyName: str

class Nickname(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "DEFAULT",
        "MAIDEN_NAME",
        "INITIALS",
        "GPLUS",
        "OTHER_NAME",
        "ALTERNATE_NAME",
        "SHORT_NAME",
    ]
    metadata: FieldMetadata
    value: str

class MiscKeyword(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    type: typing_extensions.Literal[
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
    formattedType: str

class Interest(typing_extensions.TypedDict, total=False):
    value: str
    metadata: FieldMetadata

class Skill(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

class UpdateContactGroupRequest(typing_extensions.TypedDict, total=False):
    contactGroup: ContactGroup

class CalendarUrl(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    url: str
    formattedType: str
    type: str

class Membership(typing_extensions.TypedDict, total=False):
    domainMembership: DomainMembership
    metadata: FieldMetadata
    contactGroupMembership: ContactGroupMembership

class Person(typing_extensions.TypedDict, total=False):
    userDefined: typing.List[UserDefined]
    relations: typing.List[Relation]
    memberships: typing.List[Membership]
    ageRanges: typing.List[AgeRangeType]
    locales: typing.List[Locale]
    residences: typing.List[Residence]
    phoneNumbers: typing.List[PhoneNumber]
    braggingRights: typing.List[BraggingRights]
    interests: typing.List[Interest]
    calendarUrls: typing.List[CalendarUrl]
    metadata: PersonMetadata
    biographies: typing.List[Biography]
    sipAddresses: typing.List[SipAddress]
    genders: typing.List[Gender]
    occupations: typing.List[Occupation]
    photos: typing.List[Photo]
    skills: typing.List[Skill]
    addresses: typing.List[Address]
    imClients: typing.List[ImClient]
    nicknames: typing.List[Nickname]
    etag: str
    names: typing.List[Name]
    fileAses: typing.List[FileAs]
    birthdays: typing.List[Birthday]
    resourceName: str
    emailAddresses: typing.List[EmailAddress]
    externalIds: typing.List[ExternalId]
    coverPhotos: typing.List[CoverPhoto]
    miscKeywords: typing.List[MiscKeyword]
    clientData: typing.List[ClientData]
    relationshipStatuses: typing.List[RelationshipStatus]
    events: typing.List[Event]
    urls: typing.List[Url]
    locations: typing.List[Location]
    taglines: typing.List[Tagline]
    ageRange: typing_extensions.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "LESS_THAN_EIGHTEEN",
        "EIGHTEEN_TO_TWENTY",
        "TWENTY_ONE_OR_OLDER",
    ]
    organizations: typing.List[Organization]
    relationshipInterests: typing.List[RelationshipInterest]

class ModifyContactGroupMembersRequest(typing_extensions.TypedDict, total=False):
    resourceNamesToAdd: typing.List[str]
    resourceNamesToRemove: typing.List[str]

class Source(typing_extensions.TypedDict, total=False):
    updateTime: str
    etag: str
    profileMetadata: ProfileMetadata
    type: typing_extensions.Literal[
        "SOURCE_TYPE_UNSPECIFIED",
        "ACCOUNT",
        "PROFILE",
        "DOMAIN_PROFILE",
        "CONTACT",
        "OTHER_CONTACT",
        "DOMAIN_CONTACT",
    ]
    id: str

class AgeRangeType(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    ageRange: typing_extensions.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "LESS_THAN_EIGHTEEN",
        "EIGHTEEN_TO_TWENTY",
        "TWENTY_ONE_OR_OLDER",
    ]

class ContactGroup(typing_extensions.TypedDict, total=False):
    memberResourceNames: typing.List[str]
    formattedName: str
    metadata: ContactGroupMetadata
    memberCount: int
    groupType: typing_extensions.Literal[
        "GROUP_TYPE_UNSPECIFIED", "USER_CONTACT_GROUP", "SYSTEM_CONTACT_GROUP"
    ]
    resourceName: str
    name: str
    etag: str

class Biography(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "TEXT_PLAIN", "TEXT_HTML"
    ]

class GetPeopleResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[PersonResponse]

class ContactGroupResponse(typing_extensions.TypedDict, total=False):
    contactGroup: ContactGroup
    requestedResourceName: str
    status: Status

class ModifyContactGroupMembersResponse(typing_extensions.TypedDict, total=False):
    canNotRemoveLastContactGroupResourceNames: typing.List[str]
    notFoundResourceNames: typing.List[str]

class Gender(typing_extensions.TypedDict, total=False):
    value: str
    metadata: FieldMetadata
    formattedValue: str
    addressMeAs: str

class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: typing.List[Person]
    totalItems: int
    nextSyncToken: str
    totalPeople: int
    nextPageToken: str

class ListOtherContactsResponse(typing_extensions.TypedDict, total=False):
    otherContacts: typing.List[Person]
    nextSyncToken: str
    nextPageToken: str

class UpdateContactPhotoRequest(typing_extensions.TypedDict, total=False):
    personFields: str
    sources: typing.List[str]
    photoBytes: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Birthday(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    text: str
    date: Date

class Tagline(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

class CopyOtherContactToMyContactsGroupRequest(
    typing_extensions.TypedDict, total=False
):
    sources: typing.List[str]
    readMask: str
    copyMask: str

class Event(typing_extensions.TypedDict, total=False):
    date: Date
    formattedType: str
    type: str
    metadata: FieldMetadata

class PhoneNumber(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    formattedType: str
    type: str
    value: str
    canonicalForm: str

class Location(typing_extensions.TypedDict, total=False):
    buildingId: str
    metadata: FieldMetadata
    current: bool
    floor: str
    deskCode: str
    floorSection: str
    value: str
    type: str

class Residence(typing_extensions.TypedDict, total=False):
    current: bool
    metadata: FieldMetadata
    value: str

class Locale(typing_extensions.TypedDict, total=False):
    value: str
    metadata: FieldMetadata

class DeleteContactPhotoResponse(typing_extensions.TypedDict, total=False):
    person: Person

class CoverPhoto(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    default: bool
    url: str

class ListContactGroupsResponse(typing_extensions.TypedDict, total=False):
    totalItems: int
    nextPageToken: str
    contactGroups: typing.List[ContactGroup]
    nextSyncToken: str

class ClientData(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str
    key: str

class Url(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str
    formattedType: str
    type: str

class Relation(typing_extensions.TypedDict, total=False):
    formattedType: str
    person: str
    type: str
    metadata: FieldMetadata

class BatchGetContactGroupsResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[ContactGroupResponse]

class Date(typing_extensions.TypedDict, total=False):
    year: int
    day: int
    month: int

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class DomainMembership(typing_extensions.TypedDict, total=False):
    inViewerDomain: bool

class Address(typing_extensions.TypedDict, total=False):
    type: str
    formattedValue: str
    postalCode: str
    metadata: FieldMetadata
    streetAddress: str
    extendedAddress: str
    region: str
    city: str
    poBox: str
    formattedType: str
    countryCode: str
    country: str

class RelationshipStatus(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str
    formattedValue: str

class ExternalId(typing_extensions.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

class BraggingRights(typing_extensions.TypedDict, total=False):
    value: str
    metadata: FieldMetadata

class UserDefined(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str
    key: str

class ContactGroupMembership(typing_extensions.TypedDict, total=False):
    contactGroupResourceName: str
    contactGroupId: str

class ContactGroupMetadata(typing_extensions.TypedDict, total=False):
    deleted: bool
    updateTime: str

class PersonResponse(typing_extensions.TypedDict, total=False):
    requestedResourceName: str
    status: Status
    person: Person
    httpStatusCode: int

class RelationshipInterest(typing_extensions.TypedDict, total=False):
    formattedValue: str
    metadata: FieldMetadata
    value: str

class SearchDirectoryPeopleResponse(typing_extensions.TypedDict, total=False):
    people: typing.List[Person]
    nextPageToken: str
    totalSize: int

class Occupation(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

class CreateContactGroupRequest(typing_extensions.TypedDict, total=False):
    contactGroup: ContactGroup

class ImClient(typing_extensions.TypedDict, total=False):
    protocol: str
    formattedType: str
    metadata: FieldMetadata
    type: str
    username: str
    formattedProtocol: str

class PersonMetadata(typing_extensions.TypedDict, total=False):
    deleted: bool
    previousResourceNames: typing.List[str]
    objectType: typing_extensions.Literal["OBJECT_TYPE_UNSPECIFIED", "PERSON", "PAGE"]
    sources: typing.List[Source]
    linkedPeopleResourceNames: typing.List[str]

class Photo(typing_extensions.TypedDict, total=False):
    default: bool
    url: str
    metadata: FieldMetadata
