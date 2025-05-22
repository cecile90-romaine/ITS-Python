# dal modulo esercizio_film.py importare la classe MovieCatalog
from esercizio_film import MovieCatalog
# inizializzare un catalogo, ovvero un oggetto della classe MovieCatalog
catalog: MovieCatalog = MovieCatalog()

# print(catalogo)
catalog.add_movies(" Steven Spielberg",["casper", " Ritorno al futuro"])
print(catalog)
catalog.add_movies("Steven Spielberg", ["ET"])
catalog.add_movies("Quentin Tarantino",["Pulp Fiction", "Kill Bill"])
catalog.remove_movie("Quentin Tarantino","Kill Bill")
catalog.remove_movie("Quentin Tarantino", "Pulp Fiction")
print(catalog)
print(catalog.list_directors())
print(catalog.get_movies_by_director("Tim Burton"))
print(catalog.get_movies_by_director("Steven Spielbert"))