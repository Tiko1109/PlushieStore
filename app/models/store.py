from app.models import BaseModel
from app.extensions import db


class City(db.Model, BaseModel):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name_geo = db.Column(db.String, nullable=False)
    name_eng = db.Column(db.String, nullable=False)
    delivery_cost = db.Column(db.Float, nullable=False)
    delivery_delay = db.Column(db.Integer, nullable=False)


class Toy(db.Model, BaseModel):
    __tablename__ = "toys"

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String, nullable=False)
    name_geo = db.Column(db.String, nullable=False)
    name_eng = db.Column(db.String, nullable=False)
    desc_eng = db.Column(db.Text, nullable=False)
    desc_geo = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    is_popular = db.Column(db.Boolean, nullable=False)
    meta_geo = db.Column(db.String, nullable=False)
    meta_eng = db.Column(db.String, nullable=False)
    category_id = db.Column(db.ForeignKey("toy_categories.id"))
    category = db.relationship("ToyCategory", uselist=False)


class ToyCategory(db.Model, BaseModel):
    __tablename__ = "toy_categories"

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String, nullable=False)
    name_geo = db.Column(db.String, nullable=False)
    name_eng = db.Column(db.String, nullable=False)
    description_geo = db.Column(db.String, nullable=False)
    description_eng = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name_geo


class Order(db.Model, BaseModel):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String, nullable=False)
    ordered_toys = db.Column(db.String, nullable=False)
    order_price = db.Column(db.Float, nullable=False)
    customer_info = db.Column(db.String, nullable=False)
    customer_phone = db.Column(db.String, nullable=False)
    customer_address = db.Column(db.String, nullable=False)
    customer_note = db.Column(db.String, nullable=False)
    order_status = db.Column(db.String, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False)
    admin_note = db.Column(db.String)
    user_id = db.Column(db.ForeignKey("users.id", name="fk_order_user"))
    user = db.relationship("User", uselist=False)

