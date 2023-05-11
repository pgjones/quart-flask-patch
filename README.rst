Quart-Flask-Patch
=================

|Build Status| |docs| |pypi| |python| |license|

Quart-Flask-Patch is a Quart extension that patches Quart to work with
Flask extensions.

Quickstart
----------

Quart-Flask-Patch must be imported first in your main module, so that
the patching occurs before any other code is initialised.

.. code-block:: python

   import quart_flask_patch
   ...


Contributing
------------

Quart-Flask-Patch is developed on `GitHub
<https://github.com/pgjones/quart-flask-patch>`_. If you come across
an issue, or have a feature request please open an `issue
<https://github.com/pgjones/quart-flask-patch/issues>`_. If you want
to contribute a fix or the feature-implementation please do (typo
fixes welcome), by proposing a `merge request
<https://github.com/pgjones/quart-flask-patch/merge_requests>`_.

Testing
~~~~~~~

The best way to test Quart-Flask-Patch is with `Tox
<https://tox.readthedocs.io>`_,

.. code-block:: console

    $ pip install tox
    $ tox

this will check the code style and run the tests.

Help
----

The Quart-Flask-Patch `documentation
<https://quart-flask-patch.readthedocs.io/en/latest/>`_ is the best
places to start, after that try searching `stack overflow
<https://stackoverflow.com/questions/tagged/quart>`_ or ask for help
`on gitter <https://gitter.im/python-quart/lobby>`_. If you still
can't find an answer please `open an issue
<https://github.com/pgjones/quart-flask-patch/issues>`_.


.. |Build Status| image:: https://github.com/pgjones/quart-flask-patch/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/pgjones/quart-flask-patch/commits/main

.. |docs| image:: https://readthedocs.org/projects/quart-flask-patch/badge/?version=latest&style=flat
   :target: https://quart-flask-patch.readthedocs.io/en/latest/

.. |pypi| image:: https://img.shields.io/pypi/v/quart-flask-patch.svg
   :target: https://pypi.python.org/pypi/Quart-Flask-Patch/

.. |python| image:: https://img.shields.io/pypi/pyversions/quart-flask-patch.svg
   :target: https://pypi.python.org/pypi/Quart-Flask-Patch/

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/pgjones/quart-flask-patch/blob/main/LICENSE
