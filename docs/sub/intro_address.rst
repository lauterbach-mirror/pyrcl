#########
Addresses
#########

Address support is provided by the :py:attr:`AddressService<lauterbach.trace32.rcl.AddressService>` class. Each debugger has its own instance, which can be used through its :py:attr:`address<lauterbach.trace32.rcl.Debugger.address>` attribute.

TRACE32 supports addresses in the following format: `<access_class>:<machine_id>:::<space_id>::<address_offset>`. In pyrcl it is possible to create address objects by specifying each field explicitly, or by specifying a TRACE32 compatible string.


********
Explicit
********

.. code-block:: python

	>>> addr = dbg.address(access='D', value=0x0) 


**********************
Implicit (from string)
**********************

.. code-block:: python

	>>> addr = dbg.address.from_string('D:0x0')

