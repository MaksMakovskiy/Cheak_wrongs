from flask import Flask, render_template, request, jsonify
import json
from crud import CrudUser


app = Flask(__name__)

user = CrudUser("data.json")

@app.route("/")
def get_all_user():
	return jsonify(user.get_all_user())

@app.route("/register")
def create_new_user() -> "html":
	new_user: dict(str, Any) = request.json
	print(new_user)
	user.add_new_user(new_user["login"], {"password": new_user["password"]})
	user.write_to_file()
	return render_template("replander.html")
	

if __name__ == "__main__":
    app.run(debug=True)
