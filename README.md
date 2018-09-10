# datosgobar-acerca
Sub-secciones del "Acerca" de datosgobar.

## Generar sub-sección en markdown

1. Agregar un `.md` en el repositorio con la nueva sub-sección
2. Correr `python markdown_to_html.py section-name.md docs/section-name.html docs/andino-html/section-name.html "Section Name"` para generar tanto el HTML que debe subirse al container de Andino (docs/andino-html) como el HTML previsualizable localmente (docs).
3. Agregar el comando para generar la nueva sección en el `make build` del `Makefile`. Esta receta regenera los html de todos los markdown de las secciones.
4. Usar `make start_python_server` para previsualizar las secciones en `docs` localmente.
