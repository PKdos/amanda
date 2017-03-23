# -*- encoding: utf-8 -*-

import pygeoip
import pprint
gi = pygeoip.GeoIP('GeoLiteCity.dat')
def geoM(x):
    pprint.pprint("Country code:-------------------- %s " %(str(gi.country_code_by_name(x))))
    pprint.pprint("Full record:--------------------- %s " %(str(gi.record_by_addr(x))))
    pprint.pprint("Country name:-------------------- %s " %(str(gi.country_name_by_addr(x))))
    pprint.pprint("Timezone: ------------------------%s " %(str(gi.time_zone_by_addr(x))))