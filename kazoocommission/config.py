""" Kazoo Commission Runtime Configuration Options

.. note::
   Remember that this file is Python code. You can use your creativity to
   set the configuration in other ways that meet your needs, such as
   environmental variables.
"""

import os


# Settings for Kazoo Commission Server
KAZOO_COUCH_DB_URL = os.environ.get('KAZOO_COUCH_DB_URL',
                                    'http://localhost:5984')
""" URL to connect to CouchDB for 2600hz Kazoo """

DEBUG = 'KAZOO_COMMISSION_DEBUG' in os.environ
""" Enable Server Debug Mode """

DISABLE_SSL_CLIENT_SUBJECT_VALIDATION = \
    'KAZOO_COMMISSION_DISABLE_SSL_CLIENT_SUBJECT_VALIDATION' in os.environ
""" Whether or not the server will validate the MAC address of the requested
    device against the the X-SSL-Subject header passed from the web server.
    Highly recommended for security. """

# Settings for Template Generation
SIP_OUTBOUND_PROXY = os.environ.get('KAZOO_COMMISSION_SIP_OUTBOUND_PROXY',
                                    'localhost')

SIP_DNS_SRV = not 'SIP_DNS_A_RECORD' in os.environ
""" Use DNS SRV Record Mode - Defaults to DNS SRV Record if left unset """

FIRMWARE_SERVER_URL = os.environ.get('KAZOO_COMMISSION_FIRMWARE_SERVER_URL',
                                     'http://localhost/firmware')
""" URL of base directory firmware is served from (note: each template has
    its own subdirectory for firmware) """
