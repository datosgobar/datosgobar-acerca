<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
<link type="text/css" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css" media="all" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/datosgobar/series-tiempo-ar-explorer@ts_components_2.6.6/dist/css/components.css" type="text/css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
<script type='text/javascript' src='https://cdn.jsdelivr.net/gh/datosgobar/series-tiempo-ar-explorer@ts_components_2.6.6/dist/js/components.js'></script>

<style>
.row {
    display: flex;
    justify-content: space-around;
    margin: auto;
}

.center-block {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.full-width {
    width: 100%;
}

.exportable-graph {
    width: 100%;
}

.cardWrapper {
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 10px;
}
.card.full {
    -webkit-box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.5);
    background: #ffffff;
    border-radius: 4px;
    box-shadow: 0 2px 2px rgba(0,0,0,0.2);
}
</style>

# Monitoreo

## La Red de Nodos de Datos Abiertos

La política de apertura de datos de la Administración Pública Nacional se apoya en una red de organismos que publican sus catálogos de datos abiertos siguiendo un estándar internacional de metadatos que facilita su búsqueda y comprensión.

Este estándar estructura la documentación de activos de datos en datasets (conjuntos de datos estrechamente relacionados entre sí) y distribuciones (archivos descargables).

<div class="row panels-row">
    <div id="catalogos-red-card" class="col-xs-12 col-sm-4 col-md-4 cardWrapper"></div>
    <div id="datasets-red-card2" class="col-xs-12 col-sm-4 col-md-4 cardWrapper"></div>
    <div id="distribuciones-red-card" class="col-xs-12 col-sm-4 col-md-4 cardWrapper"></div>
</div>


## Federación selectiva

En el Portal Nacional de Datos Públicos (datos.gob.ar) se federan todos los datasets de la red que cumplen con un piso de calidad en términos de:

* **Metadatos**: deben pasar una validación automática y deben facilitar la búsqueda y comprensión del contexto de los datos publicados.
* **Relevancia**: deben ser de interés público.
* **Reusabilidad**: deben publicarse con un nivel de granularidad, actualización, formato, etc que garanticen posibilidades de reutilización razonables.

Los metadatos del total de los archivos publicados por la red de nodos se puede [descargar acá](https://infra.datos.gob.ar/catalog/modernizacion/dataset/8/distribution/8.3/download/distribuciones.csv).

<div class="row panels-row">
    <div class="col-xs-12 col-sm-12 col-md-6 center-block">
        <div class="row panels-row">
            <div id="datasets-red-card" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
            <div id="datasets-validos-red-card" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
        </div>
    </div>
    <div class="col-xs-12 col-sm-12 col-md-6 center-block">
        <div class="row panels-row">
            <div id="datasets-federados-card" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
            <div id="datasets-federados-pct-card" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
        </div>
    </div>
</div>
<div class="row panels-row">
    <div id="datasets-federados-graphic" style="margin-bottom: 40px;" class="col-xs-12 col-sm-12 col-md-6 full-width center-block"></div>
</div>

En todo momento buscamos facilitar la búsqueda y comprensión de datos similares. Cuando observás una caída en la cantidad de datasets de la red significa que hemos encontrado conjuntos de datos muy parecidos entre sí y pedimos a los organismos que los fusionen generando menos datasets.

Otras caídas temporales pueden deberse a que en determinado momento algún catálogo no estuvo accesible en línea y sus datasets no podían verse. Sin embargo, en datos.gob.ar la disponibilidad de los metadatos se mantiene, aunque los datos puedan estar inaccesibles momentáneamente mientras el organismo soluciona los inconvenientes.

## Indicadores de los nodos

## API Georef

El [Servicio de Normalización de Datos Geográficos de Argentina](http://apis.datos.gob.ar/georef) se usa como (1) **referencia** para consultar las listas canónicas de provincias, departamentos, localidades y otras entidades, (2) para **normalizar** sus nombres, (3) para **georreferenciar direcciones** en Argentina y para (4) **enriquecer puntos de coordenadas** con información de las unidades territoriales que los contienen.

<div class="row panels-row">
    <div class="col-xs-12 col-sm-12 col-md-6 center-block">
        <div class="row panels-row">
            <div id="georef-consultas-historicas" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
            <div id="georef-consultas-diarias-promedio" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
        </div>
    </div>
    <div class="col-xs-12 col-sm-12 col-md-6 center-block">
        <div class="row panels-row">
            <div id="georef-consultas-diarias-ayer" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
            <div id="georef-usuarios-unicos" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
        </div>
    </div>
</div>
<div class="row panels-row">
    <div id="georef-graphic" style="margin-bottom: 40px;" class="col-xs-12 col-sm-12 col-md-6 full-width center-block"></div>
</div>

## API Series de Tiempo

La [API de Series de Tiempo de la República Argentina](http://apis.datos.gob.ar/series) se usa para consultar indicadores de todos los organismos de la Administración Pública Nacional que los publiquen en formato de series de tiempo. Permite filtrar por tiempo, hacer agregaciones temporales, transformar unidades de medida y combinar series de distintas fuentes en una única consulta, entre otras funcionalidades.

<div class="row panels-row">
    <div class="col-xs-12 col-sm-12 col-md-6 center-block">
        <div class="row panels-row">
            <div id="series-consultas-historicas" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
            <div id="series-consultas-diarias-promedio" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
        </div>
    </div>
    <div class="col-xs-12 col-sm-12 col-md-6 center-block">
        <div class="row panels-row">
            <div id="series-consultas-diarias-ayer" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
            <div id="series-usuarios-unicos" class="col-xs-12 col-sm-6 col-md-6 cardWrapper"></div>
        </div>
    </div>
</div>
<div class="row panels-row">
    <div id="series-graphic" style="margin-bottom: 40px;" class="col-xs-12 col-sm-12 col-md-6 full-width center-block"></div>
</div>

<script>
    window.onload = function() {
        // COLORES SUGERIDOS "#0072BB","#2E7D33","#C62828","#F9A822","#6A1B99", "#EC407A","#C2185B","#6A1B99","#039BE5","#6EA100"

        // componentes de series de tiempo para cada sección

        // SECCION: Indice de Precios al Consumidor Nacional
        TSComponents.Card.render('datasets-red-card', {
            serieId: "ddaa_apn_002",
            color: '#0072BB',
            hasChart: 'none',
            title: "Datasets en toda la red",
            links: "none",
            units: "",
            source: "",
            hasFrame: false
        })

        TSComponents.Card.render('datasets-validos-red-card', {
            serieId: "ddaa_apn_006",
            color: '#2E7D33',
            hasChart: 'none',
            title: "Datasets metadatos válidos en toda la red",
            links: "none",
            units: "",
            source: "",
            hasFrame: false
        })

        TSComponents.Card.render('datasets-federados-card', {
            serieId: "ddaa_datosgobar_002",
            color: '#C62828',
            hasChart: 'none',
            title: "Datasets federados en datos.gob.ar",
            links: "none",
            units: "",
            source: "",
            hasFrame: false
        })

        TSComponents.Card.render('datasets-federados-pct-card', {
            serieId: 'ddaa_apn_005',
            color: '#EC407A',
            hasChart: 'none',
            title: "Datasets federados en datos.gob.ar (%)",
            links: "none",
            units: "",
            source: "",
            hasFrame: false
        })

        TSComponents.Graphic.render('datasets-federados-graphic', {
            graphicUrl: 'https://apis.datos.gob.ar/series/api/series/?ids=ddaa_apn_002,ddaa_apn_006,ddaa_datosgobar_002',
            chartTypes: {
                "ddaa_apn_002": "area",
                "ddaa_apn_006": "area",
                "ddaa_datosgobar_002": "area"
            }
        })

        TSComponents.Card.render('catalogos-red-card', {
            serieId: 'ddaa_apn_001',
            title: "Catálogos"
        })

        TSComponents.Card.render('datasets-red-card2', {
            serieId: 'ddaa_apn_002',
            title: "Datasets"
        })

        TSComponents.Card.render('distribuciones-red-card', {
            serieId: 'ddaa_apn_009',
            title: "Distribuciones"
        })

        // API georef
        TSComponents.Card.render('georef-consultas-historicas', {
            serieId: 'apis_georef_005',
            color: "#0072BB",
            source: "",
            units: "",
            links: "none",
            title: "Consultas históricas"
        })

        TSComponents.Card.render('georef-consultas-diarias-promedio', {
            serieId: 'ddaa_apn_009',
            color: "#2E7D33",
            source: "",
            units: "",
            links: "none",
            title: "Consultas diarias (promedio último mes)",
            collapse: "month"
        })

        TSComponents.Card.render('georef-consultas-diarias-ayer', {
            serieId: 'ddaa_apn_009',
            color: "#C62828",
            source: "",
            units: "",
            links: "none",
            title: "Consultas diarias (último día)"
        })

        TSComponents.Card.render('georef-usuarios-unicos', {
            serieId: 'apis_georef_004',
            color: "#F9A822",
            source: "",
            units: "",
            links: "none",
            title: "Usuarios únicos diarios (promedio último mes)",
            collapse: "month"
        })

        TSComponents.Graphic.render('georef-graphic', {
            graphicUrl: 'https://apis.datos.gob.ar/series/api/series/?ids=apis_georef_001,apis_georef_002,apis_georef_003',
            title: "Consultas diarias realizadas"
        })

        // API series
        TSComponents.Card.render('series-consultas-historicas', {
            serieId: 'apis_series_005',
            color: "#0072BB",
            source: "",
            units: "",
            links: "none",
            title: "Consultas históricas"
        })

        TSComponents.Card.render('series-consultas-diarias-promedio', {
            serieId: 'ddaa_apn_009',
            color: "#2E7D33",
            source: "",
            units: "",
            links: "none",
            title: "Consultas diarias (promedio último mes)",
            collapse: "month"
        })

        TSComponents.Card.render('series-consultas-diarias-ayer', {
            serieId: 'ddaa_apn_009',
            color: "#C62828",
            source: "",
            units: "",
            links: "none",
            title: "Consultas diarias (último día)"
        })

        TSComponents.Card.render('series-usuarios-unicos', {
            serieId: 'apis_series_004',
            color: "#F9A822",
            source: "",
            units: "",
            links: "none",
            title: "Usuarios únicos diarios (promedio último mes)",
            collapse: "month"
        })

        TSComponents.Graphic.render('series-graphic', {
            graphicUrl: 'https://apis.datos.gob.ar/series/api/series/?ids=apis_series_001,apis_series_002,apis_series_003',
            title: "Consultas diarias realizadas"
        })


    }
</script>