#!/home/projects/docs/2_acad_docs/acad_courses/other_courses/100daysofweb/static-sites-pelican/venv/bin/python3

# $Id: rstpep2html.py 9115 2022-07-28 17:06:24Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML from PEP
(Python Enhancement Proposal) documents.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except Exception:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates (X)HTML from reStructuredText-format PEP files.  '
               + default_description)

publish_cmdline(reader_name='pep', writer_name='pep_html',
                description=description)
