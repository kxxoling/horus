Horus
=====

Finds the best matched programmers for companies.

.. image:: https://travis-ci.org/kxxoling/librorum.svg?branch=master
    :target: https://travis-ci.org/kxxoling/librorum

The name horus comes from ancient Egyptian god “Horus” who controls the sky.

The project “horus” aims to connects the best matched programmers and companny
or their agent -- HRs.


Deploy
------

Normal
~~~~~~

Usually, you can deploy it on you favorite environment.

0. Get the code

.. code-block:: shell

    git clone https://github.com/kxxoling/horus


1. Install all requirements

.. code-block:: shell

    pip install -r requirements.txt

2. Start main service and create db

.. code-block:: shell

    python run.py


docker and docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~

``docker-compose`` is now supported, just make sure docker and docker-compose is
installed, and input the following command:

.. code-block:: shell

    docker-compose up

The site will be serve at port 5000.

