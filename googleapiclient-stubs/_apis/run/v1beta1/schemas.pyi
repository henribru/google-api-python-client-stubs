import typing

import typing_extensions

_list = list

@typing.type_check_only
class CustomResourceColumnDefinition(typing_extensions.TypedDict, total=False):
    description: str
    format: str
    jsonPath: str
    name: str
    priority: int
    type: str

@typing.type_check_only
class CustomResourceDefinition(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: CustomResourceDefinitionSpec

@typing.type_check_only
class CustomResourceDefinitionNames(typing_extensions.TypedDict, total=False):
    categories: _list[str]
    kind: str
    listKind: str
    plural: str
    shortNames: _list[str]
    singular: str

@typing.type_check_only
class CustomResourceDefinitionSpec(typing_extensions.TypedDict, total=False):
    additionalPrinterColumns: _list[CustomResourceColumnDefinition]
    group: str
    names: CustomResourceDefinitionNames
    scope: str
    subresources: CustomResourceSubresources
    validation: CustomResourceValidation
    version: str
    versions: _list[CustomResourceDefinitionVersion]

@typing.type_check_only
class CustomResourceDefinitionVersion(typing_extensions.TypedDict, total=False):
    name: str
    served: bool
    storage: bool

@typing.type_check_only
class CustomResourceSubresourceScale(typing_extensions.TypedDict, total=False):
    labelSelectorPath: str
    specReplicasPath: str
    statusReplicasPath: str

@typing.type_check_only
class CustomResourceSubresourceStatus(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CustomResourceSubresources(typing_extensions.TypedDict, total=False):
    scale: CustomResourceSubresourceScale
    status: CustomResourceSubresourceStatus

@typing.type_check_only
class CustomResourceValidation(typing_extensions.TypedDict, total=False):
    openAPIV3Schema: JSONSchemaProps

@typing.type_check_only
class ExternalDocumentation(typing_extensions.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class JSON(typing_extensions.TypedDict, total=False):
    raw: str

AlternativeJSONSchemaProps = typing_extensions.TypedDict(
    "AlternativeJSONSchemaProps",
    {
        "additionalItems": JSONSchemaPropsOrBool,
        "additionalProperties": JSONSchemaPropsOrBool,
        "allOf": _list[JSONSchemaProps],
        "anyOf": _list[JSONSchemaProps],
        "default": JSON,
        "definitions": dict[str, typing.Any],
        "dependencies": dict[str, typing.Any],
        "description": str,
        "enum": _list[str],
        "example": JSON,
        "exclusiveMaximum": bool,
        "exclusiveMinimum": bool,
        "externalDocs": ExternalDocumentation,
        "format": str,
        "id": str,
        "items": JSONSchemaPropsOrArray,
        "maxItems": str,
        "maxLength": str,
        "maxProperties": str,
        "maximum": float,
        "minItems": str,
        "minLength": str,
        "minProperties": str,
        "minimum": float,
        "multipleOf": float,
        "not": JSONSchemaProps,
        "oneOf": _list[JSONSchemaProps],
        "pattern": str,
        "patternProperties": dict[str, typing.Any],
        "properties": dict[str, typing.Any],
        "ref": str,
        "required": _list[str],
        "schema": str,
        "title": str,
        "type": str,
        "uniqueItems": bool,
    },
    total=False,
)

@typing.type_check_only
class JSONSchemaProps(AlternativeJSONSchemaProps): ...

@typing.type_check_only
class JSONSchemaPropsOrArray(typing_extensions.TypedDict, total=False):
    jsonSchemas: _list[JSONSchemaProps]
    schema: JSONSchemaProps

@typing.type_check_only
class JSONSchemaPropsOrBool(typing_extensions.TypedDict, total=False):
    allows: bool
    schema: JSONSchemaProps

@typing.type_check_only
class JSONSchemaPropsOrStringArray(typing_extensions.TypedDict, total=False):
    property: _list[str]
    schema: JSONSchemaProps

@typing.type_check_only
class ListCustomResourceDefinitionsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[CustomResourceDefinition]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

AlternativeListMeta = typing_extensions.TypedDict(
    "AlternativeListMeta",
    {
        "continue": str,
        "resourceVersion": str,
        "selfLink": str,
    },
    total=False,
)

@typing.type_check_only
class ListMeta(AlternativeListMeta): ...

@typing.type_check_only
class ObjectMeta(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clusterName: str
    creationTimestamp: str
    deletionGracePeriodSeconds: int
    deletionTimestamp: str
    finalizers: _list[str]
    generateName: str
    generation: int
    labels: dict[str, typing.Any]
    name: str
    namespace: str
    ownerReferences: _list[OwnerReference]
    resourceVersion: str
    selfLink: str
    uid: str

@typing.type_check_only
class OwnerReference(typing_extensions.TypedDict, total=False):
    apiVersion: str
    blockOwnerDeletion: bool
    controller: bool
    kind: str
    name: str
    uid: str
