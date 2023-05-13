from flask_login import LoginManager
from quart import Quart, ResponseReturnValue

app = Quart(__name__)
login_manager = LoginManager(app)


@app.route("/")
async def index() -> ResponseReturnValue:
    return "Hello"


async def test_flask_login() -> None:
    test_client = app.test_client()

    response = await test_client.get("/")
    assert response.status_code == 200
