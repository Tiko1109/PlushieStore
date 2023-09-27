from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, IntegerField, SubmitField


class ProfielForm(FlaskForm):
    email = EmailField("ელფოსტა")
    phone = IntegerField("ტელეფონის ნომერი")
    fullname = StringField("სახელი და გვარი")

    submit = SubmitField("შენახვა")

