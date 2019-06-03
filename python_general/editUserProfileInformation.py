# Python to edit Portal user profile information
# Connecting to my ArcGIS Enterprise

### I have a dodgy SSL certificate (self-signed) so need to ignore the error

from arcgis.gis import GIS
gis = GIS("https://test0205.local.net/arcgis/home","siteadmin",verify_cert=False)



# Let's make sure that I am getting the right server
gis



# Members can share content publicly
# default is set to 'true'

upd = {'canSharePublic':'false'}
gis.update_properties(upd)


# Allow members to edit biographica information and who can see their profile
# it is 'false' by default

upd = {'updateUserProfileDisabled':'true'}
gis.update_properties(upd)


#Removes external sources for data as well anything owned by esri, esri_nav and esri_<lang>
#Determines whether a set of Esri-provided content that requires external access to the internet is enabled. The default is true.

upd = {'externalContentEnabled':'false'}
gis.update_properties(upd)



# Password policy editing

upd = {"passwordPolicy": {
  "type": "custom",
  "minLength": 8,
  "minUpper": 1,
  "minLower": 1,
  "minLetter": 1,
  "minDigit": 1,
  "minOther": 1,
  "expirationInDays": 45,
  "historySize": 5,
  "created": 1544538809633,
  "modified": -1
}}
gis.update_properties(upd)

#...doesn't work
