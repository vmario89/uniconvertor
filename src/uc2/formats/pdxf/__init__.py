# -*- coding: utf-8 -*-
#
#  Copyright (C) 2012 by Ihor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import zipfile

from uc2.formats.pdxf import const
from uc2.formats.pdxf import model
from uc2.formats.pdxf.presenter import PDXF_Presenter
from uc2.utils.mixutils import merge_cnf

PDXF_HEADER = (b'\x50\x4b\x03\x04\x14\x00\x00\x00')


def pdxf_loader(appdata, filename, translate=True, cnf=None, **kw):
    cnf = merge_cnf(cnf, kw)
    pdxf_doc = PDXF_Presenter(appdata, cnf, filename)
    return pdxf_doc


def pdxf_saver(pdxf_doc, filename, translate=True, cnf=None, **kw):
    cnf = merge_cnf(cnf, kw)
    pdxf_doc.save(filename)


def check_pdxf(path):
    if not zipfile.is_zipfile(path):
        return False

    pdxf_file = zipfile.ZipFile(path, 'r')
    fl = pdxf_file.namelist()
    if 'mimetype' not in fl or not pdxf_file.read('mimetype') == const.DOC_MIME:
        return False
    return True
