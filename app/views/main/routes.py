from flask import Blueprint, render_template, session, redirect, request, url_for
from app.config import Config
from os import path
from app.models import ToyCategory, Toy, User, Order
from app.views.main.forms import ProfielForm
from flask_login import current_user, login_required

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPALTE_FOLDER)


@main_blueprint.route("/")
def home():
    toys = Toy.query.filter_by(is_popular=True)[:7]
    categories = ToyCategory.query.all()
    return render_template("index.html", categories=categories, toys=toys)


@main_blueprint.route("/terms")
def terms():
    return render_template("terms.html")


@main_blueprint.route("/questions")
def questions():
    return render_template("questions.html")


@main_blueprint.route("/change_ln")
def change_language():
    if session['locale'] == 'EN':
        session['locale'] = 'KA'
    else:
        session['locale'] = 'EN'

    previous_url = request.referrer
    return redirect(previous_url)


@main_blueprint.route("/profile", methods=['POST', 'GET'])
@login_required
def profile():
    form = ProfielForm()
    user = User.query.get(current_user.id)
    if form.validate_on_submit():
        user.email = form.email.data
        user.phone = form.phone.data
        fullname = form.fullname.data
        user.first_name = fullname.split(' ')[0]
        user.last_name = fullname.split(' ')[1]

        user.save()

        return redirect(url_for('main.profile'))
    else:
        print(form.errors)
    orders = Order.query.filter_by(user_id=current_user.id)
    toy_ids = []
    for ord in orders:
        ids = ord.ordered_toys.split(',')
        for id in ids:
            toy_ids.append(int(id))
    toy_ids = set(toy_ids)
    toys = Toy.query.filter(Toy.id.in_(toy_ids)).all()
    return render_template("profile.html", form=form, orders=orders, toys=toys)


@main_blueprint.route("/payment-status/<status>")
def payment(status):
    return render_template("payment.html", status=status)