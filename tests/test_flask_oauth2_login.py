from flask_oauth2_login import GoogleLogin
from quart import Quart, ResponseReturnValue

app = Quart(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "super-secret"
app.config["GOOGLE_LOGIN_REDIRECT_SCHEME"] = "http"

google_login = GoogleLogin(app)


@app.route("/")
async def home() -> ResponseReturnValue:
    return google_login.authorization_url()


async def test_flask_oauth2_login() -> None:
    test_client = app.test_client()
    response = await test_client.get("/")
    assert response.status_code == 200
