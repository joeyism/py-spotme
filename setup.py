# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


from setuptools import setup


version = "1.1.1"

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

with open("requirements.txt", "rb") as f:
    req = f.read().decode("utf-8")


setup(
    name = "spotme",
    packages = ["spotme"],
    entry_points = {
        "console_scripts": ['spotme = spotme.spotme:main']
        },
    version = version,
    description = "A command line tool that allows you to spin up AWS EC2 Spot Instances instantly",
    long_description = long_descr,
    author = "Joey Sham",
    author_email = "sham.joey@gmail.com",
    url = "https://github.com/joeyism/py-spotme",
    install_requires=req
    )
