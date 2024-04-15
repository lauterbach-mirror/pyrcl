###########
Breakpoints
###########

Breakpoint support is provided by the :py:attr:`BreakpointService<lauterbach.trace32.rcl.BreakpointService>` class. Each debugger has its own instance, which can be used through its :py:attr:`breakpoint<lauterbach.trace32.rcl.Debugger.breakpoint>` attribute.


*******************
Setting Breakpoints
*******************

.. code-block:: python
	
	>>> bp = dbg.breakpoint.set()
	>>> print(bp)


************************
Manipulating Breakpoints
************************

Breakpoint objects can be used to manipulate breakpoints.


Disabling and Enabling Breakpoints
==================================

.. code-block:: python

	>>> bp = dbg.breakpoint.set()
	>>> bp.disable()
	>>> bp.enable()


Deleting and setting Breakpoints
================================

.. code-block:: python
	
	>>> bp = dbg.breakpoint.set()
	>>> bp.delete()
	>>> bp.set()


***************
Breakpoint list
***************

Returns a list with all current breakpoint objects.

.. code-block:: python
	
	>>> bps = dbg.breakpoint.list()
	>>> for bp in bps:
	>>>     print(bp)

