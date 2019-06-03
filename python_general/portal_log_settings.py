# USAGE: Print out the Log Settings

from arcgis.gis import GIS
from utils import localLogger
from utils.exceptions import *

gis = GIS("https://sdmsdev1w004.ordsvy.gov.uk/portal", "siteadmin", "siteadmin1")
logs = gis.admin.logs
logsettings = logs.settings
for key, value in list(dict(logsettings).items()):
    print(("{} : {}".format(key, value)))

print ("Checking the log status")
localLogger.initialise("portal_config.logfile")
# localLogger.initialise(None,False,"DEBUG")