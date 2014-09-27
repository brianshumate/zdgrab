from setuptools import setup
import sys

extra = {}
if sys.version_info < (3,):
        extra['use_3to2'] = True

setup(name="zdgrab",
      version="2.0",
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
      url="http://github.com/fprimex/zdgrab",
      license="Apache",
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "zdesk",
      ],
      **extra
)
