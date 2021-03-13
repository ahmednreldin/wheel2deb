import pytest

from _wheel2deb.tools import parse_debian_control


def test_parse_debian_control(tmp_path):
    (tmp_path / 'debian').mkdir()
    with open(str(tmp_path / 'debian' / 'control'), 'w') as f:
        f.write("""Source: python-absl-py
Section: python
Priority: optional
Maintainer: wheel2deb <wheel2deb@upciti.com>
Build-Depends: debhelper
Standards-Version: 3.9.6

Package: python-absl-py
Architecture: all
Depends: ${misc:Depends}, ${shlibs:Depends}, python (>= 2.7~), python-enum34, python-six, python:any
Description: Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.
 This package was generated by wheel2deb.py v0.1
Homepage: https://github.com/abseil/abseil-py""")

    control = parse_debian_control(tmp_path)

    assert control['Section'] == 'python'
    assert control['Package'] == 'python-absl-py'
    assert control['Build-Depends'][0] == 'debhelper'
