import typing

import typing_extensions

@typing.type_check_only
class AdWordsLocationExtensions(typing_extensions.TypedDict, total=False):
    adPhone: str

@typing.type_check_only
class AssociateLocationRequest(typing_extensions.TypedDict, total=False):
    placeId: str

@typing.type_check_only
class Attribute(typing_extensions.TypedDict, total=False):
    name: str
    repeatedEnumValue: RepeatedEnumAttributeValue
    uriValues: typing.List[UriAttributeValue]
    valueType: typing_extensions.Literal[
        "ATTRIBUTE_VALUE_TYPE_UNSPECIFIED", "BOOL", "ENUM", "URL", "REPEATED_ENUM"
    ]
    values: typing.List[typing.Any]

@typing.type_check_only
class AttributeMetadata(typing_extensions.TypedDict, total=False):
    deprecated: bool
    displayName: str
    groupDisplayName: str
    parent: str
    repeatable: bool
    valueMetadata: typing.List[AttributeValueMetadata]
    valueType: typing_extensions.Literal[
        "ATTRIBUTE_VALUE_TYPE_UNSPECIFIED", "BOOL", "ENUM", "URL", "REPEATED_ENUM"
    ]

@typing.type_check_only
class AttributeValueMetadata(typing_extensions.TypedDict, total=False):
    displayName: str
    value: typing.Any

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    attributes: typing.List[Attribute]
    name: str

@typing.type_check_only
class BatchGetCategoriesResponse(typing_extensions.TypedDict, total=False):
    categories: typing.List[Category]

@typing.type_check_only
class BusinessHours(typing_extensions.TypedDict, total=False):
    periods: typing.List[TimePeriod]

@typing.type_check_only
class Categories(typing_extensions.TypedDict, total=False):
    additionalCategories: typing.List[Category]
    primaryCategory: Category

@typing.type_check_only
class Category(typing_extensions.TypedDict, total=False):
    displayName: str
    moreHoursTypes: typing.List[MoreHoursType]
    name: str
    serviceTypes: typing.List[ServiceType]

@typing.type_check_only
class Chain(typing_extensions.TypedDict, total=False):
    chainNames: typing.List[ChainName]
    locationCount: int
    name: str
    websites: typing.List[ChainUri]

@typing.type_check_only
class ChainName(typing_extensions.TypedDict, total=False):
    displayName: str
    languageCode: str

@typing.type_check_only
class ChainUri(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class ClearLocationAssociationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FreeFormServiceItem(typing_extensions.TypedDict, total=False):
    category: str
    label: Label

@typing.type_check_only
class GoogleLocation(typing_extensions.TypedDict, total=False):
    location: Location
    name: str
    requestAdminRightsUri: str

@typing.type_check_only
class GoogleUpdatedLocation(typing_extensions.TypedDict, total=False):
    diffMask: str
    location: Location
    pendingMask: str

@typing.type_check_only
class Label(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    languageCode: str

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListAttributeMetadataResponse(typing_extensions.TypedDict, total=False):
    attributeMetadata: typing.List[AttributeMetadata]
    nextPageToken: str

@typing.type_check_only
class ListCategoriesResponse(typing_extensions.TypedDict, total=False):
    categories: typing.List[Category]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    adWordsLocationExtensions: AdWordsLocationExtensions
    categories: Categories
    labels: typing.List[str]
    languageCode: str
    latlng: LatLng
    metadata: Metadata
    moreHours: typing.List[MoreHours]
    name: str
    openInfo: OpenInfo
    phoneNumbers: PhoneNumbers
    profile: Profile
    regularHours: BusinessHours
    relationshipData: RelationshipData
    serviceArea: ServiceAreaBusiness
    serviceItems: typing.List[ServiceItem]
    specialHours: SpecialHours
    storeCode: str
    storefrontAddress: PostalAddress
    title: str
    websiteUri: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    canDelete: bool
    canHaveFoodMenus: bool
    canModifyServiceList: bool
    canOperateHealthData: bool
    canOperateLocalPost: bool
    canOperateLodgingData: bool
    duplicateLocation: str
    hasGoogleUpdated: bool
    hasPendingEdits: bool
    mapsUri: str
    newReviewUri: str
    placeId: str

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MoreHours(typing_extensions.TypedDict, total=False):
    hoursTypeId: str
    periods: typing.List[TimePeriod]

@typing.type_check_only
class MoreHoursType(typing_extensions.TypedDict, total=False):
    displayName: str
    hoursTypeId: str
    localizedDisplayName: str

@typing.type_check_only
class OpenInfo(typing_extensions.TypedDict, total=False):
    canReopen: bool
    openingDate: Date
    status: typing_extensions.Literal[
        "OPEN_FOR_BUSINESS_UNSPECIFIED",
        "OPEN",
        "CLOSED_PERMANENTLY",
        "CLOSED_TEMPORARILY",
    ]

@typing.type_check_only
class PhoneNumbers(typing_extensions.TypedDict, total=False):
    additionalPhones: typing.List[str]
    primaryPhone: str

@typing.type_check_only
class PlaceInfo(typing_extensions.TypedDict, total=False):
    placeId: str
    placeName: str

@typing.type_check_only
class Places(typing_extensions.TypedDict, total=False):
    placeInfos: typing.List[PlaceInfo]

@typing.type_check_only
class PostalAddress(typing_extensions.TypedDict, total=False):
    addressLines: typing.List[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: typing.List[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class Profile(typing_extensions.TypedDict, total=False):
    description: str

@typing.type_check_only
class RelationshipData(typing_extensions.TypedDict, total=False):
    childrenLocations: typing.List[RelevantLocation]
    parentChain: str
    parentLocation: RelevantLocation

@typing.type_check_only
class RelevantLocation(typing_extensions.TypedDict, total=False):
    placeId: str
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DEPARTMENT_OF", "INDEPENDENT_ESTABLISHMENT_IN"
    ]

@typing.type_check_only
class RepeatedEnumAttributeValue(typing_extensions.TypedDict, total=False):
    setValues: typing.List[str]
    unsetValues: typing.List[str]

@typing.type_check_only
class SearchChainsResponse(typing_extensions.TypedDict, total=False):
    chains: typing.List[Chain]

@typing.type_check_only
class SearchGoogleLocationsRequest(typing_extensions.TypedDict, total=False):
    location: Location
    pageSize: int
    query: str

@typing.type_check_only
class SearchGoogleLocationsResponse(typing_extensions.TypedDict, total=False):
    googleLocations: typing.List[GoogleLocation]

@typing.type_check_only
class ServiceAreaBusiness(typing_extensions.TypedDict, total=False):
    businessType: typing_extensions.Literal[
        "BUSINESS_TYPE_UNSPECIFIED",
        "CUSTOMER_LOCATION_ONLY",
        "CUSTOMER_AND_BUSINESS_LOCATION",
    ]
    places: Places
    regionCode: str

@typing.type_check_only
class ServiceItem(typing_extensions.TypedDict, total=False):
    freeFormServiceItem: FreeFormServiceItem
    price: Money
    structuredServiceItem: StructuredServiceItem

@typing.type_check_only
class ServiceType(typing_extensions.TypedDict, total=False):
    displayName: str
    serviceTypeId: str

@typing.type_check_only
class SpecialHourPeriod(typing_extensions.TypedDict, total=False):
    closeTime: TimeOfDay
    closed: bool
    endDate: Date
    openTime: TimeOfDay
    startDate: Date

@typing.type_check_only
class SpecialHours(typing_extensions.TypedDict, total=False):
    specialHourPeriods: typing.List[SpecialHourPeriod]

@typing.type_check_only
class StructuredServiceItem(typing_extensions.TypedDict, total=False):
    description: str
    serviceTypeId: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimePeriod(typing_extensions.TypedDict, total=False):
    closeDay: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    closeTime: TimeOfDay
    openDay: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    openTime: TimeOfDay

@typing.type_check_only
class UriAttributeValue(typing_extensions.TypedDict, total=False):
    uri: str
