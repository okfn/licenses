Machine readable list of open (http://opensource.org/,
http://opendefinition.org/) licenses and web service - see
<http://licenses.opendefinition.org/>.

For more information, including details of web service usage, see
<http://licenses.opendefinition.org/> or <pre>index.html</pre> in this
directory.

## License

All data (and associated content) is placed in the Public Domain using the
[Public Domain Dedication and
License](http://opendatacommons.org/licenses/pddl/1-0/). All code is licensed
under the [MIT License](http://www.opensource.org/licenses/mit-license.php).


## Layout

<pre>
README.md
index.html # home page
licenses/{id}.json # json versions of licenses
licenses/jsonp/{id}.js # jsonp
licenses/groups/ # special groups of licenses
bin/ # scripts
</pre>

Note: grups and jsonp versions are generated as part of the build and deploy
process for the service.

## Build and Deployment

To build files for deployment do:

    bin/deploy.py run

For deployment simply upload the current directory files to a relevant online
location.

We currently use github pages (we previously used s3).

## Changelog

### HEAD

* Complete rewrite to be simpler (just data, no longer python library).
  See <https://github.com/okfn/licenses/issues/1>

### v0.6.1 2011-02-22

* Minor tweak to CC by-sa license name

### v0.6 2011-02-11

* Heavy refactoring and simplification
* Improve and add documentation

### v0.5 2010-05-11

* Addition of Licenses SoS v2.0 capabilities


### v0.4 2010-03-08

* This module is redesigned to be a web service
* Addition of Licenses SoS v1.0 capabilities (Specification of Service)


### v0.3 2010-03-06 and older

* Module is designed to be imported to provide its list of licenses

