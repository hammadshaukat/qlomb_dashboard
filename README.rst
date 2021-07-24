Qlomb Dashboard
===============

The Awesome Qlomb Dashboard Project!

.. image:: https://img.shields.io/badge/python-3.8.5-blue.svg
     :target: https://www.python.org/downloads/release/python-385/
     :alt: python 3.8.5
.. image:: https://img.shields.io/badge/django-3.0.8-green.svg
     :target: https://docs.djangoproject.com/en/3.0/releases/3.0.8/
     :alt: django 3.0.8


Getting Up and Running Locally
------------------------------
Setting Up Development Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Make sure to have the following on your host:

*Python 3.8

*PostgreSQL.

First things first.
^^^^^^^^^^^^^^^^^^^
Create a virtualenv::

    $ python3.8 -m venv <virtual env path>

Activate the virtualenv you have just created::

    $ source <virtual env path>/bin/activate

Install development requirements::

    $ pip install -r requirements/local.txt

Create a new PostgreSQL database using createdb::

    $ createdb qlomb-dashboard -U postgres --password <password>

Note:
if this is the first time a database is created on your machine you might need an initial PostgreSQL set up to allow local connections & set a password for the postgres user. The postgres documentation explains the syntax of the config file that you need to change.

Install prostgresql::

    $ sudo apt-get install postgresql

then fire::

    $ sudo apt-get install python-psycopg2

and last::

    $ sudo apt-get install libpq-dev


Set the environment variables for your database(s):

create an .env file in the root of your project and define all the variables you need in it::

    DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/qlomb-dashboard
    USE_DOCKER=no

Apply migrations::

    $ python manage.py migrate

If you’re running synchronously, see the application being served through Django development server::

    $ python manage.py runserver localhost:8000


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy qlomb_dashboard

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest
