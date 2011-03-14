=======
Prowlpy
=======

| Originally Written by Jacob Burch <jacoburch@gmail.com>, 7/6/2009
| Modified by Olivier Hervieu <olivier.hervieu@gmail.com>
| Updated for Prowl API 1.2 by Ken Pepple, 3/5/2011

Python module for posting to the iPhone Push Notification service Prowl: http://www.prowlapp.com/

Dependencies:
=============
The socket module must be compiled with SSL support.


Coming Backwards Incompatible Changes for 0.6
=====================================
- Anything referencing '*apikey' will be renamed to api_key
- the package is now in a prowlpy directory, not python. the python directory will be removed

Change Log:
===========
v0.52
-----
- changed demo variables names
- changed to VERSION from __version__
- removed __author__ et al. variables from the packages
- cleaned up the installation setup

v0.51
-----
- updated return values of retrieve_apikey and retrieve_token

v0.50
-----

- updated for prowl API v1.2
- added retrieve_apikey and retrieve_token
- add new example script
- added url support for post

V0.43
-----

- Remove httplib2 dependency, add providerkey support.

V0.42
-----

- Got rid of Now-uncessary URL Encoding.
- Working on incorporating forked changes while not totally breaking backward compatibility with the vanilla add function

V0.41
-----

- Adding priority setting
- Removed debug code

V0.4
----

- Added Prowl.add alias for Post
- Switched post to use (oddly enough) POST instead of GET
- Added a Prowl.veryify_key method

V0.3
----

- Changed to handle the new API system.

V0.2
----

- Basic working module

Todo:
-----

- Test against character-limits.
- More detailed Exceptions based on the returned XML document
