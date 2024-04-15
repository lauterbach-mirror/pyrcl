#######
Symbols
#######

Symbol access is provided by the :py:attr:`SymbolService<lauterbach.trace32.rcl.SymbolService>` class. Each debugger has its own instance, which can be used through its :py:attr:`symbol<lauterbach.trace32.rcl.Debugger.symbol>` attribute.


****************
Querying symbols
****************

.. code-block:: python

	>>> sym_main = dbg.symbol.query_by_name(name='main')
	>>> print(sym_main)
