#!/usr/bin/env python
import os
import re
from setuptools import find_packages, setup

from mutant import __version__


MODULE_PATH = os.path.abspath(os.path.dirname(__file__))

LINK_REQUIREMENT = re.compile(
    r'^https://.+#egg=(?P<package>.+)-(?P<version>\d(?:\.\d)*)$'
)


install_requires = ['django>=1.7']
dependency_links = []

for requirement in (l.strip() for l in open(os.path.join(MODULE_PATH, 'requirements/base.txt'))):
    match = LINK_REQUIREMENT.match(requirement)
    if match:
        install_requires.append("%(package)s==%(version)s" % match.groupdict())
        dependency_links.append(match.group())
    else:
        install_requires.append(requirement)


setup(
    name='django-mutant',
    version=__version__,
    description='Dynamic model definition and alteration (evolving schemas)',
    long_description=open(os.path.join(MODULE_PATH, 'README.rst')).read(),
    url='https://github.com/charettes/django-mutant',
    author='Simon Charette',
    author_email='charette.s@gmail.com',
    install_requires=install_requires,
    dependency_links=dependency_links,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
