import typing

import typing_extensions

_list = list

@typing.type_check_only
class Accessibility(typing_extensions.TypedDict, total=False):
    mobilityAccessible: bool
    mobilityAccessibleElevator: bool
    mobilityAccessibleElevatorException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleParking: bool
    mobilityAccessibleParkingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessiblePool: bool
    mobilityAccessiblePoolException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Activities(typing_extensions.TypedDict, total=False):
    beachAccess: bool
    beachAccessException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    beachFront: bool
    beachFrontException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bicycleRental: bool
    bicycleRentalException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    boutiqueStores: bool
    boutiqueStoresException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    casino: bool
    casinoException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeBicycleRental: bool
    freeBicycleRentalException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeWatercraftRental: bool
    freeWatercraftRentalException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    gameRoom: bool
    gameRoomException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    golf: bool
    golfException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    horsebackRiding: bool
    horsebackRidingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    nightclub: bool
    nightclubException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateBeach: bool
    privateBeachException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    scuba: bool
    scubaException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    snorkeling: bool
    snorkelingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tennis: bool
    tennisException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSkiing: bool
    waterSkiingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    watercraftRental: bool
    watercraftRentalException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Business(typing_extensions.TypedDict, total=False):
    businessCenter: bool
    businessCenterException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    meetingRooms: bool
    meetingRoomsCount: int
    meetingRoomsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    meetingRoomsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Connectivity(typing_extensions.TypedDict, total=False):
    freeWifi: bool
    freeWifiException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    publicAreaWifiAvailable: bool
    publicAreaWifiAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    publicInternetTerminal: bool
    publicInternetTerminalException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wifiAvailable: bool
    wifiAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class EcoCertification(typing_extensions.TypedDict, total=False):
    awarded: bool
    awardedException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ecoCertificate: typing_extensions.Literal[
        "ECO_CERTIFICATE_UNSPECIFIED",
        "ISO14001",
        "ISO50001",
        "ASIAN_ECOTOURISM",
        "BIOSPHERE_RESPOSNIBLE_TOURISM",
        "BUREAU_VERITAS",
        "CONTROL_UNION",
        "EARTHCHECK",
        "ECO_CERTIFICATION_MALTA",
        "ECOTOURISM_AUSTRALIAS_ECO",
        "GREAT_GREEN_DEAL",
        "GREEN_GLOBE",
        "GREEN_GROWTH2050",
        "GREEN_KEY",
        "GREEN_KEY_ECO_RATING",
        "GREEN_SEAL",
        "GREEN_STAR",
        "GREEN_TOURISM_ACTIVE",
        "HILTON_LIGHTSTAY",
        "HOSTELLING_INTERNATIONALS_QUALITY_AND_SUSTAINABILITY",
        "HOTELES_MAS_VERDES",
        "NORDIC_SWAN_ECOLABEL",
        "PREFERRED_BY_NATURE_SUSTAINABLE_TOURISM",
        "SUSTAINABLE_TRAVEL_IRELAND",
        "TOF_TIGERS_INITITIVES_PUG",
        "TRAVELIFE",
        "UNITED_CERTIFICATION_SYSTEMS_LIMITED",
        "VIREO_SRL",
    ]

@typing.type_check_only
class EnergyEfficiency(typing_extensions.TypedDict, total=False):
    carbonFreeEnergySources: bool
    carbonFreeEnergySourcesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energyConservationProgram: bool
    energyConservationProgramException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energyEfficientHeatingAndCoolingSystems: bool
    energyEfficientHeatingAndCoolingSystemsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energyEfficientLighting: bool
    energyEfficientLightingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energySavingThermostats: bool
    energySavingThermostatsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    greenBuildingDesign: bool
    greenBuildingDesignException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    independentOrganizationAuditsEnergyUse: bool
    independentOrganizationAuditsEnergyUseException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class EnhancedCleaning(typing_extensions.TypedDict, total=False):
    commercialGradeDisinfectantCleaning: bool
    commercialGradeDisinfectantCleaningException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    commonAreasEnhancedCleaning: bool
    commonAreasEnhancedCleaningException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    employeesTrainedCleaningProcedures: bool
    employeesTrainedCleaningProceduresException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    employeesTrainedThoroughHandWashing: bool
    employeesTrainedThoroughHandWashingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    employeesWearProtectiveEquipment: bool
    employeesWearProtectiveEquipmentException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    guestRoomsEnhancedCleaning: bool
    guestRoomsEnhancedCleaningException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Families(typing_extensions.TypedDict, total=False):
    babysitting: bool
    babysittingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kidsActivities: bool
    kidsActivitiesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kidsClub: bool
    kidsClubException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class FoodAndDrink(typing_extensions.TypedDict, total=False):
    bar: bool
    barException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    breakfastAvailable: bool
    breakfastAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    breakfastBuffet: bool
    breakfastBuffetException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    buffet: bool
    buffetException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dinnerBuffet: bool
    dinnerBuffetException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeBreakfast: bool
    freeBreakfastException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    restaurant: bool
    restaurantException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    restaurantsCount: int
    restaurantsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    roomService: bool
    roomServiceException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tableService: bool
    tableServiceException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    twentyFourHourRoomService: bool
    twentyFourHourRoomServiceException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    vendingMachine: bool
    vendingMachineException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class GetGoogleUpdatedLodgingResponse(typing_extensions.TypedDict, total=False):
    diffMask: str
    lodging: Lodging

@typing.type_check_only
class GuestUnitFeatures(typing_extensions.TypedDict, total=False):
    bungalowOrVilla: bool
    bungalowOrVillaException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    connectingUnitAvailable: bool
    connectingUnitAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    executiveFloor: bool
    executiveFloorException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxAdultOccupantsCount: int
    maxAdultOccupantsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxChildOccupantsCount: int
    maxChildOccupantsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxOccupantsCount: int
    maxOccupantsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateHome: bool
    privateHomeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    suite: bool
    suiteException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tier: typing_extensions.Literal[
        "UNIT_TIER_UNSPECIFIED", "STANDARD_UNIT", "DELUXE_UNIT"
    ]
    tierException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    totalLivingAreas: LivingArea
    views: ViewsFromUnit

@typing.type_check_only
class GuestUnitType(typing_extensions.TypedDict, total=False):
    codes: _list[str]
    features: GuestUnitFeatures
    label: str

@typing.type_check_only
class HealthAndSafety(typing_extensions.TypedDict, total=False):
    enhancedCleaning: EnhancedCleaning
    increasedFoodSafety: IncreasedFoodSafety
    minimizedContact: MinimizedContact
    personalProtection: PersonalProtection
    physicalDistancing: PhysicalDistancing

@typing.type_check_only
class Housekeeping(typing_extensions.TypedDict, total=False):
    dailyHousekeeping: bool
    dailyHousekeepingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    housekeepingAvailable: bool
    housekeepingAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    turndownService: bool
    turndownServiceException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class IncreasedFoodSafety(typing_extensions.TypedDict, total=False):
    diningAreasAdditionalSanitation: bool
    diningAreasAdditionalSanitationException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    disposableFlatware: bool
    disposableFlatwareException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    foodPreparationAndServingAdditionalSafety: bool
    foodPreparationAndServingAdditionalSafetyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    individualPackagedMeals: bool
    individualPackagedMealsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    singleUseFoodMenus: bool
    singleUseFoodMenusException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LanguageSpoken(typing_extensions.TypedDict, total=False):
    languageCode: str
    spoken: bool
    spokenException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingArea(typing_extensions.TypedDict, total=False):
    accessibility: LivingAreaAccessibility
    eating: LivingAreaEating
    features: LivingAreaFeatures
    layout: LivingAreaLayout
    sleeping: LivingAreaSleeping

@typing.type_check_only
class LivingAreaAccessibility(typing_extensions.TypedDict, total=False):
    adaCompliantUnit: bool
    adaCompliantUnitException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hearingAccessibleDoorbell: bool
    hearingAccessibleDoorbellException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hearingAccessibleFireAlarm: bool
    hearingAccessibleFireAlarmException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hearingAccessibleUnit: bool
    hearingAccessibleUnitException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleBathtub: bool
    mobilityAccessibleBathtubException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleShower: bool
    mobilityAccessibleShowerException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleToilet: bool
    mobilityAccessibleToiletException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleUnit: bool
    mobilityAccessibleUnitException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaEating(typing_extensions.TypedDict, total=False):
    coffeeMaker: bool
    coffeeMakerException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cookware: bool
    cookwareException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dishwasher: bool
    dishwasherException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    indoorGrill: bool
    indoorGrillException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kettle: bool
    kettleException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kitchenAvailable: bool
    kitchenAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    microwave: bool
    microwaveException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    minibar: bool
    minibarException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    outdoorGrill: bool
    outdoorGrillException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    oven: bool
    ovenException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    refrigerator: bool
    refrigeratorException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sink: bool
    sinkException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    snackbar: bool
    snackbarException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    stove: bool
    stoveException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    teaStation: bool
    teaStationException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    toaster: bool
    toasterException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaFeatures(typing_extensions.TypedDict, total=False):
    airConditioning: bool
    airConditioningException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bathtub: bool
    bathtubException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bidet: bool
    bidetException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dryer: bool
    dryerException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    electronicRoomKey: bool
    electronicRoomKeyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    fireplace: bool
    fireplaceException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hairdryer: bool
    hairdryerException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    heating: bool
    heatingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    inunitSafe: bool
    inunitSafeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    inunitWifiAvailable: bool
    inunitWifiAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ironingEquipment: bool
    ironingEquipmentException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    payPerViewMovies: bool
    payPerViewMoviesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateBathroom: bool
    privateBathroomException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    shower: bool
    showerException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    toilet: bool
    toiletException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tv: bool
    tvCasting: bool
    tvCastingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tvException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tvStreaming: bool
    tvStreamingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    universalPowerAdapters: bool
    universalPowerAdaptersException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    washer: bool
    washerException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaLayout(typing_extensions.TypedDict, total=False):
    balcony: bool
    balconyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    livingAreaSqMeters: float
    livingAreaSqMetersException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    loft: bool
    loftException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    nonSmoking: bool
    nonSmokingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    patio: bool
    patioException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    stairs: bool
    stairsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaSleeping(typing_extensions.TypedDict, total=False):
    bedsCount: int
    bedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bunkBedsCount: int
    bunkBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cribsCount: int
    cribsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    doubleBedsCount: int
    doubleBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    featherPillows: bool
    featherPillowsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hypoallergenicBedding: bool
    hypoallergenicBeddingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kingBedsCount: int
    kingBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    memoryFoamPillows: bool
    memoryFoamPillowsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    otherBedsCount: int
    otherBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    queenBedsCount: int
    queenBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    rollAwayBedsCount: int
    rollAwayBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    singleOrTwinBedsCount: int
    singleOrTwinBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sofaBedsCount: int
    sofaBedsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    syntheticPillows: bool
    syntheticPillowsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Lodging(typing_extensions.TypedDict, total=False):
    accessibility: Accessibility
    activities: Activities
    allUnits: GuestUnitFeatures
    business: Business
    commonLivingArea: LivingArea
    connectivity: Connectivity
    families: Families
    foodAndDrink: FoodAndDrink
    guestUnits: _list[GuestUnitType]
    healthAndSafety: HealthAndSafety
    housekeeping: Housekeeping
    metadata: LodgingMetadata
    name: str
    parking: Parking
    pets: Pets
    policies: Policies
    pools: Pools
    property: Property
    services: Services
    someUnits: GuestUnitFeatures
    sustainability: Sustainability
    transportation: Transportation
    wellness: Wellness

@typing.type_check_only
class LodgingMetadata(typing_extensions.TypedDict, total=False):
    updateTime: str

@typing.type_check_only
class MinimizedContact(typing_extensions.TypedDict, total=False):
    contactlessCheckinCheckout: bool
    contactlessCheckinCheckoutException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    digitalGuestRoomKeys: bool
    digitalGuestRoomKeysException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    housekeepingScheduledRequestOnly: bool
    housekeepingScheduledRequestOnlyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noHighTouchItemsCommonAreas: bool
    noHighTouchItemsCommonAreasException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noHighTouchItemsGuestRooms: bool
    noHighTouchItemsGuestRoomsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    plasticKeycardsDisinfected: bool
    plasticKeycardsDisinfectedException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    roomBookingsBuffer: bool
    roomBookingsBufferException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Parking(typing_extensions.TypedDict, total=False):
    electricCarChargingStations: bool
    electricCarChargingStationsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeParking: bool
    freeParkingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeSelfParking: bool
    freeSelfParkingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeValetParking: bool
    freeValetParkingException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    parkingAvailable: bool
    parkingAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    selfParkingAvailable: bool
    selfParkingAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    valetParkingAvailable: bool
    valetParkingAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class PaymentOptions(typing_extensions.TypedDict, total=False):
    cash: bool
    cashException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cheque: bool
    chequeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    creditCard: bool
    creditCardException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    debitCard: bool
    debitCardException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobileNfc: bool
    mobileNfcException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class PersonalProtection(typing_extensions.TypedDict, total=False):
    commonAreasOfferSanitizingItems: bool
    commonAreasOfferSanitizingItemsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    faceMaskRequired: bool
    faceMaskRequiredException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    guestRoomHygieneKitsAvailable: bool
    guestRoomHygieneKitsAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    protectiveEquipmentAvailable: bool
    protectiveEquipmentAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Pets(typing_extensions.TypedDict, total=False):
    catsAllowed: bool
    catsAllowedException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dogsAllowed: bool
    dogsAllowedException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    petsAllowed: bool
    petsAllowedException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    petsAllowedFree: bool
    petsAllowedFreeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class PhysicalDistancing(typing_extensions.TypedDict, total=False):
    commonAreasPhysicalDistancingArranged: bool
    commonAreasPhysicalDistancingArrangedException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    physicalDistancingRequired: bool
    physicalDistancingRequiredException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safetyDividers: bool
    safetyDividersException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sharedAreasLimitedOccupancy: bool
    sharedAreasLimitedOccupancyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wellnessAreasHavePrivateSpaces: bool
    wellnessAreasHavePrivateSpacesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Policies(typing_extensions.TypedDict, total=False):
    allInclusiveAvailable: bool
    allInclusiveAvailableException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    allInclusiveOnly: bool
    allInclusiveOnlyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    checkinTime: TimeOfDay
    checkinTimeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    checkoutTime: TimeOfDay
    checkoutTimeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kidsStayFree: bool
    kidsStayFreeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxChildAge: int
    maxChildAgeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxKidsStayFreeCount: int
    maxKidsStayFreeCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    paymentOptions: PaymentOptions
    smokeFreeProperty: bool
    smokeFreePropertyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Pools(typing_extensions.TypedDict, total=False):
    adultPool: bool
    adultPoolException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hotTub: bool
    hotTubException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    indoorPool: bool
    indoorPoolException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    indoorPoolsCount: int
    indoorPoolsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lazyRiver: bool
    lazyRiverException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lifeguard: bool
    lifeguardException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    outdoorPool: bool
    outdoorPoolException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    outdoorPoolsCount: int
    outdoorPoolsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    pool: bool
    poolException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    poolsCount: int
    poolsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wadingPool: bool
    wadingPoolException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterPark: bool
    waterParkException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterslide: bool
    waterslideException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wavePool: bool
    wavePoolException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Property(typing_extensions.TypedDict, total=False):
    builtYear: int
    builtYearException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    floorsCount: int
    floorsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lastRenovatedYear: int
    lastRenovatedYearException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    roomsCount: int
    roomsCountException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Services(typing_extensions.TypedDict, total=False):
    baggageStorage: bool
    baggageStorageException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    concierge: bool
    conciergeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    convenienceStore: bool
    convenienceStoreException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    currencyExchange: bool
    currencyExchangeException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    elevator: bool
    elevatorException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    frontDesk: bool
    frontDeskException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    fullServiceLaundry: bool
    fullServiceLaundryException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    giftShop: bool
    giftShopException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    languagesSpoken: _list[LanguageSpoken]
    selfServiceLaundry: bool
    selfServiceLaundryException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    socialHour: bool
    socialHourException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    twentyFourHourFrontDesk: bool
    twentyFourHourFrontDeskException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wakeUpCalls: bool
    wakeUpCallsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Sustainability(typing_extensions.TypedDict, total=False):
    energyEfficiency: EnergyEfficiency
    sustainabilityCertifications: SustainabilityCertifications
    sustainableSourcing: SustainableSourcing
    wasteReduction: WasteReduction
    waterConservation: WaterConservation

@typing.type_check_only
class SustainabilityCertifications(typing_extensions.TypedDict, total=False):
    breeamCertification: typing_extensions.Literal[
        "BREEAM_CERTIFICATION_UNSPECIFIED",
        "NO_BREEAM_CERTIFICATION",
        "BREEAM_PASS",
        "BREEAM_GOOD",
        "BREEAM_VERY_GOOD",
        "BREEAM_EXCELLENT",
        "BREEAM_OUTSTANDING",
    ]
    breeamCertificationException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ecoCertifications: _list[EcoCertification]
    leedCertification: typing_extensions.Literal[
        "LEED_CERTIFICATION_UNSPECIFIED",
        "NO_LEED_CERTIFICATION",
        "LEED_CERTIFIED",
        "LEED_SILVER",
        "LEED_GOLD",
        "LEED_PLATINUM",
    ]
    leedCertificationException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class SustainableSourcing(typing_extensions.TypedDict, total=False):
    ecoFriendlyToiletries: bool
    ecoFriendlyToiletriesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    locallySourcedFoodAndBeverages: bool
    locallySourcedFoodAndBeveragesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    organicCageFreeEggs: bool
    organicCageFreeEggsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    organicFoodAndBeverages: bool
    organicFoodAndBeveragesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    responsiblePurchasingPolicy: bool
    responsiblePurchasingPolicyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    responsiblySourcesSeafood: bool
    responsiblySourcesSeafoodException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    veganMeals: bool
    veganMealsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    vegetarianMeals: bool
    vegetarianMealsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class Transportation(typing_extensions.TypedDict, total=False):
    airportShuttle: bool
    airportShuttleException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    carRentalOnProperty: bool
    carRentalOnPropertyException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeAirportShuttle: bool
    freeAirportShuttleException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freePrivateCarService: bool
    freePrivateCarServiceException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    localShuttle: bool
    localShuttleException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateCarService: bool
    privateCarServiceException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    transfer: bool
    transferException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class ViewsFromUnit(typing_extensions.TypedDict, total=False):
    beachView: bool
    beachViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cityView: bool
    cityViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    gardenView: bool
    gardenViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lakeView: bool
    lakeViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    landmarkView: bool
    landmarkViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    oceanView: bool
    oceanViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    poolView: bool
    poolViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    valleyView: bool
    valleyViewException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class WasteReduction(typing_extensions.TypedDict, total=False):
    compostableFoodContainersAndCutlery: bool
    compostableFoodContainersAndCutleryException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    compostsExcessFood: bool
    compostsExcessFoodException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    donatesExcessFood: bool
    donatesExcessFoodException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    foodWasteReductionProgram: bool
    foodWasteReductionProgramException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noSingleUsePlasticStraws: bool
    noSingleUsePlasticStrawsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noSingleUsePlasticWaterBottles: bool
    noSingleUsePlasticWaterBottlesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noStyrofoamFoodContainers: bool
    noStyrofoamFoodContainersException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    recyclingProgram: bool
    recyclingProgramException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    refillableToiletryContainers: bool
    refillableToiletryContainersException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyDisposesBatteries: bool
    safelyDisposesBatteriesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyDisposesElectronics: bool
    safelyDisposesElectronicsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyDisposesLightbulbs: bool
    safelyDisposesLightbulbsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyHandlesHazardousSubstances: bool
    safelyHandlesHazardousSubstancesException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    soapDonationProgram: bool
    soapDonationProgramException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    toiletryDonationProgram: bool
    toiletryDonationProgramException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterBottleFillingStations: bool
    waterBottleFillingStationsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class WaterConservation(typing_extensions.TypedDict, total=False):
    independentOrganizationAuditsWaterUse: bool
    independentOrganizationAuditsWaterUseException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    linenReuseProgram: bool
    linenReuseProgramException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    towelReuseProgram: bool
    towelReuseProgramException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSavingShowers: bool
    waterSavingShowersException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSavingSinks: bool
    waterSavingSinksException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSavingToilets: bool
    waterSavingToiletsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Wellness(typing_extensions.TypedDict, total=False):
    doctorOnCall: bool
    doctorOnCallException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ellipticalMachine: bool
    ellipticalMachineException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    fitnessCenter: bool
    fitnessCenterException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeFitnessCenter: bool
    freeFitnessCenterException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeWeights: bool
    freeWeightsException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    massage: bool
    massageException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    salon: bool
    salonException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sauna: bool
    saunaException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    spa: bool
    spaException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    treadmill: bool
    treadmillException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    weightMachine: bool
    weightMachineException: typing_extensions.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
