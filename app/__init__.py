from flask import Flask
from flask_migrate import Migrate

from .database import db
from .views import api

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI="mysql://root:flask-db@flask-backend-db:3306/flask_db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
migrate = Migrate(app, db)
app.register_blueprint(api)

# from .models import User

db.init_app(app)

app.run(debug=True, reloader=True)
