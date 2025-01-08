# uns-python
Class for managing UNS objects

UNS (Universal Namespace) is a proposed standard for assigning namespaces
in any project. Using UNS, namespace conflicts can be avoided in settings,
file names, etc. UNS builds on the URI system. With a few exceptions, UNS
can be regarded as a subset of URIs. See https://github.com/mikosullivan/uns
for a full description of the standard.

This Python package provides simple translation between URI and UNS. It
consists of a single class. That class can be instantiated with any of
the format for UNS (namespace, URI, file name) and can output to any of
those formats.