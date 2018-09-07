#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convierte archivos markdown a template html de "Acerca" de datosgobar

    python markdown_to_html.py publica-datos.md docs/publica-datos.html
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os
import sys

import markdown
from bs4 import BeautifulSoup


def main(input_path, output_path):
    with open(input_path, "r") as f:
        md = f.read().decode("utf-8")

    with open(output_path, "wb") as f:
        html = markdown.markdown(md)
        # bs = BeautifulSoup(html, "html5lib")
        # pretty_html = bs.prettify()

        andino_html = """
{{% extends "gobar_page.html" %}} {{% block page %}}

<div class="container-fluid" id="template-config-container">
    <div class="restricted-max-width ">
        <div id="template-config" class="col-xs-12 col-md-10 col-md-offset-1 about-template-container" style="padding: 0 60px;">

{document}

        </div>
    </div>
</div>

{{% endblock %}}
        """.format(document=html)

        f.write(andino_html.encode("utf-8"))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
