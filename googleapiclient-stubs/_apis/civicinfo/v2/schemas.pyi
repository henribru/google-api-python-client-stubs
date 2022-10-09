import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdministrationRegion(dict[str, typing.Any]): ...

@typing.type_check_only
class AdministrativeBody(typing_extensions.TypedDict, total=False):
    absenteeVotingInfoUrl: str
    ballotInfoUrl: str
    correspondenceAddress: SimpleAddressType
    electionInfoUrl: str
    electionNoticeText: str
    electionNoticeUrl: str
    electionOfficials: _list[ElectionOfficial]
    electionRegistrationConfirmationUrl: str
    electionRegistrationUrl: str
    electionRulesUrl: str
    hoursOfOperation: str
    name: str
    physicalAddress: SimpleAddressType
    voter_services: _list[str]
    votingLocationFinderUrl: str

@typing.type_check_only
class Candidate(typing_extensions.TypedDict, total=False):
    candidateUrl: str
    channels: _list[Channel]
    email: str
    name: str
    orderOnBallot: str
    party: str
    phone: str
    photoUrl: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    id: str
    type: str

@typing.type_check_only
class Contest(typing_extensions.TypedDict, total=False):
    ballotPlacement: str
    ballotTitle: str
    candidates: _list[Candidate]
    district: ElectoralDistrict
    electorateSpecifications: str
    level: _list[str]
    numberElected: str
    numberVotingFor: str
    office: str
    primaryParties: _list[str]
    primaryParty: str
    referendumBallotResponses: _list[str]
    referendumBrief: str
    referendumConStatement: str
    referendumEffectOfAbstain: str
    referendumPassageThreshold: str
    referendumProStatement: str
    referendumSubtitle: str
    referendumText: str
    referendumTitle: str
    referendumUrl: str
    roles: _list[str]
    sources: _list[Source]
    special: str
    type: str

@typing.type_check_only
class DivisionSearchResponse(typing_extensions.TypedDict, total=False):
    kind: str
    results: _list[DivisionSearchResult]

@typing.type_check_only
class DivisionSearchResult(typing_extensions.TypedDict, total=False):
    aliases: _list[str]
    name: str
    ocdId: str

@typing.type_check_only
class Election(typing_extensions.TypedDict, total=False):
    electionDay: str
    id: str
    name: str
    ocdDivisionId: str
    shapeLookupBehavior: typing_extensions.Literal[
        "shapeLookupDefault", "shapeLookupDisabled", "shapeLookupEnabled"
    ]

@typing.type_check_only
class ElectionOfficial(typing_extensions.TypedDict, total=False):
    emailAddress: str
    faxNumber: str
    name: str
    officePhoneNumber: str
    title: str

@typing.type_check_only
class ElectionsQueryResponse(typing_extensions.TypedDict, total=False):
    elections: _list[Election]
    kind: str

@typing.type_check_only
class ElectoralDistrict(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    scope: typing_extensions.Literal[
        "statewide",
        "congressional",
        "stateUpper",
        "stateLower",
        "countywide",
        "judicial",
        "schoolBoard",
        "citywide",
        "special",
        "countyCouncil",
        "township",
        "ward",
        "cityCouncil",
        "national",
    ]

@typing.type_check_only
class FeatureIdProto(typing_extensions.TypedDict, total=False):
    cellId: str
    fprint: str
    temporaryData: MessageSet

@typing.type_check_only
class GeocodingSummary(typing_extensions.TypedDict, total=False):
    addressUnderstood: bool
    featureId: FeatureIdProto
    featureType: typing_extensions.Literal[
        "typeAny",
        "typeTransportation",
        "typeRoute",
        "typeDeprecatedHighwayDoNotUse",
        "typeHighway",
        "typeHighway1",
        "typeHighway2",
        "typeHighway3",
        "typeHighway4",
        "typeHighway5",
        "typeHighway6",
        "typeHighway7",
        "typeHighway8",
        "typeHighway9",
        "typeBicycleRoute",
        "typeTrail",
        "typeSegment",
        "typeRoad",
        "typeRailway",
        "typeStandardTrack",
        "typeJrTrack",
        "typeNarrowTrack",
        "typeMonorailTrack",
        "typeSubwayTrack",
        "typeLightRailTrack",
        "typeBroadTrack",
        "typeHighSpeedRail",
        "typeTrolleyTrack",
        "typeFerry",
        "typeFerryBoat",
        "typeFerryTrain",
        "typeVirtualSegment",
        "typeIntersection",
        "typeTransit",
        "typeTransitStation",
        "typeBusStation",
        "typeTramwayStation",
        "typeTrainStation",
        "typeSubwayStation",
        "typeFerryTerminal",
        "typeAirport",
        "typeAirportCivil",
        "typeAirportMilitary",
        "typeAirportMixed",
        "typeHeliport",
        "typeSeaplaneBase",
        "typeAirstrip",
        "typeCableCarStation",
        "typeGondolaLiftStation",
        "typeFunicularStation",
        "typeSpecialStation",
        "typeHorseCarriageStation",
        "typeMonorailStation",
        "typeSeaport",
        "typeTransitStop",
        "typeTransitTrip",
        "typeTransitDeparture",
        "typeTransitLeg",
        "typeTransitLine",
        "typeTransitAgencyDeprecatedValue",
        "typeTransitTransfer",
        "typeSegmentPath",
        "typeRoadSign",
        "typeIntersectionGroup",
        "typePathway",
        "typeRestrictionGroup",
        "typeTollCluster",
        "typePolitical",
        "typeCountry",
        "typeAdministrativeArea",
        "typeAdministrativeArea1",
        "typeUsState",
        "typeGbCountry",
        "typeJpTodoufuken",
        "typeAdministrativeArea2",
        "typeGbFormerPostalCounty",
        "typeGbTraditionalCounty",
        "typeAdministrativeArea3",
        "typeAdministrativeArea4",
        "typeAdministrativeArea5",
        "typeAdministrativeArea6",
        "typeAdministrativeArea7",
        "typeAdministrativeArea8",
        "typeAdministrativeArea9",
        "typeColloquialArea",
        "typeReservation",
        "typeLocality",
        "typeGbPostTown",
        "typeJpGun",
        "typeJpShikuchouson",
        "typeJpSubShikuchouson",
        "typeColloquialCity",
        "typeSublocality",
        "typeUsBorough",
        "typeGbDependentLocality",
        "typeJpOoaza",
        "typeJpKoaza",
        "typeJpGaiku",
        "typeGbDoubleDependentLocality",
        "typeJpChiban",
        "typeJpEdaban",
        "typeSublocality1",
        "typeSublocality2",
        "typeSublocality3",
        "typeSublocality4",
        "typeSublocality5",
        "typeNeighborhood",
        "typeConstituency",
        "typeDesignatedMarketArea",
        "typeSchoolDistrict",
        "typeLandParcel",
        "typeDisputedArea",
        "typePoliceJurisdiction",
        "typeStatisticalArea",
        "typeConstituencyFuture",
        "typePark",
        "typeGolfCourse",
        "typeLocalPark",
        "typeNationalPark",
        "typeUsNationalPark",
        "typeUsNationalMonument",
        "typeNationalForest",
        "typeProvincialPark",
        "typeProvincialForest",
        "typeCampgrounds",
        "typeHikingArea",
        "typeBusiness",
        "typeGovernment",
        "typeBorderCrossing",
        "typeCityHall",
        "typeCourthouse",
        "typeEmbassy",
        "typeLibrary",
        "typeSchool",
        "typeUniversity",
        "typeEmergency",
        "typeHospital",
        "typePharmacy",
        "typePolice",
        "typeFire",
        "typeDoctor",
        "typeDentist",
        "typeVeterinarian",
        "typeTravelService",
        "typeLodging",
        "typeRestaurant",
        "typeGasStation",
        "typeParking",
        "typePostOffice",
        "typeRestArea",
        "typeCashMachine",
        "typeCarRental",
        "typeCarRepair",
        "typeShopping",
        "typeGrocery",
        "typeTouristDestination",
        "typeEcoTouristDestination",
        "typeBirdWatching",
        "typeFishing",
        "typeHunting",
        "typeNatureReserve",
        "typeTemple",
        "typeChurch",
        "typeGurudwara",
        "typeHinduTemple",
        "typeMosque",
        "typeSynagogue",
        "typeStadium",
        "typeBar",
        "typeMovieRental",
        "typeCoffee",
        "typeGolf",
        "typeBank",
        "typeDoodle",
        "typeGrounds",
        "typeAirportGrounds",
        "typeBuildingGrounds",
        "typeCemetery",
        "typeHospitalGrounds",
        "typeIndustrial",
        "typeMilitary",
        "typeShoppingCenter",
        "typeSportsComplex",
        "typeUniversityGrounds",
        "typeDeprecatedTarmac",
        "typeEnclosedTrafficArea",
        "typeParkingLot",
        "typeParkingGarage",
        "typeOffRoadArea",
        "typeBorder",
        "typeBuilding",
        "typeGeocodedAddress",
        "typeNaturalFeature",
        "typeTerrain",
        "typeSand",
        "typeBeach",
        "typeDune",
        "typeRocky",
        "typeIce",
        "typeGlacier",
        "typeBuiltUpArea",
        "typeVegetation",
        "typeShrubbery",
        "typeWoods",
        "typeAgricultural",
        "typeGrassland",
        "typeTundra",
        "typeDesert",
        "typeSaltFlat",
        "typeWater",
        "typeOcean",
        "typeBay",
        "typeBight",
        "typeLagoon",
        "typeSea",
        "typeStrait",
        "typeInlet",
        "typeFjord",
        "typeLake",
        "typeSeasonalLake",
        "typeReservoir",
        "typePond",
        "typeRiver",
        "typeRapids",
        "typeDistributary",
        "typeConfluence",
        "typeWaterfall",
        "typeSpring",
        "typeGeyser",
        "typeHotSpring",
        "typeSeasonalRiver",
        "typeWadi",
        "typeEstuary",
        "typeWetland",
        "typeWaterNavigation",
        "typeFord",
        "typeCanal",
        "typeHarbor",
        "typeChannel",
        "typeReef",
        "typeReefFlat",
        "typeReefGrowth",
        "typeReefExtent",
        "typeReefRockSubmerged",
        "typeIrrigation",
        "typeDam",
        "typeDrinkingWater",
        "typeCurrent",
        "typeWateringHole",
        "typeTectonic",
        "typeWateringHoleDeprecated",
        "typeVolcano",
        "typeLavaField",
        "typeFissure",
        "typeFault",
        "typeLandMass",
        "typeContinent",
        "typeIsland",
        "typeAtoll",
        "typeOceanRockExposed",
        "typeCay",
        "typePeninsula",
        "typeIsthmus",
        "typeElevated",
        "typePeak",
        "typeNunatak",
        "typeSpur",
        "typePass",
        "typePlateau",
        "typeRidge",
        "typeRavine",
        "typeCrater",
        "typeKarst",
        "typeCliff",
        "typeVista",
        "typeDigitalElevationModel",
        "typeUpland",
        "typeTerrace",
        "typeSlope",
        "typeContourLine",
        "typePan",
        "typeUnstableHillside",
        "typeMountainRange",
        "typeUndersea",
        "typeSubmarineSeamount",
        "typeSubmarineRidge",
        "typeSubmarineGap",
        "typeSubmarinePlateau",
        "typeSubmarineDeep",
        "typeSubmarineValley",
        "typeSubmarineBasin",
        "typeSubmarineSlope",
        "typeSubmarineCliff",
        "typeSubmarinePlain",
        "typeSubmarineFractureZone",
        "typeCave",
        "typeRock",
        "typeArchipelago",
        "typePostal",
        "typePostalCode",
        "typePostalCodePrefix",
        "typePremise",
        "typeSubPremise",
        "typeSuite",
        "typePostTown",
        "typePostalRound",
        "typeMetaFeature",
        "typeDataSource",
        "typeLocale",
        "typeTimezone",
        "typeBusinessChain",
        "typePhoneNumberPrefix",
        "typePhoneNumberAreaCode",
        "typeBusinessCorridor",
        "typeAddressTemplate",
        "typeTransitAgency",
        "typeFutureGeometry",
        "typeEvent",
        "typeEarthquake",
        "typeHurricane",
        "typeWeatherCondition",
        "typeTransient",
        "typeEntrance",
        "typeCartographic",
        "typeHighTension",
        "typeSkiTrail",
        "typeSkiLift",
        "typeSkiBoundary",
        "typeWatershedBoundary",
        "typeTarmac",
        "typeWall",
        "typePicnicArea",
        "typePlayGround",
        "typeTrailHead",
        "typeGolfTeeingGround",
        "typeGolfPuttingGreen",
        "typeGolfRough",
        "typeGolfSandBunker",
        "typeGolfFairway",
        "typeGolfHole",
        "typeDeprecatedGolfShop",
        "typeCampingSite",
        "typeDesignatedBarbecuePit",
        "typeDesignatedCookingArea",
        "typeCampfirePit",
        "typeWaterFountain",
        "typeLitterReceptacle",
        "typeLockerArea",
        "typeAnimalEnclosure",
        "typeCartographicLine",
        "typeEstablishment",
        "typeEstablishmentGrounds",
        "typeEstablishmentBuilding",
        "typeEstablishmentPoi",
        "typeEstablishmentService",
        "typeCelestial",
        "typeRoadMonitor",
        "typePublicSpacesAndMonuments",
        "typeStatue",
        "typeTownSquare",
        "typeLevel",
        "typeCompound",
        "typeCompoundGrounds",
        "typeCompoundBuilding",
        "typeCompoundSection",
        "typeTerminalPoint",
        "typeRegulatedArea",
        "typeLogicalBorder",
        "typeDoNotUseReservedToCatchGeneratedFiles",
        "typeUnknown",
    ]
    positionPrecisionMeters: float
    queryString: str

@typing.type_check_only
class GeographicDivision(typing_extensions.TypedDict, total=False):
    alsoKnownAs: _list[str]
    name: str
    officeIndices: _list[int]

@typing.type_check_only
class MessageSet(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Office(typing_extensions.TypedDict, total=False):
    divisionId: str
    levels: _list[str]
    name: str
    officialIndices: _list[int]
    roles: _list[str]
    sources: _list[Source]

@typing.type_check_only
class Official(typing_extensions.TypedDict, total=False):
    address: _list[SimpleAddressType]
    channels: _list[Channel]
    emails: _list[str]
    geocodingSummaries: _list[GeocodingSummary]
    name: str
    party: str
    phones: _list[str]
    photoUrl: str
    urls: _list[str]

@typing.type_check_only
class PollingLocation(typing_extensions.TypedDict, total=False):
    address: SimpleAddressType
    endDate: str
    latitude: float
    longitude: float
    name: str
    notes: str
    pollingHours: str
    sources: _list[Source]
    startDate: str
    voterServices: str

@typing.type_check_only
class Precinct(typing_extensions.TypedDict, total=False):
    administrationRegionId: str
    contestId: _list[str]
    datasetId: str
    earlyVoteSiteId: _list[str]
    electoralDistrictId: _list[str]
    id: str
    mailOnly: bool
    name: str
    number: str
    ocdId: _list[str]
    pollingLocationId: _list[str]
    spatialBoundaryId: _list[str]
    splitName: str
    ward: str

@typing.type_check_only
class RepresentativeInfoData(typing_extensions.TypedDict, total=False):
    divisions: dict[str, typing.Any]
    offices: _list[Office]
    officials: _list[Official]

@typing.type_check_only
class RepresentativeInfoResponse(typing_extensions.TypedDict, total=False):
    divisions: dict[str, typing.Any]
    kind: str
    normalizedInput: SimpleAddressType
    offices: _list[Office]
    officials: _list[Official]

@typing.type_check_only
class SimpleAddressType(typing_extensions.TypedDict, total=False):
    city: str
    line1: str
    line2: str
    line3: str
    locationName: str
    state: str
    zip: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    name: str
    official: bool

@typing.type_check_only
class VoterInfoResponse(typing_extensions.TypedDict, total=False):
    contests: _list[Contest]
    dropOffLocations: _list[PollingLocation]
    earlyVoteSites: _list[PollingLocation]
    election: Election
    kind: str
    mailOnly: bool
    normalizedInput: SimpleAddressType
    otherElections: _list[Election]
    pollingLocations: _list[PollingLocation]
    precinctId: str
    precincts: _list[Precinct]
    state: _list[AdministrationRegion]
