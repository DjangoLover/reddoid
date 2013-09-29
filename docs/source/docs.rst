.. reddoid documentation

Documentation
=============

The following line was added to Sphynx Makefile:

.. code-block:: Makefile

    serve:
        cd build/html/ && python -m SimpleHTTPServer 8001

It allows to call ``make serve`` and examine the documentation at http://localhost:8001
