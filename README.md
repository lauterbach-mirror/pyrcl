# pyrcl

## Release Notes

### v1.1.4

* Marked `MemoryError` as deprecated, use `MemoryAccessError` instead
* Marked `MemoryReadError` as deprecated, use `MemoryReadAccessError` instead
* Marked `MemoryWriteError` as deprecated, use `MemoryWriteAccessError` instead

### v1.1.3

* Added support for readthedocs

### v1.1.2

* Fixed an issue where a TCP connection closed by the peer was not properly detected

### v1.1.1

* Fixed memory bundles

### v1.1.0

* Drop support for Python 3.6, 3.7, 3.8
* Add support for memory bundles
* Add partial support for direct access API

### v1.0.10

* Added missing functions `library.t32_gettracestate` and `library.t32_readtrace`
* Changed logger name to "lauterbach.trace32.rcl"

### v1.0.9

* Fixed error related functions to not use dbg.fnc(), otherwise the error state is reset. Affected functions:
  * def error_address(self) -> Address: (dropped)
  * def error_cmdline(self) -> str:
  * def error_fileline(self) -> int: (dropped)
  * def error_filename(self) -> str: (dropped)
  * def error_firstid(self) -> str:
  * def error_id(self) -> str:
  * def error_message(self) -> str:
  * def error_occurred(self) -> bool:
  * def error_position(self) -> int: (dropped)

### v1.0.8

* Fixed missing breakpoint actions `WATCH`, `TRACEENABLE`, `TRACEDATA`, `TRACEON`, `TRACEOFF` and `TRACETRIGGER`

### v1.0.7

* Fixed missing module level export of `hexversion()`

### v1.0.6

* Fixed missing module level exports of `version` and multiple exceptions
* Fixed breakpoint core and size parameters
* Added `ConnectionError` as baseclass of `ApiConnectionError`

### v1.0.5

Various bugfixes

### v1.0.4

Various bugfixes

### v1.0.3

Various bugfixes

### v1.0.2

Various bugfixes

### v1.0.1

Various bugfixes

### v1.0.0

Initial release
