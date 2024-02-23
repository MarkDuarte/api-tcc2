from flask import Flask, request, jsonify
from database import db
from config.config import Config
from config.login_manager import login_manager
from routes.app_routes_config import RouteConfig

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

with app.app_context():
  db.create_all()

router_config = RouteConfig(app)
router_config.configure_all_routes()

if __name__ == '__main__':
  app.run(debug=True, port=3333)