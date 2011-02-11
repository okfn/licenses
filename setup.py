from setuptools import setup
__version__ = 0.6

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
    description=description.split('.')[0],
    long_description=description,
    license='Public Domain',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='http://bitbucket.org/okfn/licenses',
    packages=['licenses'],
    scripts=['licenses-deploy-level1', 'licenses-deploy-level2'],
    include_package_data = True,
    install_requires=[
        ],
    package_data = {
        '': ['licenses.db'],
    },
    zip_safe= False,
)
