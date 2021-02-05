from setuptools import setup , find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = "negar",
  version = "0.6.0",
  description = "call negar in your python source code and error & text log to a file ...",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = "SYS113",
  author_email = "051.SYS113@gmail.com",
  url = "https://github.com/sys113/negar",
  keywords = ["negar", "log", "error", "save"],
  packages = find_packages(),
  install_requires=['tzlocal'],
  classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: Implementation",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
)
