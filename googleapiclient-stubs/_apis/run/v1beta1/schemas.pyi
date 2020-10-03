import typing

import typing_extensions

class CustomResourceSubresourceStatus(typing_extensions.TypedDict, total=False): ...

class CustomResourceValidation(typing_extensions.TypedDict, total=False):
    openAPIV3Schema: JSONSchemaProps

class JSON(typing_extensions.TypedDict, total=False):
    raw: str

class ExternalDocumentation(typing_extensions.TypedDict, total=False):
    description: str
    url: str

class CustomResourceSubresources(typing_extensions.TypedDict, total=False):
    scale: CustomResourceSubresourceScale
    status: CustomResourceSubresourceStatus

class JSONSchemaPropsOrArray(typing_extensions.TypedDict, total=False):
    jsonSchemas: typing.List[JSONSchemaProps]
    schema: JSONSchemaProps

class CustomResourceColumnDefinition(typing_extensions.TypedDict, total=False):
    description: str
    jsonPath: str
    format: str
    type: str
    name: str
    priority: int

class JSONSchemaProps(typing.Dict[str, typing.Any]): ...

class ObjectMeta(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    finalizers: typing.List[str]
    generateName: str
    annotations: typing.Dict[str, typing.Any]
    generation: int
    deletionTimestamp: str
    namespace: str
    deletionGracePeriodSeconds: int
    resourceVersion: str
    ownerReferences: typing.List[OwnerReference]
    name: str
    uid: str
    creationTimestamp: str
    clusterName: str
    selfLink: str

ListMeta = typing_extensions.TypedDict(
    "ListMeta",
    {
        "continue": str,
        "selfLink": str,
        "resourceVersion": str,
    },
    total=False,
)

class ListCustomResourceDefinitionsResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[CustomResourceDefinition]
    metadata: ListMeta
    apiVersion: str
    unreachable: typing.List[str]
    kind: str

class CustomResourceSubresourceScale(typing_extensions.TypedDict, total=False):
    specReplicasPath: str
    labelSelectorPath: str
    statusReplicasPath: str

class CustomResourceDefinitionNames(typing_extensions.TypedDict, total=False):
    kind: str
    shortNames: typing.List[str]
    listKind: str
    singular: str
    plural: str
    categories: typing.List[str]

class OwnerReference(typing_extensions.TypedDict, total=False):
    name: str
    kind: str
    uid: str
    apiVersion: str
    controller: bool
    blockOwnerDeletion: bool

class JSONSchemaPropsOrBool(typing.Dict[str, typing.Any]): ...

class CustomResourceDefinitionVersion(typing_extensions.TypedDict, total=False):
    served: bool
    storage: bool
    name: str

class JSONSchemaPropsOrStringArray(typing_extensions.TypedDict, total=False):
    property: typing.List[str]
    schema: JSONSchemaProps

class CustomResourceDefinition(typing.Dict[str, typing.Any]): ...
class CustomResourceDefinitionSpec(typing.Dict[str, typing.Any]): ...
