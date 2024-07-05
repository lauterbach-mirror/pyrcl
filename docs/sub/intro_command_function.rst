######################
Commands and Functions
######################

TRACE32 debugger commands and functions are provided using the :py:attr:`CommandService<lauterbach.trace32.rcl.CommandService>` and :py:attr:`FunctionService<lauterbach.trace32.rcl.FunctionService>` class. Each debugger has its own instance for each, which can be used through it's :py:attr:`cmd<lauterbach.trace32.rcl.Debugger.cmd>` and :py:attr:`fnc<lauterbach.trace32.rcl.Debugger.fnc>` attribute.

Commands and functions are the basis for the TRACE32 configuration.

Example: Select CPU and print selected CPU

.. code-block:: python

	>>> dbg.cmd("SYStem.CPU CortexA55")
	>>> cpu = dbg.fnc("CPU()")
	>>> print(cpu)
	CortexA55

CMM scripts must be executed using the :py:attr:`dbg.cmm()<lauterbach.trace32.rcl.Debugger.cmm>` function:

.. code-block:: python

	>>> dbg.cmm("script.cmm")
