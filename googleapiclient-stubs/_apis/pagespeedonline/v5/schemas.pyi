import typing

import typing_extensions
@typing.type_check_only
class AuditRefs(typing_extensions.TypedDict, total=False):
    group: str
    id: str
    weight: float

@typing.type_check_only
class Bucket(typing_extensions.TypedDict, total=False):
    max: int
    min: int
    proportion: float

AlternativeCategories = typing_extensions.TypedDict(
    "AlternativeCategories",
    {
        "accessibility": LighthouseCategoryV5,
        "best-practices": LighthouseCategoryV5,
        "performance": LighthouseCategoryV5,
        "pwa": LighthouseCategoryV5,
        "seo": LighthouseCategoryV5,
    },
    total=False,
)
@typing.type_check_only
class Categories(AlternativeCategories): ...

@typing.type_check_only
class CategoryGroupV5(typing_extensions.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class ConfigSettings(typing_extensions.TypedDict, total=False):
    channel: str
    emulatedFormFactor: str
    formFactor: str
    locale: str
    onlyCategories: typing.Any

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    benchmarkIndex: float
    hostUserAgent: str
    networkUserAgent: str

@typing.type_check_only
class I18n(typing_extensions.TypedDict, total=False):
    rendererFormattedStrings: RendererFormattedStrings

@typing.type_check_only
class LighthouseAuditResultV5(typing_extensions.TypedDict, total=False):
    description: str
    details: typing.Dict[str, typing.Any]
    displayValue: str
    errorMessage: str
    explanation: str
    id: str
    numericValue: float
    score: typing.Any
    scoreDisplayMode: str
    title: str
    warnings: typing.Any

@typing.type_check_only
class LighthouseCategoryV5(typing_extensions.TypedDict, total=False):
    auditRefs: typing.List[AuditRefs]
    description: str
    id: str
    manualDescription: str
    score: typing.Any
    title: str

@typing.type_check_only
class LighthouseResultV5(typing_extensions.TypedDict, total=False):
    audits: typing.Dict[str, typing.Any]
    categories: Categories
    categoryGroups: typing.Dict[str, typing.Any]
    configSettings: ConfigSettings
    environment: Environment
    fetchTime: str
    finalUrl: str
    i18n: I18n
    lighthouseVersion: str
    requestedUrl: str
    runWarnings: typing.List[typing.Any]
    runtimeError: RuntimeError
    stackPacks: typing.List[StackPack]
    timing: Timing
    userAgent: str

@typing.type_check_only
class PagespeedApiLoadingExperienceV5(typing_extensions.TypedDict, total=False):
    id: str
    initial_url: str
    metrics: typing.Dict[str, typing.Any]
    origin_fallback: bool
    overall_category: str

@typing.type_check_only
class PagespeedApiPagespeedResponseV5(typing_extensions.TypedDict, total=False):
    analysisUTCTimestamp: str
    captchaResult: str
    id: str
    kind: str
    lighthouseResult: LighthouseResultV5
    loadingExperience: PagespeedApiLoadingExperienceV5
    originLoadingExperience: PagespeedApiLoadingExperienceV5
    version: PagespeedVersion

@typing.type_check_only
class PagespeedVersion(typing_extensions.TypedDict, total=False):
    major: str
    minor: str

@typing.type_check_only
class RendererFormattedStrings(typing_extensions.TypedDict, total=False):
    auditGroupExpandTooltip: str
    crcInitialNavigation: str
    crcLongestDurationLabel: str
    errorLabel: str
    errorMissingAuditInfo: str
    labDataTitle: str
    lsPerformanceCategoryDescription: str
    manualAuditsGroupTitle: str
    notApplicableAuditsGroupTitle: str
    opportunityResourceColumnLabel: str
    opportunitySavingsColumnLabel: str
    passedAuditsGroupTitle: str
    scorescaleLabel: str
    toplevelWarningsMessage: str
    varianceDisclaimer: str
    warningHeader: str

@typing.type_check_only
class RuntimeError(typing_extensions.TypedDict, total=False):
    code: str
    message: str

@typing.type_check_only
class StackPack(typing_extensions.TypedDict, total=False):
    descriptions: typing.Dict[str, typing.Any]
    iconDataURL: str
    id: str
    title: str

@typing.type_check_only
class Timing(typing_extensions.TypedDict, total=False):
    total: float

@typing.type_check_only
class UserPageLoadMetricV5(typing_extensions.TypedDict, total=False):
    category: str
    distributions: typing.List[Bucket]
    formFactor: str
    median: int
    metricId: str
    percentile: int
