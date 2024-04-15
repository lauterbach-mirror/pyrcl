######
Basics
######

pyrcl is using the TRACE32 "Remote API" protocol. So in order to use the pyrcl module the TRACE32 software must be started with an open Remote API port.


**************************************
Connecting to already running software
**************************************


Preparing the TRACE32 software
==============================

The TRACE32 software has to be configured for use with a remote control, such as the API. If you are using Windows and T32Start application to start the TRAC32 software, you need to open the configuration at “advanced settings” where you can select “Use Port: yes” in the "API Port" folder. The automatically created config file will have the necessary lines automatically.

.. code-block:: text

	<mandatory blank line>

	RCL=NETASSIST
	PORT=20000
	PACKLEN=1024

	RCL=NETTCP
	PORT=20000

	<mandatory blank line>

To allow and configure remote control when not using T32Start application, add one of the above sections to the file "config.t32". The section starting with NETASSIST enables the api to use UDP ports, the other section stating NETTCP enables the api to use a TCP port.

PACKLEN specifies the maximum package length in bytes for the UDP socket communication. It must not be
bigger than 2048 and must fit to the value used to connect the client. The port number specifies the port which is used to communicate with the API. The default is 20000. If this port is already in use, try one higher than 20000.

Further information can be found in "api_remote_c.pdf" in your TRACE32 installation.


Importing
=========

Make sure you have :ref:`installed<installation>` pyrcl.

.. code-block:: python

	import lauterbach.trace32.rcl as t32


Connecting
==========

Connecting is done using :py:attr:`t32.connect()<lauterbach.trace32.rcl.connect>`.


Connecting with default parameters
----------------------------------

If you use default parameters, you can use:

.. code-block:: python

	import lauterbach.trace32.rcl as t32
	dbg = t32.connect()

This will establish a connection to the remote api with default parameters. These translate to a TCP protocol with port 20000 at localhost and a timeout of 1 second.


Connecting with parameters
--------------------------

Otherwise you can specify the parameters when calling t32.connect().

.. code-block:: python

	import lauterbach.trace32.rcl as t32
	dbg = t32.connect(node='localhost', port=20000, protocol="TCP", timeout=10.0)

or:

.. code-block:: python

	import lauterbach.trace32.rcl as t32
	dbg = t32.connect(node='localhost', port=20000, protocol="UDP", packlen=1024, timeout=10.0)


Connecting to multiple debuggers
--------------------------------

It is also possible to connect to multiple debuggers. Assuming you have two debuggers, one running with port 20000 (default) and one debugger two running with port 20001:

.. code-block:: python

	import lauterbach.trace32.rcl as t32
	dbg1 = t32.connect()
	dbg2 = t32.connect(port=20001)


Using arguments and autoconnect()
---------------------------------

Since many usecases require to leave the port parameter variable upon skript execution, the rcl module offers a commandline friendly method :py:attr:`t32.autoconnect()<lauterbach.trace32.rcl.autoconnect>`. This allows to omit the api port and node in the code and pass those parameters as arguments with the call of your script.

.. code-block:: python

	import lauterbach.trace32.rcl as t32
	dbg = t32.autoconnect()
        dbg.print("hello world")

.. code-block:: bash

   python hello_world.py --node=server01 --port=20001


