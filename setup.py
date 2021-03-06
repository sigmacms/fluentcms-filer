#!/usr/bin/env python

import os
import re
import sys
import codecs

from setuptools import setup, find_packages

# When creating the sdist, make sure the django.mo file also exists:
if 'sdist' in sys.argv or 'develop' in sys.argv:
    os.chdir('fluentcms_filer')

    for plugin in ['file', 'picture', 'teaser']:
        os.chdir(plugin)
        try:
            from django.core.management.commands.compilemessages import Command
            command = Command()
            command.execute(stdout=sys.stderr, exclude=[], verbosity=1)
        except ImportError:
            # < Django 1.7
            from django.core.management.commands.compilemessages import compile_messages
            compile_messages(sys.stderr, exclude=[])
        finally:
            os.chdir('..')

    os.chdir('..')


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name='fluentcms-filer',
    version=find_version('fluentcms_filer', '__init__.py'),
    license='Apache License, Version 2.0',

    install_requires=[
        'django-fluent-contents>=1.0',
        'django-filer>=0.9',
    ],
    requires=[
        'Django (>=1.4)',
    ],

    description='django-filer content plugins for django-fluent-pages',
    long_description=read('README.rst'),

    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',

    url='https://github.com/bashu/fluentcms-filer',
    download_url='https://github.com/bashu/fluentcms-filer/zipball/master',

    packages=find_packages(exclude=('example*',)),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
