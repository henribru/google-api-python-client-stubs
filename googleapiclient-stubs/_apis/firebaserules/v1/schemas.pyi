import typing

import typing_extensions

class TestSuite(typing_extensions.TypedDict, total=False):
    testCases: typing.List[TestCase]

class Ruleset(typing_extensions.TypedDict, total=False):
    createTime: str
    source: Source
    metadata: Metadata
    name: str

class ExpressionReport(typing.Dict[str, typing.Any]): ...

class GetReleaseExecutableResponse(typing_extensions.TypedDict, total=False):
    syncTime: str
    executable: str
    executableVersion: typing_extensions.Literal[
        "RELEASE_EXECUTABLE_VERSION_UNSPECIFIED",
        "FIREBASE_RULES_EXECUTABLE_V1",
        "FIREBASE_RULES_EXECUTABLE_V2",
    ]
    updateTime: str
    rulesetName: str
    language: typing_extensions.Literal[
        "LANGUAGE_UNSPECIFIED", "FIREBASE_RULES", "EVENT_FLOW_TRIGGERS"
    ]

class UpdateReleaseRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    release: Release

class TestResult(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "SUCCESS", "FAILURE"]
    functionCalls: typing.List[FunctionCall]
    errorPosition: SourcePosition
    visitedExpressions: typing.List[VisitedExpression]
    expressionReports: typing.List[ExpressionReport]
    debugMessages: typing.List[str]

class Issue(typing_extensions.TypedDict, total=False):
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "DEPRECATION", "WARNING", "ERROR"
    ]
    sourcePosition: SourcePosition
    description: str

class SourcePosition(typing_extensions.TypedDict, total=False):
    endOffset: int
    currentOffset: int
    column: int
    line: int
    fileName: str

class ListRulesetsResponse(typing_extensions.TypedDict, total=False):
    rulesets: typing.List[Ruleset]
    nextPageToken: str

class ValueCount(typing_extensions.TypedDict, total=False):
    value: typing.Any
    count: int

class ListReleasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releases: typing.List[Release]

class Release(typing_extensions.TypedDict, total=False):
    updateTime: str
    name: str
    rulesetName: str
    createTime: str

class FunctionMock(typing_extensions.TypedDict, total=False):
    args: typing.List[Arg]
    result: Result
    function: str

class TestCase(typing_extensions.TypedDict, total=False):
    functionMocks: typing.List[FunctionMock]
    request: typing.Any
    resource: typing.Any
    expectation: typing_extensions.Literal["EXPECTATION_UNSPECIFIED", "ALLOW", "DENY"]
    pathEncoding: typing_extensions.Literal[
        "ENCODING_UNSPECIFIED", "URL_ENCODED", "PLAIN"
    ]
    expressionReportLevel: typing_extensions.Literal[
        "LEVEL_UNSPECIFIED", "NONE", "FULL", "VISITED"
    ]

class Result(typing_extensions.TypedDict, total=False):
    value: typing.Any
    undefined: Empty

class FunctionCall(typing_extensions.TypedDict, total=False):
    args: typing.List[typing.Any]
    function: str

class Metadata(typing_extensions.TypedDict, total=False):
    services: typing.List[str]

class TestRulesetResponse(typing_extensions.TypedDict, total=False):
    testResults: typing.List[TestResult]
    issues: typing.List[Issue]

class TestRulesetRequest(typing_extensions.TypedDict, total=False):
    testSuite: TestSuite
    source: Source

class Empty(typing_extensions.TypedDict, total=False): ...

class Arg(typing_extensions.TypedDict, total=False):
    exactValue: typing.Any
    anyValue: Empty

class File(typing_extensions.TypedDict, total=False):
    name: str
    content: str
    fingerprint: str

class VisitedExpression(typing_extensions.TypedDict, total=False):
    value: typing.Any
    sourcePosition: SourcePosition

class Source(typing_extensions.TypedDict, total=False):
    files: typing.List[File]
