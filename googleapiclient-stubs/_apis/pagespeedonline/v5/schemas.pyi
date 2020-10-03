import typing

import typing_extensions

class LighthouseAuditResultV5(typing_extensions.TypedDict, total=False):
    scoreDisplayMode: str
    score: typing.Any
    explanation: str
    displayValue: str
    numericValue: float
    id: str
    errorMessage: str
    title: str
    description: str
    warnings: typing.Any
    details: typing.Dict[str, typing.Any]

class UserPageLoadMetricV5(typing_extensions.TypedDict, total=False):
    distributions: typing.List[Bucket]
    category: str
    percentile: int
    metricId: str
    formFactor: str
    median: int

class ConfigSettings(typing_extensions.TypedDict, total=False):
    onlyCategories: typing.Any
    locale: str
    emulatedFormFactor: str
    channel: str

class RendererFormattedStrings(typing_extensions.TypedDict, total=False):
    notApplicableAuditsGroupTitle: str
    opportunityResourceColumnLabel: str
    manualAuditsGroupTitle: str
    warningHeader: str
    varianceDisclaimer: str
    passedAuditsGroupTitle: str
    errorLabel: str
    toplevelWarningsMessage: str
    scorescaleLabel: str
    auditGroupExpandTooltip: str
    labDataTitle: str
    lsPerformanceCategoryDescription: str
    crcInitialNavigation: str
    crcLongestDurationLabel: str
    errorMissingAuditInfo: str
    opportunitySavingsColumnLabel: str

class Environment(typing_extensions.TypedDict, total=False):
    benchmarkIndex: float
    networkUserAgent: str
    hostUserAgent: str

class PagespeedApiLoadingExperienceV5(typing_extensions.TypedDict, total=False):
    metrics: typing.Dict[str, typing.Any]
    id: str
    overall_category: str
    origin_fallback: bool
    initial_url: str

class RuntimeError(typing_extensions.TypedDict, total=False):
    code: str
    message: str

class AuditRefs(typing_extensions.TypedDict, total=False):
    group: str
    id: str
    weight: float

class I18n(typing_extensions.TypedDict, total=False):
    rendererFormattedStrings: RendererFormattedStrings

class Bucket(typing_extensions.TypedDict, total=False):
    min: int
    proportion: float
    max: int

class CategoryGroupV5(typing_extensions.TypedDict, total=False):
    description: str
    title: str

class LighthouseResultV5(typing_extensions.TypedDict, total=False):
    environment: Environment
    runtimeError: RuntimeError
    configSettings: ConfigSettings
    stackPacks: typing.List[StackPack]
    userAgent: str
    fetchTime: str
    finalUrl: str
    timing: Timing
    categories: Categories
    categoryGroups: typing.Dict[str, typing.Any]
    audits: typing.Dict[str, typing.Any]
    runWarnings: typing.List[typing.Any]
    i18n: I18n
    lighthouseVersion: str
    requestedUrl: str

class StackPack(typing_extensions.TypedDict, total=False):
    title: str
    descriptions: typing.Dict[str, typing.Any]
    id: str
    iconDataURL: str

class PagespeedVersion(typing_extensions.TypedDict, total=False):
    minor: str
    major: str

class Timing(typing_extensions.TypedDict, total=False):
    total: float

class LighthouseCategoryV5(typing_extensions.TypedDict, total=False):
    title: str
    auditRefs: typing.List[AuditRefs]
    manualDescription: str
    score: typing.Any
    id: str
    description: str

Categories = typing_extensions.TypedDict(
    "Categories",
    {
        "seo": LighthouseCategoryV5,
        "best-practices": LighthouseCategoryV5,
        "accessibility": LighthouseCategoryV5,
        "performance": LighthouseCategoryV5,
        "pwa": LighthouseCategoryV5,
    },
    total=False,
)

class PagespeedApiPagespeedResponseV5(typing_extensions.TypedDict, total=False):
    version: PagespeedVersion
    kind: str
    id: str
    captchaResult: str
    originLoadingExperience: PagespeedApiLoadingExperienceV5
    loadingExperience: PagespeedApiLoadingExperienceV5
    analysisUTCTimestamp: str
    lighthouseResult: LighthouseResultV5
