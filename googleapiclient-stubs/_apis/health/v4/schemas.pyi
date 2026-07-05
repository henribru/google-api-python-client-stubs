import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActiveEnergyBurned(typing_extensions.TypedDict, total=False):
    interval: ObservationTimeInterval
    kcal: float

@typing.type_check_only
class ActiveEnergyBurnedRollupValue(typing_extensions.TypedDict, total=False):
    kcalSum: float

@typing.type_check_only
class ActiveMinutes(typing_extensions.TypedDict, total=False):
    activeMinutesByActivityLevel: _list[ActiveMinutesByActivityLevel]
    interval: ObservationTimeInterval

@typing.type_check_only
class ActiveMinutesByActivityLevel(typing_extensions.TypedDict, total=False):
    activeMinutes: str
    activityLevel: typing_extensions.Literal[
        "ACTIVITY_LEVEL_UNSPECIFIED", "LIGHT", "MODERATE", "VIGOROUS"
    ]

@typing.type_check_only
class ActiveMinutesRollupByActivityLevel(typing_extensions.TypedDict, total=False):
    activeMinutesSum: str
    activityLevel: typing_extensions.Literal[
        "ACTIVITY_LEVEL_UNSPECIFIED", "LIGHT", "MODERATE", "VIGOROUS"
    ]

@typing.type_check_only
class ActiveMinutesRollupValue(typing_extensions.TypedDict, total=False):
    activeMinutesRollupByActivityLevel: _list[ActiveMinutesRollupByActivityLevel]

@typing.type_check_only
class ActiveZoneMinutes(typing_extensions.TypedDict, total=False):
    activeZoneMinutes: str
    heartRateZone: typing_extensions.Literal[
        "HEART_RATE_ZONE_UNSPECIFIED", "FAT_BURN", "CARDIO", "PEAK"
    ]
    interval: ObservationTimeInterval

@typing.type_check_only
class ActiveZoneMinutesRollupValue(typing_extensions.TypedDict, total=False):
    sumInCardioHeartZone: str
    sumInFatBurnHeartZone: str
    sumInPeakHeartZone: str

@typing.type_check_only
class ActivityLevel(typing_extensions.TypedDict, total=False):
    activityLevelType: typing_extensions.Literal[
        "ACTIVITY_LEVEL_TYPE_UNSPECIFIED",
        "SEDENTARY",
        "LIGHTLY_ACTIVE",
        "MODERATELY_ACTIVE",
        "VERY_ACTIVE",
    ]
    interval: ObservationTimeInterval

@typing.type_check_only
class ActivityLevelRollupByActivityLevelType(typing_extensions.TypedDict, total=False):
    activityLevelType: typing_extensions.Literal[
        "ACTIVITY_LEVEL_TYPE_UNSPECIFIED",
        "SEDENTARY",
        "LIGHTLY_ACTIVE",
        "MODERATELY_ACTIVE",
        "VERY_ACTIVE",
    ]
    totalDuration: str

@typing.type_check_only
class ActivityLevelRollupValue(typing_extensions.TypedDict, total=False):
    activityLevelRollupsByActivityLevelType: _list[
        ActivityLevelRollupByActivityLevelType
    ]

@typing.type_check_only
class AlertWindow(typing_extensions.TypedDict, total=False):
    civilEndTime: CivilDateTime
    civilStartTime: CivilDateTime
    endTime: str
    endUtcOffset: str
    heartBeats: _list[HeartBeat]
    positive: bool
    startTime: str
    startUtcOffset: str

@typing.type_check_only
class Altitude(typing_extensions.TypedDict, total=False):
    gainMillimeters: str
    interval: ObservationTimeInterval

@typing.type_check_only
class AltitudeRollupValue(typing_extensions.TypedDict, total=False):
    gainMillimetersSum: str

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    googleWebClientId: str
    packageName: str
    webClientId: str

@typing.type_check_only
class BasalEnergyBurned(typing_extensions.TypedDict, total=False):
    interval: ObservationTimeInterval
    kcal: float

@typing.type_check_only
class BatchDeleteDataPointsRequest(typing_extensions.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class BloodGlucose(typing_extensions.TypedDict, total=False):
    bloodGlucoseMilligramsPerDeciliter: float
    mealType: typing_extensions.Literal[
        "MEAL_TYPE_UNSPECIFIED", "BREAKFAST", "LUNCH", "DINNER", "SNACK"
    ]
    measurementSource: typing_extensions.Literal[
        "MEASUREMENT_SOURCE_UNSPECIFIED",
        "SELF_MONITORING_BLOOD_GLUCOSE",
        "CONTINUOUS_GLUCOSE_MONITORING",
        "LAB_TEST",
    ]
    measurementTiming: typing_extensions.Literal[
        "MEASUREMENT_TIMING_UNSPECIFIED",
        "AFTER_MEAL",
        "BEFORE_MEAL",
        "FASTING",
        "GENERAL",
        "BEFORE_BED",
        "OVER_NIGHT",
    ]
    notes: str
    sampleTime: ObservationSampleTime
    specimen: typing_extensions.Literal[
        "SPECIMEN_UNSPECIFIED",
        "CAPILLARY_BLOOD",
        "INTERSTITIAL_FLUID",
        "PLASMA",
        "SERUM",
        "TEARS",
        "WHOLE_BLOOD",
    ]

@typing.type_check_only
class BloodGlucoseRollupValue(typing_extensions.TypedDict, total=False):
    bloodGlucoseMilligramsPerDeciliterAvg: float

@typing.type_check_only
class BodyFat(typing_extensions.TypedDict, total=False):
    percentage: float
    sampleTime: ObservationSampleTime

@typing.type_check_only
class BodyFatRollupValue(typing_extensions.TypedDict, total=False):
    bodyFatPercentageAvg: float

@typing.type_check_only
class CaloriesInHeartRateZoneRollupValue(typing_extensions.TypedDict, total=False):
    caloriesInHeartRateZones: _list[CaloriesInHeartRateZoneValue]

@typing.type_check_only
class CaloriesInHeartRateZoneValue(typing_extensions.TypedDict, total=False):
    heartRateZone: typing_extensions.Literal[
        "HEART_RATE_ZONE_TYPE_UNSPECIFIED", "LIGHT", "MODERATE", "VIGOROUS", "PEAK"
    ]
    kcal: float

@typing.type_check_only
class CivilDateTime(typing_extensions.TypedDict, total=False):
    date: Date
    time: TimeOfDay

@typing.type_check_only
class CivilTimeInterval(typing_extensions.TypedDict, total=False):
    end: CivilDateTime
    start: CivilDateTime

@typing.type_check_only
class CoreBodyTemperature(typing_extensions.TypedDict, total=False):
    id: str
    measurementLocation: typing_extensions.Literal[
        "MEASUREMENT_LOCATION_UNSPECIFIED",
        "OTHER",
        "ARMPIT",
        "BODY",
        "EAR",
        "FINGER",
        "GASTRO_INTESTINAL",
        "MOUTH",
        "RECTUM",
        "TOE",
        "EAR_DRUM",
        "TEMPORAL_ARTERY",
        "FOREHEAD",
        "URINARY_BLADDER",
        "NASAL",
        "NASOPHARYNGEAL",
        "WRIST",
        "VAGINA",
    ]
    sampleTime: ObservationSampleTime
    temperatureCelsius: float

@typing.type_check_only
class CoreBodyTemperatureRollupValue(typing_extensions.TypedDict, total=False):
    temperatureCelsiusAvg: float
    temperatureCelsiusMax: float
    temperatureCelsiusMin: float

@typing.type_check_only
class CreateSubscriberPayload(typing_extensions.TypedDict, total=False):
    endpointAuthorization: EndpointAuthorization
    endpointUri: str
    subscriberConfigs: _list[SubscriberConfig]

@typing.type_check_only
class CreateSubscriptionPayload(typing_extensions.TypedDict, total=False):
    dataTypes: _list[str]
    user: str

@typing.type_check_only
class DailyHeartRateVariability(typing_extensions.TypedDict, total=False):
    averageHeartRateVariabilityMilliseconds: float
    date: Date
    deepSleepRootMeanSquareOfSuccessiveDifferencesMilliseconds: float
    entropy: float
    nonRemHeartRateBeatsPerMinute: str

@typing.type_check_only
class DailyHeartRateZones(typing_extensions.TypedDict, total=False):
    date: Date
    heartRateZones: _list[HeartRateZone]

@typing.type_check_only
class DailyOxygenSaturation(typing_extensions.TypedDict, total=False):
    averagePercentage: float
    date: Date
    lowerBoundPercentage: float
    standardDeviationPercentage: float
    upperBoundPercentage: float

@typing.type_check_only
class DailyRespiratoryRate(typing_extensions.TypedDict, total=False):
    breathsPerMinute: float
    date: Date

@typing.type_check_only
class DailyRestingHeartRate(typing_extensions.TypedDict, total=False):
    beatsPerMinute: str
    dailyRestingHeartRateMetadata: DailyRestingHeartRateMetadata
    date: Date

@typing.type_check_only
class DailyRestingHeartRateMetadata(typing_extensions.TypedDict, total=False):
    calculationMethod: typing_extensions.Literal[
        "CALCULATION_METHOD_UNSPECIFIED", "WITH_SLEEP", "ONLY_WITH_AWAKE_DATA"
    ]

@typing.type_check_only
class DailyRollUpDataPointsRequest(typing_extensions.TypedDict, total=False):
    dataSourceFamily: str
    pageSize: int
    pageToken: str
    range: CivilTimeInterval
    windowSizeDays: int

@typing.type_check_only
class DailyRollUpDataPointsResponse(typing_extensions.TypedDict, total=False):
    rollupDataPoints: _list[DailyRollupDataPoint]

@typing.type_check_only
class DailyRollupDataPoint(typing_extensions.TypedDict, total=False):
    activeEnergyBurned: ActiveEnergyBurnedRollupValue
    activeMinutes: ActiveMinutesRollupValue
    activeZoneMinutes: ActiveZoneMinutesRollupValue
    activityLevel: ActivityLevelRollupValue
    altitude: AltitudeRollupValue
    bloodGlucose: BloodGlucoseRollupValue
    bodyFat: BodyFatRollupValue
    caloriesInHeartRateZone: CaloriesInHeartRateZoneRollupValue
    civilEndTime: CivilDateTime
    civilStartTime: CivilDateTime
    coreBodyTemperature: CoreBodyTemperatureRollupValue
    distance: DistanceRollupValue
    floors: FloorsRollupValue
    heartRate: HeartRateRollupValue
    heartRateVariabilityPersonalRange: HeartRateVariabilityPersonalRangeRollupValue
    hydrationLog: HydrationLogRollupValue
    nutritionLog: NutritionLogRollupValue
    restingHeartRatePersonalRange: RestingHeartRatePersonalRangeRollupValue
    runVo2Max: RunVO2MaxRollupValue
    sedentaryPeriod: SedentaryPeriodRollupValue
    steps: StepsRollupValue
    swimLengthsData: SwimLengthsDataRollupValue
    timeInHeartRateZone: TimeInHeartRateZoneRollupValue
    totalCalories: TotalCaloriesRollupValue
    weight: WeightRollupValue

@typing.type_check_only
class DailySleepTemperatureDerivations(typing_extensions.TypedDict, total=False):
    baselineTemperatureCelsius: float
    date: Date
    nightlyTemperatureCelsius: float
    relativeNightlyStddev30dCelsius: float

@typing.type_check_only
class DailyVO2Max(typing_extensions.TypedDict, total=False):
    cardioFitnessLevel: typing_extensions.Literal[
        "CARDIO_FITNESS_LEVEL_UNSPECIFIED",
        "POOR",
        "FAIR",
        "AVERAGE",
        "GOOD",
        "VERY_GOOD",
        "EXCELLENT",
    ]
    date: Date
    estimated: bool
    vo2Max: float
    vo2MaxCovariance: float

@typing.type_check_only
class DataPoint(typing_extensions.TypedDict, total=False):
    activeEnergyBurned: ActiveEnergyBurned
    activeMinutes: ActiveMinutes
    activeZoneMinutes: ActiveZoneMinutes
    activityLevel: ActivityLevel
    altitude: Altitude
    basalEnergyBurned: BasalEnergyBurned
    bloodGlucose: BloodGlucose
    bodyFat: BodyFat
    coreBodyTemperature: CoreBodyTemperature
    dailyHeartRateVariability: DailyHeartRateVariability
    dailyHeartRateZones: DailyHeartRateZones
    dailyOxygenSaturation: DailyOxygenSaturation
    dailyRespiratoryRate: DailyRespiratoryRate
    dailyRestingHeartRate: DailyRestingHeartRate
    dailySleepTemperatureDerivations: DailySleepTemperatureDerivations
    dailyVo2Max: DailyVO2Max
    dataSource: DataSource
    distance: Distance
    electrocardiogram: Electrocardiogram
    exercise: Exercise
    floors: Floors
    food: Food
    foodMeasurementUnit: FoodMeasurementUnit
    heartRate: HeartRate
    heartRateVariability: HeartRateVariability
    height: Height
    hydrationLog: HydrationLog
    irregularRhythmNotification: IrregularRhythmNotification
    name: str
    nutritionLog: NutritionLog
    oxygenSaturation: OxygenSaturation
    respiratoryRateSleepSummary: RespiratoryRateSleepSummary
    runVo2Max: RunVO2Max
    sedentaryPeriod: SedentaryPeriod
    sleep: Sleep
    steps: Steps
    swimLengthsData: SwimLengthsData
    timeInHeartRateZone: TimeInHeartRateZone
    vo2Max: VO2Max
    weight: Weight

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    application: Application
    device: Device
    platform: typing_extensions.Literal[
        "PLATFORM_UNSPECIFIED",
        "FITBIT",
        "HEALTH_CONNECT",
        "HEALTH_KIT",
        "FIT",
        "FITBIT_WEB_API",
        "NEST",
        "GOOGLE_WEB_API",
        "GOOGLE_PARTNER_INTEGRATION",
    ]
    recordingMethod: typing_extensions.Literal[
        "RECORDING_METHOD_UNSPECIFIED",
        "MANUAL",
        "PASSIVELY_MEASURED",
        "DERIVED",
        "ACTIVELY_MEASURED",
        "UNKNOWN",
    ]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateTime(typing_extensions.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: TimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    displayName: str
    formFactor: typing_extensions.Literal[
        "FORM_FACTOR_UNSPECIFIED",
        "FITNESS_BAND",
        "WATCH",
        "PHONE",
        "RING",
        "CHEST_STRAP",
        "SCALE",
        "TABLET",
        "HEAD_MOUNTED",
        "SMART_DISPLAY",
    ]
    manufacturer: str

@typing.type_check_only
class Distance(typing_extensions.TypedDict, total=False):
    interval: ObservationTimeInterval
    millimeters: str

@typing.type_check_only
class DistanceRollupValue(typing_extensions.TypedDict, total=False):
    millimetersSum: str

@typing.type_check_only
class Electrocardiogram(typing_extensions.TypedDict, total=False):
    beatsPerMinuteAvg: str
    interval: SessionTimeInterval
    leadNumber: int
    medicalDeviceInfo: MedicalDeviceInfo
    millivoltsScalingFactor: int
    resultClassification: typing_extensions.Literal[
        "RESULT_CLASSIFICATION_UNSPECIFIED",
        "NORMAL_SINUS_RHYTHM",
        "ATRIAL_FIBRILLATION",
        "INCONCLUSIVE",
        "INCONCLUSIVE_HIGH_HEART_RATE",
        "INCONCLUSIVE_LOW_HEART_RATE",
        "UNREADABLE",
        "NOT_ANALYZED",
    ]
    samplingFrequencyHertz: int
    waveformSamples: _list[int]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EndpointAuthorization(typing_extensions.TypedDict, total=False):
    secret: str
    secretSet: bool

@typing.type_check_only
class EnergyQuantity(typing_extensions.TypedDict, total=False):
    kcal: float
    userProvidedUnit: typing_extensions.Literal[
        "ENERGY_UNIT_UNSPECIFIED",
        "JOULE",
        "KILOJOULE",
        "KILOCALORIE",
        "SMALL_CALORIE",
        "CALORIE",
    ]

@typing.type_check_only
class EnergyQuantityRollup(typing_extensions.TypedDict, total=False):
    kcalSum: float
    userProvidedUnitLast: typing_extensions.Literal[
        "ENERGY_UNIT_UNSPECIFIED",
        "JOULE",
        "KILOJOULE",
        "KILOCALORIE",
        "SMALL_CALORIE",
        "CALORIE",
    ]

@typing.type_check_only
class Exercise(typing_extensions.TypedDict, total=False):
    activeDuration: str
    createTime: str
    displayName: str
    exerciseEvents: _list[ExerciseEvent]
    exerciseMetadata: ExerciseMetadata
    exerciseType: typing_extensions.Literal[
        "EXERCISE_TYPE_UNSPECIFIED",
        "AEROBIC_WORKOUT",
        "ARCHERY",
        "ASSAULT_BIKE",
        "BACKPACKING",
        "BADMINTON",
        "BALLET",
        "BALLROOM_DANCE",
        "BARRE_CLASS",
        "BASEBALL",
        "BASKETBALL",
        "BIKING",
        "BILLIARDS",
        "BODY_WEIGHT",
        "BOOTCAMP",
        "BOWLING",
        "BOXING",
        "BREAKDANCING",
        "CALISTHENICS",
        "CANOEING",
        "CARDIO_SCULPT",
        "CARDIO_WORKOUT",
        "CARPENTRY",
        "CHEERLEADING",
        "CIRCUIT_TRAINING",
        "CLEANING",
        "CLIMBING",
        "CORE_TRAINING",
        "CRICKET",
        "CROQUET",
        "CROSS_COUNTRY_SKI",
        "CROSS_TRAINING",
        "CROSSFIT",
        "CURLING",
        "DANCING",
        "DIVING",
        "ELECTRIC_BIKE",
        "ELECTRIC_SCOOTER",
        "ELLIPTICAL",
        "EQUESTRIAN_SPORTS",
        "EXERCISE_CLASS",
        "FENCING",
        "FIELD_HOCKEY",
        "FISHING",
        "FITNESS_GAMING",
        "FOILING",
        "FOOTBALL_AMERICAN",
        "FOOTBALL_AUSTRALIAN",
        "FREE_WEIGHTS",
        "FRISBEE_PLAYING_GENERAL",
        "FUNCTIONAL_STRENGTH_TRAINING",
        "GARDENING",
        "GOLF",
        "GYMNASTICS",
        "HANDBALL",
        "HAND_CYCLING",
        "HIIT",
        "HIKING",
        "HIP_HOP",
        "HOCKEY",
        "HOEING",
        "HOUSEHOLD_CHORES",
        "HUNTING",
        "ICE_SKATING",
        "INCLINE_RUN",
        "INCLINE_WALK",
        "INDOOR_CLIMBING",
        "INTERVAL_WORKOUT",
        "JAZZ_DANCE",
        "JIU_JITSU",
        "JUMPING_ROPE",
        "KARATE",
        "KAYAKING",
        "KICKBOXING",
        "KITESURFING",
        "LACROSSE",
        "MARTIAL_ARTS",
        "MEDITATE",
        "MODERN_DANCE",
        "MOTOCROSS",
        "MOTORCYCLE",
        "MOUNTAIN_BIKE",
        "MOWING_LAWN",
        "MUAY_THAI",
        "MULTISPORT",
        "MUSICAL_PERFORMANCE",
        "NORDIC_WALKING",
        "ORIENTEERING",
        "OTHER",
        "OUTDOOR_BIKE",
        "OUTDOOR_WORKOUT",
        "PADDLEBOARDING",
        "PADEL",
        "PAINTING",
        "PARAGLIDING",
        "PARKOUR",
        "PICKELBALL",
        "PILATES",
        "POLO",
        "POWERLIFTING",
        "POWER_WALKING",
        "RACKET_SPORTS",
        "RACQUETBALL",
        "RESISTANCE_BANDS",
        "ROCK_CLIMBING",
        "ROLLERBLADING",
        "ROLLER_SKATING",
        "ROWING",
        "ROWING_MACHINE",
        "RUCKING",
        "RUGBY",
        "RUNNING",
        "SAILING",
        "SCOOTERING",
        "SCUBA_DIVING",
        "SHOOTING",
        "SHOVELING",
        "SKATEBOARDING",
        "SKATING",
        "SKIING",
        "SKYDIVING",
        "SNORKELING",
        "SNOWBOARDING",
        "SNOWMOBILING",
        "SNOWSHOEING",
        "SNOW_SPORT",
        "SOCCER",
        "SOFTBALL",
        "SPEED_SKATING",
        "SPINNING",
        "SPORT",
        "SQUASH",
        "STAIRCLIMBER",
        "STATIONARY_BIKE",
        "STEP_TRAINING",
        "STRENGTH_TRAINING",
        "STRETCHING",
        "STROLLER_WALK",
        "SURFING",
        "SWIMMING",
        "SWIMMING_OPEN_WATER",
        "SWIMMING_POOL",
        "SYNCHRONIZED_SWIMMING",
        "TABATA_WORKOUT",
        "TABLE_TENNIS",
        "TAEKWONDO",
        "TAI_CHI",
        "TANGO",
        "TENNIS",
        "TRACK_AND_FIELD",
        "TRAIL_RUN",
        "TRAMPOLINE",
        "TREADMILL",
        "TREADMILL_WALK",
        "TRX",
        "ULTIMATE_FRISBEE",
        "UNICYCLING",
        "VOLLEYBALL",
        "VOLLEYBALL_BEACH",
        "WAKEBOARDING",
        "WALKING",
        "WALK_WITH_WEIGHTS",
        "WATER_AEROBICS",
        "WATER_JOGGING",
        "WATER_POLO",
        "WATER_SKIING",
        "WATER_SPORT",
        "WATER_VOLLEYBALL",
        "WEEDING",
        "WEIGHTLIFTING",
        "WEIGHT_MACHINES",
        "WEIGHTS",
        "WHEELCHAIR",
        "WINDSURFING",
        "WORKOUT",
        "WRESTLING",
        "YOGA",
        "YOGA_BIKRAM",
        "YOGA_HATHA",
        "YOGA_POWER",
        "YOGA_VINYASA",
        "ZUMBA",
    ]
    interval: SessionTimeInterval
    metricsSummary: MetricsSummary
    notes: str
    splitSummaries: _list[SplitSummary]
    splits: _list[SplitSummary]
    updateTime: str

@typing.type_check_only
class ExerciseEvent(typing_extensions.TypedDict, total=False):
    eventTime: str
    eventUtcOffset: str
    exerciseEventType: typing_extensions.Literal[
        "EXERCISE_EVENT_TYPE_UNSPECIFIED",
        "START",
        "STOP",
        "PAUSE",
        "RESUME",
        "AUTO_PAUSE",
        "AUTO_RESUME",
    ]

@typing.type_check_only
class ExerciseMetadata(typing_extensions.TypedDict, total=False):
    hasGps: bool
    poolLengthMillimeters: str

@typing.type_check_only
class ExportExerciseTcxResponse(typing_extensions.TypedDict, total=False):
    tcxData: str

@typing.type_check_only
class Floors(typing_extensions.TypedDict, total=False):
    count: str
    interval: ObservationTimeInterval

@typing.type_check_only
class FloorsRollupValue(typing_extensions.TypedDict, total=False):
    countSum: str

@typing.type_check_only
class Food(typing_extensions.TypedDict, total=False):
    accessLevel: typing_extensions.Literal[
        "FOOD_ACCESS_LEVEL_UNSPECIFIED",
        "FOOD_ACCESS_LEVEL_PUBLIC",
        "FOOD_ACCESS_LEVEL_PRIVATE",
    ]
    brand: str
    defaultServing: FoodServing
    description: str
    displayName: str
    energyAvg: EnergyQuantity
    energyFromFat: EnergyQuantity
    energyMax: EnergyQuantity
    energyMin: EnergyQuantity
    languageCode: str
    mealType: typing_extensions.Literal[
        "MEAL_TYPE_UNSPECIFIED",
        "BEFORE_BREAKFAST",
        "BREAKFAST",
        "BEFORE_LUNCH",
        "LUNCH",
        "BEFORE_DINNER",
        "DINNER",
        "AFTER_DINNER",
        "SNACK",
        "ANYTIME",
    ]
    nutrients: _list[NutrientQuantity]
    servings: _list[FoodServing]
    totalCarbohydrate: WeightQuantity
    totalFat: WeightQuantity

@typing.type_check_only
class FoodMeasurementUnit(typing_extensions.TypedDict, total=False):
    displayName: str
    pluralDisplayName: str

@typing.type_check_only
class FoodServing(typing_extensions.TypedDict, total=False):
    amount: float
    foodMeasurementUnit: str
    foodMeasurementUnitDisplayName: str
    foodMeasurementUnitDisplayNamePlural: str
    multiplier: float

@typing.type_check_only
class GoogleDevicesandservicesHealthV4DataType(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleDevicesandservicesHealthV4User(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleDevicesandservicesHealthV4WebhookNotificationCloudLog(
    typing_extensions.TypedDict, total=False
):
    httpResponse: HttpResponse

@typing.type_check_only
class HeartBeat(typing_extensions.TypedDict, total=False):
    beatsPerMinute: int
    civilTime: CivilDateTime
    physicalTime: str
    utcOffset: str

@typing.type_check_only
class HeartRate(typing_extensions.TypedDict, total=False):
    beatsPerMinute: str
    metadata: HeartRateMetadata
    sampleTime: ObservationSampleTime

@typing.type_check_only
class HeartRateMetadata(typing_extensions.TypedDict, total=False):
    motionContext: typing_extensions.Literal[
        "MOTION_CONTEXT_UNSPECIFIED", "ACTIVE", "SEDENTARY"
    ]
    sensorLocation: typing_extensions.Literal[
        "SENSOR_LOCATION_UNSPECIFIED",
        "CHEST",
        "WRIST",
        "FINGER",
        "HAND",
        "EAR_LOBE",
        "FOOT",
    ]

@typing.type_check_only
class HeartRateRollupValue(typing_extensions.TypedDict, total=False):
    beatsPerMinuteAvg: float
    beatsPerMinuteMax: float
    beatsPerMinuteMin: float

@typing.type_check_only
class HeartRateVariability(typing_extensions.TypedDict, total=False):
    rootMeanSquareOfSuccessiveDifferencesMilliseconds: float
    sampleTime: ObservationSampleTime
    standardDeviationMilliseconds: float

@typing.type_check_only
class HeartRateVariabilityPersonalRangeRollupValue(
    typing_extensions.TypedDict, total=False
):
    averageHeartRateVariabilityMillisecondsMax: float
    averageHeartRateVariabilityMillisecondsMin: float

@typing.type_check_only
class HeartRateZone(typing_extensions.TypedDict, total=False):
    heartRateZoneType: typing_extensions.Literal[
        "HEART_RATE_ZONE_TYPE_UNSPECIFIED", "LIGHT", "MODERATE", "VIGOROUS", "PEAK"
    ]
    maxBeatsPerMinute: str
    minBeatsPerMinute: str

@typing.type_check_only
class Height(typing_extensions.TypedDict, total=False):
    heightMillimeters: str
    sampleTime: ObservationSampleTime

@typing.type_check_only
class HttpHeader(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class HttpResponse(typing_extensions.TypedDict, total=False):
    body: str
    headers: _list[HttpHeader]
    reason: str
    status: int

@typing.type_check_only
class HydrationLog(typing_extensions.TypedDict, total=False):
    amountConsumed: VolumeQuantity
    interval: SessionTimeInterval

@typing.type_check_only
class HydrationLogRollupValue(typing_extensions.TypedDict, total=False):
    amountConsumed: VolumeQuantityRollup

@typing.type_check_only
class Identity(typing_extensions.TypedDict, total=False):
    healthUserId: str
    legacyUserId: str
    name: str

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class IrnProfile(typing_extensions.TypedDict, total=False):
    enrollmentStatus: bool
    name: str
    onboardingStatus: bool
    updateTime: str

@typing.type_check_only
class IrregularRhythmNotification(typing_extensions.TypedDict, total=False):
    alertWindows: _list[AlertWindow]
    interval: SessionTimeInterval
    medicalDeviceInfo: MedicalDeviceInfo

@typing.type_check_only
class ListDataPointsResponse(typing_extensions.TypedDict, total=False):
    dataPoints: _list[DataPoint]
    nextPageToken: str

@typing.type_check_only
class ListPairedDevicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    pairedDevices: _list[PairedDevice]

@typing.type_check_only
class ListSubscribersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscribers: _list[Subscriber]
    totalSize: int

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class MedicalDeviceInfo(typing_extensions.TypedDict, total=False):
    algorithmVersion: str
    deviceModel: str
    featureVersion: str
    firmwareVersion: str
    serviceVersion: str

@typing.type_check_only
class MetricsSummary(typing_extensions.TypedDict, total=False):
    activeZoneMinutes: str
    averageHeartRateBeatsPerMinute: str
    averagePaceSecondsPerMeter: float
    averageSpeedMillimetersPerSecond: float
    caloriesKcal: float
    distanceMillimeters: float
    elevationGainMillimeters: float
    heartRateZoneDurations: TimeInHeartRateZones
    mobilityMetrics: MobilityMetrics
    runVo2Max: float
    steps: str
    totalSwimLengths: float

@typing.type_check_only
class MobilityMetrics(typing_extensions.TypedDict, total=False):
    avgCadenceStepsPerMinute: float
    avgGroundContactTimeDuration: str
    avgStrideLengthMillimeters: str
    avgVerticalOscillationMillimeters: str
    avgVerticalRatio: float

@typing.type_check_only
class NutrientQuantity(typing_extensions.TypedDict, total=False):
    nutrient: typing_extensions.Literal[
        "NUTRIENT_UNSPECIFIED",
        "BIOTIN",
        "CAFFEINE",
        "CALCIUM",
        "CHLORIDE",
        "CARBOHYDRATES",
        "CHOLESTEROL",
        "CHROMIUM",
        "COPPER",
        "DIETARY_FIBER",
        "FOLIC_ACID",
        "IODINE",
        "IRON",
        "MAGNESIUM",
        "MANGANESE",
        "MOLYBDENUM",
        "MONOUNSATURATED_FAT",
        "NIACIN",
        "PANTOTHENIC_ACID",
        "PHOSPHORUS",
        "POLYUNSATURATED_FAT",
        "POTASSIUM",
        "PROTEIN",
        "RIBOFLAVIN",
        "SATURATED_FAT",
        "SELENIUM",
        "SODIUM",
        "SUGAR",
        "THIAMIN",
        "TRANS_FAT",
        "UNSATURATED_FAT",
        "VITAMIN_A",
        "VITAMIN_B12",
        "VITAMIN_B6",
        "VITAMIN_C",
        "VITAMIN_D",
        "VITAMIN_E",
        "VITAMIN_K",
        "ZINC",
        "FOLATE",
    ]
    quantity: WeightQuantity

@typing.type_check_only
class NutrientQuantityRollup(typing_extensions.TypedDict, total=False):
    nutrient: typing_extensions.Literal[
        "NUTRIENT_UNSPECIFIED",
        "BIOTIN",
        "CAFFEINE",
        "CALCIUM",
        "CHLORIDE",
        "CARBOHYDRATES",
        "CHOLESTEROL",
        "CHROMIUM",
        "COPPER",
        "DIETARY_FIBER",
        "FOLIC_ACID",
        "IODINE",
        "IRON",
        "MAGNESIUM",
        "MANGANESE",
        "MOLYBDENUM",
        "MONOUNSATURATED_FAT",
        "NIACIN",
        "PANTOTHENIC_ACID",
        "PHOSPHORUS",
        "POLYUNSATURATED_FAT",
        "POTASSIUM",
        "PROTEIN",
        "RIBOFLAVIN",
        "SATURATED_FAT",
        "SELENIUM",
        "SODIUM",
        "SUGAR",
        "THIAMIN",
        "TRANS_FAT",
        "UNSATURATED_FAT",
        "VITAMIN_A",
        "VITAMIN_B12",
        "VITAMIN_B6",
        "VITAMIN_C",
        "VITAMIN_D",
        "VITAMIN_E",
        "VITAMIN_K",
        "ZINC",
        "FOLATE",
    ]
    quantity: WeightQuantityRollup

@typing.type_check_only
class NutritionLog(typing_extensions.TypedDict, total=False):
    energy: EnergyQuantity
    energyFromFat: EnergyQuantity
    food: str
    foodDisplayName: str
    interval: SessionTimeInterval
    mealType: typing_extensions.Literal[
        "MEAL_TYPE_UNSPECIFIED",
        "BEFORE_BREAKFAST",
        "BREAKFAST",
        "BEFORE_LUNCH",
        "LUNCH",
        "BEFORE_DINNER",
        "DINNER",
        "AFTER_DINNER",
        "SNACK",
        "ANYTIME",
    ]
    nutrients: _list[NutrientQuantity]
    serving: Serving
    totalCarbohydrate: WeightQuantity
    totalFat: WeightQuantity

@typing.type_check_only
class NutritionLogRollupValue(typing_extensions.TypedDict, total=False):
    energy: EnergyQuantityRollup
    energyFromFat: EnergyQuantityRollup
    nutrients: _list[NutrientQuantityRollup]
    totalCarbohydrate: WeightQuantityRollup
    totalFat: WeightQuantityRollup

@typing.type_check_only
class ObservationSampleTime(typing_extensions.TypedDict, total=False):
    civilTime: CivilDateTime
    physicalTime: str
    utcOffset: str

@typing.type_check_only
class ObservationTimeInterval(typing_extensions.TypedDict, total=False):
    civilEndTime: CivilDateTime
    civilStartTime: CivilDateTime
    endTime: str
    endUtcOffset: str
    startTime: str
    startUtcOffset: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OutOfBedSegment(typing_extensions.TypedDict, total=False):
    endTime: str
    endUtcOffset: str
    startTime: str
    startUtcOffset: str

@typing.type_check_only
class OxygenSaturation(typing_extensions.TypedDict, total=False):
    percentage: float
    sampleTime: ObservationSampleTime

@typing.type_check_only
class PairedDevice(typing_extensions.TypedDict, total=False):
    batteryLevel: int
    batteryStatus: str
    deviceType: typing_extensions.Literal["DEVICE_TYPE_UNSPECIFIED", "TRACKER", "SCALE"]
    deviceVersion: str
    features: _list[str]
    lastSyncTime: str
    macAddress: str
    name: str

@typing.type_check_only
class Profile(typing_extensions.TypedDict, total=False):
    age: int
    autoRunningStrideLengthMm: int
    autoWalkingStrideLengthMm: int
    membershipStartDate: Date
    name: str
    userConfiguredRunningStrideLengthMm: int
    userConfiguredWalkingStrideLengthMm: int

@typing.type_check_only
class ReconcileDataPointsResponse(typing_extensions.TypedDict, total=False):
    dataPoints: _list[ReconciledDataPoint]
    nextPageToken: str

@typing.type_check_only
class ReconciledDataPoint(typing_extensions.TypedDict, total=False):
    activeEnergyBurned: ActiveEnergyBurned
    activeMinutes: ActiveMinutes
    activeZoneMinutes: ActiveZoneMinutes
    activityLevel: ActivityLevel
    altitude: Altitude
    basalEnergyBurned: BasalEnergyBurned
    bloodGlucose: BloodGlucose
    bodyFat: BodyFat
    coreBodyTemperature: CoreBodyTemperature
    dailyHeartRateVariability: DailyHeartRateVariability
    dailyHeartRateZones: DailyHeartRateZones
    dailyOxygenSaturation: DailyOxygenSaturation
    dailyRespiratoryRate: DailyRespiratoryRate
    dailyRestingHeartRate: DailyRestingHeartRate
    dailySleepTemperatureDerivations: DailySleepTemperatureDerivations
    dailyVo2Max: DailyVO2Max
    dataPointName: str
    distance: Distance
    exercise: Exercise
    floors: Floors
    heartRate: HeartRate
    heartRateVariability: HeartRateVariability
    height: Height
    hydrationLog: HydrationLog
    nutritionLog: NutritionLog
    oxygenSaturation: OxygenSaturation
    respiratoryRateSleepSummary: RespiratoryRateSleepSummary
    runVo2Max: RunVO2Max
    sedentaryPeriod: SedentaryPeriod
    sleep: Sleep
    steps: Steps
    swimLengthsData: SwimLengthsData
    timeInHeartRateZone: TimeInHeartRateZone
    vo2Max: VO2Max
    weight: Weight

@typing.type_check_only
class RespiratoryRateSleepSummary(typing_extensions.TypedDict, total=False):
    deepSleepStats: RespiratoryRateSleepSummaryStatistics
    fullSleepStats: RespiratoryRateSleepSummaryStatistics
    lightSleepStats: RespiratoryRateSleepSummaryStatistics
    remSleepStats: RespiratoryRateSleepSummaryStatistics
    sampleTime: ObservationSampleTime

@typing.type_check_only
class RespiratoryRateSleepSummaryStatistics(typing_extensions.TypedDict, total=False):
    breathsPerMinute: float
    signalToNoise: float
    standardDeviation: float

@typing.type_check_only
class RestingHeartRatePersonalRangeRollupValue(
    typing_extensions.TypedDict, total=False
):
    beatsPerMinuteMax: float
    beatsPerMinuteMin: float

@typing.type_check_only
class RollUpDataPointsRequest(typing_extensions.TypedDict, total=False):
    dataSourceFamily: str
    pageSize: int
    pageToken: str
    range: Interval
    windowSize: str

@typing.type_check_only
class RollUpDataPointsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rollupDataPoints: _list[RollupDataPoint]

@typing.type_check_only
class RollupDataPoint(typing_extensions.TypedDict, total=False):
    activeEnergyBurned: ActiveEnergyBurnedRollupValue
    activeMinutes: ActiveMinutesRollupValue
    activeZoneMinutes: ActiveZoneMinutesRollupValue
    activityLevel: ActivityLevelRollupValue
    altitude: AltitudeRollupValue
    bloodGlucose: BloodGlucoseRollupValue
    bodyFat: BodyFatRollupValue
    caloriesInHeartRateZone: CaloriesInHeartRateZoneRollupValue
    coreBodyTemperature: CoreBodyTemperatureRollupValue
    distance: DistanceRollupValue
    endTime: str
    floors: FloorsRollupValue
    heartRate: HeartRateRollupValue
    hydrationLog: HydrationLogRollupValue
    nutritionLog: NutritionLogRollupValue
    runVo2Max: RunVO2MaxRollupValue
    sedentaryPeriod: SedentaryPeriodRollupValue
    startTime: str
    steps: StepsRollupValue
    swimLengthsData: SwimLengthsDataRollupValue
    timeInHeartRateZone: TimeInHeartRateZoneRollupValue
    totalCalories: TotalCaloriesRollupValue
    weight: WeightRollupValue

@typing.type_check_only
class RunVO2Max(typing_extensions.TypedDict, total=False):
    runVo2Max: float
    sampleTime: ObservationSampleTime

@typing.type_check_only
class RunVO2MaxRollupValue(typing_extensions.TypedDict, total=False):
    rateAvg: float
    rateMax: float
    rateMin: float

@typing.type_check_only
class SedentaryPeriod(typing_extensions.TypedDict, total=False):
    interval: ObservationTimeInterval

@typing.type_check_only
class SedentaryPeriodRollupValue(typing_extensions.TypedDict, total=False):
    durationSum: str

@typing.type_check_only
class Serving(typing_extensions.TypedDict, total=False):
    amount: float
    foodMeasurementUnit: str
    foodMeasurementUnitDisplayName: str

@typing.type_check_only
class SessionTimeInterval(typing_extensions.TypedDict, total=False):
    civilEndTime: CivilDateTime
    civilStartTime: CivilDateTime
    endTime: str
    endUtcOffset: str
    startTime: str
    startUtcOffset: str

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    autoStrideEnabled: bool
    distanceUnit: typing_extensions.Literal[
        "DISTANCE_UNIT_UNSPECIFIED", "DISTANCE_UNIT_MILES", "DISTANCE_UNIT_KILOMETERS"
    ]
    foodLanguageCode: str
    glucoseUnit: typing_extensions.Literal[
        "GLUCOSE_UNIT_UNSPECIFIED", "GLUCOSE_UNIT_MG_DL", "GLUCOSE_UNIT_MMOL_L"
    ]
    heightUnit: typing_extensions.Literal[
        "HEIGHT_UNIT_UNSPECIFIED", "HEIGHT_UNIT_INCHES", "HEIGHT_UNIT_CENTIMETERS"
    ]
    languageLocale: str
    name: str
    strideLengthRunningType: typing_extensions.Literal[
        "STRIDE_LENGTH_TYPE_UNSPECIFIED",
        "STRIDE_LENGTH_TYPE_DEFAULT",
        "STRIDE_LENGTH_TYPE_MANUAL",
        "STRIDE_LENGTH_TYPE_AUTO",
    ]
    strideLengthWalkingType: typing_extensions.Literal[
        "STRIDE_LENGTH_TYPE_UNSPECIFIED",
        "STRIDE_LENGTH_TYPE_DEFAULT",
        "STRIDE_LENGTH_TYPE_MANUAL",
        "STRIDE_LENGTH_TYPE_AUTO",
    ]
    swimUnit: typing_extensions.Literal[
        "SWIM_UNIT_UNSPECIFIED", "SWIM_UNIT_METERS", "SWIM_UNIT_YARDS"
    ]
    temperatureUnit: typing_extensions.Literal[
        "TEMPERATURE_UNIT_UNSPECIFIED",
        "TEMPERATURE_UNIT_CELSIUS",
        "TEMPERATURE_UNIT_FAHRENHEIT",
    ]
    timeZone: str
    utcOffset: str
    waterUnit: typing_extensions.Literal[
        "WATER_UNIT_UNSPECIFIED", "WATER_UNIT_ML", "WATER_UNIT_FL_OZ", "WATER_UNIT_CUP"
    ]
    weightUnit: typing_extensions.Literal[
        "WEIGHT_UNIT_UNSPECIFIED",
        "WEIGHT_UNIT_POUNDS",
        "WEIGHT_UNIT_STONE",
        "WEIGHT_UNIT_KILOGRAMS",
    ]

@typing.type_check_only
class Sleep(typing_extensions.TypedDict, total=False):
    createTime: str
    interval: SessionTimeInterval
    metadata: SleepMetadata
    outOfBedSegments: _list[OutOfBedSegment]
    stages: _list[SleepStage]
    summary: SleepSummary
    type: typing_extensions.Literal["SLEEP_TYPE_UNSPECIFIED", "CLASSIC", "STAGES"]
    updateTime: str

@typing.type_check_only
class SleepMetadata(typing_extensions.TypedDict, total=False):
    externalId: str
    manuallyEdited: bool
    nap: bool
    processed: bool
    stagesStatus: typing_extensions.Literal[
        "STAGES_STATE_UNSPECIFIED",
        "REJECTED_COVERAGE",
        "REJECTED_MAX_GAP",
        "REJECTED_START_GAP",
        "REJECTED_END_GAP",
        "REJECTED_NAP",
        "REJECTED_SERVER",
        "TIMEOUT",
        "SUCCEEDED",
        "PROCESSING_INTERNAL_ERROR",
    ]

@typing.type_check_only
class SleepStage(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    endUtcOffset: str
    startTime: str
    startUtcOffset: str
    type: typing_extensions.Literal[
        "SLEEP_STAGE_TYPE_UNSPECIFIED",
        "AWAKE",
        "LIGHT",
        "DEEP",
        "REM",
        "ASLEEP",
        "RESTLESS",
    ]
    updateTime: str

@typing.type_check_only
class SleepSummary(typing_extensions.TypedDict, total=False):
    minutesAfterWakeUp: str
    minutesAsleep: str
    minutesAwake: str
    minutesInSleepPeriod: str
    minutesToFallAsleep: str
    stagesSummary: _list[StageSummary]

@typing.type_check_only
class SplitSummary(typing_extensions.TypedDict, total=False):
    activeDuration: str
    endTime: str
    endUtcOffset: str
    metricsSummary: MetricsSummary
    splitType: typing_extensions.Literal[
        "SPLIT_TYPE_UNSPECIFIED", "MANUAL", "DURATION", "DISTANCE", "CALORIES"
    ]
    startTime: str
    startUtcOffset: str

@typing.type_check_only
class StageSummary(typing_extensions.TypedDict, total=False):
    count: str
    minutes: str
    type: typing_extensions.Literal[
        "SLEEP_STAGE_TYPE_UNSPECIFIED",
        "AWAKE",
        "LIGHT",
        "DEEP",
        "REM",
        "ASLEEP",
        "RESTLESS",
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Steps(typing_extensions.TypedDict, total=False):
    count: str
    interval: ObservationTimeInterval

@typing.type_check_only
class StepsRollupValue(typing_extensions.TypedDict, total=False):
    countSum: str

@typing.type_check_only
class Subscriber(typing_extensions.TypedDict, total=False):
    createTime: str
    endpointAuthorization: EndpointAuthorization
    endpointUri: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNVERIFIED", "ACTIVE", "INACTIVE"
    ]
    subscriberConfigs: _list[SubscriberConfig]
    updateTime: str

@typing.type_check_only
class SubscriberConfig(typing_extensions.TypedDict, total=False):
    dataTypes: _list[str]
    subscriptionCreatePolicy: typing_extensions.Literal[
        "SUBSCRIPTION_CREATE_POLICY_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    dataTypes: _list[str]
    name: str
    user: str

@typing.type_check_only
class SwimLengthsData(typing_extensions.TypedDict, total=False):
    interval: ObservationTimeInterval
    strokeCount: str
    swimStrokeType: typing_extensions.Literal[
        "SWIM_STROKE_TYPE_UNSPECIFIED",
        "FREESTYLE",
        "BACKSTROKE",
        "BREASTSTROKE",
        "BUTTERFLY",
    ]

@typing.type_check_only
class SwimLengthsDataRollupValue(typing_extensions.TypedDict, total=False):
    strokeCountSum: str

@typing.type_check_only
class TimeInHeartRateZone(typing_extensions.TypedDict, total=False):
    heartRateZoneType: typing_extensions.Literal[
        "HEART_RATE_ZONE_TYPE_UNSPECIFIED", "LIGHT", "MODERATE", "VIGOROUS", "PEAK"
    ]
    interval: ObservationTimeInterval

@typing.type_check_only
class TimeInHeartRateZoneRollupValue(typing_extensions.TypedDict, total=False):
    timeInHeartRateZones: _list[TimeInHeartRateZoneValue]

@typing.type_check_only
class TimeInHeartRateZoneValue(typing_extensions.TypedDict, total=False):
    duration: str
    heartRateZone: typing_extensions.Literal[
        "HEART_RATE_ZONE_TYPE_UNSPECIFIED", "LIGHT", "MODERATE", "VIGOROUS", "PEAK"
    ]

@typing.type_check_only
class TimeInHeartRateZones(typing_extensions.TypedDict, total=False):
    lightTime: str
    moderateTime: str
    peakTime: str
    vigorousTime: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class TotalCaloriesRollupValue(typing_extensions.TypedDict, total=False):
    kcalSum: float

@typing.type_check_only
class VO2Max(typing_extensions.TypedDict, total=False):
    measurementMethod: typing_extensions.Literal[
        "MEASUREMENT_METHOD_UNSPECIFIED",
        "FITBIT_RUN",
        "GOOGLE_DEMOGRAPHIC",
        "COOPER_TEST",
        "HEART_RATE_RATIO",
        "METABOLIC_CART",
        "MULTISTAGE_FITNESS_TEST",
        "ROCKPORT_FITNESS_TEST",
        "MAX_EXERCISE",
        "PREDICTION_SUB_MAX_EXERCISE",
        "PREDICTION_NON_EXERCISE",
        "OTHER",
    ]
    sampleTime: ObservationSampleTime
    vo2Max: float

@typing.type_check_only
class VolumeQuantity(typing_extensions.TypedDict, total=False):
    milliliters: float
    userProvidedUnit: typing_extensions.Literal[
        "VOLUME_UNIT_UNSPECIFIED",
        "CUP_IMPERIAL",
        "CUP_US",
        "FLUID_OUNCE_IMPERIAL",
        "FLUID_OUNCE_US",
        "LITER",
        "MILLILITER",
        "PINT_IMPERIAL",
        "PINT_US",
    ]

@typing.type_check_only
class VolumeQuantityRollup(typing_extensions.TypedDict, total=False):
    millilitersSum: float
    userProvidedUnitLast: typing_extensions.Literal[
        "VOLUME_UNIT_UNSPECIFIED",
        "CUP_IMPERIAL",
        "CUP_US",
        "FLUID_OUNCE_IMPERIAL",
        "FLUID_OUNCE_US",
        "LITER",
        "MILLILITER",
        "PINT_IMPERIAL",
        "PINT_US",
    ]

@typing.type_check_only
class Weight(typing_extensions.TypedDict, total=False):
    notes: str
    sampleTime: ObservationSampleTime
    weightGrams: float

@typing.type_check_only
class WeightQuantity(typing_extensions.TypedDict, total=False):
    grams: float
    userProvidedUnit: typing_extensions.Literal[
        "WEIGHT_UNIT_UNSPECIFIED",
        "GRAM",
        "KILOGRAM",
        "OUNCE",
        "POUND",
        "STONE",
        "MILLIGRAM",
        "MICROGRAM",
        "NANOGRAM",
    ]

@typing.type_check_only
class WeightQuantityRollup(typing_extensions.TypedDict, total=False):
    gramsSum: float
    userProvidedUnitLast: typing_extensions.Literal[
        "WEIGHT_UNIT_UNSPECIFIED",
        "GRAM",
        "KILOGRAM",
        "OUNCE",
        "POUND",
        "STONE",
        "MILLIGRAM",
        "MICROGRAM",
        "NANOGRAM",
    ]

@typing.type_check_only
class WeightRollupValue(typing_extensions.TypedDict, total=False):
    weightGramsAvg: float
