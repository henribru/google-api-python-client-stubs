import typing

import typing_extensions

_list = list

@typing.type_check_only
class AndroidxCrawlerOutputPoint(typing_extensions.TypedDict, total=False):
    xCoordinate: int
    yCoordinate: int

@typing.type_check_only
class GoogleFirebaseAppdistroV1Release(typing_extensions.TypedDict, total=False):
    binaryDownloadUri: str
    buildVersion: str
    createTime: str
    displayVersion: str
    firebaseConsoleUri: str
    name: str
    releaseNotes: GoogleFirebaseAppdistroV1ReleaseNotes
    testingUri: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1ReleaseNotes(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseResponse(
    typing_extensions.TypedDict, total=False
):
    release: GoogleFirebaseAppdistroV1Release
    result: typing_extensions.Literal[
        "UPLOAD_RELEASE_RESULT_UNSPECIFIED",
        "RELEASE_CREATED",
        "RELEASE_UPDATED",
        "RELEASE_UNMODIFIED",
    ]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaAabCertificate(
    typing_extensions.TypedDict, total=False
):
    certificateHashMd5: str
    certificateHashSha1: str
    certificateHashSha256: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaAiInstructions(
    typing_extensions.TypedDict, total=False
):
    appDescription: str
    steps: _list[GoogleFirebaseAppdistroV1alphaAiStep]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaAiStep(typing_extensions.TypedDict, total=False):
    assertion: str
    goal: str
    hint: str
    successCriteria: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaAiStepResult(
    typing_extensions.TypedDict, total=False
):
    assertionDetails: GoogleFirebaseAppdistroV1alphaAssertionDetails
    goalDetails: GoogleFirebaseAppdistroV1alphaGoalDetails
    state: typing_extensions.Literal[
        "STEP_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "PASSED",
        "FAILED",
        "TIMED_OUT",
        "GOAL_ACTION_LIMIT_REACHED",
    ]
    step: GoogleFirebaseAppdistroV1alphaAiStep

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaApp(typing_extensions.TypedDict, total=False):
    aabCertificate: GoogleFirebaseAppdistroV1alphaAabCertificate
    aabState: typing_extensions.Literal[
        "AAB_STATE_UNSPECIFIED",
        "ACTIVE",
        "PLAY_ACCOUNT_NOT_LINKED",
        "NO_APP_WITH_GIVEN_BUNDLE_ID_IN_PLAY_ACCOUNT",
        "APP_NOT_PUBLISHED",
        "AAB_STATE_UNAVAILABLE",
        "PLAY_IAS_TERMS_NOT_ACCEPTED",
    ]
    appId: str
    bundleId: str
    contactEmail: str
    platform: str
    projectNumber: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaAppCrash(typing_extensions.TypedDict, total=False):
    message: str
    stackTrace: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaAssertionDetails(
    typing_extensions.TypedDict, total=False
):
    explanation: str
    result: bool
    screenshot: GoogleFirebaseAppdistroV1alphaScreenshot

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaCancelReleaseTestResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaCreateReleaseNotesRequest(
    typing_extensions.TypedDict, total=False
):
    releaseNotes: GoogleFirebaseAppdistroV1alphaReleaseNotes

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaCreateReleaseNotesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaDeviceAction(
    typing_extensions.TypedDict, total=False
):
    description: str
    deviceInteractions: _list[GoogleFirebaseAppdistroV1alphaDeviceInteraction]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaDeviceExecution(
    typing_extensions.TypedDict, total=False
):
    aiStepResults: _list[GoogleFirebaseAppdistroV1alphaAiStepResult]
    appCrash: GoogleFirebaseAppdistroV1alphaAppCrash
    crawlGraphUri: str
    device: GoogleFirebaseAppdistroV1alphaTestDevice
    failedReason: typing_extensions.Literal[
        "FAILED_REASON_UNSPECIFIED",
        "CRASHED",
        "NOT_INSTALLED",
        "UNABLE_TO_CRAWL",
        "DEVICE_OUT_OF_MEMORY",
        "FAILED_AI_STEP",
        "TIMED_OUT",
    ]
    inconclusiveReason: typing_extensions.Literal[
        "INCONCLUSIVE_REASON_UNSPECIFIED",
        "QUOTA_EXCEEDED",
        "INFRASTRUCTURE_FAILURE",
        "SERVICE_NOT_ACTIVATED",
        "NO_SIGNATURE",
        "NO_LAUNCHER_ACTIVITY",
        "FORBIDDEN_PERMISSIONS",
        "DEVICE_ADMIN_RECEIVER",
        "NO_CODE_APK",
        "INVALID_APK_PREVIEW_SDK",
    ]
    resultsStoragePath: str
    roboStats: GoogleFirebaseAppdistroV1alphaRoboStats
    screenshotUris: _list[str]
    state: typing_extensions.Literal[
        "TEST_STATE_UNSPECIFIED", "IN_PROGRESS", "PASSED", "FAILED", "INCONCLUSIVE"
    ]
    videoUri: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaDeviceInteraction(
    typing_extensions.TypedDict, total=False
):
    keyCode: str
    screenshot: GoogleFirebaseAppdistroV1alphaScreenshot
    swipe: GoogleFirebaseAppdistroV1alphaDeviceInteractionSwipe
    tap: AndroidxCrawlerOutputPoint
    textInput: str
    wait: GoogleFirebaseAppdistroV1alphaDeviceInteractionWait

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaDeviceInteractionSwipe(
    typing_extensions.TypedDict, total=False
):
    end: AndroidxCrawlerOutputPoint
    start: AndroidxCrawlerOutputPoint

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaDeviceInteractionWait(
    typing_extensions.TypedDict, total=False
):
    duration: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaEnableAccessOnReleaseRequest(
    typing_extensions.TypedDict, total=False
):
    buildVersion: str
    displayVersion: str
    emails: _list[str]
    groupIds: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaEnableAccessOnReleaseResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGetReleaseByUploadHashResponse(
    typing_extensions.TypedDict, total=False
):
    release: GoogleFirebaseAppdistroV1alphaRelease

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGetTesterUdidsResponse(
    typing_extensions.TypedDict, total=False
):
    testerUdids: _list[GoogleFirebaseAppdistroV1alphaTesterUdid]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGetUploadStatusResponse(
    typing_extensions.TypedDict, total=False
):
    errorCode: typing_extensions.Literal[
        "ERROR_UNSPECIFIED",
        "INVALID_ZIP",
        "MISSING_PLIST",
        "MISSING_PROFILE",
        "VERSION_TOO_LONG",
        "MISSING_UUIDS",
        "MISSING_RESOURCES",
        "MISSING_MANIFEST",
        "IOS_METADATA_ERROR",
        "ANDROID_METADATA_ERROR",
        "UNSUPPORTED_PLATFORM_TYPE",
        "BUNDLE_ID_MISMATCH",
        "APK_NOT_ZIP_ALIGNED",
        "INVALID_CERTIFICATE",
        "APK_TOO_LARGE",
        "AAB_NOT_PUBLISHED",
        "INVALID_PLIST_DEVICE_FAMILIES",
        "AAB_TOS_NOT_ACCEPTED",
        "APP_NAME_TOO_LONG",
        "AAB_DEVELOPER_ACCOUNT_NOT_LINKED",
        "AAB_NO_APP_WITH_GIVEN_PACKAGE_NAME_IN_ACCOUNT",
        "AAB_UPLOAD_ERROR",
    ]
    message: str
    release: GoogleFirebaseAppdistroV1alphaRelease
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "IN_PROGRESS", "ALREADY_UPLOADED", "SUCCESS", "ERROR"
    ]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGoalAction(
    typing_extensions.TypedDict, total=False
):
    deviceAction: GoogleFirebaseAppdistroV1alphaDeviceAction
    explanation: str
    terminalAction: GoogleFirebaseAppdistroV1alphaTerminalAction

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGoalDetails(
    typing_extensions.TypedDict, total=False
):
    goalActions: _list[GoogleFirebaseAppdistroV1alphaGoalAction]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaJwt(typing_extensions.TypedDict, total=False):
    token: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaListReleaseTestsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    releaseTests: _list[GoogleFirebaseAppdistroV1alphaReleaseTest]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaListTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    testCases: _list[GoogleFirebaseAppdistroV1alphaTestCase]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaLoginCredential(
    typing_extensions.TypedDict, total=False
):
    fieldHints: GoogleFirebaseAppdistroV1alphaLoginCredentialFieldHints
    google: bool
    password: str
    username: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaLoginCredentialFieldHints(
    typing_extensions.TypedDict, total=False
):
    passwordResourceName: str
    usernameResourceName: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaProvisionAppResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaRelease(typing_extensions.TypedDict, total=False):
    buildVersion: str
    displayVersion: str
    distributedAt: str
    id: str
    instanceId: str
    lastActivityAt: str
    openInvitationCount: int
    receivedAt: str
    releaseNotesSummary: str
    testerCount: int
    testerWithInstallCount: int

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaReleaseNotes(
    typing_extensions.TypedDict, total=False
):
    releaseNotes: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaReleaseTest(
    typing_extensions.TypedDict, total=False
):
    aiInstructions: GoogleFirebaseAppdistroV1alphaAiInstructions
    createTime: str
    deviceExecutions: _list[GoogleFirebaseAppdistroV1alphaDeviceExecution]
    displayName: str
    loginCredential: GoogleFirebaseAppdistroV1alphaLoginCredential
    name: str
    testCase: str
    testState: typing_extensions.Literal[
        "TEST_STATE_UNSPECIFIED", "IN_PROGRESS", "PASSED", "FAILED", "INCONCLUSIVE"
    ]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaRoboCrawler(
    typing_extensions.TypedDict, total=False
):
    aiInstructions: GoogleFirebaseAppdistroV1alphaAiInstructions
    loginCredential: GoogleFirebaseAppdistroV1alphaLoginCredential

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaRoboStats(typing_extensions.TypedDict, total=False):
    actionsPerformed: int
    crawlDuration: str
    distinctVisitedScreens: int
    mainActivityCrawlTimedOut: bool

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaScreenshot(
    typing_extensions.TypedDict, total=False
):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaTerminalAction(
    typing_extensions.TypedDict, total=False
):
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED", "GOAL_IMPOSSIBLE", "GOAL_COMPLETE"
    ]
    screenshot: GoogleFirebaseAppdistroV1alphaScreenshot

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaTestCase(typing_extensions.TypedDict, total=False):
    aiInstructions: GoogleFirebaseAppdistroV1alphaAiInstructions
    displayName: str
    name: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaTestConfig(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    roboCrawler: GoogleFirebaseAppdistroV1alphaRoboCrawler
    testDevices: _list[GoogleFirebaseAppdistroV1alphaTestDevice]

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaTestDevice(
    typing_extensions.TypedDict, total=False
):
    locale: str
    model: str
    orientation: str
    version: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaTesterUdid(
    typing_extensions.TypedDict, total=False
):
    name: str
    platform: str
    udid: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
