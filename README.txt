A list of open (http://opensource.org/, http://opendefinition.org/) licenses
together with API and web service.

How to use the Licenses Package
===============================

This package can be used in three ways (develop, distribute, and deploy).

1.  To create and access license data in JSON form.

    The package contains a data file (./licenses/licenses.db) and a scraper
    (licenses/scrape.py) which and updates the data file::

        $ hg clone https://bitbucket.org/okfn/licenses
        $ cd licenses
        $ python licenses/scrape.py

    A report will be printed about changes to the licenses data.


2.  Access of the data via a simple python API::

      >>> from licenses import Licenses
      >>> L = Licenses()
      >>> for l in L: print l
      ...
      odc-odbl
      ...
      >>> print l['odb-odbl']
      {'status': 'active', ...
      >>>

3.  Deployment as a service.

    Install or update the Python package, then create the service files::

        $ python licenses/deploy.py <path> <hostname>

    A whole set of files will be created at <path> which can then be served
    directly by your webserver.

