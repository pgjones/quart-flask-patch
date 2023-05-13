from flask_sqlalchemy import SQLAlchemy
from quart import Quart, ResponseReturnValue

app = Quart(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return "<User %r>" % self.username


@app.before_serving
async def startup() -> None:
    async with app.app_context():
        db.create_all()
        User.query.delete()
        guest = User("guest", "guest@example.com")
        db.session.add(guest)
        db.session.commit()


@app.route("/")
async def index() -> ResponseReturnValue:
    users = User.query.all()
    return users[0].username


async def test_flask_sqlalchemy() -> None:
    async with app.test_app():
        test_client = app.test_client()
        response = await test_client.get("/")
        assert (await response.get_data(as_text=True)) == "guest"
