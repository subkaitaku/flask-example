from flask import Blueprint, render_template

# from .models import User

api = Blueprint("route", __name__)


@api.get("/hello")
def hello():
    return render_template('index.html', txt='Hello World!')
