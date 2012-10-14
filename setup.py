# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

PACKAGE = "a1lite"
NAME = "django_a1lite"
DESCRIPTION = "django application for using http://a1pay.ru/ payment gateway"
AUTHOR = "Dmitry Kuksinsky"
AUTHOR_EMAIL = "dgk@dgk.su"
URL = "https://github.com/dgk/django_a1lite"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    #long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=[PACKAGE,],
    package_dir={PACKAGE: PACKAGE},
    package_data={PACKAGE: [
        'fixtures/*.json',
        'templates/*/*.html',
        'locale/*/*/django.*',
        'migrations/*.py',
        'templatetags/*.py',
    ]},

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)
