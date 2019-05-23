from flask import Flask, render_template, request, redirect, url_for, make_response
from smartninja_nosql.odm import Model

app = Flask(__name__)

class User(Model):
    def __init__(self, name, mail, **kwargs):
        self.name = name
        self.mail = mail

        super().__init__(**kwargs)


@app.route("/")
def index():
    email_address = request.cookies.get("user_mail")

    user = User.fetch_one(query=["mail", "==", email_address])

    return render_template("index.html", user=user)


@app.route("/login", methods=["POST"])
def login():
    user_name = request.form.get("user-name")
    user_mail = request.form.get("user-mail")

    user = User(name=user_name, mail=user_mail)
    user.create()

    response = make_response(redirect(url_for("index")))
    response.set_cookie("user_mail", user_mail)

    return response


if __name__ == "__main__":
    app.debug = True
    app.run()
