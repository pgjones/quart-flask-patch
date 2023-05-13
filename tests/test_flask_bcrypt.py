from flask_bcrypt import Bcrypt
from quart import Quart

app = Quart(__name__)
bcrypt = Bcrypt(app)


def test_bcrypt() -> None:
    pw_hash = bcrypt.generate_password_hash("hunter2")
    assert bcrypt.check_password_hash(pw_hash, "hunter2")
