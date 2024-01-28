from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gymmgt/__init__.py
from gymmgt import __version__ as version


setup(
	name="gymmgt",
	version=version,
	description="A gym management system is a software application designed to help gym owners and managers streamline their operations and manage day-to-day tasks. This may include things like membership management, scheduling, billing and payments, facility and equipment management, and reporting and analytics.",
	author="Jaydeep-Sigzen",
	author_email="jaydeep@sigzen.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
