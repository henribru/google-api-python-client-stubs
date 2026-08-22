import typing

_list = list

@typing.type_check_only
class AdWordsLocationExtensions(typing.TypedDict, total=False):
    adPhone: str

@typing.type_check_only
class Attribute(typing.TypedDict, total=False):
    name: str
    repeatedEnumValue: RepeatedEnumAttributeValue
    uriValues: _list[UriAttributeValue]
    valueType: typing.Literal[
        "ATTRIBUTE_VALUE_TYPE_UNSPECIFIED", "BOOL", "ENUM", "URL", "REPEATED_ENUM"
    ]
    values: _list[typing.Any]

@typing.type_check_only
class AttributeMetadata(typing.TypedDict, total=False):
    deprecated: bool
    displayName: str
    groupDisplayName: str
    parent: str
    repeatable: bool
    valueMetadata: _list[AttributeValueMetadata]
    valueType: typing.Literal[
        "ATTRIBUTE_VALUE_TYPE_UNSPECIFIED", "BOOL", "ENUM", "URL", "REPEATED_ENUM"
    ]

@typing.type_check_only
class AttributeValueMetadata(typing.TypedDict, total=False):
    displayName: str
    value: typing.Any

@typing.type_check_only
class Attributes(typing.TypedDict, total=False):
    attributes: _list[Attribute]
    name: str

@typing.type_check_only
class BatchGetCategoriesResponse(typing.TypedDict, total=False):
    categories: _list[Category]

@typing.type_check_only
class BusinessHours(typing.TypedDict, total=False):
    periods: _list[TimePeriod]

@typing.type_check_only
class Categories(typing.TypedDict, total=False):
    additionalCategories: _list[Category]
    primaryCategory: Category

@typing.type_check_only
class Category(typing.TypedDict, total=False):
    displayName: str
    moreHoursTypes: _list[MoreHoursType]
    name: str
    serviceTypes: _list[ServiceType]

@typing.type_check_only
class Chain(typing.TypedDict, total=False):
    chainNames: _list[ChainName]
    locationCount: int
    name: str
    websites: _list[ChainUri]

@typing.type_check_only
class ChainName(typing.TypedDict, total=False):
    displayName: str
    languageCode: str

@typing.type_check_only
class ChainUri(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FreeFormServiceItem(typing.TypedDict, total=False):
    category: str
    label: Label

@typing.type_check_only
class GoogleLocation(typing.TypedDict, total=False):
    location: Location
    name: str
    requestAdminRightsUri: str

@typing.type_check_only
class GoogleUpdatedLocation(typing.TypedDict, total=False):
    diffMask: str
    location: Location
    pendingMask: str

@typing.type_check_only
class Label(typing.TypedDict, total=False):
    description: str
    displayName: str
    languageCode: str

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListAttributeMetadataResponse(typing.TypedDict, total=False):
    attributeMetadata: _list[AttributeMetadata]
    nextPageToken: str

@typing.type_check_only
class ListCategoriesResponse(typing.TypedDict, total=False):
    categories: _list[Category]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    adWordsLocationExtensions: AdWordsLocationExtensions
    categories: Categories
    labels: _list[str]
    languageCode: str
    latlng: LatLng
    metadata: Metadata
    moreHours: _list[MoreHours]
    name: str
    openInfo: OpenInfo
    phoneNumbers: PhoneNumbers
    profile: Profile
    regularHours: BusinessHours
    relationshipData: RelationshipData
    serviceArea: ServiceAreaBusiness
    serviceItems: _list[ServiceItem]
    specialHours: SpecialHours
    storeCode: str
    storefrontAddress: PostalAddress
    title: str
    websiteUri: str

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    canDelete: bool
    canHaveBusinessCalls: bool
    canHaveFoodMenus: bool
    canModifyServiceList: bool
    canOperateHealthData: bool
    canOperateLocalPost: bool
    canOperateLodgingData: bool
    duplicateLocation: str
    hasGoogleUpdated: bool
    hasPendingEdits: bool
    hasVoiceOfMerchant: bool
    isParticularlyPersonalPlace: bool
    mapsUri: str
    newReviewUri: str
    placeId: str

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MoreHours(typing.TypedDict, total=False):
    hoursTypeId: str
    periods: _list[TimePeriod]

@typing.type_check_only
class MoreHoursType(typing.TypedDict, total=False):
    displayName: str
    hoursTypeId: str
    localizedDisplayName: str

@typing.type_check_only
class OpenInfo(typing.TypedDict, total=False):
    canReopen: bool
    openingDate: Date
    status: typing.Literal[
        "OPEN_FOR_BUSINESS_UNSPECIFIED",
        "OPEN",
        "CLOSED_PERMANENTLY",
        "CLOSED_TEMPORARILY",
    ]

@typing.type_check_only
class PhoneNumbers(typing.TypedDict, total=False):
    additionalPhones: _list[str]
    primaryPhone: str

@typing.type_check_only
class PlaceInfo(typing.TypedDict, total=False):
    placeId: str
    placeName: str

@typing.type_check_only
class Places(typing.TypedDict, total=False):
    placeInfos: _list[PlaceInfo]

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
class Profile(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class RelationshipData(typing.TypedDict, total=False):
    childrenLocations: _list[RelevantLocation]
    parentChain: str
    parentLocation: RelevantLocation

@typing.type_check_only
class RelevantLocation(typing.TypedDict, total=False):
    placeId: str
    relationType: typing.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DEPARTMENT_OF", "INDEPENDENT_ESTABLISHMENT_IN"
    ]

@typing.type_check_only
class RepeatedEnumAttributeValue(typing.TypedDict, total=False):
    setValues: _list[str]
    unsetValues: _list[str]

@typing.type_check_only
class SearchChainsResponse(typing.TypedDict, total=False):
    chains: _list[Chain]

@typing.type_check_only
class SearchGoogleLocationsRequest(typing.TypedDict, total=False):
    location: Location
    pageSize: int
    query: str

@typing.type_check_only
class SearchGoogleLocationsResponse(typing.TypedDict, total=False):
    googleLocations: _list[GoogleLocation]

@typing.type_check_only
class ServiceAreaBusiness(typing.TypedDict, total=False):
    businessType: typing.Literal[
        "BUSINESS_TYPE_UNSPECIFIED",
        "CUSTOMER_LOCATION_ONLY",
        "CUSTOMER_AND_BUSINESS_LOCATION",
    ]
    places: Places
    regionCode: str

@typing.type_check_only
class ServiceItem(typing.TypedDict, total=False):
    freeFormServiceItem: FreeFormServiceItem
    price: Money
    structuredServiceItem: StructuredServiceItem

@typing.type_check_only
class ServiceType(typing.TypedDict, total=False):
    displayName: str
    serviceTypeId: str

@typing.type_check_only
class SpecialHourPeriod(typing.TypedDict, total=False):
    closeTime: TimeOfDay
    closed: bool
    endDate: Date
    openTime: TimeOfDay
    startDate: Date

@typing.type_check_only
class SpecialHours(typing.TypedDict, total=False):
    specialHourPeriods: _list[SpecialHourPeriod]

@typing.type_check_only
class StructuredServiceItem(typing.TypedDict, total=False):
    description: str
    serviceTypeId: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimePeriod(typing.TypedDict, total=False):
    closeDay: typing.Literal[
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
    openDay: typing.Literal[
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
class UriAttributeValue(typing.TypedDict, total=False):
    uri: str
