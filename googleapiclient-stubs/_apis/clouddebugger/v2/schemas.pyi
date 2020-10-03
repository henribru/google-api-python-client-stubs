import typing

import typing_extensions

class ProjectRepoId(typing_extensions.TypedDict, total=False):
    repoName: str
    projectId: str

class CloudRepoSourceContext(typing_extensions.TypedDict, total=False):
    aliasContext: AliasContext
    aliasName: str
    revisionId: str
    repoId: RepoId

class FormatMessage(typing_extensions.TypedDict, total=False):
    format: str
    parameters: typing.List[str]

class UpdateActiveBreakpointResponse(typing_extensions.TypedDict, total=False): ...

class SourceLocation(typing_extensions.TypedDict, total=False):
    column: int
    path: str
    line: int

class GitSourceContext(typing_extensions.TypedDict, total=False):
    url: str
    revisionId: str

class SetBreakpointResponse(typing_extensions.TypedDict, total=False):
    breakpoint: Breakpoint

class CloudWorkspaceSourceContext(typing_extensions.TypedDict, total=False):
    workspaceId: CloudWorkspaceId
    snapshotId: str

class GetBreakpointResponse(typing_extensions.TypedDict, total=False):
    breakpoint: Breakpoint

class Debuggee(typing_extensions.TypedDict, total=False):
    isDisabled: bool
    description: str
    canaryMode: typing_extensions.Literal[
        "CANARY_MODE_UNSPECIFIED",
        "CANARY_MODE_ALWAYS_ENABLED",
        "CANARY_MODE_ALWAYS_DISABLED",
        "CANARY_MODE_DEFAULT_ENABLED",
        "CANARY_MODE_DEFAULT_DISABLED",
    ]
    project: str
    uniquifier: str
    isInactive: bool
    status: StatusMessage
    labels: typing.Dict[str, typing.Any]
    extSourceContexts: typing.List[ExtendedSourceContext]
    sourceContexts: typing.List[SourceContext]
    id: str
    agentVersion: str

class Empty(typing_extensions.TypedDict, total=False): ...

class RegisterDebuggeeRequest(typing_extensions.TypedDict, total=False):
    debuggee: Debuggee

class ListDebuggeesResponse(typing_extensions.TypedDict, total=False):
    debuggees: typing.List[Debuggee]

class Variable(typing.Dict[str, typing.Any]): ...

class RegisterDebuggeeResponse(typing_extensions.TypedDict, total=False):
    agentId: str
    debuggee: Debuggee

class ExtendedSourceContext(typing_extensions.TypedDict, total=False):
    context: SourceContext
    labels: typing.Dict[str, typing.Any]

class CloudWorkspaceId(typing_extensions.TypedDict, total=False):
    name: str
    repoId: RepoId

class AliasContext(typing_extensions.TypedDict, total=False):
    name: str
    kind: typing_extensions.Literal["ANY", "FIXED", "MOVABLE", "OTHER"]

class StatusMessage(typing_extensions.TypedDict, total=False):
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
    isError: bool
    description: FormatMessage

class ListBreakpointsResponse(typing_extensions.TypedDict, total=False):
    nextWaitToken: str
    breakpoints: typing.List[Breakpoint]

class UpdateActiveBreakpointRequest(typing_extensions.TypedDict, total=False):
    breakpoint: Breakpoint

class GerritSourceContext(typing_extensions.TypedDict, total=False):
    revisionId: str
    aliasContext: AliasContext
    gerritProject: str
    aliasName: str
    hostUri: str

class SourceContext(typing_extensions.TypedDict, total=False):
    gerrit: GerritSourceContext
    git: GitSourceContext
    cloudWorkspace: CloudWorkspaceSourceContext
    cloudRepo: CloudRepoSourceContext

class ListActiveBreakpointsResponse(typing_extensions.TypedDict, total=False):
    nextWaitToken: str
    breakpoints: typing.List[Breakpoint]
    waitExpired: bool

class RepoId(typing_extensions.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

class StackFrame(typing_extensions.TypedDict, total=False):
    locals: typing.List[Variable]
    location: SourceLocation
    function: str
    arguments: typing.List[Variable]

class Breakpoint(typing.Dict[str, typing.Any]): ...
