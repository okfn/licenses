from setuptools import setup
__version__ = 0.5

setup(
    name='licenses',
    version=__version__,

    # general metadata
    description='Web service that lists open (http://opensource.org/, http://opendefinition.org/) licenses',
    long_description='''
Todo: More about purpose of package.
Todo: More about installing package (easy_install licenses).
Todo: More about linking data at build-time (import licenses; print License().get_group_licenses('all_alphabetical')).
Todo: More about deploying package as a service (licenses-deploy DEST FQDN).
Todo: More about linking data at run-time (easy_install licenseservice; import ...).
    ''',
    license='PD',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='http://www.knowledgeforge.net/okfn/licenses/',
    packages=['licenses'],
    scripts=['licenses-deploy-level1', 'licenses-deploy-level2'],
    include_package_data = True,
    package_data = {
        '': ['licenses.db'],
    },
    zip_safe= False,
)
