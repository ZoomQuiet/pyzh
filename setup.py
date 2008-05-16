try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from pkg_resources import DistributionNotFound

import sys
import os
import glob

execfile(os.path.join('zhutils', 'release.py'))

# setup params
required_modules = []
extra_modules = {}

setup(
    name="zhutils",
    version=version,
    author=author,
    author_email=email,
    download_url="http://code.google.com/p/pyzh/downloads/list",
    license=license,
    keywords = "traditional, simplified, chinese",
    description=description,
    long_description=long_description,
    url=url,
    zip_safe=False,
    install_requires = required_modules,
    extras_require = extra_modules,
    include_package_data = True,
    packages=find_packages(exclude=["ez_setup", 'examples']),
    entry_points = """
    #[console_scripts]
    #f2j = zhpy.commandline:commandline
    #j2f
    """,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite = 'nose.collector',
    )

