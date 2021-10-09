import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditRefs(typing_extensions.TypedDict, total=False):
    acronym: str
    group: str
    id: str
    relevantAudits: _list[str]
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
    details: dict[str, typing.Any]
    displayValue: str
    errorMessage: str
    explanation: str
    id: str
    numericUnit: str
    numericValue: float
    score: typing.Any
    scoreDisplayMode: str
    title: str
    warnings: typing.Any

@typing.type_check_only
class LighthouseCategoryV5(typing_extensions.TypedDict, total=False):
    auditRefs: _list[AuditRefs]
    description: str
    id: str
    manualDescription: str
    score: typing.Any
    title: str

@typing.type_check_only
class LighthouseResultV5(typing_extensions.TypedDict, total=False):
    audits: dict[str, typing.Any]
    categories: Categories
    categoryGroups: dict[str, typing.Any]
    configSettings: ConfigSettings
    environment: Environment
    fetchTime: str
    finalUrl: str
    i18n: I18n
    lighthouseVersion: str
    requestedUrl: str
    runWarnings: _list[typing.Any]
    runtimeError: RuntimeError
    stackPacks: _list[StackPack]
    timing: Timing
    userAgent: str

@typing.type_check_only
class PagespeedApiLoadingExperienceV5(typing_extensions.TypedDict, total=False):
    id: str
    initial_url: str
    metrics: dict[str, typing.Any]
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
    calculatorLink: str
    crcInitialNavigation: str
    crcLongestDurationLabel: str
    dropdownCopyJSON: str
    dropdownDarkTheme: str
    dropdownPrintExpanded: str
    dropdownPrintSummary: str
    dropdownSaveGist: str
    dropdownSaveHTML: str
    dropdownSaveJSON: str
    dropdownViewer: str
    errorLabel: str
    errorMissingAuditInfo: str
    footerIssue: str
    labDataTitle: str
    lsPerformanceCategoryDescription: str
    manualAuditsGroupTitle: str
    notApplicableAuditsGroupTitle: str
    opportunityResourceColumnLabel: str
    opportunitySavingsColumnLabel: str
    passedAuditsGroupTitle: str
    runtimeDesktopEmulation: str
    runtimeMobileEmulation: str
    runtimeNoEmulation: str
    runtimeSettingsAxeVersion: str
    runtimeSettingsBenchmark: str
    runtimeSettingsCPUThrottling: str
    runtimeSettingsChannel: str
    runtimeSettingsDevice: str
    runtimeSettingsFetchTime: str
    runtimeSettingsNetworkThrottling: str
    runtimeSettingsTitle: str
    runtimeSettingsUA: str
    runtimeSettingsUANetwork: str
    runtimeSettingsUrl: str
    runtimeUnknown: str
    scorescaleLabel: str
    showRelevantAudits: str
    snippetCollapseButtonLabel: str
    snippetExpandButtonLabel: str
    thirdPartyResourcesLabel: str
    throttlingProvided: str
    toplevelWarningsMessage: str
    varianceDisclaimer: str
    viewTreemapLabel: str
    warningAuditsGroupTitle: str
    warningHeader: str

@typing.type_check_only
class RuntimeError(typing_extensions.TypedDict, total=False):
    code: str
    message: str

@typing.type_check_only
class StackPack(typing_extensions.TypedDict, total=False):
    descriptions: dict[str, typing.Any]
    iconDataURL: str
    id: str
    title: str

@typing.type_check_only
class Timing(typing_extensions.TypedDict, total=False):
    total: float

@typing.type_check_only
class UserPageLoadMetricV5(typing_extensions.TypedDict, total=False):
    category: str
    distributions: _list[Bucket]
    formFactor: str
    median: int
    metricId: str
    percentile: int
