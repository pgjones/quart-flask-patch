from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from quart import Quart, render_template_string, ResponseReturnValue

app = Quart(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])


@app.route("/slow")
@limiter.limit("1 per day")
async def slow() -> ResponseReturnValue:
    return await render_template_string("Slow")


@app.route("/fast")
async def fast() -> ResponseReturnValue:
    return await render_template_string("Fast")


async def test_flask_limiter() -> None:
    test_client = app.test_client()
    await test_client.get("/slow")
    response = await test_client.get("/slow")
    assert response.status_code == 429
    await test_client.get("/fast")
    response = await test_client.get("/fast")
    assert (await response.get_data(as_text=True)) == "Fast"
