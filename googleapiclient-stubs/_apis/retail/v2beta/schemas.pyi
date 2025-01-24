import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudRetailLoggingErrorContext(typing_extensions.TypedDict, total=False):
    httpRequest: GoogleCloudRetailLoggingHttpRequestContext
    reportLocation: GoogleCloudRetailLoggingSourceLocation

@typing.type_check_only
class GoogleCloudRetailLoggingErrorLog(typing_extensions.TypedDict, total=False):
    context: GoogleCloudRetailLoggingErrorContext
    importPayload: GoogleCloudRetailLoggingImportErrorContext
    message: str
    requestPayload: dict[str, typing.Any]
    responsePayload: dict[str, typing.Any]
    serviceContext: GoogleCloudRetailLoggingServiceContext
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudRetailLoggingHttpRequestContext(
    typing_extensions.TypedDict, total=False
):
    responseStatusCode: int

@typing.type_check_only
class GoogleCloudRetailLoggingImportErrorContext(
    typing_extensions.TypedDict, total=False
):
    catalogItem: str
    gcsPath: str
    lineNumber: str
    operationName: str
    product: str
    userEvent: str

@typing.type_check_only
class GoogleCloudRetailLoggingServiceContext(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudRetailLoggingSourceLocation(typing_extensions.TypedDict, total=False):
    functionName: str

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2BigQueryOutputResult(typing_extensions.TypedDict, total=False):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2CreateModelMetadata(typing_extensions.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2ExportAnalyticsMetricsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ExportErrorsConfig
    outputResult: GoogleCloudRetailV2OutputResult

@typing.type_check_only
class GoogleCloudRetailV2ExportErrorsConfig(typing_extensions.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2ExportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2GcsOutputResult(typing_extensions.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2ImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2ImportErrorsConfig(typing_extensions.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2ImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2ImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig
    importSummary: GoogleCloudRetailV2UserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2Model(typing_extensions.TypedDict, total=False):
    createTime: str
    dataState: typing_extensions.Literal[
        "DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"
    ]
    displayName: str
    filteringOption: typing_extensions.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    modelFeaturesConfig: GoogleCloudRetailV2ModelModelFeaturesConfig
    name: str
    optimizationObjective: str
    periodicTuningState: typing_extensions.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2ModelServingConfigList]
    servingState: typing_extensions.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing_extensions.Literal[
        "TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"
    ]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfig(
    typing_extensions.TypedDict, total=False
):
    contextProductsType: typing_extensions.Literal[
        "CONTEXT_PRODUCTS_TYPE_UNSPECIFIED",
        "SINGLE_CONTEXT_PRODUCT",
        "MULTIPLE_CONTEXT_PRODUCTS",
    ]

@typing.type_check_only
class GoogleCloudRetailV2ModelModelFeaturesConfig(
    typing_extensions.TypedDict, total=False
):
    frequentlyBoughtTogetherConfig: (
        GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfig
    )

@typing.type_check_only
class GoogleCloudRetailV2ModelServingConfigList(
    typing_extensions.TypedDict, total=False
):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2OutputResult(typing_extensions.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2BigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2GcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2PurgeMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2PurgeProductsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2PurgeProductsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2PurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2TuneModelMetadata(typing_extensions.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2TuneModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2UserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQueryOutputResult(
    typing_extensions.TypedDict, total=False
):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCreateModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2alphaEnrollSolutionMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaEnrollSolutionResponse(
    typing_extensions.TypedDict, total=False
):
    enrolledSolution: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaExportAnalyticsMetricsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaExportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaExportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaGcsOutputResult(typing_extensions.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2alphaImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    transformedUserEventsMetadata: GoogleCloudRetailV2alphaTransformedUserEventsMetadata
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    importSummary: GoogleCloudRetailV2alphaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterAccountLink(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    feedFilters: _list[
        GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilter
    ]
    feedLabel: str
    id: str
    languageCode: str
    merchantCenterAccountId: str
    name: str
    projectId: str
    source: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilter(
    typing_extensions.TypedDict, total=False
):
    primaryFeedId: str
    primaryFeedName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModel(typing_extensions.TypedDict, total=False):
    createTime: str
    dataState: typing_extensions.Literal[
        "DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"
    ]
    displayName: str
    filteringOption: typing_extensions.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    modelFeaturesConfig: GoogleCloudRetailV2alphaModelModelFeaturesConfig
    name: str
    optimizationObjective: str
    pageOptimizationConfig: GoogleCloudRetailV2alphaModelPageOptimizationConfig
    periodicTuningState: typing_extensions.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2alphaModelServingConfigList]
    servingState: typing_extensions.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing_extensions.Literal[
        "TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"
    ]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfig(
    typing_extensions.TypedDict, total=False
):
    contextProductsType: typing_extensions.Literal[
        "CONTEXT_PRODUCTS_TYPE_UNSPECIFIED",
        "SINGLE_CONTEXT_PRODUCT",
        "MULTIPLE_CONTEXT_PRODUCTS",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaModelModelFeaturesConfig(
    typing_extensions.TypedDict, total=False
):
    frequentlyBoughtTogetherConfig: (
        GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfig
    )

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfig(
    typing_extensions.TypedDict, total=False
):
    pageOptimizationEventType: str
    panels: _list[GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel]
    restriction: typing_extensions.Literal[
        "RESTRICTION_UNSPECIFIED",
        "NO_RESTRICTION",
        "UNIQUE_SERVING_CONFIG_RESTRICTION",
        "UNIQUE_MODEL_RESTRICTION",
        "UNIQUE_MODEL_TYPE_RESTRICTION",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate(
    typing_extensions.TypedDict, total=False
):
    servingConfigId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate]
    defaultCandidate: GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate
    displayName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelServingConfigList(
    typing_extensions.TypedDict, total=False
):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaOutputResult(typing_extensions.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2alphaBigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2alphaGcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaTransformedUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    sourceEventsCount: str
    transformedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2betaCatalogAttribute

@typing.type_check_only
class GoogleCloudRetailV2betaAddControlRequest(
    typing_extensions.TypedDict, total=False
):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    addTime: str
    allowMissing: bool
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesRequest(
    typing_extensions.TypedDict, total=False
):
    addMask: str
    addTime: str
    allowMissing: bool
    localInventories: _list[GoogleCloudRetailV2betaLocalInventory]

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAlertConfig(typing_extensions.TypedDict, total=False):
    alertPolicies: _list[GoogleCloudRetailV2betaAlertConfigAlertPolicy]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2betaAlertConfigAlertPolicy(
    typing_extensions.TypedDict, total=False
):
    alertGroup: str
    enrollStatus: typing_extensions.Literal[
        "ENROLL_STATUS_UNSPECIFIED", "ENROLLED", "DECLINED"
    ]
    recipients: _list[GoogleCloudRetailV2betaAlertConfigAlertPolicyRecipient]

@typing.type_check_only
class GoogleCloudRetailV2betaAlertConfigAlertPolicyRecipient(
    typing_extensions.TypedDict, total=False
):
    emailAddress: str

@typing.type_check_only
class GoogleCloudRetailV2betaAttributesConfig(typing_extensions.TypedDict, total=False):
    attributeConfigLevel: typing_extensions.Literal[
        "ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED",
        "PRODUCT_LEVEL_ATTRIBUTE_CONFIG",
        "CATALOG_LEVEL_ATTRIBUTE_CONFIG",
    ]
    catalogAttributes: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2betaAudience(typing_extensions.TypedDict, total=False):
    ageGroups: _list[str]
    genders: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchRemoveCatalogAttributesRequest(
    typing_extensions.TypedDict, total=False
):
    attributeKeys: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchRemoveCatalogAttributesResponse(
    typing_extensions.TypedDict, total=False
):
    deletedCatalogAttributes: _list[str]
    resetCatalogAttributes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudRetailV2betaUpdateGenerativeQuestionConfigRequest]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2betaGenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2betaBigQueryOutputResult(
    typing_extensions.TypedDict, total=False
):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaBigQuerySource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaCatalog(typing_extensions.TypedDict, total=False):
    displayName: str
    merchantCenterLinkingConfig: GoogleCloudRetailV2betaMerchantCenterLinkingConfig
    name: str
    productLevelConfig: GoogleCloudRetailV2betaProductLevelConfig

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttribute(typing_extensions.TypedDict, total=False):
    dynamicFacetableOption: typing_extensions.Literal[
        "DYNAMIC_FACETABLE_OPTION_UNSPECIFIED",
        "DYNAMIC_FACETABLE_ENABLED",
        "DYNAMIC_FACETABLE_DISABLED",
    ]
    exactSearchableOption: typing_extensions.Literal[
        "EXACT_SEARCHABLE_OPTION_UNSPECIFIED",
        "EXACT_SEARCHABLE_ENABLED",
        "EXACT_SEARCHABLE_DISABLED",
    ]
    facetConfig: GoogleCloudRetailV2betaCatalogAttributeFacetConfig
    inUse: bool
    indexableOption: typing_extensions.Literal[
        "INDEXABLE_OPTION_UNSPECIFIED", "INDEXABLE_ENABLED", "INDEXABLE_DISABLED"
    ]
    key: str
    recommendationsFilteringOption: typing_extensions.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    retrievableOption: typing_extensions.Literal[
        "RETRIEVABLE_OPTION_UNSPECIFIED", "RETRIEVABLE_ENABLED", "RETRIEVABLE_DISABLED"
    ]
    searchableOption: typing_extensions.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]
    type: typing_extensions.Literal["UNKNOWN", "TEXTUAL", "NUMERICAL"]

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfig(
    typing_extensions.TypedDict, total=False
):
    facetIntervals: _list[GoogleCloudRetailV2betaInterval]
    ignoredFacetValues: _list[
        GoogleCloudRetailV2betaCatalogAttributeFacetConfigIgnoredFacetValues
    ]
    mergedFacet: GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacet
    mergedFacetValues: _list[
        GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacetValue
    ]
    rerankConfig: GoogleCloudRetailV2betaCatalogAttributeFacetConfigRerankConfig

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigIgnoredFacetValues(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacet(
    typing_extensions.TypedDict, total=False
):
    mergedFacetKey: str

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacetValue(
    typing_extensions.TypedDict, total=False
):
    mergedValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigRerankConfig(
    typing_extensions.TypedDict, total=False
):
    facetValues: _list[str]
    rerankFacet: bool

@typing.type_check_only
class GoogleCloudRetailV2betaCollectUserEventRequest(
    typing_extensions.TypedDict, total=False
):
    ets: str
    prebuiltRule: str
    rawJson: str
    uri: str
    userEvent: str

@typing.type_check_only
class GoogleCloudRetailV2betaColorInfo(typing_extensions.TypedDict, total=False):
    colorFamilies: _list[str]
    colors: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponse(
    typing_extensions.TypedDict, total=False
):
    attributeResults: dict[str, typing.Any]
    attributionToken: str
    completionResults: _list[
        GoogleCloudRetailV2betaCompleteQueryResponseCompletionResult
    ]
    recentSearchResults: _list[
        GoogleCloudRetailV2betaCompleteQueryResponseRecentSearchResult
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseAttributeResult(
    typing_extensions.TypedDict, total=False
):
    suggestions: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseCompletionResult(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    suggestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseRecentSearchResult(
    typing_extensions.TypedDict, total=False
):
    recentSearch: str

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionConfig(typing_extensions.TypedDict, total=False):
    allowlistInputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig
    autoLearning: bool
    denylistInputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig
    lastAllowlistImportOperation: str
    lastDenylistImportOperation: str
    lastSuggestionsImportOperation: str
    matchingOrder: str
    maxSuggestions: int
    minPrefixLength: int
    name: str
    suggestionsInputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionDataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRetailV2betaBigQuerySource

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionDetail(typing_extensions.TypedDict, total=False):
    completionAttributionToken: str
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaCondition(typing_extensions.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudRetailV2betaConditionTimeRange]
    pageCategories: _list[str]
    queryTerms: _list[GoogleCloudRetailV2betaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudRetailV2betaConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaControl(typing_extensions.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    displayName: str
    facetSpec: GoogleCloudRetailV2betaSearchRequestFacetSpec
    name: str
    rule: GoogleCloudRetailV2betaRule
    searchSolutionUseCase: _list[
        typing_extensions.Literal[
            "SEARCH_SOLUTION_USE_CASE_UNSPECIFIED",
            "SEARCH_SOLUTION_USE_CASE_SEARCH",
            "SEARCH_SOLUTION_USE_CASE_BROWSE",
        ]
    ]
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
        ]
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaCreateModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaCustomAttribute(typing_extensions.TypedDict, total=False):
    indexable: bool
    numbers: _list[float]
    searchable: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaExperimentInfo(typing_extensions.TypedDict, total=False):
    experiment: str
    servingConfigExperiment: (
        GoogleCloudRetailV2betaExperimentInfoServingConfigExperiment
    )

@typing.type_check_only
class GoogleCloudRetailV2betaExperimentInfoServingConfigExperiment(
    typing_extensions.TypedDict, total=False
):
    experimentServingConfig: str
    originalServingConfig: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportAnalyticsMetricsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    outputConfig: GoogleCloudRetailV2betaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaExportAnalyticsMetricsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaExportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportProductsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    outputConfig: GoogleCloudRetailV2betaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaExportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaExportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    outputConfig: GoogleCloudRetailV2betaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaExportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaFulfillmentInfo(typing_extensions.TypedDict, total=False):
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaGcsOutputResult(typing_extensions.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2betaGcsSource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaGenerativeQuestionConfig(
    typing_extensions.TypedDict, total=False
):
    allowedInConversation: bool
    catalog: str
    exampleValues: _list[str]
    facet: str
    finalQuestion: str
    frequency: float
    generatedQuestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaGenerativeQuestionsFeatureConfig(
    typing_extensions.TypedDict, total=False
):
    catalog: str
    featureEnabled: bool
    minimumProducts: int

@typing.type_check_only
class GoogleCloudRetailV2betaGetDefaultBranchResponse(
    typing_extensions.TypedDict, total=False
):
    branch: str
    note: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaImage(typing_extensions.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRetailV2betaImportCompletionDataRequest(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig
    notificationPubsubTopic: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2betaImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportProductsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2betaProductInputConfig
    notificationPubsubTopic: str
    reconciliationMode: typing_extensions.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    requestId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2betaUserEventInputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    importSummary: GoogleCloudRetailV2betaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2betaInterval(typing_extensions.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudRetailV2betaListCatalogsResponse(
    typing_extensions.TypedDict, total=False
):
    catalogs: _list[GoogleCloudRetailV2betaCatalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListControlsResponse(
    typing_extensions.TypedDict, total=False
):
    controls: _list[GoogleCloudRetailV2betaControl]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListGenerativeQuestionConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2betaGenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2betaListModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudRetailV2betaModel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListProductsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    products: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaListServingConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudRetailV2betaServingConfig]

@typing.type_check_only
class GoogleCloudRetailV2betaLocalInventory(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    availability: typing_extensions.Literal[
        "AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    fulfillmentTypes: _list[str]
    placeId: str
    priceInfo: GoogleCloudRetailV2betaPriceInfo

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterFeedFilter(
    typing_extensions.TypedDict, total=False
):
    primaryFeedId: str
    primaryFeedName: str

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterLink(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    destinations: _list[str]
    feeds: _list[GoogleCloudRetailV2betaMerchantCenterFeedFilter]
    languageCode: str
    merchantCenterAccountId: str
    regionCode: str

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterLinkingConfig(
    typing_extensions.TypedDict, total=False
):
    links: _list[GoogleCloudRetailV2betaMerchantCenterLink]

@typing.type_check_only
class GoogleCloudRetailV2betaModel(typing_extensions.TypedDict, total=False):
    createTime: str
    dataState: typing_extensions.Literal[
        "DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"
    ]
    displayName: str
    filteringOption: typing_extensions.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    modelFeaturesConfig: GoogleCloudRetailV2betaModelModelFeaturesConfig
    name: str
    optimizationObjective: str
    periodicTuningState: typing_extensions.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2betaModelServingConfigList]
    servingState: typing_extensions.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing_extensions.Literal[
        "TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"
    ]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfig(
    typing_extensions.TypedDict, total=False
):
    contextProductsType: typing_extensions.Literal[
        "CONTEXT_PRODUCTS_TYPE_UNSPECIFIED",
        "SINGLE_CONTEXT_PRODUCT",
        "MULTIPLE_CONTEXT_PRODUCTS",
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaModelModelFeaturesConfig(
    typing_extensions.TypedDict, total=False
):
    frequentlyBoughtTogetherConfig: (
        GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfig
    )

@typing.type_check_only
class GoogleCloudRetailV2betaModelServingConfigList(
    typing_extensions.TypedDict, total=False
):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaOutputConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudRetailV2betaOutputConfigBigQueryDestination
    gcsDestination: GoogleCloudRetailV2betaOutputConfigGcsDestination

@typing.type_check_only
class GoogleCloudRetailV2betaOutputConfigBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    datasetId: str
    tableIdPrefix: str
    tableType: str

@typing.type_check_only
class GoogleCloudRetailV2betaOutputConfigGcsDestination(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaOutputResult(typing_extensions.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2betaBigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2betaGcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2betaPauseModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPinControlMetadata(
    typing_extensions.TypedDict, total=False
):
    allMatchedPins: dict[str, typing.Any]
    droppedPins: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaPinControlMetadataProductPins(
    typing_extensions.TypedDict, total=False
):
    productId: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaPredictRequest(typing_extensions.TypedDict, total=False):
    filter: str
    labels: dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    userEvent: GoogleCloudRetailV2betaUserEvent
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponse(typing_extensions.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudRetailV2betaPredictResponsePredictionResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponsePredictionResult(
    typing_extensions.TypedDict, total=False
):
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaPriceInfo(typing_extensions.TypedDict, total=False):
    cost: float
    currencyCode: str
    originalPrice: float
    price: float
    priceEffectiveTime: str
    priceExpireTime: str
    priceRange: GoogleCloudRetailV2betaPriceInfoPriceRange

@typing.type_check_only
class GoogleCloudRetailV2betaPriceInfoPriceRange(
    typing_extensions.TypedDict, total=False
):
    originalPrice: GoogleCloudRetailV2betaInterval
    price: GoogleCloudRetailV2betaInterval

@typing.type_check_only
class GoogleCloudRetailV2betaProduct(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    audience: GoogleCloudRetailV2betaAudience
    availability: typing_extensions.Literal[
        "AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    availableQuantity: int
    availableTime: str
    brands: _list[str]
    categories: _list[str]
    collectionMemberIds: _list[str]
    colorInfo: GoogleCloudRetailV2betaColorInfo
    conditions: _list[str]
    description: str
    expireTime: str
    fulfillmentInfo: _list[GoogleCloudRetailV2betaFulfillmentInfo]
    gtin: str
    id: str
    images: _list[GoogleCloudRetailV2betaImage]
    languageCode: str
    localInventories: _list[GoogleCloudRetailV2betaLocalInventory]
    materials: _list[str]
    name: str
    patterns: _list[str]
    priceInfo: GoogleCloudRetailV2betaPriceInfo
    primaryProductId: str
    promotions: _list[GoogleCloudRetailV2betaPromotion]
    publishTime: str
    rating: GoogleCloudRetailV2betaRating
    retrievableFields: str
    sizes: _list[str]
    tags: _list[str]
    title: str
    ttl: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PRIMARY", "VARIANT", "COLLECTION"
    ]
    uri: str
    variants: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaProductAttributeInterval(
    typing_extensions.TypedDict, total=False
):
    interval: GoogleCloudRetailV2betaInterval
    name: str

@typing.type_check_only
class GoogleCloudRetailV2betaProductAttributeValue(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaProductDetail(typing_extensions.TypedDict, total=False):
    product: GoogleCloudRetailV2betaProduct
    quantity: int

@typing.type_check_only
class GoogleCloudRetailV2betaProductInlineSource(
    typing_extensions.TypedDict, total=False
):
    products: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaProductInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRetailV2betaBigQuerySource
    gcsSource: GoogleCloudRetailV2betaGcsSource
    productInlineSource: GoogleCloudRetailV2betaProductInlineSource

@typing.type_check_only
class GoogleCloudRetailV2betaProductLevelConfig(
    typing_extensions.TypedDict, total=False
):
    ingestionProductType: str
    merchantCenterProductIdField: str

@typing.type_check_only
class GoogleCloudRetailV2betaPromotion(typing_extensions.TypedDict, total=False):
    promotionId: str

@typing.type_check_only
class GoogleCloudRetailV2betaPurchaseTransaction(
    typing_extensions.TypedDict, total=False
):
    cost: float
    currencyCode: str
    id: str
    revenue: float
    tax: float

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRating(typing_extensions.TypedDict, total=False):
    averageRating: float
    ratingCount: int
    ratingHistogram: _list[int]

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    userEventRejoinScope: typing_extensions.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveControlRequest(
    typing_extensions.TypedDict, total=False
):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaReplaceCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2betaCatalogAttribute
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaResumeModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRule(typing_extensions.TypedDict, total=False):
    boostAction: GoogleCloudRetailV2betaRuleBoostAction
    condition: GoogleCloudRetailV2betaCondition
    doNotAssociateAction: GoogleCloudRetailV2betaRuleDoNotAssociateAction
    filterAction: GoogleCloudRetailV2betaRuleFilterAction
    forceReturnFacetAction: GoogleCloudRetailV2betaRuleForceReturnFacetAction
    ignoreAction: GoogleCloudRetailV2betaRuleIgnoreAction
    onewaySynonymsAction: GoogleCloudRetailV2betaRuleOnewaySynonymsAction
    pinAction: GoogleCloudRetailV2betaRulePinAction
    redirectAction: GoogleCloudRetailV2betaRuleRedirectAction
    removeFacetAction: GoogleCloudRetailV2betaRuleRemoveFacetAction
    replacementAction: GoogleCloudRetailV2betaRuleReplacementAction
    twowaySynonymsAction: GoogleCloudRetailV2betaRuleTwowaySynonymsAction

@typing.type_check_only
class GoogleCloudRetailV2betaRuleBoostAction(typing_extensions.TypedDict, total=False):
    boost: float
    productsFilter: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleDoNotAssociateAction(
    typing_extensions.TypedDict, total=False
):
    doNotAssociateTerms: _list[str]
    queryTerms: _list[str]
    terms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleFilterAction(typing_extensions.TypedDict, total=False):
    filter: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleForceReturnFacetAction(
    typing_extensions.TypedDict, total=False
):
    facetPositionAdjustments: _list[
        GoogleCloudRetailV2betaRuleForceReturnFacetActionFacetPositionAdjustment
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleForceReturnFacetActionFacetPositionAdjustment(
    typing_extensions.TypedDict, total=False
):
    attributeName: str
    position: int

@typing.type_check_only
class GoogleCloudRetailV2betaRuleIgnoreAction(typing_extensions.TypedDict, total=False):
    ignoreTerms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleOnewaySynonymsAction(
    typing_extensions.TypedDict, total=False
):
    onewayTerms: _list[str]
    queryTerms: _list[str]
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRulePinAction(typing_extensions.TypedDict, total=False):
    pinMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleRemoveFacetAction(
    typing_extensions.TypedDict, total=False
):
    attributeNames: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleReplacementAction(
    typing_extensions.TypedDict, total=False
):
    queryTerms: _list[str]
    replacementTerm: str
    term: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleTwowaySynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequest(typing_extensions.TypedDict, total=False):
    boostSpec: GoogleCloudRetailV2betaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    conversationalSearchSpec: (
        GoogleCloudRetailV2betaSearchRequestConversationalSearchSpec
    )
    dynamicFacetSpec: GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec
    entity: str
    facetSpecs: _list[GoogleCloudRetailV2betaSearchRequestFacetSpec]
    filter: str
    labels: dict[str, typing.Any]
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    personalizationSpec: GoogleCloudRetailV2betaSearchRequestPersonalizationSpec
    query: str
    queryExpansionSpec: GoogleCloudRetailV2betaSearchRequestQueryExpansionSpec
    searchMode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED", "PRODUCT_SEARCH_ONLY", "FACETED_SEARCH_ONLY"
    ]
    spellCorrectionSpec: GoogleCloudRetailV2betaSearchRequestSpellCorrectionSpec
    tileNavigationSpec: GoogleCloudRetailV2betaSearchRequestTileNavigationSpec
    userInfo: GoogleCloudRetailV2betaUserInfo
    variantRollupKeys: _list[str]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec
    ]
    skipBoostSpecValidation: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestConversationalSearchSpec(
    typing_extensions.TypedDict, total=False
):
    conversationId: str
    followupConversationRequested: bool
    userAnswer: GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswer

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswer(
    typing_extensions.TypedDict, total=False
):
    selectedAnswer: GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswerSelectedAnswer
    textAnswer: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswerSelectedAnswer(
    typing_extensions.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue
    productAttributeValues: _list[GoogleCloudRetailV2betaProductAttributeValue]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudRetailV2betaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudRetailV2betaInterval]
    key: str
    orderBy: str
    prefixes: _list[str]
    query: str
    restrictedValues: _list[str]
    returnMinMax: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestPersonalizationSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestTileNavigationSpec(
    typing_extensions.TypedDict, total=False
):
    appliedTiles: _list[GoogleCloudRetailV2betaTile]
    tileNavigationRequested: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponse(typing_extensions.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    conversationalSearchResult: (
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResult
    )
    correctedQuery: str
    experimentInfo: _list[GoogleCloudRetailV2betaExperimentInfo]
    facets: _list[GoogleCloudRetailV2betaSearchResponseFacet]
    invalidConditionBoostSpecs: _list[
        GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec
    ]
    nextPageToken: str
    pinControlMetadata: GoogleCloudRetailV2betaPinControlMetadata
    queryExpansionInfo: GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudRetailV2betaSearchResponseSearchResult]
    tileNavigationResult: GoogleCloudRetailV2betaSearchResponseTileNavigationResult
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseConversationalSearchResult(
    typing_extensions.TypedDict, total=False
):
    additionalFilter: (
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResultAdditionalFilter
    )
    additionalFilters: _list[
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResultAdditionalFilter
    ]
    conversationId: str
    followupQuestion: str
    refinedQuery: str
    suggestedAnswers: _list[
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResultSuggestedAnswer
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseConversationalSearchResultAdditionalFilter(
    typing_extensions.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseConversationalSearchResultSuggestedAnswer(
    typing_extensions.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseFacet(
    typing_extensions.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudRetailV2betaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseFacetFacetValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    interval: GoogleCloudRetailV2betaInterval
    maxValue: float
    minValue: float
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo(
    typing_extensions.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseSearchResult(
    typing_extensions.TypedDict, total=False
):
    id: str
    matchingVariantCount: int
    matchingVariantFields: dict[str, typing.Any]
    personalLabels: _list[str]
    product: GoogleCloudRetailV2betaProduct
    variantRollupValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseTileNavigationResult(
    typing_extensions.TypedDict, total=False
):
    tiles: _list[GoogleCloudRetailV2betaTile]

@typing.type_check_only
class GoogleCloudRetailV2betaServingConfig(typing_extensions.TypedDict, total=False):
    boostControlIds: _list[str]
    displayName: str
    diversityLevel: str
    diversityType: typing_extensions.Literal[
        "DIVERSITY_TYPE_UNSPECIFIED", "RULE_BASED_DIVERSITY", "DATA_DRIVEN_DIVERSITY"
    ]
    doNotAssociateControlIds: _list[str]
    dynamicFacetSpec: GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec
    enableCategoryFilterLevel: str
    facetControlIds: _list[str]
    filterControlIds: _list[str]
    ignoreControlIds: _list[str]
    ignoreRecsDenylist: bool
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    personalizationSpec: GoogleCloudRetailV2betaSearchRequestPersonalizationSpec
    priceRerankingLevel: str
    redirectControlIds: _list[str]
    replacementControlIds: _list[str]
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
        ]
    ]
    twowaySynonymsControlIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaSetDefaultBranchRequest(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    force: bool
    note: str

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    inventory: GoogleCloudRetailV2betaProduct
    setMask: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaTile(typing_extensions.TypedDict, total=False):
    productAttributeInterval: GoogleCloudRetailV2betaProductAttributeInterval
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue
    representativeProductId: str

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaUpdateGenerativeQuestionConfigRequest(
    typing_extensions.TypedDict, total=False
):
    generativeQuestionConfig: GoogleCloudRetailV2betaGenerativeQuestionConfig
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaUserEvent(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    attributionToken: str
    cartId: str
    completionDetail: GoogleCloudRetailV2betaCompletionDetail
    entity: str
    eventTime: str
    eventType: str
    experimentIds: _list[str]
    filter: str
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageViewId: str
    productDetails: _list[GoogleCloudRetailV2betaProductDetail]
    purchaseTransaction: GoogleCloudRetailV2betaPurchaseTransaction
    referrerUri: str
    searchQuery: str
    sessionId: str
    uri: str
    userInfo: GoogleCloudRetailV2betaUserInfo
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudRetailV2betaUserEvent]

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRetailV2betaBigQuerySource
    gcsSource: GoogleCloudRetailV2betaGcsSource
    userEventInlineSource: GoogleCloudRetailV2betaUserEventInlineSource

@typing.type_check_only
class GoogleCloudRetailV2betaUserInfo(typing_extensions.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int
