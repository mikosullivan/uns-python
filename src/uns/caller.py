#!/usr/bin/python3
from uns import *

print ('--- from filename ------------------------')
raw = "idocs.com~color~dude"
print (raw)
color = UNS(raw)
print( type(color.uri()) )
print( color.uri_str() )
print( color.filename() )
print( color.namespace() )

print ('--- from URI -----------------------------')
raw = "https://idocs.com~color~dude"
print (raw)
uri = urllib.parse.urlparse(raw)
color = UNS(uri)
print( type(color.uri()) )
print( color.uri_str() )
print( color.filename() )
print( color.namespace() )