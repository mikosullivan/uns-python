#!/usr/bin/python
from uns import UNS
import urllib.parse

def run_checks(uns):
    assert ( isinstance(uns.uri(), urllib.parse.ParseResult) )
    assert ( uns.uri_str() == 'https://idocs.com/color/dude' )
    assert ( uns.filename() == 'idocs.com~color~dude' )
    assert ( uns.namespace() == 'idocs.com/color/dude' )

run_checks(UNS('https://idocs.com/color/dude'))
run_checks(UNS('idocs.com~color~dude'))
run_checks(UNS('idocs.com/color/dude'))
run_checks(UNS(urllib.parse.urlparse('https://idocs.com/color/dude')))



# print ('--- from weird URI -----------------------------')
# raw = "https://idocs.com~color~dude"
# uri = urllib.parse.urlparse(raw)
# color = UNS(uri)
# print( type(color.uri()) )
# print( color.uri_str() )
# print( color.filename() )
# print( color.namespace() )

# done
print ('[done]')