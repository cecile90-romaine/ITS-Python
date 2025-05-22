class Book:
    def __init__(self, title:str, author:str, isbn:str):
        self._title = title
        self._author = author
        self._isbn = isbn
        
    def __str__(self) -> str:
        return f'title={self._title}; Author={self._author}; ISBN={self._isbn}'
    
    @classmethod
    def from_string(cls, str_repr: str):
        words: list[str] = str_repr.split(',')
        return Book(words[0], words[1], words[2])
    if __name__ == '__main__':
        book_str: str = "La Divina Comedia,D. Alighieri,999000666"
        b = Book.from_string(book_str)
        print(b)