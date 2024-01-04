from flask import Flask, request
from atom import Atom
from atom import views

app = Flask(__name__)

@app.route("/login")
@Atom.apply(view=views.signed_in)
def login():
    print(request.user.id)
    return "Logged in"

app.run()