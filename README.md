Machine readable list of open (http://opensource.org/,
http://opendefinition.org/) licenses and web service - see
<http://licenses.opendefinition.org/>.

Layout:

<pre>
README.md
index.html # home page
datapackage.json # data package info
licenses/{id}.json # json versions of licenses
licenses/{id}.json.js # jsonp
bin/ # scripts
</pre>

Note: jsonp versions are only created as part of the build and deploy process
for the service.

## Build and Deployment

To build files for deployment do:

    bin/deploy.py

For deployment simply upload the current directory files to a relevant online
location.

We currently, use github pages (but previously used s3).

## Changelog

HEAD
====

* Complete rewrite to be simpler (just data, no longer python library).
  See <https://github.com/okfn/licenses/issues/1>

v0.6.1 2011-02-22
=================

* Minor tweak to CC by-sa license name

v0.6 2011-02-11
===============

* Heavy refactoring and simplification
* Improve and add documentation

v0.5 2010-05-11
===============

* Addition of Licenses SoS v2.0 capabilities


v0.4 2010-03-08
===============

* This module is redesigned to be a web service
* Addition of Licenses SoS v1.0 capabilities (Specification of Service)


v0.3 2010-03-06 and older
=========================

* Module is designed to be imported to provide its list of licenses

