from setuptools import setup
__version__ = '0.6.1'

try:
    fo = open('README.txt')
    description = fo.read()
except:
    description = ''
finally:
    fo.close()

setup(
    name='licenses',
    version=__version__,

    # general metadata
    description=description.split('\n\n')[0],
    long_description=description,
    license='Public Domain',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='http://licenses.opendefinition.org/',
    download_url='http://bitbucket.org/okfn/licenses',
    packages=['licenses'],
    include_package_data = True,
    install_requires=[
        ],
    package_data = {
        '': ['licenses.db'],
    },
    zip_safe= False,
)
