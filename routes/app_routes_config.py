from routes.auth_routes import AuthRoutes

class RouteConfig:
    def __init__(self, app):
        self.app = app

    def configure_all_routes(self):
        auth_routes = AuthRoutes()
        auth_routes.configure_auth_routes(self.app)
