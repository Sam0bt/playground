#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

def setup():
    qt4.configure("librecad.pro")

def build():
    qt4.make()

def install():
    pisitools.dobin("unix/librecad")
     
    pisitools.insinto("/usr/share/librecad/fonts/", "unix/resources/fonts/*")
    pisitools.insinto("/usr/share/librecad/library/", "unix/resources/library/*")
    pisitools.insinto("/usr/share/librecad/patterns/", "unix/resources/patterns/*")
    pisitools.insinto("/usr/share/librecad/qm/", "unix/resources/qm/*")
     
    pisitools.dodoc("README.md", "gpl-2.0.txt")
     
     
