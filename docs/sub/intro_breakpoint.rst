###########
Breakpoints
###########

Breakpoint support is provided by the :py:attr:`BreakpointService<lauterbach.trace32.rcl.BreakpointService>` class. Each debugger has its own instance, which can be used through its :py:attr:`breakpoint<lauterbach.trace32.rcl.Debugger.breakpoint>` attribute.


*******************
Setting Breakpoints
*******************

Detailed information about breakpoints in TRACE32 can be found in `general_ref_b.pdf <https://www.lauterbach.com/pdf/general_ref_b.pdf>`_ chapter "Break.Set".

.. code-block:: python
	
	>>> bp = dbg.breakpoint.set(<arguments>)
	>>> print(bp)

The arguments are the same as for :py:attr:`Breakpoint<lauterbach.trace32.rcl.Breakpoint>` objects.

One way to set a breakpoint is to set it directly to an address:

.. code-block:: python

	>>> addr = dbg.address.from_string("P:0x1234")
	>>> bp = dbg.breakpoint.set(address=addr)
	>>> print(bp)

It's also possible to set a breakpoint to a symbol:

	>>> sym = dbg.symbol.query_by_name(name="main")
	>>> print(sym)
	>>> bp = dbg.breakpoint.set(address=sym.address)
	>>> print(bp)


Other breakpoint parameters
===========================

Other supported breakpoint parameters include action, implementation and type. Please refer to the breakpoint reference for details.


************************
Manipulating Breakpoints
************************

Breakpoint objects can be used to manipulate breakpoints.


Disabling and Enabling Breakpoints
==================================

.. code-block:: python

	>>> bp = dbg.breakpoint.set(<arguments>)
	>>> bp.disable()
	>>> bp.enable()


Deleting and setting Breakpoints
================================

.. code-block:: python
	
	>>> bp = dbg.breakpoint.set(<arguments>)
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
