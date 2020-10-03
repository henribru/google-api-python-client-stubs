import typing

import typing_extensions

class IamPolicyAnalysisResult(typing_extensions.TypedDict, total=False):
    iamBinding: Binding
    fullyExplored: bool
    attachedResourceFullName: str
    identityList: GoogleCloudAssetV1p4beta1IdentityList
    accessControlLists: typing.List[GoogleCloudAssetV1p4beta1AccessControlList]

class GoogleCloudAssetV1p4beta1Access(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    role: str
    permission: str

class GoogleCloudAssetV1p4beta1Identity(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    name: str

class GoogleCloudAssetV1p4beta1AccessControlList(
    typing_extensions.TypedDict, total=False
):
    accesses: typing.List[GoogleCloudAssetV1p4beta1Access]
    resourceEdges: typing.List[GoogleCloudAssetV1p4beta1Edge]
    resources: typing.List[GoogleCloudAssetV1p4beta1Resource]

class Options(typing_extensions.TypedDict, total=False):
    expandRoles: bool
    outputResourceEdges: bool
    expandGroups: bool
    outputGroupEdges: bool
    expandResources: bool
    analyzeServiceAccountImpersonation: bool

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class GoogleCloudAssetV1p4beta1Resource(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    fullResourceName: str

class AccessSelector(typing_extensions.TypedDict, total=False):
    roles: typing.List[str]
    permissions: typing.List[str]

class IamPolicyAnalysisOutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

class IdentitySelector(typing_extensions.TypedDict, total=False):
    identity: str

class IamPolicyAnalysis(typing_extensions.TypedDict, total=False):
    fullyExplored: bool
    analysisQuery: IamPolicyAnalysisQuery
    analysisResults: typing.List[IamPolicyAnalysisResult]

class IamPolicyAnalysisQuery(typing_extensions.TypedDict, total=False):
    identitySelector: IdentitySelector
    parent: str
    accessSelector: AccessSelector
    resourceSelector: ResourceSelector

class GoogleCloudAssetV1p4beta1AnalysisState(typing_extensions.TypedDict, total=False):
    cause: str
    code: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]

class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

class ResourceSelector(typing_extensions.TypedDict, total=False):
    fullResourceName: str

class GoogleCloudAssetV1p4beta1Edge(typing_extensions.TypedDict, total=False):
    targetNode: str
    sourceNode: str

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

class ExportIamPolicyAnalysisRequest(typing_extensions.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    options: Options
    outputConfig: IamPolicyAnalysisOutputConfig

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    description: str
    location: str
    expression: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    metadata: typing.Dict[str, typing.Any]
    done: bool
    response: typing.Dict[str, typing.Any]
    name: str

class GoogleCloudAssetV1p4beta1IdentityList(typing_extensions.TypedDict, total=False):
    identities: typing.List[GoogleCloudAssetV1p4beta1Identity]
    groupEdges: typing.List[GoogleCloudAssetV1p4beta1Edge]

class AnalyzeIamPolicyResponse(typing_extensions.TypedDict, total=False):
    mainAnalysis: IamPolicyAnalysis
    nonCriticalErrors: typing.List[GoogleCloudAssetV1p4beta1AnalysisState]
    serviceAccountImpersonationAnalysis: typing.List[IamPolicyAnalysis]
    fullyExplored: bool
