Django Account Keeping
======================

A reusable Django app for keeping track of transactions in your bank accounts.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-nox


Add all relevant apps to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'django_nox',
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate


Usage
-----



Running & Sorting Results
#########################

Once you've installed it, the request times will be log in database, and you can run this command to analyze the resulting data::

    $ python manage.py nox_analyze



Settings
#########
To configured some parmas in settings.py


NOX_SLOW_REQUEST
################

Default: 0

Slow request. Number of rows from which a request will be assumed to be slow and store to database.


Enjoy!
######

Email me with any questions: [liangjinfeng@youmi.com](liangjinfeng@youmi.com).
