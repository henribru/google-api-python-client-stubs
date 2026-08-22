import typing

_list = list

@typing.type_check_only
class Arg(typing.TypedDict, total=False):
    anyValue: Empty
    exactValue: typing.Any

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExpressionReport(typing.TypedDict, total=False):
    children: _list[ExpressionReport]
    sourcePosition: SourcePosition
    values: _list[ValueCount]

@typing.type_check_only
class File(typing.TypedDict, total=False):
    content: str
    fingerprint: str
    name: str

@typing.type_check_only
class FunctionCall(typing.TypedDict, total=False):
    args: _list[typing.Any]
    function: str

@typing.type_check_only
class FunctionMock(typing.TypedDict, total=False):
    args: _list[Arg]
    function: str
    result: Result

@typing.type_check_only
class GetReleaseExecutableResponse(typing.TypedDict, total=False):
    executable: str
    executableVersion: typing.Literal[
        "RELEASE_EXECUTABLE_VERSION_UNSPECIFIED",
        "FIREBASE_RULES_EXECUTABLE_V1",
        "FIREBASE_RULES_EXECUTABLE_V2",
    ]
    language: typing.Literal[
        "LANGUAGE_UNSPECIFIED", "FIREBASE_RULES", "EVENT_FLOW_TRIGGERS"
    ]
    rulesetName: str
    syncTime: str
    updateTime: str

@typing.type_check_only
class Issue(typing.TypedDict, total=False):
    description: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "DEPRECATION", "WARNING", "ERROR"]
    sourcePosition: SourcePosition

@typing.type_check_only
class ListReleasesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    releases: _list[Release]

@typing.type_check_only
class ListRulesetsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rulesets: _list[Ruleset]

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    services: _list[str]

@typing.type_check_only
class Release(typing.TypedDict, total=False):
    createTime: str
    name: str
    rulesetName: str
    updateTime: str

@typing.type_check_only
class Result(typing.TypedDict, total=False):
    undefined: Empty
    value: typing.Any

@typing.type_check_only
class Ruleset(typing.TypedDict, total=False):
    attachmentPoint: str
    createTime: str
    metadata: Metadata
    name: str
    source: Source

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    files: _list[File]

@typing.type_check_only
class SourcePosition(typing.TypedDict, total=False):
    column: int
    currentOffset: int
    endOffset: int
    fileName: str
    line: int

@typing.type_check_only
class TestCase(typing.TypedDict, total=False):
    expectation: typing.Literal["EXPECTATION_UNSPECIFIED", "ALLOW", "DENY"]
    expressionReportLevel: typing.Literal[
        "LEVEL_UNSPECIFIED", "NONE", "FULL", "VISITED"
    ]
    functionMocks: _list[FunctionMock]
    pathEncoding: typing.Literal["ENCODING_UNSPECIFIED", "URL_ENCODED", "PLAIN"]
    request: typing.Any
    resource: typing.Any

@typing.type_check_only
class TestResult(typing.TypedDict, total=False):
    debugMessages: _list[str]
    errorPosition: SourcePosition
    expressionReports: _list[ExpressionReport]
    functionCalls: _list[FunctionCall]
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCESS", "FAILURE"]
    visitedExpressions: _list[VisitedExpression]

@typing.type_check_only
class TestRulesetRequest(typing.TypedDict, total=False):
    source: Source
    testSuite: TestSuite

@typing.type_check_only
class TestRulesetResponse(typing.TypedDict, total=False):
    issues: _list[Issue]
    testResults: _list[TestResult]

@typing.type_check_only
class TestSuite(typing.TypedDict, total=False):
    testCases: _list[TestCase]

@typing.type_check_only
class UpdateReleaseRequest(typing.TypedDict, total=False):
    release: Release
    updateMask: str

@typing.type_check_only
class ValueCount(typing.TypedDict, total=False):
    count: int
    value: typing.Any

@typing.type_check_only
class VisitedExpression(typing.TypedDict, total=False):
    sourcePosition: SourcePosition
    value: typing.Any
