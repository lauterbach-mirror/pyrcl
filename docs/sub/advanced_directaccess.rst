#############
Direct Access
#############

The Direct Access API Functions are used to access IP blocks of the target that are not handled by the 
debugger. The API provides functions at different abstraction level to minimize the communication overhead. 
So it is possible to toggle certain pin of the debuggers probe, program complete JTAG shifts or modify 
registers on a certain bus. The API functions are divided into functions that set parameters and functions 
that execute actions based to the previously set parameters to save communication time. Multiple sets of 
parameters are possible, because there are multiple IP block in the target. These sets are called Instances. 
Depending to the accessed IP blocks there are different instance types that can be used.

A detailed description of the Direct Access API can be found here: `api_remote_c.pdf <https://repo.lauterbach.com/pdf/api_remote_c.pdf>`__.


.. ***************************************************************
.. Configuration of instance parameters and independent parameters
.. ***************************************************************

.. TODO


****************************
ICD TAP Access API Functions
****************************

This chapter describes all functions available for direct access to the JTAG TAP controller. 


Raw shifts
==========

Example: Read the IDCODE

.. code-block:: python

	def read_idcode() -> int:
		# Create bundle
		bundle = pyrcl.DirectAccessBundle()
		# JTAG reset with TMS -> Test-Logic-Reset
		access = pyrcl.DirectAccessShiftRaw(num_bits=5, tms=b"\xFF")
		bundle.add_access(access)
		# Test-Logic-Reset -> Shift-DR
		access = pyrcl.DirectAccessShiftRaw(num_bits=4, tms=b"\x02")
		bundle.add_access(access)
		# Read IDCODE
		access = pyrcl.DirectAccessShiftRaw(num_bits=32, tdo=True, options=pyrcl.DirectAccessShiftRawOptions(lasttms_one=True)
		bundle.add_access(access)
		# Execute bundle
		results = dbg.directaccess.execute(bundle)
		# Return IDCODE
		return int.from_bytes(result[-1].tdo, byteorder="little")
