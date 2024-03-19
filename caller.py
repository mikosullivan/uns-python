#!/usr/bin/python3
from uns import *

raw = "idocs.com~color~dude"
color = UNS(raw)
print( type(color.uri()) )
print( urllib.parse.urlunparse(color.uri()) )

print ('---------------------------')

raw = "https://idocs.com~color~dude"
raw = urllib.parse.urlparse(raw)
color = UNS(raw)
print( type(color.uri()) )
print( urllib.parse.urlunparse(color.uri()) )
