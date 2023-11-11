import folium as fm
import networkx as nx
import osmnx as ox
from geopy.distance import geodesic
from tqdm import tqdm

place = "г Смоленск, Смоленская область, Россия"  # город для которого нужен граф
G = ox.graph_from_place(
    place, network_type="walk"
)  # загрузка графа по адрессу места (в нашем случае город)


def build_geocode(
    name1=None, name2=None
):  # функция для перевода адрессов в геокод (lat, lon)
    assert name1 is not None, "1st name is None"
    assert name2 is not None, "2nd name is None"

    place1 = ox.geocode(
        name1
    )  # метод перевода из коробки для карт OSM(Open Street Map)
    place2 = ox.geocode(
        name2
    )  # метод перевода из коробки для карт OSM(Open Street Map)

    return place1, place2


def build_path(
    graph=None, point1=(), point2=(), mode="time"
):  # функция для отрисовки карты
    assert graph is not None, "Your graph is NoneType object"
    assert len(point1) == 2, "1st point hasn`t 2 coordinates"
    assert len(point2) == 2, "2nd point hasn`t 2 coordinates"

    start_node = ox.nearest_nodes(
        graph, point1[1], point1[0]
    )  # для полученных координат находится ближайшая нода
    finish_node = ox.nearest_nodes(
        graph, point2[1], point2[0]
    )  # для полученных координат находится ближайшая нода

    route = nx.shortest_path(
        graph, start_node, finish_node, weight=mode
    )  # строится короткий путь по Алгоритму Дейкстры по атрибуту mode(параметр функции)

    shortest_route_map = ox.plot_route_folium(graph, route)  # отрисовка карты

    fm.TileLayer("openstreetmap").add_to(shortest_route_map)  # добавление стиля

    # маркеры начала и конца пути
    start_marker = fm.Marker(
        location=point1, popup="Начало маршрута", icon=fm.Icon(color="green")
    )

    finish_marker = fm.Marker(
        location=point2, popup="Конец маршрута", icon=fm.Icon(color="red")
    )

    # добавление их на карту
    start_marker.add_to(shortest_route_map)
    finish_marker.add_to(shortest_route_map)

    # цикл на добавление синих маркеров с центрами достопримечательностей(чтобы понять как идёт путь)
    # for i in range(gdf.shape[0]):
    #     if i == 100:
    #         break
    #     marker = fm.Marker(
    #         location=(Y[i], X[i]), popup=gdf.name[i], icon=fm.Icon(color="blue")
    #     )
    #     marker.add_to(shortest_route_map)

    return shortest_route_map


start_name = """
36, улица Октябрьской Революции, Ленинский район, городской округ Смоленск, 
Смоленская область, Центральный федеральный округ, 210000, Россия
"""
# start_name = '''
# переулок Ульянова 1, город Смоленск, Россия
# '''
# start_name = '''
# проспект Гагарина, 1, город Смоленск, Россия
# '''

finish_name = """
Гимназия им. Пржевальского, улица Ленина, Ленинский район, городской округ Смоленск, 
Смоленская область, Центральный федеральный округ, 210000, Россия
"""
# finish_name =  '''
# Смоленский филиал МЭИ, город Смоленск, Россия
# '''
# finish_name =  '''
# улица Соболева, 1
# '''

points = build_geocode(start_name, finish_name)
m = build_path(G, points[0], points[1], "length")
# m.save('map.html')

from string import Template

html_string = """\
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="keywords" content="">
            <meta name="description" content="">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
            <meta name="robots" content="index, follow">
            <link rel="shortcut icon" type="image/png" href="favicon.png">
            
            <link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css?6554">
            <link rel="stylesheet" type="text/css" href="style.css?8690">
            <link rel="stylesheet" type="text/css" href="./css/all.min.css">
            <link href='https://fonts.googleapis.com/css?family=Old+Standard+TT&display=swap&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
            <link href='https://fonts.googleapis.com/css?family=PT+Serif+Caption&display=swap&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
            <title>Home-1</title>


            
        <!-- Analytics -->
        
        <!-- Analytics END -->
            
        </head>
        <body>

        <!-- Preloader -->
        <div id="page-loading-blocs-notifaction" class="page-preloader"></div>
        <!-- Preloader END -->

        <!-- Main container -->
        <div class="page-container">
            
        <header>

        <!-- hero -->
        <div class="bloc bloc-fill-screen b-parallax d-bloc bloc-bg-texture texture-darken " id="hero">
            <div class="parallax bg-photo-2023-11-10-2023-46-07 bgc-7376">
            </div>
            <div class="bloc-bg-mask">
                <svg class="svg-mask hero-fill-mask" viewBox="0 0 500 500" preserveAspectRatio="xMidYMid slice"><path d="m0 0h500v500h-500z"></path></svg>
            </div>
            <div class="container fill-bloc-top-edge">
                    <div class="row">
                        <div class="col-12">
                            <nav class="navbar row navbar-expand-md navbar-dark" role="navigation">
                                <a class="navbar-brand ltc-6728 logo-style" style="width: 70%;" href="index.html">SMOLSTEPS</a>
                                <button id="nav-toggle" type="button" class="ui-navbar-toggler navbar-toggler border-0 p-0 mr-md-0 ml-auto" data-toggle="collapse" data-target=".navbar-44256" aria-expanded="false" aria-label="Toggle navigation">
                                    <span class="navbar-toggler-icon"><svg height="32" viewBox="0 0 32 32" width="32"><path class="svg-menu-icon " d="m2 9h28m-28 7h28m-28 7h28"></path></svg></span>
                                </button>
                                <div class="collapse navbar-collapse navbar-44256">
                                        <ul class="site-navigation nav navbar-nav ml-auto">
                                            <li class="nav-item">
                                                <a href="index.html" class="nav-link a-btn ltc-6728">Главная</a>
                                            </li>
                                            <li class="nav-item">
                                                <a href="route.html" class="nav-link a-btn ltc-6728">Маршруты</a>
                                            </li>
                                            <li class="nav-item">
                                                <a href="news.html" class="nav-link a-btn ltc-6728">Новости</a>
                                            </li>
                                            <li class="nav-item">
                                                <a href="news.html" class="nav-link a-btn ltc-6728">Отзывы</a>
                                            </li>
                                            <li class="nav-item">
                                                <a href="contact.html" class="nav-link a-btn ltc-6728">Контакты</a>
                                            </li>
                                        </ul>
                                    </div>
                            </nav>
                            <div class="row">
                                    <div class="col-lg-5">
                                        <h3 class="mb-4">
                                            <span class="fa fa-star"></span>Тип маршрута
                                        </h3>
                                        <div class="form-check">
                                            <input class="form-check-input" type="radio" name="radioSetOne" value="option1">
                                            <label class="form-check-label">
                                                Прямой
                                            </label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="radio" name="radioSetOne" value="option1">
                                            <label class="form-check-label">
                                                Круговой
                                            </label>
                                        </div>
                                        <div class="form-group">
                                            <label>
                                                Откуда
                                            </label>
                                            <input class="form-control">
                                            <div class="divider-h">
                                            </div>
                                            <input class="form-control" id="input_1720">
                                            <div class="divider-h">
                                            </div>
                                            <div class="blockquote">
                                                <p>
                                                    Продолжительность пути:
                                                </p>
                                                <div class="form-group">
                                                    <select class="form-control">
                                                        <option value="0">
                                                            Option 1
                                                        </option>
                                                        <option value="1">
                                                            Option 2
                                                        </option>
                                                    </select>
                                                    <div class="divider-h">
                                                    </div>
                                                    <div class="text-center">
                                                        <a href="index.html" class="btn btn-d btn-lg btn-style">Отметить область поиска</a>
                                                        <h3 class="mb-4">
                                                            <span class="fa fa-star"></span>Какие достопримечательности Вас интересуют?
                                                        </h3>
                                                        <div class="form-check">
                                                            <input class="form-check-input" type="checkbox">
                                                            <label class="form-check-label">
                                                                Интересное место
                                                            </label>
                                                        </div>
                                                        <div class="form-check">
                                                            <input class="form-check-input" type="checkbox">
                                                            <label class="form-check-label">
                                                                Исторические объекты
                                                            </label>
                                                        </div>
                                                        <div class="form-check">
                                                            <input class="form-check-input" type="checkbox">
                                                            <label class="form-check-label">
                                                                Религиозные объекты
                                                            </label>
                                                        </div>
                                                        <div class="form-check">
                                                            <input class="form-check-input" type="checkbox">
                                                            <label class="form-check-label">
                                                                Культурный объект
                                                            </label>
                                                        </div><a href="index.html" class="btn btn-d btn-lg btn-button-style">Построить маршрут</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col offset-lg--1">
                                    {table}
                                    </div>
                                </div>
                        </div>
                    </div>
                </div>
            <div class="container">
                        <div class="row">
                            <div class="col-12">
                            </div>
                        </div>
                    </div>
        </div>
        <!-- hero END -->
        </header>
        <!-- ScrollToTop Button -->
        <button aria-label="Scroll to top button" class="bloc-button btn btn-d scrollToTop" onclick="scrollToTarget('1',this)"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 32 32"><path class="scroll-to-top-btn-icon" d="M30,22.656l-14-13-14,13"/></svg></button>
        <!-- ScrollToTop Button END-->


        <footer>

        <!-- footer -->
        <div class="bloc bgc-7376 d-bloc" id="footer">
            <div class="container bloc-lg-lg bloc-md bloc-lg-md">
                <div class="row">
                    <div class="col-md-3 offset-md-0 offset-lg-0 col-lg-3 offset-sm-0 col-sm-3 text-lg-left">
                        <a href="index.html" class="a-btn a-block footer-link ltc-6728">Главная</a>
                    </div>
                    <div class="col-md-3 offset-md-0 offset-lg-0 col-lg-3 offset-sm-0 col-sm-3">
                        <a href="report.html" class="a-btn a-block footer-link ltc-6728">Маршруты</a>
                    </div>
                    <div class="col-md-3 text-lg-left offset-md-0 offset-lg-0 col-lg-3 offset-sm-0 col-sm-3">
                        <a href="route.html" class="a-btn a-block footer-link ltc-6728">Отзывы</a>
                    </div>
                    <div class="col-md-3 text-lg-center offset-md-0 offset-lg-0 col-lg-3 offset-sm-0 col-sm-3">
                        <a href="contact.html" class="a-btn a-block footer-link ltc-6728">Контакты</a>
                    </div>
                    <div class="align-self-end text-center col-sm-12 text-lg-center">
                        <div><div class="social-link-bric">
        <a href="https://twitter.com/blocsapp" class="twitter-link" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="rgba(255,255,255,0.50)" viewBox="0 0 24 24" style="margin-left: 17px; margin-right: 17px;"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path></svg></a>

        <a href="https://www.facebook.com/cazoobi" class="facebook-link" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="rgba(255,255,255,0.50)" viewBox="0 0 24 24" style="margin-left: 17px; margin-right: 17px;"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path></svg></a>

        <a href="https://www.instagram.com/cazoobi" class="instagram-link" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="rgba(255,255,255,0.50)" viewBox="0 0 24 24" style="margin-left: 17px; margin-right: 17px;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"></path></svg></a>

        </div>
                        </div>
                        <div class="divider-h mx-auto footer-divider">
                            </div>
                    </div>
                    <div class="col-md-12 col-sm-12 text-lg-center col-lg-12">
                            <p class="mx-auto d-block text-center">
                                © Copyright 2023 | Blocs Theme | All Rights Reserved
                            </p>
                        </div>
                </div>
            </div>
        </div>
        <!-- footer END -->

        </footer>
        </div>
        <!-- Main container END -->
            


        <!-- Additional JS -->
        <script src="./js/jquery.min.js?5088"></script>
        <script src="./js/bootstrap.bundle.min.js?9871"></script>
        <script src="./js/blocs.min.js?6119"></script>
        <script src="./js/lazysizes.min.js" defer></script>
        <script src="./js/universal-parallax.min.js?1456"></script><!-- Additional JS END -->
        </body>
        </html>
        """

import datetime

now = datetime.datetime.now()
now = now.strftime("%d-%m-%Y %H:%M")

html_string_time = Template(html_string).safe_substitute(code=now)

with open("map.html", "w", encoding="utf-8") as f:
    # f.write(html_string.format(table=df.to_html(classes='styled-table')))
    table = m.get_root().render()
    # table = m.get_root().script.render()
    # header = m.get_root().header.render()
    # body_html = m.get_root().html.render()
    print(type(table))
    # table_formatted = table.replace("<tr>", '<tr align="center">')
    f.write(html_string_time.format(table=table))
