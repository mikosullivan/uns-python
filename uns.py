"""
UNS - Uniform Namespace

This module provides a class to parse URIs into UNS.
"""

import urllib.parse

class UNS:

  def __init__(self, raw):
    """
    Initialize the UNS object
    
    Parameters:
      raw (str): The raw URI or namespace string
    """
    
    # if a URI was passed in, use that
    if isinstance(raw, urllib.parse.ParseResult):
      self.__uri = raw  
    
    # else attempt to parse the param
    else:    
      if not raw.startswith(("http://", "https://")):  
        # add scheme if missing
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

  def filename(self):
    """
    Get the filename from the namespace
    
    Returns:
      str: The filename
    """

    return self.namespace().replace("/", "~")