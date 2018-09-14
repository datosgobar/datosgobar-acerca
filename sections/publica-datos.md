# Publicá datos

<div style="background: #eeeeee; border-color: #999999; margin-top: 25px;margin-bottom: 10px; padding: 50px; padding-bottom: 40px; padding-top: 0px; border: 1px solid transparent; border-radius: 4px;">

    <h2>Datos abiertos: qué son y por qué tu organismo quiere abrirlos</h2>

    <p>Los datos públicos son todos aquellos que el sector público genera y/o administra para el cumplimiento de sus misiones y funciones. No todos los datos públicos <em>están publicados</em>; y no es lo mismo <em>publicar datos</em> que <em>abrir datos</em>.</p>

    <p>La diferencia entre un dato <em>publicado</em> y uno <em>abierto</em> es <strong>todo lo que hace que el dato público sea valioso y fácil de reutilizar</strong> por terceros dentro y fuera del sector público, o incluso por uno mismo:</p>

    <ul>
    <li>Que sea fácil de encontrar.</li>
    <li>Que sea fácil de usar por distintos usuarios, para distintos usos y mediante distintas herramientas.</li>
    <li>Que se pueda cruzar con otros datos (públicos o no, abiertos o no).</li>
    <li>Que se pueda integrar en sistemas y aplicaciones.</li>
    </ul>

    <p>Abrir los datos de tu organismo te ayuda a:</p>

    <ul>
    <li>Bajar los costos de compartir datos.</li>
    <li>Organizar tu flujo de trabajo con datos.</li>
    <li>Transparentar la gestión.</li>
    <li>Promover la generación de valor agregado por terceros.</li>
    </ul>

    <p>Si querés saber más sobre datos abiertos podés consultar nuestro <strong><a href="https://www.argentina.gob.ar/sites/default/files/2._kit_de_datos_abiertos.pdf">Kit de Datos Abiertos</a></strong>.</p>
</div>

## Introducción

**Todos los archivos de datos, servicios web de datos y aplicaciones web diseñadas para la descarga de datos** que tu organismo tiene en su propiedad digital en internet o en [argentina.gob.ar](https://www.argentina.gob.ar/) son datos públicos que esperan ser abiertos.

Para abrir los datos de tu organismo, te proponemos estos pasos:

1. Publicá en datos.gob.ar
2. Mejorá la calidad de tus datos
3. Publicá datos como un servicio

---

## 1. Publicá en datos.gob.ar

El Portal Nacional de Datos Abiertos (**[datos.gob.ar](http://datos.gob.ar)**) es el punto de acceso para buscar y acceder fácilmente a los datos que publican los organismos de la Administración Pública Nacional.

Si querés incorporar los datos de tu organismo al Portal Nacional, acá te contamos los pasos del proceso para hacerlo:

### Creá un catálogo de datos abiertos

El primer paso para incorporarte a datos.gob.ar es inventariar los datos que tenés y dónde están alojados, y para eso necesitamos que confecciones un catálogo de datos. 

Un catálogo de datos abiertos es una lista de activos de datos y sus metadatos, que te describen qué son y cómo podés usarlos. **Facilita encontrar y entender los datos publicados por organismos del Estado**.

Para armar un catálogo, no necesitás tener un portal web; podés crearlo  de varias maneras: 


* **Instalando un Portal Andino**. Instalando un portal web de datos abiertos (Ej: [https://datos.agroindustria.gob.ar](https://datos.agroindustria.gob.ar) - portal de datos abiertos del Ministerio de Agroindustria). Leé más sobre qué es y cómo instalar **[Portal Andino](http://andino.datos.gob.ar/)**.
* **Completando un Excel**. Subiendo un archivo Excel a una URL (Ej: [http://estadisticas.produccion.gob.ar/catalogo.xlsx](http://estadisticas.produccion.gob.ar/catalogo.xlsx) - catálogo de la Secretaría de Transformación Productiva).
* **Generando un JSON**. Generando y subiendo un archivo JSON a una URL (Ej: [https://www.presupuestoabierto.gob.ar/datasets/data.json](https://www.presupuestoabierto.gob.ar/datasets/data.json) - catálogo de la Subsecretaría de Presupuesto). Esto podrías hacerlo mediante una aplicación propia, otro portal de datos abiertos, etc.

Ver más [ejemplos de catálogos](http://infra.datos.gob.ar/catalog/modernizacion/dataset/8/distribution/8.1/download/nodos.csv).

Leé más sobre cómo [crear un catálogo sin usar Portal Andino](https://paquete-apertura-datos.readthedocs.io/es/stable/guia_metadatos.html#otros-catalogos).

### Documentá tus datos

**Para que los datos sean abiertos, es fundamental documentarlos** como *datasets* en tu catálogo de datos abiertos.

Leé más sobre cómo documentar tus datos en nuestra **[Guía para el uso y la publicación de metadatos](https://paquete-apertura-datos.readthedocs.io/es/stable/guia_metadatos.html)**.

El [equipo de Datos](https://datosgobar.github.io/) del Ministerio de Modernización está para ayudarte en este proceso contactanos a [datos@modernizacion.gob.ar](mailto:datos@modernizacion.gob.ar) para que te asistamos en cómo hacerlo mejor y cómo planificar tus próximos pasos.

### Sumá tu catálogo a datos.gob.ar

Si tu catálogo cumple con el **[Perfil Nacional de Metadatos para Datos Abiertos](https://paquete-apertura-datos.readthedocs.io/es/stable/guia_metadatos.html#campos-del-perfil)** puede integrarse a datos.gob.ar. Cualquier modificación en tu catálogo se verá reflejada automáticamente en datos.gob.ar.

* Escribinos a [datos@modernizacion.gob.ar](mailto:datos@modernizacion.gob.ar) con la URL de tu catálogo para que te sumemos a **[datos.gob.ar](http://datos.gob.ar)**.
* Si sos desarrollador, y querés ver si tu catalogo está listo para estar en datos.gob.ar [validalo con **pydatajson**](https://pydatajson.readthedocs.io/es/stable/MANUAL.html#validacion).

A partir de que nos enviás la URL de tu catálogo, el equipo de Datos Argentina analiza cada dataset nuevo que publicás y te ayuda a mejorar la calidad de sus datos y metadatos, antes de agregarlo a **[datos.gob.ar](http://datos.gob.ar)**.

Ahora que ya estás publicando te proponemos trabajar en la calidad de tu datos.

## 2. Mejorá la calidad de tus datos

Una vez que tenés un catálogo de datos abiertos podés mejorar la calidad de tus datos siguiendo buenas prácticas.

### Compartí tus datos en formatos abiertos

La diferencia entre un dato *publicado* y uno *abierto* es que este debe ser fácil de utilizar por distintos usuarios, para distintos usos y mediante distintas herramientas.

Leé sobre cómo publicar en formatos abiertos en nuestra **[Guía para la publicación de datos en formatos abiertos](http://paquete-apertura-datos.readthedocs.io/es/stable/guia_abiertos.html)**.

Si sos desarrollador y querés implementar rutinas de transformación y limpieza de datos que sigan estas buenas prácticas, podés usar **[Data Cleaner](http://data-cleaner.readthedocs.io/)**.

### Normalizá y enriquecé tus datos

Para que tus datos se puedan cruzar fácilmente con otros es necesario que sigas estándares para llamar a las mismas cosas, de la misma manera.

Leé sobre cómo estandarizar tus datos en nuestra **[Guía para la identificación y uso de entidades interoperables](https://paquete-apertura-datos.readthedocs.io/es/stable/guia_interoperables.html)**.

Si tenés datos con provincias, departamentos, municipios, localidades, calles o coordenadas podés usar la **[API del Servicio de Normalización de Datos Geográficos](http://apis.datos.gob.ar/georef/)** para normalizar o enriquecer entidades geográficas de la Argentina.

## 3. Publicá datos como un servicio

Publicar datos como un servicio web es un paso más hacia facilitar y potenciar la reutilización de tus datos por parte de analistas, programadores y otros organismos.

Un servicio web es una URL configurable que te permite hacer consultas personalizadas a una base de datos, y actualizarlas fácilmente cuantas veces quieras.

Si ya tenés un servicio de datos, **leé nuestras recomendaciones para documentarlo y compartirlo**.

Si no tenés un servicio pero publicas series estadísticas, podés **sumarlas a la API de Series de Tiempo de la República Argentina**.

### Documentá y compartí tus servicios de datos

Si tenés un servicio de datos que querés compartir públicamente:

* Hace que sea más fácil de usar: documentá la interfaz y sus funcionalidades, escribí ejemplos de uso, sé lo más claro posible con los términos de uso. (Ej.: **[Series de Tiempo](http://apis.datos.gob.ar/series/)**, **[Servicio de Normalización de Datos Geográficos](http://apis.datos.gob.ar/georef/)**)

Te recomendamos revisar [Read the Docs](http://apis.datos.gob.ar/series/) y [OpenAPI](https://swagger.io/) como soporte para tu documentación, podés ver nuestro [ejemplo de Series de Tiempo](https://github.com/datosgobar/series-tiempo-ar-api) y nuestro [ejemplo del Servicio de Normalización de Datos Geográficos](https://github.com/datosgobar/georef-ar-api).

* Ayudá a que sea fácil de encontrar: sumá la URL de la documentación del servicio al catálogo de datos de tu organismo e [indicá que es una API en tus metadatos](https://paquete-apertura-datos.readthedocs.io/es/stable/guia_metadatos.html#distribucion-distribution).
* Cuidá tu infraestructura: publicá la base de datos completa en formatos abiertos junto con el servicio (Ej.: [dataset de Series de Tiempo](http://datos.gob.ar/dataset/modernizacion-base-series-tiempo-administracion-publica-nacional)).

### Sumá tus datos a la API de Series de Tiempo

Si publicás indicadores o estadísticas con evolución cronológica (como el [nivel de actividad](http://datos.gob.ar/series/api/series/?ids=143.3_NO_PR_2004_A_21)), podés sumarlos fácilmente a la **[API de Series de Tiempo de la República Argentina](http://apis.datos.gob.ar/series/)** y:

* Visualizarlas en el **[Explorador de Series de Tiempo](http://datos.gob.ar/series)** y compartir tus gráficos.
* [Integrar consultas a tus datos en planillas de cálculo](https://series-tiempo-ar-api.readthedocs.io/es/latest/spreadsheet_integration/).
* [Programar consultas a tus datos](https://series-tiempo-ar-api.readthedocs.io/es/latest/python_usage/) en distintos lenguajes.
* Armar tableros de seguimiento como [este ejemplo](https://datosgobar.github.io/series-tiempo-ar-landing/) usando [este proyecto](https://github.com/datosgobar/series-tiempo-ar-landing).

Para sumar tus series a la API:

* Publicá tus indicadores o estadísticas en archivos CSV, siguiendo [este formato estándar](https://paquete-apertura-datos.readthedocs.io/es/stable/guia_metadatos.html#distribucion-de-series-de-tiempo).
* [Documentá tus archivos CSV con series de tiempo](https://paquete-apertura-datos.readthedocs.io/es/stable/guia_metadatos.html#documentar-un-dataset-de-series-de-tiempo) en tu **catálogo de datos abiertos**.
* [Avisanos que tu catálogo tiene series de tiempo](mailto:datos@modernizacion.gob.ar), para que lo agreguemos a la API.

Si sos desarrollador, tenés tus series de tiempo en archivos Excel y es difícil convertirlos al formato estándar en CSV, podés usar el **[Scraper de Series de Tiempo](https://github.com/datosgobar/series-tiempo-ar-scraping)**.

Si querés explorar nuevas formas de usar la API de Series de Tiempo para automatizar reportes, análisis, visualizaciones o desarrollar aplicaciones web, mirá [este taller](https://github.com/datosgobar/taller-series-tiempo-mediaparty-2018).

## ¿Tenés dudas? Escribinos

Para comenzar te recomendamos leer nuestro [Kit de Datos Abiertos](https://www.argentina.gob.ar/sites/default/files/2._kit_de_datos_abiertos.pdf). También podés [contactarnos](mailto:datos@modernizacion.gob.ar).
