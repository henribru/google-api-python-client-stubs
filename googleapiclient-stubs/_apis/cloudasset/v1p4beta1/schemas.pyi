import typing

import typing_extensions
@typing.type_check_only
class AccessSelector(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
    roles: typing.List[str]

@typing.type_check_only
class AnalyzeIamPolicyResponse(typing_extensions.TypedDict, total=False):
    fullyExplored: bool
    mainAnalysis: IamPolicyAnalysis
    nonCriticalErrors: typing.List[GoogleCloudAssetV1p4beta1AnalysisState]
    serviceAccountImpersonationAnalysis: typing.List[IamPolicyAnalysis]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class ExportIamPolicyAnalysisRequest(typing_extensions.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    options: Options
    outputConfig: IamPolicyAnalysisOutputConfig

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1Access(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    permission: str
    role: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1AccessControlList(
    typing_extensions.TypedDict, total=False
):
    accesses: typing.List[GoogleCloudAssetV1p4beta1Access]
    resourceEdges: typing.List[GoogleCloudAssetV1p4beta1Edge]
    resources: typing.List[GoogleCloudAssetV1p4beta1Resource]

@typing.type_check_only
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

@typing.type_check_only
class GoogleCloudAssetV1p4beta1Edge(typing_extensions.TypedDict, total=False):
    sourceNode: str
    targetNode: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1Identity(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    name: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1IdentityList(typing_extensions.TypedDict, total=False):
    groupEdges: typing.List[GoogleCloudAssetV1p4beta1Edge]
    identities: typing.List[GoogleCloudAssetV1p4beta1Identity]

@typing.type_check_only
class GoogleCloudAssetV1p4beta1Resource(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    fullResourceName: str

@typing.type_check_only
class IamPolicyAnalysis(typing_extensions.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    analysisResults: typing.List[IamPolicyAnalysisResult]
    fullyExplored: bool

@typing.type_check_only
class IamPolicyAnalysisOutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class IamPolicyAnalysisQuery(typing_extensions.TypedDict, total=False):
    accessSelector: AccessSelector
    identitySelector: IdentitySelector
    parent: str
    resourceSelector: ResourceSelector

@typing.type_check_only
class IamPolicyAnalysisResult(typing_extensions.TypedDict, total=False):
    accessControlLists: typing.List[GoogleCloudAssetV1p4beta1AccessControlList]
    attachedResourceFullName: str
    fullyExplored: bool
    iamBinding: Binding
    identityList: GoogleCloudAssetV1p4beta1IdentityList

@typing.type_check_only
class IdentitySelector(typing_extensions.TypedDict, total=False):
    identity: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Options(typing_extensions.TypedDict, total=False):
    analyzeServiceAccountImpersonation: bool
    expandGroups: bool
    expandResources: bool
    expandRoles: bool
    outputGroupEdges: bool
    outputResourceEdges: bool

@typing.type_check_only
class ResourceSelector(typing_extensions.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
