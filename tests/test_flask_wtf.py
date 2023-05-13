from flask_wtf import FlaskForm
from quart import Quart, render_template_string, ResponseReturnValue
from wtforms import StringField
from wtforms.validators import DataRequired

app = Quart(__name__)
app.config["WTF_CSRF_ENABLED"] = False


class MyForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])


@app.route("/", methods=["GET", "POST"])
async def index() -> ResponseReturnValue:
    form = MyForm()
    if form.validate_on_submit():
        return form.name.data
    return await render_template_string("{{ form.name.label }}", form=form)


async def test_flask_wtf() -> None:
    test_client = app.test_client()
    response = await test_client.get("/")
    assert (await response.get_data(as_text=True)) == '<label for="name">name</label>'
    response = await test_client.post("/", form={"name": "bob"})
    assert (await response.get_data(as_text=True)) == "bob"
