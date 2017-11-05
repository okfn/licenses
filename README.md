[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/okfn/chat)

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

## contributions
Your contributions are very welcome. [Learn how you can help](./CONTRIBUTING.md)

## Layout

<pre>
README.md
index.html # home page
licenses/{id}.json # json versions of licenses
licenses/jsonp/{id}.js # jsonp
licenses/groups/ # special groups of licenses
bin/ # scripts
</pre>

Note: groups and jsonp versions are generated as part of the build and deploy
process for the service.

## Build and Deployment

To build files for deployment do:

    bin/deploy.py run

For deployment simply upload the current directory files to a relevant online location.

We currently use github pages (we previously used s3).

The changes in each [release](https://github.com/okfn/licenses/releases) are recorded in the [Change Log](./CHANGELOG.md).
