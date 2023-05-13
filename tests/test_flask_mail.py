from flask_mail import Mail
from quart import Quart, ResponseReturnValue

app = Quart(__name__)
app.testing = True
mail = Mail(app)


@app.route("/")
async def index() -> ResponseReturnValue:
    mail.send_message(
        subject="testing",
        body="test",
        recipients=["test@localhost"],
        sender="send@localhost",
    )
    return ""


async def test_flask_mail() -> None:
    test_client = app.test_client()
    with mail.record_messages() as outbox:
        await test_client.get("/")
        assert len(outbox) == 1
        assert outbox[0].subject == "testing"
