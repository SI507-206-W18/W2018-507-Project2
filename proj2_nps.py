## proj_nps.py
## Skeleton for Project 2, Winter 2018
## ~~~ modify this file, but don't rename it ~~~


## you can, and should add to and modify this class any way you see fit
## you can add attributes and modify the __init__ parameters,
##   as long as tests still pass
##
## the starter code is here just to make the tests run (and fail)
class NationalSite():
    def __init__(self, type, name, desc, url=None):
        self.type = type
        self.name = name
        self.description = desc
        self.url = url

        # needs to be changed, obvi.
        self.address_street = '123 Main St.'
        self.address_city = 'Smallville'
        self.address_state = 'KS'
        self.address_zip = '11111'

## you can, and should add to and modify this class any way you see fit
## you can add attributes and modify the __init__ parameters,
##   as long as tests still pass
##
## the starter code is here just to make the tests run (and fail)
class NearbyPlace():
    def __init__(self, name):
        self.name = name

## Must return the list of NationalSites for the specified state
## param: the 2-letter state abbreviation, lowercase
##        (OK to make it work for uppercase too)
def get_sites_for_state(state_abbr):
    return []


## Must return the list of NearbyPlaces for the specifite NationalSite
## param: a NationalSite object
def get_nearby_places_for_site(national_site):
    return []
