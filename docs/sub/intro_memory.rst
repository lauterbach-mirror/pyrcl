######
Memory
######

Memory access is provided by the :py:attr:`MemoryService<lauterbach.trace32.rcl.MemoryService>` class. Each debugger has its own instance, which can be used through its :py:attr:`memory<lauterbach.trace32.rcl.Debugger.memory>` attribute.


******************************
Reading / Writing 8-bit values
******************************


Signed
======

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(-128, 127)
	>>> dbg.memory.write_int8(address=address, value=value)
	>>> print(value, dbg.memory.read_int8(address=address))


Unsigned
========

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(0, 255)
	>>> dbg.memory.write_uint8(address=address, value=value)
	>>> print(value, dbg.memory.read_uint8(address=address))


*******************************
Reading / Writing 16-bit values
*******************************


Signed
======

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(-32768, 32767)
	>>> dbg.memory.write_int16(address=address, value=value)
	>>> print(value, dbg.memory.read_int16(address=address))


Unsigned
========

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(0, 65535)
	>>> dbg.memory.write_uint16(address=address, value=value)
	>>> print(value, dbg.memory.read_uint16(address=address))


*******************************
Reading / Writing 32-bit values
*******************************


Signed
======

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(-2147483648, 2147483647)
	>>> dbg.memory.write_int32(address=address, value=value)
	>>> print(value, dbg.memory.read_int32(address=address))


Unsigned
========

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(0, 4294967295)
	>>> dbg.memory.write_uint32(address=address, value=value)
	>>> print(value, dbg.memory.read_uint32(address=address))


*******************************
Reading / Writing 64-bit values
*******************************


Signed
======

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(-9223372036854775808, 9223372036854775807)
	>>> dbg.memory.write_int64(address=address, value=value)
	>>> print(value, dbg.memory.read_int64(address=address))


Unsigned
========

.. code-block:: python

	>>> import random
	>>> address = dbg.address.from_string('VM:0x0')
	>>> value = random.randint(0, 18446744073709551615)
	>>> dbg.memory.write_uint64(address=address, value=value)
	>>> print(value, dbg.memory.read_uint64(address=address))
