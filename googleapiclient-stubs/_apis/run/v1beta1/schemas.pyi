import typing

import typing_extensions
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
    categories: typing.List[str]
    kind: str
    listKind: str
    plural: str
    shortNames: typing.List[str]
    singular: str

@typing.type_check_only
class CustomResourceDefinitionSpec(typing.Dict[str, typing.Any]): ...

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
class CustomResourceValidation(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ExternalDocumentation(typing_extensions.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class JSON(typing_extensions.TypedDict, total=False):
    raw: str

@typing.type_check_only
class JSONSchemaProps(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JSONSchemaPropsOrArray(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JSONSchemaPropsOrBool(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JSONSchemaPropsOrStringArray(typing_extensions.TypedDict, total=False):
    property: typing.List[str]
    schema: JSONSchemaProps

@typing.type_check_only
class ListCustomResourceDefinitionsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: typing.List[CustomResourceDefinition]
    kind: str
    metadata: ListMeta
    unreachable: typing.List[str]

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
    annotations: typing.Dict[str, typing.Any]
    clusterName: str
    creationTimestamp: str
    deletionGracePeriodSeconds: int
    deletionTimestamp: str
    finalizers: typing.List[str]
    generateName: str
    generation: int
    labels: typing.Dict[str, typing.Any]
    name: str
    namespace: str
    ownerReferences: typing.List[OwnerReference]
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
