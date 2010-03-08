from setuptools import setup
__version__ = 0.4

setup(
    name='licenses',
    version=__version__,

    # general metadata
    description='List of open (http://opensource.org/, http://opendefinition.org/) licenses',
    long_description='''
Todo: More about purpose of package.
Todo: More about installing package (easy_install licenses).
Todo: More about linking data at build-time (import licenses; print LicensesList().all_formatted).
Todo: More about deploying package as a service (licenses-deploy DEST FQDN).
Todo: More about linking data at run-time (easy_install licenseservice; import ...).
    ''',
    license='PD',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='http://www.knowledgeforge.net/okfn/licenses/',
    py_modules=['licenses'],
    scripts=['licenses-deploy'],
)
