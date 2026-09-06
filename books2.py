from fastapi import FastAPI, Body

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, 'Computer Science', 'CodingWithBass', 'Description One', 5),
    Book(2, 'FastAPI', 'CodingWithBass', 'Description Two', 4),
    Book(3, 'Master Endpoints', 'CodingWithBass', 'Description Three', 3),
    Book(4, 'HP1', 'Author Four', 'Description Four', 2),
    Book(5, 'HP2', 'Author Five', 'Description Five', 1),
    Book(6, 'HP3', 'Author Six', 'Description Six', 5)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
    return book_request
