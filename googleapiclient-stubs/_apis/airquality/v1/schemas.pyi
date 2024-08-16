import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdditionalInfo(typing_extensions.TypedDict, total=False):
    effects: str
    sources: str

@typing.type_check_only
class AirQualityIndex(typing_extensions.TypedDict, total=False):
    aqi: int
    aqiDisplay: str
    category: str
    code: str
    color: Color
    displayName: str
    dominantPollutant: str

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class Concentration(typing_extensions.TypedDict, total=False):
    units: typing_extensions.Literal[
        "UNIT_UNSPECIFIED", "PARTS_PER_BILLION", "MICROGRAMS_PER_CUBIC_METER"
    ]
    value: float

@typing.type_check_only
class CustomLocalAqi(typing_extensions.TypedDict, total=False):
    aqi: str
    regionCode: str

@typing.type_check_only
class HealthRecommendations(typing_extensions.TypedDict, total=False):
    athletes: str
    children: str
    elderly: str
    generalPopulation: str
    heartDiseasePopulation: str
    lungDiseasePopulation: str
    pregnantWomen: str

@typing.type_check_only
class HourInfo(typing_extensions.TypedDict, total=False):
    dateTime: str
    healthRecommendations: HealthRecommendations
    indexes: _list[AirQualityIndex]
    pollutants: _list[Pollutant]

@typing.type_check_only
class HourlyForecast(typing_extensions.TypedDict, total=False):
    dateTime: str
    healthRecommendations: HealthRecommendations
    indexes: _list[AirQualityIndex]
    pollutants: _list[Pollutant]

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LookupCurrentConditionsRequest(typing_extensions.TypedDict, total=False):
    customLocalAqis: _list[CustomLocalAqi]
    extraComputations: _list[
        typing_extensions.Literal[
            "EXTRA_COMPUTATION_UNSPECIFIED",
            "LOCAL_AQI",
            "HEALTH_RECOMMENDATIONS",
            "POLLUTANT_ADDITIONAL_INFO",
            "DOMINANT_POLLUTANT_CONCENTRATION",
            "POLLUTANT_CONCENTRATION",
        ]
    ]
    languageCode: str
    location: LatLng
    uaqiColorPalette: typing_extensions.Literal[
        "COLOR_PALETTE_UNSPECIFIED",
        "RED_GREEN",
        "INDIGO_PERSIAN_DARK",
        "INDIGO_PERSIAN_LIGHT",
    ]
    universalAqi: bool

@typing.type_check_only
class LookupCurrentConditionsResponse(typing_extensions.TypedDict, total=False):
    dateTime: str
    healthRecommendations: HealthRecommendations
    indexes: _list[AirQualityIndex]
    pollutants: _list[Pollutant]
    regionCode: str

@typing.type_check_only
class LookupForecastRequest(typing_extensions.TypedDict, total=False):
    customLocalAqis: _list[CustomLocalAqi]
    dateTime: str
    extraComputations: _list[
        typing_extensions.Literal[
            "EXTRA_COMPUTATION_UNSPECIFIED",
            "LOCAL_AQI",
            "HEALTH_RECOMMENDATIONS",
            "POLLUTANT_ADDITIONAL_INFO",
            "DOMINANT_POLLUTANT_CONCENTRATION",
            "POLLUTANT_CONCENTRATION",
        ]
    ]
    languageCode: str
    location: LatLng
    pageSize: int
    pageToken: str
    period: Interval
    uaqiColorPalette: typing_extensions.Literal[
        "COLOR_PALETTE_UNSPECIFIED",
        "RED_GREEN",
        "INDIGO_PERSIAN_DARK",
        "INDIGO_PERSIAN_LIGHT",
    ]
    universalAqi: bool

@typing.type_check_only
class LookupForecastResponse(typing_extensions.TypedDict, total=False):
    hourlyForecasts: _list[HourlyForecast]
    nextPageToken: str
    regionCode: str

@typing.type_check_only
class LookupHistoryRequest(typing_extensions.TypedDict, total=False):
    customLocalAqis: _list[CustomLocalAqi]
    dateTime: str
    extraComputations: _list[
        typing_extensions.Literal[
            "EXTRA_COMPUTATION_UNSPECIFIED",
            "LOCAL_AQI",
            "HEALTH_RECOMMENDATIONS",
            "POLLUTANT_ADDITIONAL_INFO",
            "DOMINANT_POLLUTANT_CONCENTRATION",
            "POLLUTANT_CONCENTRATION",
        ]
    ]
    hours: int
    languageCode: str
    location: LatLng
    pageSize: int
    pageToken: str
    period: Interval
    uaqiColorPalette: typing_extensions.Literal[
        "COLOR_PALETTE_UNSPECIFIED",
        "RED_GREEN",
        "INDIGO_PERSIAN_DARK",
        "INDIGO_PERSIAN_LIGHT",
    ]
    universalAqi: bool

@typing.type_check_only
class LookupHistoryResponse(typing_extensions.TypedDict, total=False):
    hoursInfo: _list[HourInfo]
    nextPageToken: str
    regionCode: str

@typing.type_check_only
class Pollutant(typing_extensions.TypedDict, total=False):
    additionalInfo: AdditionalInfo
    code: str
    concentration: Concentration
    displayName: str
    fullName: str
