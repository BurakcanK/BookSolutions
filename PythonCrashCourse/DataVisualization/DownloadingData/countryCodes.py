from pygal_maps_world.i18n import COUNTRIES


def getCountryCode(countryName):
    """ Return the Pygal 2-digit country code for the given country. """
    for code, name in COUNTRIES.items():
        if name == countryName:
            return code

    # if country wasn't found, return None
    return None
