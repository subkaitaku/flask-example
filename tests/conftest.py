import MySQLdb
import pytest

from app import app, db
from app.models import User


def get_conn():
    conn = MySQLdb.connect(
        user="root", passwd="flask-db", host="flask-backend-db", db="flask_db_test"
    )
    return conn


def insert_seed():
    user_test = User(nickname="test_user")
    db.session.add(user_test)


@pytest.fixture(scope="session", autouse=True)
def cursor():
    with get_conn() as conn:
        with conn.cursor() as cur:
            app.config["TESTING"] = True
            print("\n" + "START TEST")
            yield cur
            print("\n" + "END TEST")
        conn.rollback()


@pytest.fixture(scope="session", autouse=True)
def create_init():
    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_seed()
        db.session.commit()
