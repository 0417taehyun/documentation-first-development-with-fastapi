from dataclasses import asdict

from flask import Blueprint, jsonify

from src.schema import Book


router = Blueprint(name="books", import_name=__name__)


@router.route(rule="/books", methods=["GET"])
def get_books():
    """
    Get Books

    Description
        1. Get all books.

    To-do
        1. Serach by name with query parameter. 
    ---
    tags:
      - Book
    
    definitions:
        Book:
            type: object
            properties:
                name:
                    type: str

    responses:
      200:
        description: Successful Response
        schema:
            $ref: "#/definitions/Book"
        examples:
          application/json:
            [
                {"name": "Demian"}
            ]
    """
    return jsonify([
        asdict(obj=Book(name="Demian")),
        asdict(obj=Book(name="Siddhartha"))
    ])
