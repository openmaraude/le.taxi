"""
Members info plugin for Pelican
===============================
This plugin looks for a ``members`` metadata header containing key/value pairs
and makes them available for use in templates
The first line of the members metadata defines each key, and the following
lines contain corresponding values for each member.
:members: nom, email, twitter, github, site_nome, site_href
    Danilo Shiga, daniloshiga@gmail.com, @daneoshiga, daneoshiga, Danilo Shiga, http://daniloshiga.com
"""

from collections import OrderedDict

from pelican import signals


def add_clients(generator, metadata):

    if 'clients' in metadata.keys():
        # Dealing with differences on metadata for md and rst content
        if type(metadata['clients']) == list:
            clients = metadata['clients']
        else:
            clients = metadata['clients'].splitlines()

        metadata['clients'] = OrderedDict()
        keys = map(unicode.strip, clients[0].split(','))
        for client in clients[1:]:
            values = map(unicode.strip, client.split(','))
            client_dict = dict(zip(keys, values))
            metadata['clients'][client_dict['nom']] = client_dict

def add_drivers(generator, metadata):

    if 'drivers' in metadata.keys():
        # Dealing with differences on metadata for md and rst content
        if type(metadata['drivers']) == list:
            drivers = metadata['drivers']
        else:
            drivers = metadata['drivers'].splitlines()

        metadata['drivers'] = OrderedDict()
        keys = map(unicode.strip, drivers[0].split(','))
        for driver in drivers[1:]:
            values = map(unicode.strip, driver.split(','))
            driver_dict = dict(zip(keys, values))
            metadata['drivers'][driver_dict['nom']] = driver_dict


def register():
    signals.page_generator_context.connect(add_clients)
    signals.page_generator_context.connect(add_drivers)
