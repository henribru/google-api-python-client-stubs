import typing

import typing_extensions

_list = list

@typing.type_check_only
class Content(typing_extensions.TypedDict, total=False):
    files: _list[File]
    scriptId: str

@typing.type_check_only
class CreateProjectRequest(typing_extensions.TypedDict, total=False):
    parentId: str
    title: str

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    deploymentConfig: DeploymentConfig
    deploymentId: str
    entryPoints: _list[EntryPoint]
    updateTime: str

@typing.type_check_only
class DeploymentConfig(typing_extensions.TypedDict, total=False):
    description: str
    manifestFileName: str
    scriptId: str
    versionNumber: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EntryPoint(typing_extensions.TypedDict, total=False):
    addOn: GoogleAppsScriptTypeAddOnEntryPoint
    entryPointType: typing_extensions.Literal[
        "ENTRY_POINT_TYPE_UNSPECIFIED", "WEB_APP", "EXECUTION_API", "ADD_ON"
    ]
    executionApi: GoogleAppsScriptTypeExecutionApiEntryPoint
    webApp: GoogleAppsScriptTypeWebAppEntryPoint

@typing.type_check_only
class ExecuteStreamResponse(typing_extensions.TypedDict, total=False):
    result: ScriptExecutionResult

@typing.type_check_only
class ExecutionError(typing_extensions.TypedDict, total=False):
    errorMessage: str
    errorType: str
    scriptStackTraceElements: _list[ScriptStackTraceElement]

@typing.type_check_only
class ExecutionRequest(typing_extensions.TypedDict, total=False):
    devMode: bool
    function: str
    parameters: _list[typing.Any]
    sessionState: str

@typing.type_check_only
class ExecutionResponse(typing_extensions.TypedDict, total=False):
    result: typing.Any

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    createTime: str
    functionSet: GoogleAppsScriptTypeFunctionSet
    lastModifyUser: GoogleAppsScriptTypeUser
    name: str
    source: str
    type: typing_extensions.Literal[
        "ENUM_TYPE_UNSPECIFIED", "SERVER_JS", "HTML", "JSON"
    ]
    updateTime: str

@typing.type_check_only
class GoogleAppsScriptTypeAddOnEntryPoint(typing_extensions.TypedDict, total=False):
    addOnType: typing_extensions.Literal["UNKNOWN_ADDON_TYPE", "GMAIL", "DATA_STUDIO"]
    description: str
    helpUrl: str
    postInstallTipUrl: str
    reportIssueUrl: str
    title: str

@typing.type_check_only
class GoogleAppsScriptTypeExecutionApiConfig(typing_extensions.TypedDict, total=False):
    access: typing_extensions.Literal[
        "UNKNOWN_ACCESS", "MYSELF", "DOMAIN", "ANYONE", "ANYONE_ANONYMOUS"
    ]

@typing.type_check_only
class GoogleAppsScriptTypeExecutionApiEntryPoint(
    typing_extensions.TypedDict, total=False
):
    entryPointConfig: GoogleAppsScriptTypeExecutionApiConfig

@typing.type_check_only
class GoogleAppsScriptTypeFunction(typing_extensions.TypedDict, total=False):
    name: str
    parameters: _list[str]

@typing.type_check_only
class GoogleAppsScriptTypeFunctionSet(typing_extensions.TypedDict, total=False):
    values: _list[GoogleAppsScriptTypeFunction]

@typing.type_check_only
class GoogleAppsScriptTypeProcess(typing_extensions.TypedDict, total=False):
    duration: str
    functionName: str
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
    projectName: str
    startTime: str
    userAccessLevel: typing_extensions.Literal[
        "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
    ]

@typing.type_check_only
class GoogleAppsScriptTypeUser(typing_extensions.TypedDict, total=False):
    domain: str
    email: str
    name: str
    photoUrl: str

@typing.type_check_only
class GoogleAppsScriptTypeWebAppConfig(typing_extensions.TypedDict, total=False):
    access: typing_extensions.Literal[
        "UNKNOWN_ACCESS", "MYSELF", "DOMAIN", "ANYONE", "ANYONE_ANONYMOUS"
    ]
    executeAs: typing_extensions.Literal[
        "UNKNOWN_EXECUTE_AS", "USER_ACCESSING", "USER_DEPLOYING"
    ]

@typing.type_check_only
class GoogleAppsScriptTypeWebAppEntryPoint(typing_extensions.TypedDict, total=False):
    entryPointConfig: GoogleAppsScriptTypeWebAppConfig
    url: str

@typing.type_check_only
class ListDeploymentsResponse(typing_extensions.TypedDict, total=False):
    deployments: _list[Deployment]
    nextPageToken: str

@typing.type_check_only
class ListScriptProcessesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    processes: _list[GoogleAppsScriptTypeProcess]

@typing.type_check_only
class ListUserProcessesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    processes: _list[GoogleAppsScriptTypeProcess]

@typing.type_check_only
class ListValue(typing_extensions.TypedDict, total=False):
    values: _list[Value]

@typing.type_check_only
class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class Metrics(typing_extensions.TypedDict, total=False):
    activeUsers: _list[MetricsValue]
    failedExecutions: _list[MetricsValue]
    totalExecutions: _list[MetricsValue]

@typing.type_check_only
class MetricsValue(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    value: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    response: dict[str, typing.Any]

@typing.type_check_only
class Project(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: GoogleAppsScriptTypeUser
    lastModifyUser: GoogleAppsScriptTypeUser
    parentId: str
    scriptId: str
    title: str
    updateTime: str

@typing.type_check_only
class ScriptExecutionResult(dict[str, typing.Any]): ...

@typing.type_check_only
class ScriptStackTraceElement(typing_extensions.TypedDict, total=False):
    function: str
    lineNumber: int

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Struct(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]

@typing.type_check_only
class UpdateDeploymentRequest(typing_extensions.TypedDict, total=False):
    deploymentConfig: DeploymentConfig

@typing.type_check_only
class Value(dict[str, typing.Any]): ...

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    scriptId: str
    versionNumber: int
