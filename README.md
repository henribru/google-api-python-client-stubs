# Type stubs for google-api-python-client

[![PyPI version](https://badge.fury.io/py/google-api-python-client-stubs.svg)](https://badge.fury.io/py/google-api-python-client-stubs)

This package provides type stubs for the [google-api-python-client](https://github.com/googleapis/google-api-python-client) library. 
It allows you to type check usage of the library with e.g. [mypy](http://mypy-lang.org/) and will also improve autocomplete in many editors.

**This is in no way affiliated with Google.**

The stubs were generated automatically based on Google's [Discovery Documents](https://developers.google.com/discovery/v1/reference/apis), that are bundled with google-api-python-client as of v2.

If you find incorrect annotations, please create an issue.

## Installation

```shell script
$ pip install google-api-python-client-stubs
```

## Caveats

### Performance
The stubs contain a separate overload of `googleapiclient.discovery.build` for each service and version (see `discovery.pyi`). 
This can lead to slow type inference for this function. Mypy will generally be pretty fast after the first run,
but you might experience slow autocomplete. If you're experiencing this problem you can bypass type inference with explicit annotations, 
e.g. `sheets_service: SheetsResource = build("sheets", "v4")` instead of `sheets_service = build("sheets", "v4")`.
See the next section for some caveats to this approach.

### Explicit annotations
The `google-api-python-client-stubs` is quite dynamic. 
All resources are just instances of a single class with dynamically attached methods
and the requests and responses are just dictionaries. The way this is annotated is with
classes and [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict)
that don't exist in the actual library, only in the stub files. This means you *cannot* use any of these types at runtime, it *will* cause your code to crash.
If you rely solely on type inference, this is not an issue, but as soon as you want to explicitly
annotate a variable, argument or return type in your code with one of these types, you must follow these rules:
1. Either put `from __future__ import annotations` at the top of your file or surround the annotations with quotes. 
This ensures that Python doesn't attempt to evaluate the types at runtime. 
Note that the import is only supported in Python 3.7 and above.
2. Only import the types inside an `if typing.TYPE_CHECKING` block. This ensures that the imports are only evaluated during
type checking. Note that any type not available at runtime is located under the `googleapiclient._apis` package. 
For example, `SheetsResource` should be imported from `googleapiclient._apis.sheets.v4.resources`.
If autocompleting import paths doesn't work you can find the correct path by using Mypy's [reveal_type](https://mypy.readthedocs.io/en/stable/common_issues.html#reveal-type)
on the thing you want to explicitly annotate. For `TypedDict`s this will also give you useful info about the structure of the dictionary.

### Recursive types
Mypy unfortunately doesn't support [recursive types](https://github.com/python/mypy/issues/731).
Some of Google's APIs have recursive type definitions in their schemas. Due to the lack of support these
are only annotated as regular dictionaries, so the validity of the keys and values won't be checked.

### Stubs for non-API-specific parts
There are detailed stubs for the API services, but other parts of the library have only been annotated with [stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html),
so they're mostly typed as `Any`. I believe these parts are mostly used internally by the library itself,
so for most users this should be fine. Contributions to improve these stubs are welcome, though.
