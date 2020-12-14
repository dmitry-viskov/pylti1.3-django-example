Example of usage PyLTI1p3 library within Django framework
==========================================================

`PyLTI1p3`_ is a Python implementation of LTI 1.3 Advantage Tool.

.. _PyLTI1p3: https://github.com/dmitry-viskov/pylti1.3

First of all choose and configure test LTI 1.3 Platform. It may be:

* `IMS Global test site`_
* `Canvas LMS`_ (Detailed `instruction`_ how to setup Canvas as LTI 1.3 Platform is `here`_)
* `Blackboard Learn`_ (`Documentation`_)

.. _IMS Global test site: https://lti-ri.imsglobal.org
.. _Canvas LMS: https://github.com/instructure/canvas-lms
.. _instruction: https://github.com/dmitry-viskov/pylti1.3/wiki/Configure-Canvas-as-LTI-1.3-Platform
.. _here: https://github.com/dmitry-viskov/pylti1.3/wiki/Configure-Canvas-as-LTI-1.3-Platform
.. _Blackboard Learn: https://github.com/blackboard
.. _Documentation: https://docs.blackboard.com/standards/lti/tutorials/py-lti-1p3.html

The most simple way to check example is to use ``docker`` + ``docker-compose``.
Change the necessary configs in the ``configs/game.json`` (`here is instruction`_ how to generate your own public + private keys):

.. _here is instruction: https://github.com/dmitry-viskov/pylti1.3/wiki/How-to-generate-JWT-RS256-key-and-JWKS

.. code-block:: javascript

    {
        "<issuer>" : [{ // This will usually look something like 'http://example.com'
            "default": true, // this block will be used in case if client-id was not passed
            "client_id" : "<client_id1>", // This is the id received in the 'aud' during a launch
            "auth_login_url" : "<auth_login_url>", // The platform's OIDC login endpoint
            "auth_token_url" : "<auth_token_url>", // The platform's service authorization endpoint
            "auth_audience": null, // The platform's OAuth2 Audience (aud). Is used to get platform's access token,
                                   // Usually the same as "auth_token_url" but in the common case could be a different url
            "key_set_url" : "<key_set_url>", // The platform's JWKS endpoint
            "key_set": null, // in case if platform's JWKS endpoint somehow unavailable you may paste JWKS here
            "private_key_file" : "<path_to_private_key>", // Relative path to the tool's private key
            "public_key_file": "<path_to_public_key>", // Relative path to the tool's public key
            "deployment_ids" : ["<deployment_id>"] // The deployment_id passed by the platform during launch
        }, {
            "default": false,
            "client_id" : "<client_id2>",
            ...
        }]
    }

and execute:

.. code-block:: shell

    $ docker-compose up --build

You may use virtualenv instead of docker:

.. code-block:: shell

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ cd game
    $ python manage.py runserver 127.0.0.1:9001

Now there is game example tool you can launch into on the port 9001:

.. code-block:: shell

    OIDC Login URL: http://127.0.0.1:9001/login/
    LTI Launch URL: http://127.0.0.1:9001/launch/
    JWKS URL: http://127.0.0.1:9001/jwks/
