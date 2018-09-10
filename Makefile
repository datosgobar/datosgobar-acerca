build:
	python markdown_to_html.py sections/publica-datos.md docs/publica-datos.html docs/andino-html/publica-datos.html "Publicá datos"
	python markdown_to_html.py sections/marco-legal.md docs/marco-legal.html docs/andino-html/marco-legal.html "Marco legal"
	python markdown_to_html.py sections/glosario.md docs/glosario.html docs/andino-html/glosario.html "Glosario"

start_python_server:
	cd docs/ && python -m SimpleHTTPServer 8080

doctoc:
	doctoc --github --title " " publica-datos.md
	bash fix_github_links.sh publica-datos.md
