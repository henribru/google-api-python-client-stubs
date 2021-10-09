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
class CustomResourceDefinitionSpec(dict[str, typing.Any]): ...

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
class CustomResourceValidation(dict[str, typing.Any]): ...

@typing.type_check_only
class ExternalDocumentation(typing_extensions.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class JSON(typing_extensions.TypedDict, total=False):
    raw: str

@typing.type_check_only
class JSONSchemaProps(dict[str, typing.Any]): ...

@typing.type_check_only
class JSONSchemaPropsOrArray(dict[str, typing.Any]): ...

@typing.type_check_only
class JSONSchemaPropsOrBool(dict[str, typing.Any]): ...

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
