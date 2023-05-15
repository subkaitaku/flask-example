import json

from app import app


def test_passing():
    client = app.test_client()
    client.get("/")
    res = json.loads(client.get("api/hello").data)
    expected = {"user": "test_user"}
    assert res == expected
