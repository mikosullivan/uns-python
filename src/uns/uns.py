"""
UNS - Universal Namespace

This module provides a class to parse URIs into UNS.
"""

import urllib.parse

class UNS:
  def __init__(self, raw):
    """
    Initialize the UNS object.
    
    Parameters:
      raw (str|uri): URI object or string
    """
    
    # if a URI was passed in, parse it
    if isinstance(raw, urllib.parse.ParseResult):
      raw = urllib.parse.urlunparse(raw)
    
    # add scheme if missing
    if not raw.startswith(("http://", "https://")):  
      raw = "https://" + raw
    
    # replace namespace delimiter
    raw = raw.replace("~", "/")  
    
    # Parse the URI
    self.__uri = urllib.parse.urlparse(raw)

  def namespace(self):
    """
    Get the namespace portion of the URI
    
    Returns:
      str: The namespace string
    """

    return self.__uri.netloc + self.__uri.path

  def uri(self):
    """
    Get the full URI object
    
    Returns:
      str: The URI
    """

    return self.__uri

  def uri_str(self):
    return urllib.parse.urlunparse(self.uri())

  def filename(self):
    """
    Get the filename from the namespace
    
    Returns:
      str: The filename
    """

    return self.namespace().replace("/", "~")