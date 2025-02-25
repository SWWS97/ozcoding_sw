from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []

# 엔드포인트 구현...
# 전체 데이터 보여주기 
@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200, BookSchema(many=True))
    def get(self):
        return books
    
    # arguments() 옵션을 사용해 스키마 검증을 하는 과정을 거친다. 
    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) + 1  # len()함수로 books의 길이 값에 +1 한 값을 id에 담아줌
        books.append(new_data)  # 유저가 보내온 데이터를 리스트(books = [])에 추가를 한다.
        return new_data         # 추가된 새로운 데이터를 리턴한다.
    

@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        return book
    

    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema, description="Book updated")
    def put(self, new_data, book_id):
        # 특정 ID를 가진 책을 업데이트하는 PUT 요청 처리
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        book.update(new_data)
        return book
    
    @book_blp.response(204, description="Book deleted")
    def delete(self, book_id):
        # 특정 ID를 가진 책을 삭제하는 DELETE 요청 처리
        global books
        if not any(book for book in books if book["id"] == book_id):
            abort(404, message="Book not found")
        books = [book for book in books if book["id"] != book_id]
        return ''
