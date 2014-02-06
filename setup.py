from setuptools import setup, find_packages
import sys, os

version = "1.0"

ir = ["zendesk"]

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
else:
    ir.append("configparser")

setup(name="zdgrab",
      version=version,
      scripts=["bin/zdgrab", "bin/zdsplode"],
      description="Get attachments from Zendesk tickets.",
      long_description="Get attachments from Zendesk tickets.",
      classifiers=["Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Utilities",
      ],
      keywords="zendesk attachment",
      author="Brent Woodruff",
      author_email="brent@fprimex.com",
      url="http://github.com/basho/zdgrab",
      license="Apache",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=ir,
      **extra
)
