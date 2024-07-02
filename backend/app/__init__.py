from flask import Flask
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # 拡張の初期化
    db.init_app(app)
    migrate.init_app(app, db)

    # Flask-RESTfulのAPI初期化
    from app.resources import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
