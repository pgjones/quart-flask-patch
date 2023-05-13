from flask_caching import Cache
from quart import Quart, render_template_string, ResponseReturnValue

app = Quart(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})


@cache.cached(timeout=50)
@app.route("/")
async def index() -> ResponseReturnValue:
    return await render_template_string("Hello")


async def test_flask_caching() -> None:
    test_client = app.test_client()
    response = await test_client.get("/")
    assert (await response.get_data(as_text=True)) == "Hello"
