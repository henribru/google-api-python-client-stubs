import typing

import typing_extensions

_list = list

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    builtinSimpleAction: BuiltInSimpleAction
    builtinUserInputAction: BuiltInUserInputAction
    buttonLabel: str
    externalAction: ExternalAction
    isAvailable: bool
    reasons: _list[Reason]

@typing.type_check_only
class ActionFlow(typing_extensions.TypedDict, total=False):
    dialogButtonLabel: str
    dialogCallout: Callout
    dialogMessage: TextWithTooltip
    dialogTitle: str
    id: str
    inputs: _list[InputField]
    label: str

@typing.type_check_only
class ActionInput(typing_extensions.TypedDict, total=False):
    actionFlowId: str
    inputValues: _list[InputValue]

@typing.type_check_only
class AdditionalContent(typing_extensions.TypedDict, total=False):
    paragraphs: _list[str]
    title: str

@typing.type_check_only
class AggregateProductStatus(typing_extensions.TypedDict, total=False):
    country: str
    itemLevelIssues: _list[ItemLevelIssue]
    name: str
    reportingContext: typing_extensions.Literal[
        "REPORTING_CONTEXT_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISCOVERY_ADS",
        "DEMAND_GEN_ADS",
        "DEMAND_GEN_ADS_DISCOVER_SURFACE",
        "VIDEO_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "VEHICLE_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]
    stats: Stats

@typing.type_check_only
class Breakdown(typing_extensions.TypedDict, total=False):
    details: _list[str]
    regions: _list[Region]

@typing.type_check_only
class BuiltInSimpleAction(typing_extensions.TypedDict, total=False):
    additionalContent: AdditionalContent
    attributeCode: str
    type: typing_extensions.Literal[
        "BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED",
        "VERIFY_PHONE",
        "CLAIM_WEBSITE",
        "ADD_PRODUCTS",
        "ADD_CONTACT_INFO",
        "LINK_ADS_ACCOUNT",
        "ADD_BUSINESS_REGISTRATION_NUMBER",
        "EDIT_ITEM_ATTRIBUTE",
        "FIX_ACCOUNT_ISSUE",
        "SHOW_ADDITIONAL_CONTENT",
    ]

@typing.type_check_only
class BuiltInUserInputAction(typing_extensions.TypedDict, total=False):
    actionContext: str
    flows: _list[ActionFlow]

@typing.type_check_only
class Callout(typing_extensions.TypedDict, total=False):
    fullMessage: TextWithTooltip
    styleHint: typing_extensions.Literal[
        "CALLOUT_STYLE_HINT_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]

@typing.type_check_only
class CheckboxInput(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckboxInputValue(typing_extensions.TypedDict, total=False):
    value: bool

@typing.type_check_only
class ChoiceInput(typing_extensions.TypedDict, total=False):
    options: _list[ChoiceInputOption]

@typing.type_check_only
class ChoiceInputOption(typing_extensions.TypedDict, total=False):
    additionalInput: InputField
    id: str
    label: TextWithTooltip

@typing.type_check_only
class ChoiceInputValue(typing_extensions.TypedDict, total=False):
    choiceInputOptionId: str

@typing.type_check_only
class ExternalAction(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "EXTERNAL_ACTION_TYPE_UNSPECIFIED",
        "REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER",
        "REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER",
        "LEGAL_APPEAL_IN_HELP_CENTER",
        "VERIFY_IDENTITY_IN_MERCHANT_CENTER",
    ]
    uri: str

@typing.type_check_only
class Impact(typing_extensions.TypedDict, total=False):
    breakdowns: _list[Breakdown]
    message: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]

@typing.type_check_only
class InputField(typing_extensions.TypedDict, total=False):
    checkboxInput: CheckboxInput
    choiceInput: ChoiceInput
    id: str
    label: TextWithTooltip
    required: bool
    textInput: TextInput

@typing.type_check_only
class InputValue(typing_extensions.TypedDict, total=False):
    checkboxInputValue: CheckboxInputValue
    choiceInputValue: ChoiceInputValue
    inputFieldId: str
    textInputValue: TextInputValue

@typing.type_check_only
class ItemLevelIssue(typing_extensions.TypedDict, total=False):
    attribute: str
    code: str
    description: str
    detail: str
    documentationUri: str
    productCount: str
    resolution: typing_extensions.Literal[
        "RESOLUTION_UNSPECIFIED", "MERCHANT_ACTION", "PENDING_PROCESSING"
    ]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "NOT_IMPACTED", "DEMOTED", "DISAPPROVED"
    ]

@typing.type_check_only
class ListAggregateProductStatusesResponse(typing_extensions.TypedDict, total=False):
    aggregateProductStatuses: _list[AggregateProductStatus]
    nextPageToken: str

@typing.type_check_only
class ProductChange(typing_extensions.TypedDict, total=False):
    newValue: str
    oldValue: str
    regionCode: str
    reportingContext: typing_extensions.Literal[
        "REPORTING_CONTEXT_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISCOVERY_ADS",
        "DEMAND_GEN_ADS",
        "DEMAND_GEN_ADS_DISCOVER_SURFACE",
        "VIDEO_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "VEHICLE_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ProductStatusChangeMessage(typing_extensions.TypedDict, total=False):
    account: str
    attribute: typing_extensions.Literal["ATTRIBUTE_UNSPECIFIED", "STATUS"]
    changes: _list[ProductChange]
    eventTime: str
    expirationTime: str
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing_extensions.Literal["RESOURCE_UNSPECIFIED", "PRODUCT"]

@typing.type_check_only
class Reason(typing_extensions.TypedDict, total=False):
    action: Action
    detail: str
    message: str

@typing.type_check_only
class Region(typing_extensions.TypedDict, total=False):
    code: str
    name: str

@typing.type_check_only
class RenderAccountIssuesResponse(typing_extensions.TypedDict, total=False):
    renderedIssues: _list[RenderedIssue]

@typing.type_check_only
class RenderIssuesRequestPayload(typing_extensions.TypedDict, total=False):
    contentOption: typing_extensions.Literal[
        "CONTENT_OPTION_UNSPECIFIED", "PRE_RENDERED_HTML"
    ]
    userInputActionOption: typing_extensions.Literal[
        "USER_INPUT_ACTION_RENDERING_OPTION_UNSPECIFIED",
        "REDIRECT_TO_MERCHANT_CENTER",
        "BUILT_IN_USER_INPUT_ACTIONS",
    ]

@typing.type_check_only
class RenderProductIssuesResponse(typing_extensions.TypedDict, total=False):
    renderedIssues: _list[RenderedIssue]

@typing.type_check_only
class RenderedIssue(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    impact: Impact
    prerenderedContent: str
    prerenderedOutOfCourtDisputeSettlement: str
    title: str

@typing.type_check_only
class Stats(typing_extensions.TypedDict, total=False):
    activeCount: str
    disapprovedCount: str
    expiringCount: str
    pendingCount: str

@typing.type_check_only
class TextInput(typing_extensions.TypedDict, total=False):
    additionalInfo: TextWithTooltip
    ariaLabel: str
    formatInfo: str
    type: typing_extensions.Literal[
        "TEXT_INPUT_TYPE_UNSPECIFIED", "GENERIC_SHORT_TEXT", "GENERIC_LONG_TEXT"
    ]

@typing.type_check_only
class TextInputValue(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class TextWithTooltip(typing_extensions.TypedDict, total=False):
    simpleTooltipValue: str
    simpleValue: str
    tooltipIconStyle: typing_extensions.Literal[
        "TOOLTIP_ICON_STYLE_UNSPECIFIED", "INFO", "QUESTION"
    ]

@typing.type_check_only
class TriggerActionPayload(typing_extensions.TypedDict, total=False):
    actionContext: str
    actionInput: ActionInput

@typing.type_check_only
class TriggerActionResponse(typing_extensions.TypedDict, total=False):
    message: str
