import typing

import typing_extensions
@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
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
class AgeRangeType(typing_extensions.TypedDict, total=False):
    ageRange: typing_extensions.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "LESS_THAN_EIGHTEEN",
        "EIGHTEEN_TO_TWENTY",
        "TWENTY_ONE_OR_OLDER",
    ]
    metadata: FieldMetadata

@typing.type_check_only
class BatchGetContactGroupsResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[ContactGroupResponse]

@typing.type_check_only
class Biography(typing_extensions.TypedDict, total=False):
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "TEXT_PLAIN", "TEXT_HTML"
    ]
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Birthday(typing_extensions.TypedDict, total=False):
    date: Date
    metadata: FieldMetadata
    text: str

@typing.type_check_only
class BraggingRights(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class CalendarUrl(typing_extensions.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    url: str

@typing.type_check_only
class ClientData(typing_extensions.TypedDict, total=False):
    key: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class ContactGroup(typing_extensions.TypedDict, total=False):
    clientData: typing.List[GroupClientData]
    etag: str
    formattedName: str
    groupType: typing_extensions.Literal[
        "GROUP_TYPE_UNSPECIFIED", "USER_CONTACT_GROUP", "SYSTEM_CONTACT_GROUP"
    ]
    memberCount: int
    memberResourceNames: typing.List[str]
    metadata: ContactGroupMetadata
    name: str
    resourceName: str

@typing.type_check_only
class ContactGroupMembership(typing_extensions.TypedDict, total=False):
    contactGroupId: str
    contactGroupResourceName: str

@typing.type_check_only
class ContactGroupMetadata(typing_extensions.TypedDict, total=False):
    deleted: bool
    updateTime: str

@typing.type_check_only
class ContactGroupResponse(typing_extensions.TypedDict, total=False):
    contactGroup: ContactGroup
    requestedResourceName: str
    status: Status

@typing.type_check_only
class CopyOtherContactToMyContactsGroupRequest(
    typing_extensions.TypedDict, total=False
):
    copyMask: str
    readMask: str
    sources: typing.List[str]

@typing.type_check_only
class CoverPhoto(typing_extensions.TypedDict, total=False):
    default: bool
    metadata: FieldMetadata
    url: str

@typing.type_check_only
class CreateContactGroupRequest(typing_extensions.TypedDict, total=False):
    contactGroup: ContactGroup
    readGroupFields: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeleteContactPhotoResponse(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class DomainMembership(typing_extensions.TypedDict, total=False):
    inViewerDomain: bool

@typing.type_check_only
class EmailAddress(typing_extensions.TypedDict, total=False):
    displayName: str
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    date: Date
    formattedType: str
    metadata: FieldMetadata
    type: str

@typing.type_check_only
class ExternalId(typing_extensions.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class FieldMetadata(typing_extensions.TypedDict, total=False):
    primary: bool
    source: Source
    verified: bool

@typing.type_check_only
class FileAs(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Gender(typing_extensions.TypedDict, total=False):
    addressMeAs: str
    formattedValue: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class GetPeopleResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[PersonResponse]

@typing.type_check_only
class GroupClientData(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ImClient(typing_extensions.TypedDict, total=False):
    formattedProtocol: str
    formattedType: str
    metadata: FieldMetadata
    protocol: str
    type: str
    username: str

@typing.type_check_only
class Interest(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: typing.List[Person]
    nextPageToken: str
    nextSyncToken: str
    totalItems: int
    totalPeople: int

@typing.type_check_only
class ListContactGroupsResponse(typing_extensions.TypedDict, total=False):
    contactGroups: typing.List[ContactGroup]
    nextPageToken: str
    nextSyncToken: str
    totalItems: int

@typing.type_check_only
class ListDirectoryPeopleResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nextSyncToken: str
    people: typing.List[Person]

@typing.type_check_only
class ListOtherContactsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nextSyncToken: str
    otherContacts: typing.List[Person]

@typing.type_check_only
class Locale(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    buildingId: str
    current: bool
    deskCode: str
    floor: str
    floorSection: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    contactGroupMembership: ContactGroupMembership
    domainMembership: DomainMembership
    metadata: FieldMetadata

@typing.type_check_only
class MiscKeyword(typing_extensions.TypedDict, total=False):
    formattedType: str
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

@typing.type_check_only
class ModifyContactGroupMembersRequest(typing_extensions.TypedDict, total=False):
    resourceNamesToAdd: typing.List[str]
    resourceNamesToRemove: typing.List[str]

@typing.type_check_only
class ModifyContactGroupMembersResponse(typing_extensions.TypedDict, total=False):
    canNotRemoveLastContactGroupResourceNames: typing.List[str]
    notFoundResourceNames: typing.List[str]

@typing.type_check_only
class Name(typing_extensions.TypedDict, total=False):
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
class Nickname(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    type: typing_extensions.Literal[
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
class Occupation(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Organization(typing_extensions.TypedDict, total=False):
    current: bool
    department: str
    domain: str
    endDate: Date
    formattedType: str
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
class Person(typing_extensions.TypedDict, total=False):
    addresses: typing.List[Address]
    ageRange: typing_extensions.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "LESS_THAN_EIGHTEEN",
        "EIGHTEEN_TO_TWENTY",
        "TWENTY_ONE_OR_OLDER",
    ]
    ageRanges: typing.List[AgeRangeType]
    biographies: typing.List[Biography]
    birthdays: typing.List[Birthday]
    braggingRights: typing.List[BraggingRights]
    calendarUrls: typing.List[CalendarUrl]
    clientData: typing.List[ClientData]
    coverPhotos: typing.List[CoverPhoto]
    emailAddresses: typing.List[EmailAddress]
    etag: str
    events: typing.List[Event]
    externalIds: typing.List[ExternalId]
    fileAses: typing.List[FileAs]
    genders: typing.List[Gender]
    imClients: typing.List[ImClient]
    interests: typing.List[Interest]
    locales: typing.List[Locale]
    locations: typing.List[Location]
    memberships: typing.List[Membership]
    metadata: PersonMetadata
    miscKeywords: typing.List[MiscKeyword]
    names: typing.List[Name]
    nicknames: typing.List[Nickname]
    occupations: typing.List[Occupation]
    organizations: typing.List[Organization]
    phoneNumbers: typing.List[PhoneNumber]
    photos: typing.List[Photo]
    relations: typing.List[Relation]
    relationshipInterests: typing.List[RelationshipInterest]
    relationshipStatuses: typing.List[RelationshipStatus]
    residences: typing.List[Residence]
    resourceName: str
    sipAddresses: typing.List[SipAddress]
    skills: typing.List[Skill]
    taglines: typing.List[Tagline]
    urls: typing.List[Url]
    userDefined: typing.List[UserDefined]

@typing.type_check_only
class PersonMetadata(typing_extensions.TypedDict, total=False):
    deleted: bool
    linkedPeopleResourceNames: typing.List[str]
    objectType: typing_extensions.Literal["OBJECT_TYPE_UNSPECIFIED", "PERSON", "PAGE"]
    previousResourceNames: typing.List[str]
    sources: typing.List[Source]

@typing.type_check_only
class PersonResponse(typing_extensions.TypedDict, total=False):
    httpStatusCode: int
    person: Person
    requestedResourceName: str
    status: Status

@typing.type_check_only
class PhoneNumber(typing_extensions.TypedDict, total=False):
    canonicalForm: str
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Photo(typing_extensions.TypedDict, total=False):
    default: bool
    metadata: FieldMetadata
    url: str

@typing.type_check_only
class ProfileMetadata(typing_extensions.TypedDict, total=False):
    objectType: typing_extensions.Literal["OBJECT_TYPE_UNSPECIFIED", "PERSON", "PAGE"]
    userTypes: typing.List[str]

@typing.type_check_only
class Relation(typing_extensions.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    person: str
    type: str

@typing.type_check_only
class RelationshipInterest(typing_extensions.TypedDict, total=False):
    formattedValue: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class RelationshipStatus(typing_extensions.TypedDict, total=False):
    formattedValue: str
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Residence(typing_extensions.TypedDict, total=False):
    current: bool
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class SearchDirectoryPeopleResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    people: typing.List[Person]
    totalSize: int

@typing.type_check_only
class SearchResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SearchResult]

@typing.type_check_only
class SearchResult(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class SipAddress(typing_extensions.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class Skill(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
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
    updateTime: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Tagline(typing_extensions.TypedDict, total=False):
    metadata: FieldMetadata
    value: str

@typing.type_check_only
class UpdateContactGroupRequest(typing_extensions.TypedDict, total=False):
    contactGroup: ContactGroup
    readGroupFields: str
    updateGroupFields: str

@typing.type_check_only
class UpdateContactPhotoRequest(typing_extensions.TypedDict, total=False):
    personFields: str
    photoBytes: str
    sources: typing.List[str]

@typing.type_check_only
class UpdateContactPhotoResponse(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class Url(typing_extensions.TypedDict, total=False):
    formattedType: str
    metadata: FieldMetadata
    type: str
    value: str

@typing.type_check_only
class UserDefined(typing_extensions.TypedDict, total=False):
    key: str
    metadata: FieldMetadata
    value: str
