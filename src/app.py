from flask import Flask,render_template,redirect,url_for,request
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,login_required
# importaciones de los .py
from config import config
from forms import registerForm,loginform,contactsForm
from entities.ModelUser import ModelUser

app = Flask(__name__)

db = MySQL(app)

login_manager_app = LoginManager()

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route("/")
def inicio():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = loginform()
    if request.method == "GET":
        return render_template("login.html", form=form)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        logged_user = ModelUser.login(db,email,password)
        if logged_user:
            login_user(logged_user)
            if logged_user.password:
                return redirect(url_for("contacts"))
        else:
            return render_template("login.html", form=form)
        
@app.route("/register", methods=["GET","POST"])
def register():
    form = registerForm()

    if request.method == "GET":
        return render_template("register.html", form=form)
    
    if request.method == "POST":
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        password = request.form.get("password")
        
        ModelUser.register(db,fullname,email,password)

        logged_user = ModelUser.login(db,email,password)

        if logged_user:
            return redirect(url_for("contacts"))
        else:
            return render_template("register.html", form=form)


@app.route("/contacts", methods=["GET", "POST"])
@login_required
def contacts():
    form = contactsForm()
    if request.method == "GET":
        return render_template("contacts.html", form=form)
    if request.method == "POST":
        pass

@app.route("/addcontacts", methods=["GET","POST"])
@login_required
def addcontacts():
    if request.method == "GET":
        return render_template("")
    if request.method == "POST":
        pass

@app.route("/logout")
def logout():
    logout()
    return redirect(url_for("inicio"))


def status_401(error):
    return redirect(url_for("inicio"))

def status_404(error):
    return "<h1>😿Pagina no encontrada 😿 <h1>"


if __name__ == "__main__":
    app.config.from_object(config["dev"])
    app.register_error_handler(401,status_404)
    app.register_error_handler(404,status_404)
    app.run()