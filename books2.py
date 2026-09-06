from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

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

class BookRequest(BaseModel):
    Id: Optional[int] = Field(description="Book ID is not needed on create", default=None)
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=200)
    rating: int = Field(ge=0, le=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New Book Title",
                "author": "New Book Author",
                "description": "New Book Description",
                "rating": 4
            }
        }
    }

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


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return new_book
