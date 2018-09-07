build:
	python markdown_to_html.py publica-datos.md docs/publica-datos.html

doctoc:
	doctoc --github --title " " publica-datos.md
	bash fix_github_links.sh publica-datos.md
