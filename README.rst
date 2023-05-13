Quart-Flask-Patch
=================

|Build Status| |pypi| |python| |license|

Quart-Flask-Patch is a Quart extension that patches Quart to work with
Flask extensions.

Quickstart
----------

Quart-Flask-Patch must be imported first in your main module, so that
the patching occurs before any other code is initialised. For example,
if you want to use Flask-Login,

.. code-block:: python

   import quart_flask_patch

   from quart import Quart
   import flask_login

   app = Quart(__name__)
   login_manager = flask_login.LoginManager()
   login_manager.init_app(app)

Extensions known to work
------------------------

The following flask extensions are tested and known to work with
quart,

- `Flask-BCrypt <https://flask-bcrypt.readthedocs.io>`_
- `Flask-Caching <https://flask-caching.readthedocs.io>`_
- `Flask-KVSession <https://github.com/mbr/flask-kvsession>`_
- `Flask-Limiter <https://github.com/alisaifee/flask-limiter/>`_ See
  also `Quart-Rate-Limiter
  <https://github.com/pgjones/quart-rate-limiter>`_
- `Flask-Login <https://github.com/maxcountryman/flask-login/>`_ See
  also `Quart-Login <https://github.com/0000matteo0000/quart-login>`_
  or `Quart-Auth <https://github.com/pgjones/quart-auth>`_
- `Flask-Mail <https://pythonhosted.org/Flask-Mail/>`_
- `Flask-Mako <https://pythonhosted.org/Flask-Mako/>`_
- `Flask-Seasurf <https://github.com/maxcountryman/flask-seasurf/>`_
- `Flask-SQLAlchemy <https://flask-sqlalchemy.palletsprojects.com>`_
  See also `Quart-DB <https://github.com/pgjones/quart-db>`_
- `Flask-WTF <https://flask-wtf.readthedocs.io>`_

Extensions known not to work
----------------------------

The following flask extensions have been tested are known not to work
with quart,

- `Flask-CORS <https://github.com/corydolphin/flask-cors>`_, as it
  uses ``app.make_response`` which must be awaited. Try `Quart-CORS
  <https://github.com/pgjones/quart-cors>`_ instead.
- `Flask-Restful <https://flask-restful.readthedocs.io>`_
  as it subclasses the Quart (app) class with synchronous methods
  overriding asynchronous methods. Try `Quart-OpenApi
  <https://github.com/factset/quart-openapi/>`_ or `Quart-Schema
  <https://github.com/pgjones/quart-schema>`_ instead.

Caveats
-------

Flask extensions must use the global request proxy variable to access
the request, any other access e.g. via
``~quart.local.LocalProxy._get_current_object`` will require
asynchronous access. To enable this the request body must be fully
received before any part of the request is handled, which is a
limitation not present in vanilla flask.

Trying to use Flask alongside Quart in the same runtime will likely
not work, and lead to surprising errors.

The flask extension must be limited to creating routes, using the
request and rendering templates. Any other more advanced functionality
may not work.

Synchronous functions will not run in a separate thread (unlike Quart
normally) and hence may block the event loop.

Finally the flask_patching system also relies on patching asyncio, and
hence other implementations or event loop policies are unlikely to
work.

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

.. |pypi| image:: https://img.shields.io/pypi/v/quart-flask-patch.svg
   :target: https://pypi.python.org/pypi/Quart-Flask-Patch/

.. |python| image:: https://img.shields.io/pypi/pyversions/quart-flask-patch.svg
   :target: https://pypi.python.org/pypi/Quart-Flask-Patch/

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/pgjones/quart-flask-patch/blob/main/LICENSE
