
# esercizio_2 classe Custumer
from class_movie import Movie
class Custumer:

    def __init__(self, custumer_id:str, name:str, rented_movies:list[Movie]) -> list:
        self.custumer_id = custumer_id
        self.name = name
        self.rented_movies = rented_movies(list[Movie]) 

    def rent_movie(self, movie:Movie):
        
        if movie not in self.rented_movies:

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