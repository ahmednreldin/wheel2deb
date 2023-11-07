from setuptools import setup

INSTALL_REQUIRES = [
    'setuptools',
    'wheel',
    'pkginfo',
    'jinja2',
    'colorama',
    'attrs>=17',
    'packaging',
    'pyyaml',
    'dirsync'
]

version_template = """\
# coding: utf-8
# file generated by setuptools_scm
# don't change, don't track in version control
class Version:
    def __init__(self, version):
        self._p = version.split('.')
        self._v = version
    def __getitem__(self, key):
        return self._p[key]
    def __str__(self):
        return self._v
    def __repr__(self):
        return self._v
__version__ = Version({version!r})
"""

setup(setup_requires=['setuptools-scm', 'setuptools>=38.6.0'],
      use_scm_version={
          'write_to': 'src/_wheel2deb/version.py',
          'write_to_template': version_template},
      package_dir={'': 'src'},
      install_requires=INSTALL_REQUIRES,
      include_package_data=True)