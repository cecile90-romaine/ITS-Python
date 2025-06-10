# esrcizio_3:
from class_movie import Movie
from class_customer import Custumer
class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie], customers:dict[str, Custumer]):
        self.movies = movies
        self.customers = customers


    def add_movie(self, movie_id: str, title: str, director: str) -> dict:
        self.movie_id = movie_id
        self.title = title
        self.director = director

        if movie_id in self.movies:

            print(f"il film  con ID {movie_id} esiste già")
    
        else: 
            
            self.movies[movie_id] = (movie_id, title, director)

    def register_customer(self, customer_id: str, name: str):

        if customer_id in self.customers:

            print(f"il cliente con ID {customer_id} è gia registrato")
        
        else:
            self.customers[customer_id] = customer_id, name



    def rent_movie(self, customer_id: str, movie_id: str):
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)

        if movie and movie:

           if customer not in self.customer.rented_movies:
               
               customer.rented_movies = movie
            else:
                print(f"il film {movie.title} è gia stato noleggiato")
        
        else:
            print(f"il cliente o film non trovato")

    
