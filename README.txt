How to use the Licenses Package
===============================

This package can be used in three ways (develop, distribute, and deploy).

1.  Package data development.

    The package's data can be updated by running the scraper script. 

    The package contains a data file (./licenses/licenses.db) and a 
    scraper (./licenses-scrape) which updates the data file:

        $ hg clone https://knowledgeforge.net/okfn/licenses
        $ cd licenses
        $ python licenses-scrape.py

    A report will be printed about changes to the licenses data.

    Other changes could be completed before committing and pushing:

        $ hg ci
        $ hg push


2.  Package data distribution and release.

    The package's data can be distributed by running the setup script.

    The normal Python packaging command is sufficient:

        $ hg clone https://knowledgeforge.net/okfn/licenses
        $ cd licenses
        $ python setup.py sdist

    After testing, the package can be released to the Python Package Index:

        $ python setup.py egg_info -RDb "" sdist register upload


3.  Package data service provision.

    Install or update the Python package, then create a new service:

        $ easy_install licenses
        $ licenses-deploy DEST FQDN

    Include the generated Apache configuration file in your Apache server,
    issue service level agreements which reference the Licenses Specification
    of Service v2.0, configure your service execution management to monitor
    those service levels, and configure your help desk to allow issues to be
    raised and passed on service execution management or package development
    as appropriate.

