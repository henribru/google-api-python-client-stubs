import typing

_list = list

@typing.type_check_only
class GoogleCloudResourcesettingsV1ListSettingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    settings: _list[GoogleCloudResourcesettingsV1Setting]

@typing.type_check_only
class GoogleCloudResourcesettingsV1Setting(typing.TypedDict, total=False):
    effectiveValue: GoogleCloudResourcesettingsV1Value
    etag: str
    localValue: GoogleCloudResourcesettingsV1Value
    metadata: GoogleCloudResourcesettingsV1SettingMetadata
    name: str

@typing.type_check_only
class GoogleCloudResourcesettingsV1SettingMetadata(typing.TypedDict, total=False):
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "BOOLEAN",
        "STRING",
        "STRING_SET",
        "ENUM_VALUE",
        "DURATION_VALUE",
        "STRING_MAP",
    ]
    defaultValue: GoogleCloudResourcesettingsV1Value
    description: str
    displayName: str
    readOnly: bool

@typing.type_check_only
class GoogleCloudResourcesettingsV1Value(typing.TypedDict, total=False):
    booleanValue: bool
    durationValue: str
    enumValue: GoogleCloudResourcesettingsV1ValueEnumValue
    stringMapValue: GoogleCloudResourcesettingsV1ValueStringMap
    stringSetValue: GoogleCloudResourcesettingsV1ValueStringSet
    stringValue: str

@typing.type_check_only
class GoogleCloudResourcesettingsV1ValueEnumValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleCloudResourcesettingsV1ValueStringMap(typing.TypedDict, total=False):
    mappings: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudResourcesettingsV1ValueStringSet(typing.TypedDict, total=False):
    values: _list[str]
