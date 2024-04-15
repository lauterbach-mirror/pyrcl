#########
Registers
#########

Register access is provided by the :py:attr:`RegisterService<lauterbach.trace32.rcl.RegisterService>` class. Each debugger has its own instance, which can be used through its :py:attr:`register<lauterbach.trace32.rcl.Debugger.register>` attribute.


*****************
Reading Registers
*****************


Single Register
===============

.. code-block:: python

	>>> reg = dbg.register.read(name='PC')
	>>> print(reg)
	
	
Multiple Registers
==================

.. code-block:: python

	>>> names = ["R{}".format(i) for i in range(8)]
	>>> regs = dbg.register.read_by_names(names=names)
	>>> for reg in reg:
	>>>     print(reg)


FPU Register
============

.. code-block:: python

	>>> reg = dbg.register.read(name='F0', unit="FPU")
	>>> print(reg)

	
*****************
Writing Registers
*****************


Single Register
===============

.. code-block:: python

	>>> dbg.register.write(name='R0', value=0)


Multiple Registers
==================

.. code-block:: python

	>>> names = ["R{}".format(i) for i in range(4)]
	>>> values = [0x12, 0x34, 0x56, 0x78]
	>>> dbg.register.write_by_names(names=names, values=values)
	

FPU Register
============

.. code-block:: python

	>>> dbg.register.write(name='F0', value=1.234, unit="FPU")
