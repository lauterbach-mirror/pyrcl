########
Variable
########

Access to Variables is provided by the :py:attr:`VariableService<lauterbach.trace32.rcl.VariableService>` class. Each debugger has its own instance, which can be used through its :py:attr:`variable<lauterbach.trace32.rcl.Debugger.variable>` attribute.


****************
Writing Variable
****************


.. code-block:: python

	>>> dbg.variable.write("variableName", 42)


****************
Reading Variable
****************


.. code-block:: python

	>>> variable = dbg.variable.read("variableName")
	>>> print(variable.value)
