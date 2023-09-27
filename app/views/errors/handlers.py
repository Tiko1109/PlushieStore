from flask import Blueprint, render_template
from app.config import Config
from os import path

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "errors")
error_blueprint = Blueprint("error", __name__, template_folder=TEMPALTE_FOLDER)


@error_blueprint.app_errorhandler(404)
def error_404(error):
    return render_template('error.html'), 404