#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Templates de secciones de Andino para generar html"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os


# se usa para generar el html que va al container de Andino
SECTION_TEMPLATE = """
{{% extends "gobar_page.html" %}} {{% block page %}}

<div class="container-fluid" id="template-config-container">
    <div class="restricted-max-width ">
        <div id="template-config" class="col-xs-12 col-md-10 col-md-offset-1 about-template-container" style="padding: 0 60px;">

            <br/>
            <div id="pkg-path">
                <a href="/">Datos Argentina</a> / {section_name}
            </div>

{document}

        </div>
    </div>
</div>

{{% endblock %}}
"""

# se usa para previsualizar cómo queda la sección con los estilos
# de Andino, desde Github Pages
PREVIEW_TEMPLATE = """
<!DOCTYPE html >
<!-- saved from url = (0059)http: // stg.datos.gob.ar / acerca / seccion / Public % C3 % A1 % 20datos - ->
<html lang = "es" class = " js" > <!-- <![endif] - -> < head > <meta http - equiv = "Content-Type" content = "text/html; charset=UTF-8" >
    <!--[if lte ie 8] > <script type = "text/javascript" src = "/fanstatic/vendor/:version:2018-08-16T11:43:08/html5.min.js" > < / script > <![endif] - ->
<link rel = "stylesheet" type = "text/css" href = "./assets/select2.css" >
<link rel = "stylesheet" type = "text/css" href = "./assets/main.min.css" >
<link rel = "stylesheet" type = "text/css" href = "./assets/font-awesome.min.css" >
<link rel = "stylesheet" type = "text/css" href = "./assets/harvest.css" >
<link rel = "stylesheet" type = "text/css" href = "./assets/gobar_style.css" >

      <meta name = "generator" content = "ckan 2.7.4" >
      <meta name = "viewport" content = "width=device-width, initial-scale=1.0" >

    <meta property="og:url" content="http://stg.datos.gob.ar/">
    <meta property="og:type" content="article">
    <meta property="og:title" content="Datos Argentina">
    <meta property="og:site_name" content="Datos Argentina">
    <meta property="og:description" content="Ponemos a tu alcance datos públicos en formatos abiertos para que puedas usarlos, modificarlos y compartirlos.">
    <meta property="og:image" content="http://stg.datos.gob.ar/user_images/FB-datos.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="2400">
    <meta property="og:image:height" content="1260">
    <meta property="og:locale" content="es_AR">

    <meta name="twitter:card" content="summary">
    <meta name="twitter:site:id" content="@datosgobar">
    <meta name="twitter:image:src" content="http://stg.datos.gob.ar/user_images/TW-datos.png">
    <meta name="twitter:title" content="Datos Argentina">
    <meta name="twitter:description" content="Ponemos a tu alcance datos públicos en formatos abiertos para que puedas usarlos, modificarlos y compartirlos.">
    <title>
    Datos Argentina - Publicá datos</title>


    <link rel="shortcut icon" href="http://stg.datos.gob.ar/favicon.ico">

        <script async="" src="./assets/analytics.js"></script><script async="" src="./assets/analytics.js"></script><script type="text/javascript">
  (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
  (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  }})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-101681828-1', 'auto', {{}});

  ga('set', 'anonymizeIp', true);
  ga('send', 'pageview');
</script>












  </head>


  <body data-site-root="http://stg.datos.gob.ar/" data-locale-root="http://stg.datos.gob.ar/" data-feedly-extension-exttag="3.0.3" style="">


    <style type="text/css">
        div.background-overlay{{background-color:rgba(0,0,0,0)!important;}}
    </style>

    <div class="footer-down">

<div id="header" class="container-fluid">
    <div class="restricted-max-width">
        <div id="header-spacing" class="col-xs-12 col-sm-10 col-sm-offset-1">



            <div class="col-xs-12 col-sm-5 no-padding logo-header">
                <div class="logo-and-xs-icon">
                    <i class="icon-reorder fa fa-bars" aria-hidden="true"></i>
                    <a href="http://stg.datos.gob.ar/">

                        <img src="./assets/OutlookEmoji-1504621565312_PastedImage.png" class="logo-ministerio">
                    </a>

                        <a class="edit-description-link" href="http://stg.datos.gob.ar/configurar/encabezado">
                            <svg fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg" class="edit-svg">
    <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"></path>
</svg>
                        </a>

                </div>
                <div class="xs-navbar hidden">
                    <div class="navbar-link">
                        <a href="http://stg.datos.gob.ar/dataset">
                            DATASETS
                        </a>
                    </div>
                    <hr>

                        <div class="navbar-link">
                            <a href="http://stg.datos.gob.ar/series/api">
                                SERIES
                            </a>
                        </div>


                        <div class="navbar-link">
                            <a href="http://stg.datos.gob.ar/organizaciones">
                                ORGANIZACIONES
                            </a>
                        </div>



                        <div class="navbar-link">
                            <a href="http://stg.datos.gob.ar/apis">
                                APIs
                            </a>
                        </div>





                            <div class="navbar-link dropdown-navbar-link">
                                ACERCA
                            </div>
                            <div class="about-dropdown dropdown-navbar hidden">



                                        <div class="navbar-link">
                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Nuestro%20Portal">
                                                Nuestro Portal
                                            </a>
                                        </div>

                                        <div class="navbar-link">
                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Marco%20Legal">
                                                Marco Legal
                                            </a>
                                        </div>

                                        <div class="navbar-link">
                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Glosario">
                                                Glosario
                                            </a>
                                        </div>

                                        <div class="navbar-link">
                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Nuestro%20Equipo">
                                                Nuestro Equipo
                                            </a>
                                        </div>

                                        <div class="navbar-link">
                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Public%C3%A1%20datos">
                                                Publicá datos
                                            </a>
                                        </div>



                            </div>


                        <hr><div class="navbar-link dropdown-navbar-link">
                        <span class="username">admin</span> <svg class="user-logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128.46 128.46"><path d="M128.46,64.23A63.15,63.15,0,0,0,119.84,32,64.21,64.21,0,0,0,96.48,8.62,63.12,63.12,0,0,0,64.23,0,63.12,63.12,0,0,0,32,8.62,64.2,64.2,0,0,0,8.62,32,63.15,63.15,0,0,0,0,64.23,63.15,63.15,0,0,0,8.62,96.48a64.76,64.76,0,0,0,9.82,12.86l-.16.27a70.09,70.09,0,0,0,9.2,7.34c1.46,1,3,2,4.51,2.91a63.17,63.17,0,0,0,32.25,8.62,63.17,63.17,0,0,0,32.25-8.62,66.19,66.19,0,0,0,7-4.74,72.41,72.41,0,0,0,6.61-5.51l-.14-.23a64.76,64.76,0,0,0,9.85-12.89A63.15,63.15,0,0,0,128.46,64.23Zm-20.52,41.89C101.56,96.56,88,81,66.73,79.8a26.25,26.25,0,0,0,16.88-7.9,26.44,26.44,0,0,0,8-19.41,26.44,26.44,0,0,0-8-19.4,26.42,26.42,0,0,0-19.4-8,26.41,26.41,0,0,0-19.4,8,26.44,26.44,0,0,0-8,19.4,26.44,26.44,0,0,0,8,19.41,26.25,26.25,0,0,0,16.87,7.9C40.48,81,26.88,96.52,20.49,106.09a61.14,61.14,0,0,1-8.66-11.48A59.48,59.48,0,0,1,3.71,64.23a59.48,59.48,0,0,1,8.11-30.37,60.53,60.53,0,0,1,22-22A59.45,59.45,0,0,1,64.23,3.71,59.46,59.46,0,0,1,94.6,11.83a60.54,60.54,0,0,1,22,22,59.48,59.48,0,0,1,8.11,30.37,59.48,59.48,0,0,1-8.11,30.37A61.14,61.14,0,0,1,107.94,106.12Z" style="fill:#0695d6"></path></svg>
                    </div>
                    <div class="dropdown-navbar hidden">
                        <div class="navbar-link">
                            <a href="http://stg.datos.gob.ar/configurar/mi_cuenta">
                                MI CUENTA
                            </a>
                        </div><div class="navbar-link">
                                <a href="http://stg.datos.gob.ar/configurar/titulo">
                                    CONFIGURACIÓN
                                </a>
                            </div><div class="navbar-link">
                            <a href="http://portal-andino.readthedocs.io/es/latest/quickstart/" target="_blank">
                                AYUDA
                            </a>
                        </div>

                        <div class="navbar-link">
                            <a href="http://stg.datos.gob.ar/logout">
                                SALIR
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-xs-12 col-sm-7 no-padding header-links"><a class="header-link" href="http://stg.datos.gob.ar/dataset">Datasets</a><a class="header-link" href="http://stg.datos.gob.ar/series/api">Series</a><a class="header-link" href="http://stg.datos.gob.ar/organizaciones">Organizaciones</a><a class="header-link" href="http://stg.datos.gob.ar/apis">
                            APIs
                        </a>



                            <span class="header-link dropdown">
                                Acerca <span class="caret"></span>
                                <ul class="about-dropdown" style="bottom: -200px;">



                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Nuestro%20Portal">
                                                <li>Nuestro Portal</li>
                                            </a>

                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Marco%20Legal">
                                                <li>Marco Legal</li>
                                            </a>

                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Glosario">
                                                <li>Glosario</li>
                                            </a>

                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Nuestro%20Equipo">
                                                <li>Nuestro Equipo</li>
                                            </a>

                                            <a href="http://stg.datos.gob.ar/acerca/seccion/Public%C3%A1%20datos">
                                                <li>Publicá datos</li>
                                            </a>



                                </ul>
                            </span>
                        <span class="header-link dropdown"><span class="user-divisor"></span>
                            <span>admin</span> <svg class="user-logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128.46 128.46"><path d="M128.46,64.23A63.15,63.15,0,0,0,119.84,32,64.21,64.21,0,0,0,96.48,8.62,63.12,63.12,0,0,0,64.23,0,63.12,63.12,0,0,0,32,8.62,64.2,64.2,0,0,0,8.62,32,63.15,63.15,0,0,0,0,64.23,63.15,63.15,0,0,0,8.62,96.48a64.76,64.76,0,0,0,9.82,12.86l-.16.27a70.09,70.09,0,0,0,9.2,7.34c1.46,1,3,2,4.51,2.91a63.17,63.17,0,0,0,32.25,8.62,63.17,63.17,0,0,0,32.25-8.62,66.19,66.19,0,0,0,7-4.74,72.41,72.41,0,0,0,6.61-5.51l-.14-.23a64.76,64.76,0,0,0,9.85-12.89A63.15,63.15,0,0,0,128.46,64.23Zm-20.52,41.89C101.56,96.56,88,81,66.73,79.8a26.25,26.25,0,0,0,16.88-7.9,26.44,26.44,0,0,0,8-19.41,26.44,26.44,0,0,0-8-19.4,26.42,26.42,0,0,0-19.4-8,26.41,26.41,0,0,0-19.4,8,26.44,26.44,0,0,0-8,19.4,26.44,26.44,0,0,0,8,19.41,26.25,26.25,0,0,0,16.87,7.9C40.48,81,26.88,96.52,20.49,106.09a61.14,61.14,0,0,1-8.66-11.48A59.48,59.48,0,0,1,3.71,64.23a59.48,59.48,0,0,1,8.11-30.37,60.53,60.53,0,0,1,22-22A59.45,59.45,0,0,1,64.23,3.71,59.46,59.46,0,0,1,94.6,11.83a60.54,60.54,0,0,1,22,22,59.48,59.48,0,0,1,8.11,30.37,59.48,59.48,0,0,1-8.11,30.37A61.14,61.14,0,0,1,107.94,106.12Z" style="fill:#0695d6"></path></svg>

                            <ul>
                                <a href="http://stg.datos.gob.ar/configurar/mi_cuenta">
                                    <li>Mi Cuenta</li>
                                </a><a href="http://stg.datos.gob.ar/configurar/titulo">
                                        <li>Configuración</li>
                                    </a><a href="http://portal-andino.readthedocs.io/es/latest/quickstart/" target="_blank">
                                    <li>Ayuda</li>
                                </a>

                                <a href="http://stg.datos.gob.ar/logout">
                                    <li>Salir</li>
                                </a>
                            </ul>
                        </span></div>
        </div>
    </div>
</div>



<!--[if IE 7]> <html lang="es" class="ie ie7"> <![endif]-->
<!--[if IE 8]> <html lang="es" class="ie ie8"> <![endif]-->
<!--[if IE 9]> <html lang="es" class="ie9"> <![endif]-->
<!--[if gt IE 8]><!-->  <!--<![endif]-->


      <meta name="generator" content="ckan 2.7.4">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta property="og:url" content="http://stg.datos.gob.ar/">
    <meta property="og:type" content="article">
    <meta property="og:title" content="Datos Argentina">
    <meta property="og:site_name" content="Datos Argentina">
    <meta property="og:description" content="Ponemos a tu alcance datos públicos en formatos abiertos para que puedas usarlos, modificarlos y compartirlos.">
    <meta property="og:image" content="http://stg.datos.gob.ar/user_images/FB-datos.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="2400">
    <meta property="og:image:height" content="1260">
    <meta property="og:locale" content="es_AR">

    <meta name="twitter:card" content="summary">
    <meta name="twitter:site:id" content="@datosgobar">
    <meta name="twitter:image:src" content="http://stg.datos.gob.ar/user_images/TW-datos.png">
    <meta name="twitter:title" content="Datos Argentina">
    <meta name="twitter:description" content="Ponemos a tu alcance datos públicos en formatos abiertos para que puedas usarlos, modificarlos y compartirlos.">
    <title>
    Datos Argentina</title>


    <link rel="shortcut icon" href="http://stg.datos.gob.ar/favicon.ico">

        <script type="text/javascript">
  (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
  (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  }})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-101681828-1', 'auto', {{}});

  ga('set', 'anonymizeIp', true);
  ga('send', 'pageview');
</script>


<div class="container-fluid" id="template-config-container">
    <div class="restricted-max-width ">
        <div id="template-config" class="col-xs-12 col-md-10 col-md-offset-1 about-template-container" style="padding: 0 60px;">

            <br/>
            <div id="pkg-path">
                <a href="/">Datos Argentina</a> / {section_name}
            </div>

        {document}

        </div>
    </div>
</div>


    <div class="js-hide" data-module="google-analytics" data-module-googleanalytics_resource_prefix="">
    </div>

  <script>document.getElementsByTagName('html')[0].className += ' js';</script>
<script type="text/javascript" src="./assets/jquery.min.js"></script>
<script type="text/javascript" src="./assets/select2.min.js"></script>
<script type="text/javascript" src="./assets/image-upload.min.js"></script>
<script type="text/javascript" src="./assets/googleanalytics_event_tracking.js"></script>
<script type="text/javascript" src="./assets/custom_popup.js"></script>


            <div id="footer" class="container-fluid">
    <div class="restricted-max-width">
        <div id="footer-spacer" class="col-xs-10 col-xs-offset-1">
            <div class="footer-section logo col-xs-12 col-sm-6 col-md-6">
                <p>



                        <a href="https://twitter.com/datosgobar" target="_blank" class="social-link">
                            <i class="fa fa-twitter" aria-hidden="true"></i>
                        </a>





                        <a href="https://www.facebook.com/GobAbiertoAR/" target="_blank" class="social-link">
                            <i class="fa fa-facebook" aria-hidden="true"></i>
                        </a>





                        <a href="https://github.com/datosgobar" target="_blank" class="social-link">
                            <i class="fa fa-github-alt" aria-hidden="true"></i>
                        </a>











                        <a class="edit-social-link" href="http://stg.datos.gob.ar/configurar/redes">
                            <svg fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg" class="edit-svg">
    <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"></path>
</svg>
                        </a>

                </p>
                <div class="logo-edit-container">


                    <a href="https://www.argentina.gob.ar/modernizacion" target="_blank">
                        <img src="./assets/LogoMMOD.png" class="logo-ministerio">
                    </a>

                        <a class="edit-logo-link" href="http://stg.datos.gob.ar/configurar/pie-de-pagina">
                            <svg fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg" class="edit-svg">
    <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"></path>
</svg>
                        </a>

                </div>
            </div>
            <div class="footer-section links-internos hidden-xs hidden-sm col-md-3">


                    <p><a href="http://stg.datos.gob.ar/acerca/seccion/Nuestro%20Portal">Nuestro Portal</a></p>

                    <p><a href="http://stg.datos.gob.ar/acerca/seccion/Marco%20Legal">Marco Legal</a></p>

                    <p><a href="http://stg.datos.gob.ar/acerca/seccion/Glosario">Glosario</a></p>

                    <p><a href="http://stg.datos.gob.ar/acerca/seccion/Nuestro%20Equipo">Nuestro Equipo</a></p>

                    <p><a href="http://stg.datos.gob.ar/acerca/seccion/Public%C3%A1%20datos">Publicá datos</a></p>

            </div>
            <div class="footer-section links-externos col-xs-12 col-sm-6 col-md-3">


                    <p><a href="mailto:datos@modernizacion.gob.ar">Contactanos</a></p>

                <p class="ckan-link">
                    Desarrollado por<br><a href="https://github.com/datosgobar/distribuible.datos.gob.ar" target="_blank">Andino</a> con <a href="http://ckan.org/" target="_blank"><span class="ckan-name">CKAN</span></a>
                </p>
                <p class="ckan-link">
                    Versión: 2.5.1
                </p>
            </div>
        </div>
    </div>
</div>
        </div>

    <div class="js-hide" data-module="google-analytics" data-module-googleanalytics_resource_prefix="">
    </div>

</body></html>
"""
