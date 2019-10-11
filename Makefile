build:
	python markdown_to_html.py sections/publica-datos.md docs/publica-datos.html docs/andino-html/publica-datos.html "Publicá datos"
	python markdown_to_html.py sections/marco-legal.md docs/marco-legal.html docs/andino-html/marco-legal.html "Marco legal"
	python markdown_to_html.py sections/glosario.md docs/glosario.html docs/andino-html/glosario.html "Glosario"
	python markdown_to_html.py sections/herramientas.md docs/herramientas.html docs/andino-html/herramientas.html "Herramientas"
	python markdown_to_html.py sections/monitoreo.md docs/monitoreo.html docs/andino-html/monitoreo.html "Monitoreo"

start_python_server:
	cd docs/ && python -m SimpleHTTPServer 8080

clean:
	rm docs/glosario.html
	rm docs/herramientas.html
	rm docs/marco-legal.html
	rm docs/monitoreo.html
	rm docs/publica-datos.html
	rm docs/andino-html/glosario.html
	rm docs/andino-html/herramientas.html
	rm docs/andino-html/marco-legal.html
	rm docs/andino-html/monitoreo.html
	rm docs/andino-html/publica-datos.html

doctoc:
	doctoc --github --title " " sections/marco-legal.md
	bash fix_github_links.sh sections/marco-legal.md
	doctoc --github --title " " sections/glosario.md
	bash fix_github_links.sh sections/glosario.md
	doctoc --github --title " " sections/publica-datos.md
	bash fix_github_links.sh sections/publica-datos.md
	doctoc --github --title " " sections/herramientas.md
	bash fix_github_links.sh sections/herramientas.md
	doctoc --github --title " " sections/monitoreo.md
	bash fix_github_links.sh sections/monitoreo.md
