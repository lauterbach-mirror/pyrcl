# pyrcl

## Release Notes

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
