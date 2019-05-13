#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convierte archivos markdown a template html de "Acerca" de datosgobar

    python markdown_to_html.py sections/publica-datos.md docs/publica-datos.html docs/andino-html/publica-datos.html "Publicá datos"
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import sys

import markdown

from andino_templates import PREVIEW_TEMPLATE, SECTION_TEMPLATE


def main(input_path, output_path_preview, output_path_section,
         section_name):

    # convierte el markdown a html
    with open(input_path, "r") as f:
        md = f.read()
        html = markdown.markdown(md)

    # genera el html de la sección para previsualizar en este repo
    with open(output_path_preview, "wb") as f:
        preview_html = PREVIEW_TEMPLATE.format(
            document=html,
            section_name=section_name
        )
        f.write(preview_html.encode("utf-8"))

    # genera el html de la sección para subir al container de Andino
    with open(output_path_section, "wb") as f:
        section_html = SECTION_TEMPLATE.format(
            document=html,
            section_name=section_name
        )
        f.write(section_html.encode("utf-8"))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
