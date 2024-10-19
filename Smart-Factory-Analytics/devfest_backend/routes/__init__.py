from .userRoutes import user_bp

def initialize_routes(app):
    app.register_blueprint(user_bp,url_prefix='/api/user')