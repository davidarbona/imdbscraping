# import whois
# print(whois.whois('https://www.imdb.com'))

import requests
import re
import csv
from bs4 import BeautifulSoup


def in_method(given, sub):
    return sub in given


class IMDBScraper():

    def __init__(self, url, ruta_posters, nombre_archivo, url_principal):
        self.csvfile = open('./csv/' + nombre_archivo, 'w+')
        self.url = url
        self.url_principal = url_principal
        self.datos = []
        self.ruta_posters = ruta_posters

    def realizar_scraper_info_film(self, href, name, actual_dato):
        print('realizar_scraper_info_film')
        pageFilm = requests.get(self.url_principal + href)
        soupFilm = BeautifulSoup(pageFilm.content, features="html.parser")

        originalTitle = soupFilm.find('div', {'class': 'originalTitle'})

        if originalTitle is None:
            originaltitletext = name
            otrosDatos = soupFilm.find('div', {'class': 'subtext'})
        else:
            originaltitletext: str = originalTitle.text
            otrosDatos = originalTitle.next_sibling.next_sibling

        # print(originaltitletext)
        actual_dato.append(originaltitletext)

        duracion = otrosDatos.find('time').text.strip()

        # print(duracion)
        actual_dato.append(duracion)

        fecha = otrosDatos.find('a', {'href': href + 'releaseinfo'}).text.strip()

        # print(fecha)
        actual_dato.append(fecha)

        v_as = otrosDatos.find_all('a', href=True)
        len_a_s = len(v_as)

        i = 1
        generos = ''
        for v_a in v_as:
            if i < len_a_s:
                # generos.append(v_a.text.strip())
                if i == 1:
                    generos = v_a.text.strip()
                else:
                    generos = generos + ',' + v_a.text.strip()
                # print(v_a.text.strip())
            i = i + 1

        # print(generos)
        actual_dato.append(generos)

        div_poster = soupFilm.find('div', {'class': 'poster'})
        poster_url = div_poster.find('img')['src'].strip()
        # print('imagen grande: ' + poster_url)
        actual_dato.append(poster_url)

        a_split = poster_url.split('.')

        extension = a_split[len(a_split) - 1]

        ruta = self.ruta_posters + name + '.' + extension

        self.guardar_imagen(poster_url, ruta)

        actual_dato.append(ruta)

        texto_resumen = soupFilm.find('div', {'class': 'summary_text'}).text.strip()
        # print('resumen: ' + texto_resumen)
        actual_dato.append(texto_resumen.replace('\n', ' '))

        creditos = soupFilm.find_all('div', {'class': 'credit_summary_item'})

        directores = ''
        escritores = ''
        actores = ''

        for credito in creditos:
            i = 1
            if in_method(credito.find('h4').text, 'Director'):
                for director in credito.find_all('a'):
                    if i == 1:
                        directores = director.text
                    else:
                        directores = directores + ', ' + director.text
                    i = i + 1

            i = 1
            if in_method(credito.find('h4').text, 'Writers'):
                for v_escritor in credito.find_all('a'):
                    if i == 1:
                        escritores = v_escritor.text
                    else:
                        escritores = escritores + ', ' + v_escritor.text
                    i = i + 1

            i = 1
            if in_method(credito.find('h4').text, 'Stars'):
                for actor in credito.find_all('a'):
                    if actor.text != 'See full cast & crew':
                        if i == 1:
                            actores = actor.text
                        else:
                            actores = actores + ', ' + actor.text
                        i = i + 1

        # print(directores)
        # print(escritores)
        # print(actores)
        actual_dato.append(directores)
        actual_dato.append(escritores)
        actual_dato.append(actores)

    def realizar_scraper(self):

        print('REALIZANDO SCRAPING DEL LISTADO DE LAS MEJORES 250 PELICULAS')

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, features="html.parser")
        # ruta = '/Users/davidarb/PycharmProjects/imdbscrapping'

        tds = soup.find_all('td', {'class': 'posterColumn'})
        for td in tds:
            actual_dato = []
            ranking = td.find('span', {'name': 'rk'})
            # print(ranking['data-value'])

            rating_imdb = td.find('span', {'name': 'ir'})
            # print(rating_imdb['data-value'])

            # rating_US = td.find('span', {'name': 'us'})
            # print(rating_US['data-value'])

            img = td.find('img')
            name = img['alt']
            print('Name: ' + name)

            actual_dato.append(name)
            actual_dato.append(ranking['data-value'])
            actual_dato.append(rating_imdb['data-value'])

            title_column = td.next_sibling.next_sibling
            director_actores = title_column.find('a')['title']
            # print('director_actores: ' + director_actores)

            ano = title_column.find('span').text.replace('(', '').replace(')', '')
            # print('ano: ' + ano)
            actual_dato.append(ano)

            imagen = td.find('img')['src']
            # print('imagen: ' + imagen)
            actual_dato.append(imagen)

            href = td.find('a')['href']
            # print('href: ' + href)

            self.realizar_scraper_info_film(href, name, actual_dato)

            self.datos.append(actual_dato)

            print('***SIGUIENTE PELICULA')

        print('FINAL SCRAPING')

    def guardar_imagen(self, poster_url, ruta):

        output = open(ruta, "wb")
        r = requests.get(poster_url, stream=True)
        for chunk in r:
            output.write(chunk)
        output.close()

        print('POSTER ALMACENADO CORRECTAMENTE')

    def inicializar_excel2(self):
        self.csvfile.write('Nombre;')
        self.csvfile.write('Ranking;')
        self.csvfile.write('Puntuacion IMDB;')
        self.csvfile.write('Ano;')
        self.csvfile.write('URL Imagen;')
        self.csvfile.write('Título Original;')
        self.csvfile.write('Duración;')
        self.csvfile.write('Fecha Estreno (Pais);')
        self.csvfile.write('Generos;')
        self.csvfile.write('URL Poster;')
        self.csvfile.write('Nombre imagen;')
        self.csvfile.write('Resumen;')
        self.csvfile.write('Director;')
        self.csvfile.write('Escritores;')
        self.csvfile.write('Actores;')
        self.csvfile.write("\n")

    def grabacion_excel(self):

        self.inicializar_excel2()

        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                #print(self.datos[i][j])
                self.csvfile.write((self.datos[i][j] + ';'))
            self.csvfile.write('\n')

        self.csvfile.close()

        print('FICHERO CSV GENERADO CORRECTAMENTE')
