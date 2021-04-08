from IMDBScraper import IMDBScraper

nombre_archivo = 'dataset.csv'
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
url_principal = 'https://www.imdb.com/'
ruta_posters = './posters/'

IMDBScraper = IMDBScraper(url, ruta_posters, nombre_archivo, url_principal)

IMDBScraper.realizar_scraper()
IMDBScraper.grabacion_excel()



