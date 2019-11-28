from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = "negar",
  version = "1.0",
  description = "call negar in your python source code and log to a file ...",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = "SYS113",
  author_email = "051.SYS113@gmail.com",
  url = "https://github.com/sys113/negar",
  keywords = ["negar", "log", "save"],
  install_requires=['tzlocal'],
  classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: Implementation",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  entry_points = {
        "console_scripts": ["negar_log=negar:log"]}
)