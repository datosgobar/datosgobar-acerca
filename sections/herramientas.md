# Herramientas

Acá podés ver todo lo que hacemos para potenciar la apertura y el consumo de datos públicos.

## Recursos y documentos

* Material introductorio
    - [**Kit de Datos Abiertos**](https://www.argentina.gob.ar/sites/default/files/2._kit_de_datos_abiertos.pdf). Introducción a los datos abiertos, qué son y cuáles son los recursos disponibles para publicar datos.
    - [**Glosario**](https://datosgobar.github.io/paquete-apertura-datos/glosario/). Términos y conceptos utilizados en nuestros recursos y documentos.

* Guías de buenas prácticas
    - [**Guía para la publicación de datos en formatos abiertos**](https://datosgobar.github.io/paquete-apertura-datos/guia-abiertos/). Recomendaciones para publicar datos en formatos abiertos, estructurar bien una tabla, nombrar archivos y columnas, usar estándares básicos y trabajar con planillas de cálculo.
    - [**Guía para la identificación y uso de entidades interoperables**](https://datosgobar.github.io/paquete-apertura-datos/guia-interoperables/). Recomendaciones y referencias para nombrar entidades en activos de datos, usando sus nombres y códigos oficiales.
    - [**Guía para el uso y la publicación de metadatos**](https://datosgobar.github.io/paquete-apertura-datos/guia-metadatos/). Recomendaciones y estándares para documentar activos de datos.

* Guías de implementación
    - [**Guía para la apertura de datos en organismos de la Administración Pública Nacional**](http://datos.gob.ar/acerca/seccion/Publicá%20datos). Paso a paso que pueden seguir los organismos de la APN para crear su catálogo de datos y publicar sus datos abiertos en [datos.gob.ar](http://datos.gob.ar).
    - [**Guía para la apertura de datos en gobiernos provinciales y municipales**](https://datosgobar.github.io/paquete-apertura-datos/guia-subnacionales/). Guía de implementación de políticas de apertura de datos para provincias y municipios de Argentina.

* Estándares
    - [**Perfil Regional de Metadatos**](https://perfil-regional-metadatos.readthedocs.io/) ([En Inglés](https://perfil-regional-metadatos.readthedocs.io/en/latest/) | [Github](https://github.com/datosgobar/perfil-regional-metadatos)). Iniciativa elaborada con el Grupo de Datos Abiertos de la Red GEALC de la Organización de Estados Americanos para construir un perfil de metadatos base para los países de la región.

* Talleres
    * **Taller Análisis de Datos 101** ([Github](https://github.com/datosgobar/taller-analisis-datos-101)). Taller introductorio al análisis de datos con Python, presentado en la PyconAR 2016.
    * **Taller Análisis Exploratorio de Datos** ([Github](https://github.com/datosgobar/taller-analisis-mediaparty-2017)). Taller introductorio al análisis exploratorio de datos, presentado en la MediaParty 2017.
    * **Taller SQL 101** ([Presentación](https://datosgobar.github.io/taller-sql-101/) | [Github](https://github.com/datosgobar/taller-sql-101)). Taller interno de introducción a SQL.
    * **Taller de Series de Tiempo** ([Github](https://github.com/datosgobar/taller-series-tiempo-mediaparty-2018)). Taller de uso de la API de Series de Tiempo en distintos entornos de trabajo con datos, presentado en la MediaParty 2018.
    * **Taller Github 101** ([Presentación](https://datosgobar.github.io/taller-github-101) | [Github](https://github.com/datosgobar/taller-github-101)). Taller interno de introducción al uso de Github.
    * **Taller Github 201** ([Presentación](https://datosgobar.github.io/taller-github-201) | [Github](https://github.com/datosgobar/taller-github-201)). Taller interno de conflictos de edición en Github y cómo manejarlos.
    * **Taller Repositorios en Github** ([Presentación](https://datosgobar.github.io/taller-repos-readmes/) | [Github](https://github.com/datosgobar/taller-repos-readmes)). Taller interno sobre consejos, tips, templates y políticas para estructurar repositorios y escribir buenos readmes.

* Artículos
    - [**Publicación de Medium**](https://medium.com/datos-argentina). Artículos de difusión del equipo de Datos Argentina.

## Desarrollos

### Apertura

* **Portal Andino** ([Landing de producto](http://andino.datos.gob.ar/) | [Ejemplo desarrollo](http://portal-andino.datos.gob.ar/) | [Documentación](http://portal-andino.readthedocs.io/) | [Github](http://github.com/datosgobar/portal-andino)). Distribución de CKAN desarrollada por la República Argentina dockerizada, fácil de instalar y compatible con el Perfil Nacional de Metadatos de la Política de Apertura de Datos.

* Herramientas para la apertura de datos
    - **pydatajson** ([Documentación](https://pydatajson.readthedocs.io/) | [Github](https://github.com/datosgobar/pydatajson)). Librería en python para analizar, generar y validar metadatos en formato data.json.
    - **monitoreo-apertura** ([Github](https://github.com/datosgobar/monitoreo-apertura)). Aplicación web para monitoreo de la red de nodos de datos abiertos de la Administración Pública Nacional.
    - **data-cleaner** ([Documentación](https://data-cleaner.readthedocs.io/) | [Github](https://github.com/datosgobar/data-cleaner)). Librería en python para para limpieza de datos, según estándares del Equipo de Datos Argentina.
    - **django-datajsonar** ([Github](https://github.com/datosgobar/django-datajsonar)). Aplicación en _Django_ para administrar acciones sobre la red de nodos de catálogos, basada en el Perfil Nacional de Metadatos de la Política de Apertura de Datos.

### Servicios

* Georef
    - **API del Servicio de Normalización de Datos Geográficos de Argentina** ([Documentación](http://apis.datos.gob.ar/georef/) | [Github](https://github.com/datosgobar/georef-ar-api )). Normaliza nombres de provincias, departamentos, municipios, otras unidades territoriales de la Argentina, calles y direcciones. Enriquece datasets con coordenadas agregando las unidades territoriales que las contienen.

* Series de Tiempo
    - **API de Series de Tiempo de la República Argentina** ([Documentación](https://apis.datos.gob.ar/series) | [Github](https://github.com/datosgobar/series-tiempo-ar-api)). Expone recursos para buscar y consultar indicadores con evolución temporal de organismos de la Administración Pública Nacional, realizando filtros y operaciones sobre ellos.
    - [**Explorador de Series de Tiempo**](http://datos.gob.ar/series) ([Ejemplo desarrollo](https://datosgobar.github.io/series-tiempo-ar-explorer/) | [Github](https://github.com/datosgobar/series-tiempo-ar-explorer)). Interfaz web para buscar, visualizar y compartir indicadores disponibles en la API de Series de Tiempo.
    - **Landing de Series de Tiempo** ([Ministerio de Hacienda](https://www.minhacienda.gob.ar/datos/) | [Ejemplo desarrollo](https://datosgobar.github.io/series-tiempo-ar-landing/) | [Github](https://github.com/datosgobar/series-tiempo-ar-landing)). Tablero de indicadores y gráficos de la API de Series de Tiempo, fácil de configurar y personalizar para crear diferentes instancias.
    - **Scraper de Series de Tiempo en Excel** ([Github](https://github.com/datosgobar/series-tiempo-ar-scraping)). Rutina para la extracción y transformación de series de tiempo desde Excels semi-estructurados hacia distribuciones de formato abierto, basado en una extensión experimental del Perfil Nacional de Metadatos de la política de apertura de datos de la APN.
    - [**Generador de Llamadas a la API**](https://datosgobar.github.io/series-tiempo-ar-call-generator/) ([Github](https://github.com/datosgobar/series-tiempo-ar-call-generator)). Interfaz web para buscar series de tiempo de la API y construir URLs de consulta.

* **API Gateway** ([Github](https://github.com/datosgobar/api-gateway)). Aplicación en Django y Kong para administrar cuotas y ruteo de APIs.

### Herramientas para el análisis de datos

* **textar** ([Documentación](https://textar.readthedocs.io/) | [Github](https://github.com/datosgobar/textar)). Paquete en python para análisis, clasificación y recuperación de textos, utilizado por el equipo de Datos Argentina.
* **detector-aedes** ([Documentación](https://detector-aedes.readthedocs.io/) | [Github](https://github.com/datosgobar/detector-aedes)). Algoritmos de visión computacional para analizar imágenes de Ovisensores.
