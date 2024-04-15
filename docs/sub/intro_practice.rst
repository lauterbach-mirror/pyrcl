########
Practice
########

Access to Practice macros is provided by the :py:attr:`PracticeService<lauterbach.trace32.rcl.PracticeService>` class. Each debugger has its own instance, which can be used through its :py:attr:`practice<lauterbach.trace32.rcl.Debugger.practice>` attribute.

Macros set via Remote API are global and pose as a Link between Practice and Python. Therefore hybrid solutions may be formed by for example setting practice macros before executing a python script, reading them at the beginning and writing the results back to macros.


*************
Writing Macro
*************


.. code-block:: python

	>>> dbg.practice.set_macro("&macroName", "0x1234")
	

*************
Reading Macro
*************


.. code-block:: python

	>>> macro = dbg.practice.get_macro("&macroName")
	>>> print(macro.value)