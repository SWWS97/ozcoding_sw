# Model == Table 생성
# 게시글 - board
# 유저 - user

from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')
    # 여기서 db.relationship은 데이터베이스에서 Column으로 인식이 되는게 아니라 나중에 ORM방식으로 데이터를 불러올때 활용한다.
    # 그렇기에 데이터베이스 안에선 보이지가 않는다.
                                        
class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship('User', back_populates='boards')