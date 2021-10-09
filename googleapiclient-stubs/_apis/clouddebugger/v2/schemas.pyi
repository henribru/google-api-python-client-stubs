import typing

import typing_extensions

_list = list

@typing.type_check_only
class AliasContext(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["ANY", "FIXED", "MOVABLE", "OTHER"]
    name: str

@typing.type_check_only
class Breakpoint(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["CAPTURE", "LOG"]
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
    logLevel: typing_extensions.Literal["INFO", "WARNING", "ERROR"]
    logMessageFormat: str
    stackFrames: _list[StackFrame]
    state: typing_extensions.Literal[
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
class CloudRepoSourceContext(typing_extensions.TypedDict, total=False):
    aliasContext: AliasContext
    aliasName: str
    repoId: RepoId
    revisionId: str

@typing.type_check_only
class CloudWorkspaceId(typing_extensions.TypedDict, total=False):
    name: str
    repoId: RepoId

@typing.type_check_only
class CloudWorkspaceSourceContext(typing_extensions.TypedDict, total=False):
    snapshotId: str
    workspaceId: CloudWorkspaceId

@typing.type_check_only
class Debuggee(typing_extensions.TypedDict, total=False):
    agentVersion: str
    canaryMode: typing_extensions.Literal[
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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExtendedSourceContext(typing_extensions.TypedDict, total=False):
    context: SourceContext
    labels: dict[str, typing.Any]

@typing.type_check_only
class FormatMessage(typing_extensions.TypedDict, total=False):
    format: str
    parameters: _list[str]

@typing.type_check_only
class GerritSourceContext(typing_extensions.TypedDict, total=False):
    aliasContext: AliasContext
    aliasName: str
    gerritProject: str
    hostUri: str
    revisionId: str

@typing.type_check_only
class GetBreakpointResponse(typing_extensions.TypedDict, total=False):
    breakpoint: Breakpoint

@typing.type_check_only
class GitSourceContext(typing_extensions.TypedDict, total=False):
    revisionId: str
    url: str

@typing.type_check_only
class ListActiveBreakpointsResponse(typing_extensions.TypedDict, total=False):
    breakpoints: _list[Breakpoint]
    nextWaitToken: str
    waitExpired: bool

@typing.type_check_only
class ListBreakpointsResponse(typing_extensions.TypedDict, total=False):
    breakpoints: _list[Breakpoint]
    nextWaitToken: str

@typing.type_check_only
class ListDebuggeesResponse(typing_extensions.TypedDict, total=False):
    debuggees: _list[Debuggee]

@typing.type_check_only
class ProjectRepoId(typing_extensions.TypedDict, total=False):
    projectId: str
    repoName: str

@typing.type_check_only
class RegisterDebuggeeRequest(typing_extensions.TypedDict, total=False):
    debuggee: Debuggee

@typing.type_check_only
class RegisterDebuggeeResponse(typing_extensions.TypedDict, total=False):
    agentId: str
    debuggee: Debuggee

@typing.type_check_only
class RepoId(typing_extensions.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

@typing.type_check_only
class SetBreakpointResponse(typing_extensions.TypedDict, total=False):
    breakpoint: Breakpoint

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    cloudRepo: CloudRepoSourceContext
    cloudWorkspace: CloudWorkspaceSourceContext
    gerrit: GerritSourceContext
    git: GitSourceContext

@typing.type_check_only
class SourceLocation(typing_extensions.TypedDict, total=False):
    column: int
    line: int
    path: str

@typing.type_check_only
class StackFrame(dict[str, typing.Any]): ...

@typing.type_check_only
class StatusMessage(typing_extensions.TypedDict, total=False):
    description: FormatMessage
    isError: bool
    refersTo: typing_extensions.Literal[
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
class UpdateActiveBreakpointRequest(typing_extensions.TypedDict, total=False):
    breakpoint: Breakpoint

@typing.type_check_only
class UpdateActiveBreakpointResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Variable(dict[str, typing.Any]): ...
