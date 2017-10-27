ReMap REST API
==============

This is the source code of ReMap 2018 REST API developed in Python/Django and Django REST Framework. To run the website locally, you need to install Django and a list of other Python packages which are listed in the requirements.txt file.


Get the development version from `GitHub`
--------------------------------------------

.. code-block:: bash

    git clone https://github.com/benoitballester/aziz_remap2rest.git
    cd aziz_remap2rest
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Then copy the following URL in your browser.

.. code-block:: bash

    Browseable API http://127.0.0.1:8000/api/v1/
    Live API: http://127.0.0.1:8000/#/v1

To deploy the app on a server with Apache and mod_wsgi please read this https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/modwsgi/​​


s