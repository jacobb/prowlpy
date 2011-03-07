=======
Prowlpy
=======

Originally Written by Jacob Burch, 7/6/2009
Modified by Olivier Hervieu
Updated for Prowl API 1.2 by Ken Pepple, 3/5/2011

Python module for posting to the iPhone Push Notification service Prowl: http://www.prowlapp.com/

Dependencies:
=============

No extra dependency. (Prowlpy use only basic python modules)
The socket module must be compiled with SSL support

Change Log:
===========

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