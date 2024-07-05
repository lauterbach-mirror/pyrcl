.. _installation:

############
Installation
############

pyrcl is provided as source and wheel. You will find both in your TRACE32 installation at <T32SYS>/demo/api/python/rcl/dist.

.. seealso:: General information on installing Python packages:

	`<https://packaging.python.org/tutorials/installing-packages/>`_

We recommend to install pyrcl using PIP.


Minimum Requirements
--------------------

* v1.1
	* Python: 3.9
	* TRACE32: DVD 09/2020
* v1.0
	* Python: 3.6
	* TRACE32: DVD 09/2020


Installation using pypi.org
---------------------------

When installing from pypi.org make sure you choose the correct version, see "Minimum Requirements".

.. code-block:: python

	python -m pip install lauterbach-trace32-rcl~=1.1.0


Installation using local wheel
------------------------------

.. code-block:: python

	python -m pip install ./lauterbach_trace32_rcl-1.1.0-py3-none-any.whl

.. note:: If you get the following error

	.. code-block:: text

		Could not install packages due to an EnvironmentError: [WinError 5] Access is denied:
		Consider using the '--user' option or check the permissions.
	
	you either have to run the command as admin or install to the user site.

.. code-block:: python

	python -m pip install --user ./lauterbach_trace32_rcl-1.1.0-py3-none-any.whl
