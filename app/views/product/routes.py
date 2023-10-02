from flask import Blueprint, render_template, jsonify, request
from app.config import Config
from os import path
from app.models import Toy, ToyCategory

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "product")
product_blueprint = Blueprint("product", __name__, template_folder=TEMPALTE_FOLDER)


@product_blueprint.route("/categories/<int:category_id>")
def category(category_id):
    categorie = ToyCategory.query.get(category_id)
    toys = Toy.query.filter_by(category_id=categorie.id)
    return render_template("bunnies.html", toys=toys, categorie=categorie)


@product_blueprint.route("/product/<int:id>")
def view_product(id):
    toy = Toy.query.filter_by(id=id).first()
    desc_geo = toy.desc_geo.replace("&nbsp;", " ")
    desc_eng = toy.desc_eng.replace("&nbsp;", " ")
    return render_template("product-page.html", toy=toy, desc_geo=desc_geo, desc_eng=desc_eng)


# items_info = [
#     {
#         "id": 1,
#         "stock": 2
#     },
#     {
#         "id": 2,
#         "stock": 4
#     },
#     {
#         "id": 3,
#         "stock": 1
#     }
# ]


# @product_blueprint.route("/cart", methods=['GET', 'POST'])
# def cart():
#     items_info = request.json
#     cart_items = []
#     for req in items_info:
#         toy = Toy.query.get(req["id"])
#         item = {
#             "id": toy.id,
#             "photo": toy.photo,
#             "name_geo": toy.name_geo,
#             "name_eng": toy.name_eng,
#             "desc_geo": toy.desc_geo,
#             "desc_eng": toy.desc_eng,
#             "price": toy.price,
#             "stock": req["stock"],
#             "is_popular": toy.is_popular,
#             "meta_geo": toy.meta_geo,
#             "meta_eng": toy.meta_eng,
#             "category_id": toy.category_id
#         }
#         cart_items.append(item)
#
#     return jsonify(cart_items), 200


@product_blueprint.route("/delete/<int:id>")
def delete_toy(id):
    items_info = request.json
    for item in items_info:
        if item["id"] == id:
            if item["stock"] == 1:
                items_info.remove(item)
            else:
                item["stock"] -= 1

    return jsonify(items_info), 200


@product_blueprint.route("/cart", methods=['GET', 'POST'])
def cart():
 return render_template("cart.html")