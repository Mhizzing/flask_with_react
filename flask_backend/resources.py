from flask_backend import db, ma, api
from flask_restful import Api, Resource
from flask import request
from .models import *


# Marshmallow Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class SessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Session

user_schema = UserSchema()
users_schema = UserSchema(many=True)
session_schema = SessionSchema()
sessions_schema = SessionSchema(many=True)

# API Resources
class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        new_user = User(name=request.json['name'])
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)

class SessionListResource(Resource):
    def get(self):
        sessions = Session.query.all()
        return sessions_schema.dump(sessions)

    def post(self):
        new_session = Session(date=request.json['date'])
        db.session.add(new_session)
        db.session.commit()
        return session_schema.dump(new_session)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class SessionResource(Resource):
    def get(self, session_id):
        session = Session.query.get_or_404(session_id)
        return session_schema.dump(session)

    def delete(self, session_id):
        session = Session.query.get_or_404(session_id)
        db.session.delete(session)
        db.session.commit()
        return '', 204

api.add_resource(UserListResource, '/users/')
api.add_resource(SessionListResource, '/sessions/')
api.add_resource(UserResource, '/users/<int:user_id>/')
api.add_resource(SessionResource, '/sessions/<int:session_id>/')