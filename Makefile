build:
	python markdown_to_html.py sections/publica-datos.md docs/publica-datos.html docs/andino-html/publica-datos.html "Publicá datos"
	python markdown_to_html.py sections/marco-legal.md docs/marco-legal.html docs/andino-html/marco-legal.html "Marco legal"
	python markdown_to_html.py sections/glosario.md docs/glosario.html docs/andino-html/glosario.html "Glosario"
	python markdown_to_html.py sections/productos.md docs/productos.html docs/andino-html/productos.html "Productos"

start_python_server:
	cd docs/ && python -m SimpleHTTPServer 8080

doctoc:
	doctoc --github --title " " sections/publica-datos.md
	bash fix_github_links.sh sections/publica-datos.md
	doctoc --github --title " " sections/productos.md
	bash fix_github_links.sh sections/productos.md
