
# Repositorio para Práctica 1 de Tecnología y ciclo de vida del dato

## DESCRIPCIÓN

Repositorio correspondiente a la práctica 1 de la asignatura Tecnología y ciclo de vida del dato de la UOC (Universitat Oberta de Catalunya).
En la práctica ha participado David Arbona Navarro.
En ella se ha realizado scraping sobre la pagina web IMDB (https://www.imdb.com) obteniendo toda la información posible de las 250 mejores peliculas de todos los tiempos.

## FICHEROS DEL REPOSITORIO
 
 - /
   - README.md: este propio documento con información wiki.

 - csv/
   - dataset.csv: fichero csv con todos los datos obtenidos de las películas a través de scraping.
 
 - posters/
   - *.jpg: conjunto de imagenes obtenidas por scraping correspondientes a los posteres de las películas
 
 - pdf/
   - practica1.pdf: 
 
 - src/
   - main.py: fichero python principal de ejecución del proceso de scrapinig.
   - IMDBScraper.py: implementación de la clase IMDBScraper con los atributos y métodos para poder realizar el scraping a la web de IMDB

## NOTAS ADICIONALES

- Para la ejecución del código es necesario tener instaladas las siguientes librerías:

```python
pip3 install python-whois
pip install builtwith
pip3 install requests
pip3 install beautifulsoup4
```
- Mediante el siguiente comando podemos ejecutar el código:

```python
python foodPriceScraper.py 
```

- Una vez ejecutado se generará el fichero dataset.csv con los datos obtenidos en el directorio csv, así como todas las imagenes en el directorio posters.

- El dataset obtenido con la ejecución del código fuente referenciado anteriormente se puede encontrar en el DOI siguiente: 

https://doi.org/10.5281/zenodo.4671026


## RECURSOS UTILIZADOS

- Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
- Masip, D. (2010). El lenguaje Python. Editorial UOC.
- Github Guides: Mastering Markdown. https://guides.github.com/features/mastering-markdown/ (2014)
- Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
- 






