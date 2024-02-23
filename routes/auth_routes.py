from flask import request, jsonify
from models.User import User

class AuthRoutes:
    def configure_auth_routes(self, app):
        @app.route('/login', methods=["POST"])
        def login():
            data = request.json
            username = data.get("username")
            password = data.get("password")

            if username and password:
                user = User.query.filter_by(username=username).first()

                if user and user.password == password:
                      return jsonify({"message": "Authenticated with success"})

            return jsonify({"message": "Username or Password invalid"}), 400
