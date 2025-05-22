# esercizio2:Sistema di Gestione Catalogo Film 


class MovieCatalog:
    '''
    attribuiti della classe MovieCatalog 
    self.catalog:dict[str, list[str]]
    
    '''
    # inizializzare degli oggetti della classe MovieCatalog
    def __init__(self) -> None:

       self.setCatalog()
    
    # metodi getter


    #metodo che ritorna il valore dell' attribuito self.Catalog
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    
    # metodi setter


    # metodi che consente  di inizializzare l'attribuito self.catalog
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}
    # metodi per visualizzare i detagli di un catalogo
    def __str__(self) -> str:



        string:str = "Catalogo:"
        if self.catalog:
            for key, values in self.catalog.items():
               temp_string: str = "\n" + str(key) + ": " + str(values) 
               string = string + temp_string
        return string
    
        # retun str( self.catalog)


    # metodi della clase MovieCatalog
    # metodi che aggiunge una lista di film di uno specifico registra al catalogo
    def add_movies(self, director_name: str, movies: list[str]) ->None:
        # chek se il regista non è valida
        if not director_name:
            print(" il regista non è valido")
        # chek se la lista dei film non è valida
        elif not movies:
            print("Lalista dei film non può essere vuota")
        # se i dati sono validi
        else:
            # se il registro è presente nel catalogo
            if director_name in self.catalog:
                # aggiungi la lista movies al catalogo

                # per ogni film nela lista movies
                for movie in movies:
                    # controllare che se il film movies sia stato gia aggiunto al catalogo
                    # dizionario[key] -> valore
                    # director_name è la chiave del dizionario che rappresenta il nome di un registro
                    # a questa chiave corrispondone una lista di film, ovvero i film prodotti  dal registro in questione
                    # self.catalog[director_name] -> è il valore associato alla chiave director_name
                    # ovvero è la lista di tutti i film prodotti dal regista
                    if movie in self.catalog[director_name]:
                        print(f"il film{movie} è gia presente nel catalogo")

                    # se il film non è presente
                    else: 
                    # aggingi il film  al catalog
                        self.catalog[director_name].append(movie)
        
            # se il regista non è presente nel catalogo
                else:
                    # creare un nuovo record
                    self.catalog[director_name] = movies
            # metodo che rimuove un film dalla lista dei prodotti da un regista
    def remove_movie(self, director_name:str, movie:str) -> None:
        if not director_name:
            print("il regista non è valido")
            # check se la lista di film non è valida
        elif not movie:
            print("il film non è valido")
            # se i dati sono validi
        else:
             

            # se il regista è presente nel catalogo e in caso ,
            #  controllare se il film movie è nella lista dei film prodotti dal regista in questione
            if director_name in self.catalog and movie in self.catalog[director_name]:
                # rimuovere il film dalla lista
                self.catalog[director_name].remove(movie)
                # verificare se la lista dei film è vuota
            if not self.catalog[director_name]:
                

                # rimuovere il record
                del self.catalog[director_name]
        

        # metodo  che ritorna una lista contenenti i nomi di tutti i registri del catalogo

    def list_directors(self) -> list[str] |str:
        # se il dizionario self.catalog non è vuoto 
        if self.catalog:
            return list(self.catalog.keys())
        # altrimenti( se il dizionario è vuoto)
        else:
            return f"Non ci sono regista restituisce tutti i film da esso prodotti"
    def get_movies_bydirector(self, director_name) -> list[str]| str:
            # check se il regista no è  valido
        if not director_name:
            print("il regista non è valido")
             # se  valido
        else:

            # controllo se il regista è nel catalogo
         if director_name in self.catalog:
             return self.catalog[director_name]
         # se il regista non è nel catalogo
         else:
             return f" il regista{director_name} non è nel catalogo!"

            
       

                       

