import typing

_list = list

@typing.type_check_only
class Accessibility(typing.TypedDict, total=False):
    mobilityAccessible: bool
    mobilityAccessibleElevator: bool
    mobilityAccessibleElevatorException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleParking: bool
    mobilityAccessibleParkingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessiblePool: bool
    mobilityAccessiblePoolException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Activities(typing.TypedDict, total=False):
    beachAccess: bool
    beachAccessException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    beachFront: bool
    beachFrontException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bicycleRental: bool
    bicycleRentalException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    boutiqueStores: bool
    boutiqueStoresException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    casino: bool
    casinoException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeBicycleRental: bool
    freeBicycleRentalException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeWatercraftRental: bool
    freeWatercraftRentalException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    gameRoom: bool
    gameRoomException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    golf: bool
    golfException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    horsebackRiding: bool
    horsebackRidingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    nightclub: bool
    nightclubException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateBeach: bool
    privateBeachException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    scuba: bool
    scubaException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    snorkeling: bool
    snorkelingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tennis: bool
    tennisException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSkiing: bool
    waterSkiingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    watercraftRental: bool
    watercraftRentalException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Business(typing.TypedDict, total=False):
    businessCenter: bool
    businessCenterException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    meetingRooms: bool
    meetingRoomsCount: int
    meetingRoomsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    meetingRoomsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Connectivity(typing.TypedDict, total=False):
    freeWifi: bool
    freeWifiException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    publicAreaWifiAvailable: bool
    publicAreaWifiAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    publicInternetTerminal: bool
    publicInternetTerminalException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wifiAvailable: bool
    wifiAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class EcoCertification(typing.TypedDict, total=False):
    awarded: bool
    awardedException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ecoCertificate: typing.Literal[
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
class EnergyEfficiency(typing.TypedDict, total=False):
    carbonFreeEnergySources: bool
    carbonFreeEnergySourcesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energyConservationProgram: bool
    energyConservationProgramException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energyEfficientHeatingAndCoolingSystems: bool
    energyEfficientHeatingAndCoolingSystemsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energyEfficientLighting: bool
    energyEfficientLightingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    energySavingThermostats: bool
    energySavingThermostatsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    greenBuildingDesign: bool
    greenBuildingDesignException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    independentOrganizationAuditsEnergyUse: bool
    independentOrganizationAuditsEnergyUseException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class EnhancedCleaning(typing.TypedDict, total=False):
    commercialGradeDisinfectantCleaning: bool
    commercialGradeDisinfectantCleaningException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    commonAreasEnhancedCleaning: bool
    commonAreasEnhancedCleaningException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    employeesTrainedCleaningProcedures: bool
    employeesTrainedCleaningProceduresException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    employeesTrainedThoroughHandWashing: bool
    employeesTrainedThoroughHandWashingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    employeesWearProtectiveEquipment: bool
    employeesWearProtectiveEquipmentException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    guestRoomsEnhancedCleaning: bool
    guestRoomsEnhancedCleaningException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Families(typing.TypedDict, total=False):
    babysitting: bool
    babysittingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kidsActivities: bool
    kidsActivitiesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kidsClub: bool
    kidsClubException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kidsFriendly: bool
    kidsFriendlyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class FoodAndDrink(typing.TypedDict, total=False):
    bar: bool
    barException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    breakfastAvailable: bool
    breakfastAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    breakfastBuffet: bool
    breakfastBuffetException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    buffet: bool
    buffetException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dinnerBuffet: bool
    dinnerBuffetException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeBreakfast: bool
    freeBreakfastException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    restaurant: bool
    restaurantException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    restaurantsCount: int
    restaurantsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    roomService: bool
    roomServiceException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tableService: bool
    tableServiceException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    twentyFourHourRoomService: bool
    twentyFourHourRoomServiceException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    vendingMachine: bool
    vendingMachineException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class GetGoogleUpdatedLodgingResponse(typing.TypedDict, total=False):
    diffMask: str
    lodging: Lodging

@typing.type_check_only
class GuestUnitFeatures(typing.TypedDict, total=False):
    bungalowOrVilla: bool
    bungalowOrVillaException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    connectingUnitAvailable: bool
    connectingUnitAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    executiveFloor: bool
    executiveFloorException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxAdultOccupantsCount: int
    maxAdultOccupantsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxChildOccupantsCount: int
    maxChildOccupantsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxOccupantsCount: int
    maxOccupantsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateHome: bool
    privateHomeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    suite: bool
    suiteException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tier: typing.Literal["UNIT_TIER_UNSPECIFIED", "STANDARD_UNIT", "DELUXE_UNIT"]
    tierException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    totalLivingAreas: LivingArea
    views: ViewsFromUnit

@typing.type_check_only
class GuestUnitType(typing.TypedDict, total=False):
    codes: _list[str]
    features: GuestUnitFeatures
    label: str

@typing.type_check_only
class HealthAndSafety(typing.TypedDict, total=False):
    enhancedCleaning: EnhancedCleaning
    increasedFoodSafety: IncreasedFoodSafety
    minimizedContact: MinimizedContact
    personalProtection: PersonalProtection
    physicalDistancing: PhysicalDistancing

@typing.type_check_only
class Housekeeping(typing.TypedDict, total=False):
    dailyHousekeeping: bool
    dailyHousekeepingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    housekeepingAvailable: bool
    housekeepingAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    turndownService: bool
    turndownServiceException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class IncreasedFoodSafety(typing.TypedDict, total=False):
    diningAreasAdditionalSanitation: bool
    diningAreasAdditionalSanitationException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    disposableFlatware: bool
    disposableFlatwareException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    foodPreparationAndServingAdditionalSafety: bool
    foodPreparationAndServingAdditionalSafetyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    individualPackagedMeals: bool
    individualPackagedMealsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    singleUseFoodMenus: bool
    singleUseFoodMenusException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LanguageSpoken(typing.TypedDict, total=False):
    languageCode: str
    spoken: bool
    spokenException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingArea(typing.TypedDict, total=False):
    accessibility: LivingAreaAccessibility
    eating: LivingAreaEating
    features: LivingAreaFeatures
    layout: LivingAreaLayout
    sleeping: LivingAreaSleeping

@typing.type_check_only
class LivingAreaAccessibility(typing.TypedDict, total=False):
    adaCompliantUnit: bool
    adaCompliantUnitException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hearingAccessibleDoorbell: bool
    hearingAccessibleDoorbellException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hearingAccessibleFireAlarm: bool
    hearingAccessibleFireAlarmException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hearingAccessibleUnit: bool
    hearingAccessibleUnitException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleBathtub: bool
    mobilityAccessibleBathtubException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleShower: bool
    mobilityAccessibleShowerException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleToilet: bool
    mobilityAccessibleToiletException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobilityAccessibleUnit: bool
    mobilityAccessibleUnitException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaEating(typing.TypedDict, total=False):
    coffeeMaker: bool
    coffeeMakerException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cookware: bool
    cookwareException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dishwasher: bool
    dishwasherException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    indoorGrill: bool
    indoorGrillException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kettle: bool
    kettleException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kitchenAvailable: bool
    kitchenAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    microwave: bool
    microwaveException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    minibar: bool
    minibarException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    outdoorGrill: bool
    outdoorGrillException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    oven: bool
    ovenException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    refrigerator: bool
    refrigeratorException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sink: bool
    sinkException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    snackbar: bool
    snackbarException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    stove: bool
    stoveException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    teaStation: bool
    teaStationException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    toaster: bool
    toasterException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaFeatures(typing.TypedDict, total=False):
    airConditioning: bool
    airConditioningException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bathtub: bool
    bathtubException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bidet: bool
    bidetException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dryer: bool
    dryerException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    electronicRoomKey: bool
    electronicRoomKeyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    fireplace: bool
    fireplaceException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hairdryer: bool
    hairdryerException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    heating: bool
    heatingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    inunitSafe: bool
    inunitSafeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    inunitWifiAvailable: bool
    inunitWifiAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ironingEquipment: bool
    ironingEquipmentException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    payPerViewMovies: bool
    payPerViewMoviesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateBathroom: bool
    privateBathroomException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    shower: bool
    showerException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    toilet: bool
    toiletException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tv: bool
    tvCasting: bool
    tvCastingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tvException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    tvStreaming: bool
    tvStreamingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    universalPowerAdapters: bool
    universalPowerAdaptersException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    washer: bool
    washerException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaLayout(typing.TypedDict, total=False):
    balcony: bool
    balconyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    livingAreaSqMeters: float
    livingAreaSqMetersException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    loft: bool
    loftException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    nonSmoking: bool
    nonSmokingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    patio: bool
    patioException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    stairs: bool
    stairsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class LivingAreaSleeping(typing.TypedDict, total=False):
    bedsCount: int
    bedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    bunkBedsCount: int
    bunkBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cribsCount: int
    cribsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    doubleBedsCount: int
    doubleBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    featherPillows: bool
    featherPillowsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hypoallergenicBedding: bool
    hypoallergenicBeddingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kingBedsCount: int
    kingBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    memoryFoamPillows: bool
    memoryFoamPillowsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    otherBedsCount: int
    otherBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    queenBedsCount: int
    queenBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    rollAwayBedsCount: int
    rollAwayBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    singleOrTwinBedsCount: int
    singleOrTwinBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sofaBedsCount: int
    sofaBedsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    syntheticPillows: bool
    syntheticPillowsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Lodging(typing.TypedDict, total=False):
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
class LodgingMetadata(typing.TypedDict, total=False):
    updateTime: str

@typing.type_check_only
class MinimizedContact(typing.TypedDict, total=False):
    contactlessCheckinCheckout: bool
    contactlessCheckinCheckoutException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    digitalGuestRoomKeys: bool
    digitalGuestRoomKeysException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    housekeepingScheduledRequestOnly: bool
    housekeepingScheduledRequestOnlyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noHighTouchItemsCommonAreas: bool
    noHighTouchItemsCommonAreasException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noHighTouchItemsGuestRooms: bool
    noHighTouchItemsGuestRoomsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    plasticKeycardsDisinfected: bool
    plasticKeycardsDisinfectedException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    roomBookingsBuffer: bool
    roomBookingsBufferException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Parking(typing.TypedDict, total=False):
    electricCarChargingStations: bool
    electricCarChargingStationsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeParking: bool
    freeParkingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeSelfParking: bool
    freeSelfParkingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeValetParking: bool
    freeValetParkingException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    parkingAvailable: bool
    parkingAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    selfParkingAvailable: bool
    selfParkingAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    valetParkingAvailable: bool
    valetParkingAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class PaymentOptions(typing.TypedDict, total=False):
    cash: bool
    cashException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cheque: bool
    chequeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    creditCard: bool
    creditCardException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    debitCard: bool
    debitCardException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    mobileNfc: bool
    mobileNfcException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class PersonalProtection(typing.TypedDict, total=False):
    commonAreasOfferSanitizingItems: bool
    commonAreasOfferSanitizingItemsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    faceMaskRequired: bool
    faceMaskRequiredException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    guestRoomHygieneKitsAvailable: bool
    guestRoomHygieneKitsAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    protectiveEquipmentAvailable: bool
    protectiveEquipmentAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Pets(typing.TypedDict, total=False):
    catsAllowed: bool
    catsAllowedException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    dogsAllowed: bool
    dogsAllowedException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    petsAllowed: bool
    petsAllowedException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    petsAllowedFree: bool
    petsAllowedFreeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class PhysicalDistancing(typing.TypedDict, total=False):
    commonAreasPhysicalDistancingArranged: bool
    commonAreasPhysicalDistancingArrangedException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    physicalDistancingRequired: bool
    physicalDistancingRequiredException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safetyDividers: bool
    safetyDividersException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sharedAreasLimitedOccupancy: bool
    sharedAreasLimitedOccupancyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wellnessAreasHavePrivateSpaces: bool
    wellnessAreasHavePrivateSpacesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Policies(typing.TypedDict, total=False):
    allInclusiveAvailable: bool
    allInclusiveAvailableException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    allInclusiveOnly: bool
    allInclusiveOnlyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    checkinTime: TimeOfDay
    checkinTimeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    checkoutTime: TimeOfDay
    checkoutTimeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    kidsStayFree: bool
    kidsStayFreeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxChildAge: int
    maxChildAgeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    maxKidsStayFreeCount: int
    maxKidsStayFreeCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    paymentOptions: PaymentOptions
    smokeFreeProperty: bool
    smokeFreePropertyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Pools(typing.TypedDict, total=False):
    adultPool: bool
    adultPoolException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    hotTub: bool
    hotTubException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    indoorPool: bool
    indoorPoolException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    indoorPoolsCount: int
    indoorPoolsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lazyRiver: bool
    lazyRiverException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lifeguard: bool
    lifeguardException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    outdoorPool: bool
    outdoorPoolException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    outdoorPoolsCount: int
    outdoorPoolsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    pool: bool
    poolException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    poolsCount: int
    poolsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wadingPool: bool
    wadingPoolException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterPark: bool
    waterParkException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterslide: bool
    waterslideException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wavePool: bool
    wavePoolException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Property(typing.TypedDict, total=False):
    builtYear: int
    builtYearException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    floorsCount: int
    floorsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lastRenovatedYear: int
    lastRenovatedYearException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    roomsCount: int
    roomsCountException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Services(typing.TypedDict, total=False):
    baggageStorage: bool
    baggageStorageException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    concierge: bool
    conciergeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    convenienceStore: bool
    convenienceStoreException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    currencyExchange: bool
    currencyExchangeException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    elevator: bool
    elevatorException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    frontDesk: bool
    frontDeskException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    fullServiceLaundry: bool
    fullServiceLaundryException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    giftShop: bool
    giftShopException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    languagesSpoken: _list[LanguageSpoken]
    selfServiceLaundry: bool
    selfServiceLaundryException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    socialHour: bool
    socialHourException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    twentyFourHourFrontDesk: bool
    twentyFourHourFrontDeskException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    wakeUpCalls: bool
    wakeUpCallsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Sustainability(typing.TypedDict, total=False):
    energyEfficiency: EnergyEfficiency
    sustainabilityCertifications: SustainabilityCertifications
    sustainableSourcing: SustainableSourcing
    wasteReduction: WasteReduction
    waterConservation: WaterConservation

@typing.type_check_only
class SustainabilityCertifications(typing.TypedDict, total=False):
    breeamCertification: typing.Literal[
        "BREEAM_CERTIFICATION_UNSPECIFIED",
        "NO_BREEAM_CERTIFICATION",
        "BREEAM_PASS",
        "BREEAM_GOOD",
        "BREEAM_VERY_GOOD",
        "BREEAM_EXCELLENT",
        "BREEAM_OUTSTANDING",
    ]
    breeamCertificationException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ecoCertifications: _list[EcoCertification]
    leedCertification: typing.Literal[
        "LEED_CERTIFICATION_UNSPECIFIED",
        "NO_LEED_CERTIFICATION",
        "LEED_CERTIFIED",
        "LEED_SILVER",
        "LEED_GOLD",
        "LEED_PLATINUM",
    ]
    leedCertificationException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class SustainableSourcing(typing.TypedDict, total=False):
    ecoFriendlyToiletries: bool
    ecoFriendlyToiletriesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    locallySourcedFoodAndBeverages: bool
    locallySourcedFoodAndBeveragesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    organicCageFreeEggs: bool
    organicCageFreeEggsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    organicFoodAndBeverages: bool
    organicFoodAndBeveragesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    responsiblePurchasingPolicy: bool
    responsiblePurchasingPolicyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    responsiblySourcesSeafood: bool
    responsiblySourcesSeafoodException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    veganMeals: bool
    veganMealsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    vegetarianMeals: bool
    vegetarianMealsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class Transportation(typing.TypedDict, total=False):
    airportShuttle: bool
    airportShuttleException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    carRentalOnProperty: bool
    carRentalOnPropertyException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeAirportShuttle: bool
    freeAirportShuttleException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freePrivateCarService: bool
    freePrivateCarServiceException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    localShuttle: bool
    localShuttleException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    privateCarService: bool
    privateCarServiceException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    transfer: bool
    transferException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class ViewsFromUnit(typing.TypedDict, total=False):
    beachView: bool
    beachViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    cityView: bool
    cityViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    gardenView: bool
    gardenViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    lakeView: bool
    lakeViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    landmarkView: bool
    landmarkViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    oceanView: bool
    oceanViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    poolView: bool
    poolViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    valleyView: bool
    valleyViewException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class WasteReduction(typing.TypedDict, total=False):
    compostableFoodContainersAndCutlery: bool
    compostableFoodContainersAndCutleryException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    compostsExcessFood: bool
    compostsExcessFoodException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    donatesExcessFood: bool
    donatesExcessFoodException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    foodWasteReductionProgram: bool
    foodWasteReductionProgramException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noSingleUsePlasticStraws: bool
    noSingleUsePlasticStrawsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noSingleUsePlasticWaterBottles: bool
    noSingleUsePlasticWaterBottlesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    noStyrofoamFoodContainers: bool
    noStyrofoamFoodContainersException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    recyclingProgram: bool
    recyclingProgramException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    refillableToiletryContainers: bool
    refillableToiletryContainersException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyDisposesBatteries: bool
    safelyDisposesBatteriesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyDisposesElectronics: bool
    safelyDisposesElectronicsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyDisposesLightbulbs: bool
    safelyDisposesLightbulbsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    safelyHandlesHazardousSubstances: bool
    safelyHandlesHazardousSubstancesException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    soapDonationProgram: bool
    soapDonationProgramException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    toiletryDonationProgram: bool
    toiletryDonationProgramException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterBottleFillingStations: bool
    waterBottleFillingStationsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class WaterConservation(typing.TypedDict, total=False):
    independentOrganizationAuditsWaterUse: bool
    independentOrganizationAuditsWaterUseException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    linenReuseProgram: bool
    linenReuseProgramException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    towelReuseProgram: bool
    towelReuseProgramException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSavingShowers: bool
    waterSavingShowersException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSavingSinks: bool
    waterSavingSinksException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    waterSavingToilets: bool
    waterSavingToiletsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]

@typing.type_check_only
class Wellness(typing.TypedDict, total=False):
    doctorOnCall: bool
    doctorOnCallException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    ellipticalMachine: bool
    ellipticalMachineException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    fitnessCenter: bool
    fitnessCenterException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeFitnessCenter: bool
    freeFitnessCenterException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    freeWeights: bool
    freeWeightsException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    massage: bool
    massageException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    salon: bool
    salonException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    sauna: bool
    saunaException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    spa: bool
    spaException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    treadmill: bool
    treadmillException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
    weightMachine: bool
    weightMachineException: typing.Literal[
        "EXCEPTION_UNSPECIFIED",
        "UNDER_CONSTRUCTION",
        "DEPENDENT_ON_SEASON",
        "DEPENDENT_ON_DAY_OF_WEEK",
    ]
