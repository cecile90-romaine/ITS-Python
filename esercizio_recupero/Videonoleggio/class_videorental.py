# esrcizio_3:
from class_movie import Movie
from class_customer import Customer
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

           if customer not in self.customers.rented_movies:
               
               customer.rented_movies = movie
            else:
                print(f"il film {movie.title} è gia stato noleggiato")
        
        else:
            print(f"il cliente o film non trovato")

# corezione
class VideoRentalStore:


    def __init__(self, customers: dict[str, Customer] = {}, movies: dict[str, Movie] = {}):

    
       self.movies: dict[str, Movie] = movies if movies is not None else {}
       self.customers: dict[str, Customer] = customers if customers is not None else {}



    def add_movie(self, movie_id:str, title:str, director: str) -> None:
        if movie_id in self.movies:
            print("il film è gia presente nel catalogo")
        else:
            movie:Movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie


    def register_customer(self, customer_id:str, name:str) -> None:
        if customer_id in self.customers:
            print("il cliente è già registrato")
        else:
            customer:Customer= Customer(customer_id, name)
            self.customers[customer_id] = customer

    def rent_movie(self, customer_id:str, movie_id:str) -> None:
        if customer_id not in self.customers or movie_id not in self.movies:
             print("il cliente o film non presenti nel sistema")
        else:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)


    def return_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id not in self.customers or movie_id not in self.movies:
             print("il cliente o film non presenti nel sistema")
        else:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)
        

    def get_rented_movies(self, customer_id:str)-> list[Movie]:
        if customer_id not in self.customers:
            print("il cliente non è nel sistems!")
        else:
            return self.customers[customer_id].rented_movies
        

        


