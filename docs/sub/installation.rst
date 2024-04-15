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

TRACE32: DVD 09/2020
Python: 3.6.1 


Installing local wheel
----------------------

.. code-block:: python

	python -m pip install ./lauterbach_trace32_rcl-latest-py3-none-any.whl

.. note:: If you get the following error

	.. code-block:: text

		Could not install packages due to an EnvironmentError: [WinError 5] Access is denied:
		Consider using the '--user' option or check the permissions.
	
	you either have to run the command as admin or install to the user site.


Installing to the user site
---------------------------

.. code-block:: python

	python -m pip install --user ./lauterbach_trace32_rcl-latest-py3-none-any.whl


Installing without PIP
----------------------

Installation is also possible without PIP. For this reason we provide the packed source as a .tar.gz. Extract the .tar.gz and change into the directory containing the `setup.py`.

Then run

.. code-block:: python

	python setup.py install

or 

.. code-block:: python

	python setup.py install --user