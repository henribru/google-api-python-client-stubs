import typing

import typing_extensions

class ScriptExecutionResult(typing_extensions.TypedDict, total=False):
    returnValue: Value

class Version(typing_extensions.TypedDict, total=False):
    description: str
    createTime: str
    versionNumber: int
    scriptId: str

class UpdateDeploymentRequest(typing_extensions.TypedDict, total=False):
    deploymentConfig: DeploymentConfig

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    response: typing.Dict[str, typing.Any]
    error: Status

class Struct(typing_extensions.TypedDict, total=False):
    fields: typing.Dict[str, typing.Any]

class Project(typing_extensions.TypedDict, total=False):
    title: str
    createTime: str
    parentId: str
    lastModifyUser: GoogleAppsScriptTypeUser
    creator: GoogleAppsScriptTypeUser
    updateTime: str
    scriptId: str

class ScriptStackTraceElement(typing_extensions.TypedDict, total=False):
    function: str
    lineNumber: int

class GoogleAppsScriptTypeUser(typing_extensions.TypedDict, total=False):
    name: str
    email: str
    domain: str
    photoUrl: str

class EntryPoint(typing_extensions.TypedDict, total=False):
    entryPointType: typing_extensions.Literal[
        "ENTRY_POINT_TYPE_UNSPECIFIED", "WEB_APP", "EXECUTION_API", "ADD_ON"
    ]
    executionApi: GoogleAppsScriptTypeExecutionApiEntryPoint
    addOn: GoogleAppsScriptTypeAddOnEntryPoint
    webApp: GoogleAppsScriptTypeWebAppEntryPoint

class ListDeploymentsResponse(typing_extensions.TypedDict, total=False):
    deployments: typing.List[Deployment]
    nextPageToken: str

class GoogleAppsScriptTypeExecutionApiConfig(typing_extensions.TypedDict, total=False):
    access: typing_extensions.Literal[
        "UNKNOWN_ACCESS", "MYSELF", "DOMAIN", "ANYONE", "ANYONE_ANONYMOUS"
    ]

class GoogleAppsScriptTypeExecutionApiEntryPoint(
    typing_extensions.TypedDict, total=False
):
    entryPointConfig: GoogleAppsScriptTypeExecutionApiConfig

class GoogleAppsScriptTypeWebAppConfig(typing_extensions.TypedDict, total=False):
    access: typing_extensions.Literal[
        "UNKNOWN_ACCESS", "MYSELF", "DOMAIN", "ANYONE", "ANYONE_ANONYMOUS"
    ]
    executeAs: typing_extensions.Literal[
        "UNKNOWN_EXECUTE_AS", "USER_ACCESSING", "USER_DEPLOYING"
    ]

class ListUserProcessesResponse(typing_extensions.TypedDict, total=False):
    processes: typing.List[GoogleAppsScriptTypeProcess]
    nextPageToken: str

class CreateProjectRequest(typing_extensions.TypedDict, total=False):
    parentId: str
    title: str

class ExecuteStreamResponse(typing_extensions.TypedDict, total=False):
    result: ScriptExecutionResult

class Content(typing_extensions.TypedDict, total=False):
    files: typing.List[File]
    scriptId: str

class ExecutionError(typing_extensions.TypedDict, total=False):
    errorType: str
    errorMessage: str
    scriptStackTraceElements: typing.List[ScriptStackTraceElement]

class ListValue(typing_extensions.TypedDict, total=False):
    values: typing.List[Value]

class DeploymentConfig(typing_extensions.TypedDict, total=False):
    scriptId: str
    description: str
    manifestFileName: str
    versionNumber: int

class GoogleAppsScriptTypeAddOnEntryPoint(typing_extensions.TypedDict, total=False):
    postInstallTipUrl: str
    helpUrl: str
    title: str
    description: str
    addOnType: typing_extensions.Literal["UNKNOWN_ADDON_TYPE", "GMAIL", "DATA_STUDIO"]
    reportIssueUrl: str

class MetricsValue(typing_extensions.TypedDict, total=False):
    value: str
    endTime: str
    startTime: str

class GoogleAppsScriptTypeFunctionSet(typing_extensions.TypedDict, total=False):
    values: typing.List[GoogleAppsScriptTypeFunction]

class ListScriptProcessesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    processes: typing.List[GoogleAppsScriptTypeProcess]

class Metrics(typing_extensions.TypedDict, total=False):
    failedExecutions: typing.List[MetricsValue]
    activeUsers: typing.List[MetricsValue]
    totalExecutions: typing.List[MetricsValue]

class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    versions: typing.List[Version]
    nextPageToken: str

class GoogleAppsScriptTypeWebAppEntryPoint(typing_extensions.TypedDict, total=False):
    entryPointConfig: GoogleAppsScriptTypeWebAppConfig
    url: str

class GoogleAppsScriptTypeFunction(typing_extensions.TypedDict, total=False):
    name: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Deployment(typing_extensions.TypedDict, total=False):
    deploymentId: str
    deploymentConfig: DeploymentConfig
    updateTime: str
    entryPoints: typing.List[EntryPoint]

class ExecutionRequest(typing_extensions.TypedDict, total=False):
    sessionState: str
    parameters: typing.List[typing.Any]
    devMode: bool
    function: str

class GoogleAppsScriptTypeProcess(typing_extensions.TypedDict, total=False):
    projectName: str
    processStatus: typing_extensions.Literal[
        "PROCESS_STATUS_UNSPECIFIED",
        "RUNNING",
        "PAUSED",
        "COMPLETED",
        "CANCELED",
        "FAILED",
        "TIMED_OUT",
        "UNKNOWN",
        "DELAYED",
    ]
    processType: typing_extensions.Literal[
        "PROCESS_TYPE_UNSPECIFIED",
        "ADD_ON",
        "EXECUTION_API",
        "TIME_DRIVEN",
        "TRIGGER",
        "WEBAPP",
        "EDITOR",
        "SIMPLE_TRIGGER",
        "MENU",
        "BATCH_TASK",
    ]
    startTime: str
    userAccessLevel: typing_extensions.Literal[
        "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
    ]
    functionName: str
    duration: str

class ExecutionResponse(typing_extensions.TypedDict, total=False):
    result: typing.Any

class File(typing_extensions.TypedDict, total=False):
    updateTime: str
    lastModifyUser: GoogleAppsScriptTypeUser
    source: str
    functionSet: GoogleAppsScriptTypeFunctionSet
    type: typing_extensions.Literal[
        "ENUM_TYPE_UNSPECIFIED", "SERVER_JS", "HTML", "JSON"
    ]
    createTime: str
    name: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Value(typing.Dict[str, typing.Any]): ...
