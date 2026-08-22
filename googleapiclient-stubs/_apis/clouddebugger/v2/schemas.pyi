import typing

_list = list

@typing.type_check_only
class AliasContext(typing.TypedDict, total=False):
    kind: typing.Literal["ANY", "FIXED", "MOVABLE", "OTHER"]
    name: str

@typing.type_check_only
class Breakpoint(typing.TypedDict, total=False):
    action: typing.Literal["CAPTURE", "LOG"]
    canaryExpireTime: str
    condition: str
    createTime: str
    evaluatedExpressions: _list[Variable]
    expressions: _list[str]
    finalTime: str
    id: str
    isFinalState: bool
    labels: dict[str, typing.Any]
    location: SourceLocation
    logLevel: typing.Literal["INFO", "WARNING", "ERROR"]
    logMessageFormat: str
    stackFrames: _list[StackFrame]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STATE_CANARY_PENDING_AGENTS",
        "STATE_CANARY_ACTIVE",
        "STATE_ROLLING_TO_ALL",
        "STATE_IS_FINAL",
    ]
    status: StatusMessage
    userEmail: str
    variableTable: _list[Variable]

@typing.type_check_only
class CloudRepoSourceContext(typing.TypedDict, total=False):
    aliasContext: AliasContext
    aliasName: str
    repoId: RepoId
    revisionId: str

@typing.type_check_only
class CloudWorkspaceId(typing.TypedDict, total=False):
    name: str
    repoId: RepoId

@typing.type_check_only
class CloudWorkspaceSourceContext(typing.TypedDict, total=False):
    snapshotId: str
    workspaceId: CloudWorkspaceId

@typing.type_check_only
class Debuggee(typing.TypedDict, total=False):
    agentVersion: str
    canaryMode: typing.Literal[
        "CANARY_MODE_UNSPECIFIED",
        "CANARY_MODE_ALWAYS_ENABLED",
        "CANARY_MODE_ALWAYS_DISABLED",
        "CANARY_MODE_DEFAULT_ENABLED",
        "CANARY_MODE_DEFAULT_DISABLED",
    ]
    description: str
    extSourceContexts: _list[ExtendedSourceContext]
    id: str
    isDisabled: bool
    isInactive: bool
    labels: dict[str, typing.Any]
    project: str
    sourceContexts: _list[SourceContext]
    status: StatusMessage
    uniquifier: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExtendedSourceContext(typing.TypedDict, total=False):
    context: SourceContext
    labels: dict[str, typing.Any]

@typing.type_check_only
class FormatMessage(typing.TypedDict, total=False):
    format: str
    parameters: _list[str]

@typing.type_check_only
class GerritSourceContext(typing.TypedDict, total=False):
    aliasContext: AliasContext
    aliasName: str
    gerritProject: str
    hostUri: str
    revisionId: str

@typing.type_check_only
class GetBreakpointResponse(typing.TypedDict, total=False):
    breakpoint: Breakpoint

@typing.type_check_only
class GitSourceContext(typing.TypedDict, total=False):
    revisionId: str
    url: str

@typing.type_check_only
class ListActiveBreakpointsResponse(typing.TypedDict, total=False):
    breakpoints: _list[Breakpoint]
    nextWaitToken: str
    waitExpired: bool

@typing.type_check_only
class ListBreakpointsResponse(typing.TypedDict, total=False):
    breakpoints: _list[Breakpoint]
    nextWaitToken: str

@typing.type_check_only
class ListDebuggeesResponse(typing.TypedDict, total=False):
    debuggees: _list[Debuggee]

@typing.type_check_only
class ProjectRepoId(typing.TypedDict, total=False):
    projectId: str
    repoName: str

@typing.type_check_only
class RegisterDebuggeeRequest(typing.TypedDict, total=False):
    debuggee: Debuggee

@typing.type_check_only
class RegisterDebuggeeResponse(typing.TypedDict, total=False):
    agentId: str
    debuggee: Debuggee

@typing.type_check_only
class RepoId(typing.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

@typing.type_check_only
class SetBreakpointResponse(typing.TypedDict, total=False):
    breakpoint: Breakpoint

@typing.type_check_only
class SourceContext(typing.TypedDict, total=False):
    cloudRepo: CloudRepoSourceContext
    cloudWorkspace: CloudWorkspaceSourceContext
    gerrit: GerritSourceContext
    git: GitSourceContext

@typing.type_check_only
class SourceLocation(typing.TypedDict, total=False):
    column: int
    line: int
    path: str

@typing.type_check_only
class StackFrame(typing.TypedDict, total=False):
    arguments: _list[Variable]
    function: str
    locals: _list[Variable]
    location: SourceLocation

@typing.type_check_only
class StatusMessage(typing.TypedDict, total=False):
    description: FormatMessage
    isError: bool
    refersTo: typing.Literal[
        "UNSPECIFIED",
        "BREAKPOINT_SOURCE_LOCATION",
        "BREAKPOINT_CONDITION",
        "BREAKPOINT_EXPRESSION",
        "BREAKPOINT_AGE",
        "BREAKPOINT_CANARY_FAILED",
        "VARIABLE_NAME",
        "VARIABLE_VALUE",
    ]

@typing.type_check_only
class UpdateActiveBreakpointRequest(typing.TypedDict, total=False):
    breakpoint: Breakpoint

@typing.type_check_only
class UpdateActiveBreakpointResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Variable(typing.TypedDict, total=False):
    members: _list[Variable]
    name: str
    status: StatusMessage
    type: str
    value: str
    varTableIndex: int
