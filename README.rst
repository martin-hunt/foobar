================================
Test Project for Hosted CI Tests
================================

This is useless for anything else


Sphinx Documentation
====================

Build the documentation with ``python setup.py docs`` and run doctests with
``python setup.py doctest``. Start editing the file ``docs/index.rst`` to
extend the documentation. The documentation also works with `Read the Docs
<https://readthedocs.org/>`_.


Unittest & Coverage
===================

Run ``python setup.py test`` to run all unittests defined in the subfolder
``tests`` with the help of `py.test <http://pytest.org/>`_. The py.test plugin
`pytest-cov <https://github.com/schlamar/pytest-cov>`_ is used to automatically
generate a coverage report. For usage with a continuous integration software
JUnit and Coverage XML output can be activated. h-tox`` can be specified.


Requirements Management
=======================

Add the requirements of your project to the ``requirements.txt`` file which
will be automatically used by ``setup.py``.


Licenses
========

All licenses from `choosealicense.com <http://choosealicense.com/>`_ can be
easily selected with the help of the ``--license`` flag.

