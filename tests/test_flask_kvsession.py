from flask_kvsession import KVSessionExtension
from quart import Quart, request, ResponseReturnValue, session
from simplekv.memory import DictStore

store = DictStore()

app = Quart(__name__)
app.secret_key = "secret"
KVSessionExtension(store, app)


@app.route("/")
async def index() -> ResponseReturnValue:
    previous = session.get("method", "None")
    session["method"] = request.method
    return previous


async def test_flask_kvsession() -> None:
    test_client = app.test_client()
    response = await test_client.get("/")
    assert (await response.get_data(as_text=True)) == "None"
    response = await test_client.get("/")
    assert (await response.get_data(as_text=True)) == "GET"
