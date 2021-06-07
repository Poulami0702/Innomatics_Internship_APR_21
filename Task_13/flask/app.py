import pip

package_names=['flask-session'] #packages to install
pip.main(['install'] + package_names + ['--upgrade']) 

from flask import Flask, render_template, redirect, request, session

from flask_session import Session
import secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = secret_key
Session(app)
  
notes=[]

@app.route("/", methods=["GET","POST"])
def index():
    if not session.get("name"):
        return redirect("/login")

    if request.form.get("note"):
        note = request.form.get("note")
        notes.append(note)
    return render_template('home.html', notes=notes)
  
  
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")
  
  
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
  
  
if __name__ == "__main__":
    app.run(debug=True)