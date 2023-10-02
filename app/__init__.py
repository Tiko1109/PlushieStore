from flask import Flask, session
from app.config import Config
from app.extensions import db, login_manager, migrate, ckeditor, babel
from app.commands import init_db, populate_db
from app.views import main_blueprint, product_blueprint, auth_blueprint, error_blueprint
from app.admin import admin, SecureModelView, UserView, CityView, OrderView, ToyView, ToyCategoryView
from app.models import User, Order, Toy, ToyCategory, City
from flask_admin.menu import MenuLink

BLUEPRINTS = [main_blueprint, auth_blueprint, product_blueprint, error_blueprint]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(OrderView(Order, db.session, name="შეკვეთები"))
    admin.add_view(UserView(User, db.session, name="მომხმარებლები"))
    admin.add_view(ToyView(Toy, db.session, name="სათამაშოები"))
    admin.add_view(ToyCategoryView(ToyCategory, db.session, name="კატეგორიები"))
    admin.add_view(CityView(City, db.session, name="ქალაქები"))

    admin.add_link(MenuLink("გასვლა", url="/"))

    # Flask-CKEditor
    ckeditor.init_app(app)

    # Flask-Babel
    def get_locale():
        if 'locale' not in session.keys():
            session['locale'] = 'EN'
        return session['locale']

    babel.init_app(app, locale_selector=get_locale)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
