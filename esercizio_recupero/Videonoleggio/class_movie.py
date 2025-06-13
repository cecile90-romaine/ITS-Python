# esrcizio_2 

"Progettare un sistema di videonoleggio  con i seguenti requisiti:"


# 1. class Movie: rapresenta i film da noleggiare

class Movie:

    def __unit__(self, movie_id:str, title:str, director:str, is_rented: bool) -> str:
        
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    

    def rent(self):
                              # se posibible noleggia il film
        if not self.is_rented:

            self.is_rented = True

            print(f"Il film {self.title} è stato noleggiato")

        else:
            print(f"il film {self.title} è gia noleggiato")

    def return_movie(self):

        if self.is_rented:

            self.is_rented = False
            print(f"il flim {self.title} è gia noleggioto")
        
        else:
            print(f"il film {self.title} non è stao noleggiato da questo cliente")


# corezione

class Movie:

    def __unit__(self, movie_id:str, title:str, director:str,) -> str:
        
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented: bool = False

    def rent(self) -> None:
        





        






        