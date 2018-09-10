build:
	python markdown_to_html.py publica-datos.md docs/publica-datos.html docs/andino-html/publica-datos.html "Publicá datos"

start_python_server:
	cd docs/ && python -m SimpleHTTPServer 8080

doctoc:
	doctoc --github --title " " publica-datos.md
	bash fix_github_links.sh publica-datos.md
