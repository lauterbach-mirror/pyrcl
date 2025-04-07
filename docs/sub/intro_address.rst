#########
Addresses
#########

Address support is provided by the :py:attr:`AddressService<lauterbach.trace32.rcl.AddressService>` class. Each debugger has its own instance, which can be used through its :py:attr:`address<lauterbach.trace32.rcl.Debugger.address>` attribute.

TRACE32 supports addresses in the following format: `<access_class>:<machine_id>:::<space_id>::<address_offset>`. In pyrcl it is possible to create address objects by specifying each field explicitly, or by specifying a TRACE32 compatible string.

.. note::

	**Byte-Addresses**

	If not explicitly changed (see below), the address parameter for reading and writing target memory always is a "byte" (octet) address, independently of the target architecture's native memory width. This implies that

	* For machines that are byte-addressed (i.e. natively address single bytes like x86) the byte address corresponds to the native address. On these machines incrementing the address by 1 yields the next byte in memory.
	* For machines using word-addresses (i.e. natively address memory words like many DSPs) the	byte address for use with the TRACE32 remote API is calculated multiplying the word address with the native memory width (in bytes). On these machines incrementing the native address by 1 yields the next word in memory.
	* Accessing peripheral registers or special purpose registers that are not byte addresses (e.g. Arm CP15 or PowerPC SPR) need an address correction that multiplies the register number by the byte width of the register access class. E.g. if Data.dump SPR:0x10 shows 32bit for each register number (= SPR address), the corresponding API address is 0x10*4.


********
Explicit
********

.. code-block:: pycon

	>>> addr = dbg.address(access='D', value=0x0) 


**********************
Implicit (from string)
**********************

.. code-block:: pycon

	>>> addr = dbg.address.from_string('D:0x0')
