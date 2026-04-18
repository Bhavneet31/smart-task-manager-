from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .config import Config
from flask_cors import CORS

# Initialize extensions (not bound to app yet)
db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()
limiter = Limiter(key_func=get_remote_address)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Bind extensions to app
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    limiter.init_app(app)

    # Register route blueprints
    from .routes.auth_routes import auth_bp
    from .routes.task_routes import task_bp
    from .routes.analytics_routes import analytics_bp
    from .routes.log_routes import log_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")
    app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
    app.register_blueprint(log_bp, url_prefix="/api/logs")

    # Global error handlers
    @app.errorhandler(404)
    def not_found(e):
        return {"error": "Resource not found"}, 404

    @app.errorhandler(429)
    def ratelimit_error(e):
        return {"error": "Too many requests. Slow down!"}, 429

    @app.errorhandler(500)
    def server_error(e):
        return {"error": "Internal server error"}, 500

    # Create all tables on startup
    with app.app_context():
        db.create_all()

    return app