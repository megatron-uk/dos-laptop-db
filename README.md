# 



## Installation

### Install Required Software

You will need the following software installed to run a version of the database application:

   * Python >= 3.10, including *pip*

To install all of the Python libraries needed for the application, open a terminal from the top level project directory and run:

``pip3 install -r requirements.txt``

### Run Test System

Change to the **dldb** directory and run:


``python3 manage.py runserver_plus --cert-file cert.crt``


The development server will attempt to run on *https://localhost:8080*

Or, just run ```run``` in the top level project directory.

Note that the development server is *not* suitable for exposing to the internet or running as a production service. For information on how to configure this application to run as a service, please see:

   * [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/modwsgi/)

