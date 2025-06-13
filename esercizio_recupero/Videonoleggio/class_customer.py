
# esercizio_2 classe Custumer
from class_movie import Movie
class Custumer:

    def __init__(self, custumer_id:str, name:str, rented_movies:list[Movie]) -> list:
        self.custumer_id = custumer_id
        self.name = name
        self.rented_movies = rented_movies(list[Movie]) 

    def rent_movie(self, movie:Movie):
        
        if movie not in self.rented_movies: # verifica se il film è disponibile o no

            print(f"il fiml {movie.title}è già noleggiato")
        
        else:
            self.rented_movies = (movie)

    def return_movie(self, movie: Movie):

        if movie in self.rented_movies:

            self.rented_movies = (movie)
        
        else:
            print(f"il film {movie.title} non è stato noleggiato")
        

    movie_id= Movie()


    movie_id.rent()          
    movie_id.return_movie()  


# corezione:

class Customer:
    def __init__(self, customer_id:str, name:str):
        self.customer_id:str = customer_id   # identifica il cliente
        self.name:str = name                 # mi da il nome del cliente
        self.rented_movies: list[Movie] = []  # mi da la lista dei film noleggiati


    def rent_movie( self, movie: Movie) -> None:

        if movie.is_rented:      # cui verifichiamo se il film è gia stato noleggiato

           print("il film e gia stato affitato")
        else:
            movie.rent()
            self.rented_movies.append(movie) 



    def return_movie(self,movie: Movie) -> None:
        if movie not in self.rented_movies:
            print(" l' utente non ha affitato il film")
        else:
            movie.return_movie()
            self.rented_movies.remove(movie)