"""
Who plugin for Pelican
===============================
This plugin looks for ``clients`` and ``drivers`` metadata header containing key/value pairs
and makes them available for use in templates
The first line of the ``clients`` and ``drivers`` metadata defines each key, and the following
lines contain corresponding values for each member.

clients: nom, type, logo, playstoreid, appstoreid, web, available
     tedyCab, Moteur de recherche, images/team/tedycab.png, com.transdev.tedycab, id1084982482, http://www.tedycab.com/, yes
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
            metadata['clients'][client_dict['logo']] = client_dict

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
            metadata['drivers'][driver_dict['logo']] = driver_dict


def register():
    signals.page_generator_context.connect(add_clients)
    signals.page_generator_context.connect(add_drivers)
