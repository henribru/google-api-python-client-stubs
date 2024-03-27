# Type stubs for google-api-python-client

[![PyPI version](https://badge.fury.io/py/google-api-python-client-stubs.svg)](https://badge.fury.io/py/google-api-python-client-stubs)

This package provides type stubs for the [google-api-python-client](https://github.com/googleapis/google-api-python-client) library. 
It allows you to type check usage of the library with e.g. [mypy](http://mypy-lang.org/) and will also improve autocomplete in many editors.

**This is in no way affiliated with Google.**

The stubs were generated automatically based on Google's [Discovery Documents](https://developers.google.com/discovery/v1/reference/apis), that are bundled with google-api-python-client as of v2.

If you find incorrect annotations, please create an issue.

Releases can be somewhat infrequent. If you need a new release, create an issue and I'll probably get around to it faster.

## Installation

```shell script
$ pip install google-api-python-client-stubs
```

The stubs should be automatically picked up by your editor or typechecker.

## Caveats

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
type checking, not at runtime.

Any type not available at runtime is located under the `googleapiclient._apis` package, with a subpackage for the API and a subpackage for the API version.
For example, the return type of `build("sheets", "v4")`, `SheetsResource`, should be imported from `googleapiclient._apis.sheets.v4`. Nested resources have a nested class structure, e.g. the return type of `build("sheets", "v4").spreadsheets().values()` is `SheetsResource.SpreadsheetsResource.ValuesResource`.
If autocompleting import paths doesn't work you can find the correct path by using Mypy's [reveal_type](https://mypy.readthedocs.io/en/stable/common_issues.html#reveal-type)
on the thing you want to explicitly annotate. For `TypedDict`s this will also give you useful info about the structure of the dictionary.

If you use Pyright/Pylance, you'll get a [reportMissingModuleSource](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingModuleSource) error at the import site, which indicates that the stub file doesn't have a corresponding source file. As long as the import only occurs during typechecking, this can be safely ignored. Autocomplete and typechecking will still work.

Note that since the types don't exist at runtime, they're not compatible with libraries that evaluate annotations at runtime. For example, you can't use them to annotate a field in a Pydantic model.

### Performance
The stubs contain a separate overload of `googleapiclient.discovery.build` for each service and version (see `discovery.pyi`). 
This can lead to slow type inference for this function. Mypy will generally be pretty fast after the first run,
but you might experience slow autocomplete in your editor. If you're experiencing this problem you can bypass type inference with explicit annotations, 
e.g. `sheets_service: SheetsResource = build("sheets", "v4")` instead of `sheets_service = build("sheets", "v4")`.
Note the caveats to this approach in the previous section.

### Recursive types
The stubs previously didn't include recursive type definitions due to a lack of type checker support, but this is now included. Note that if you're using Mypy, v0.990 or higher is required for this to work.

### Stubs for non-API-specific parts
There are detailed stubs for the API services, but other parts of the library have only been annotated with [stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html),
so they're mostly typed as `Any`. I believe these parts are mostly used internally by the library itself,
so for most users this should be fine. Contributions to improve these stubs are welcome, though.
