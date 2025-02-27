from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User

user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix='/user')

# API LIST:
# (1) 전체 유저 데이터 조회 (GET)
# (2) 유저 생성 (POST)

@user_blp.route('/')
class UserList(MethodView):
    # (1) 전체 유저 데이터 조회 (GET)
    def get(self):
        users = User.query.all()

        # for user in users:
        #     print(user.id)
        #     print(user.name)
        #     print(user.email)

        user_data = [
            {'id':user.id, 'name':user.name, 'email':user.email} for user in users
        ]

        return jsonify(user_data)

    # (2) 유저 생성 (POST)
    def post(self):
        data = request.json
        new_user = User(name=data['name'], email=data['email'])
        print(new_user)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"mag":"success create user"}), 201


# (1) 특정 유저 데이터 조회 (GET)
# (2) 특정 유저 데이터 업데이트 (PUT)
# (3) 특정 유저 삭제 (DELETE)

@user_blp.route("/<int:user_id>")
class UserResource(MethodView):
    # (1) 특정 유저 데이터 조회 (GET)
    def get(self,user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({'name':user.name, 'email':user.email})

    # (2) 특정 유저 데이터 업데이트 (PUT)
    def put(self,user_id):
        user = User.query.get_or_404(user_id)
        data = request.json

        user.name = data["name"]
        user.email = data['email']

        db.session.commit()

        return jsonify({"msg":"Successfully updated user data"}), 201

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({"msg":"Successfully deleted user data"})
