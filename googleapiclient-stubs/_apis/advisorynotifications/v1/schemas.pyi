import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1Attachment(
    typing_extensions.TypedDict, total=False
):
    csv: GoogleCloudAdvisorynotificationsV1Csv
    displayName: str

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1Csv(typing_extensions.TypedDict, total=False):
    dataRows: _list[GoogleCloudAdvisorynotificationsV1CsvCsvRow]
    headers: _list[str]

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1CsvCsvRow(
    typing_extensions.TypedDict, total=False
):
    entries: _list[str]

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1ListNotificationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notifications: _list[GoogleCloudAdvisorynotificationsV1Notification]
    totalSize: int

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1Message(
    typing_extensions.TypedDict, total=False
):
    attachments: _list[GoogleCloudAdvisorynotificationsV1Attachment]
    body: GoogleCloudAdvisorynotificationsV1MessageBody
    createTime: str
    localizationTime: str

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1MessageBody(
    typing_extensions.TypedDict, total=False
):
    text: GoogleCloudAdvisorynotificationsV1Text

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1Notification(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    messages: _list[GoogleCloudAdvisorynotificationsV1Message]
    name: str
    subject: GoogleCloudAdvisorynotificationsV1Subject

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1Subject(
    typing_extensions.TypedDict, total=False
):
    text: GoogleCloudAdvisorynotificationsV1Text

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1Text(typing_extensions.TypedDict, total=False):
    enText: str
    localizationState: typing_extensions.Literal[
        "LOCALIZATION_STATE_UNSPECIFIED",
        "LOCALIZATION_STATE_NOT_APPLICABLE",
        "LOCALIZATION_STATE_PENDING",
        "LOCALIZATION_STATE_COMPLETED",
    ]
    localizedText: str
