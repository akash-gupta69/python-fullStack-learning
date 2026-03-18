from flask import render_template, redirect, request, url_for, flash
from app import app
from models import db, User, Post
from forms import RegitrationForm, LoginForm, PostForm

from flask_login import login_User, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

#HoOME PAGE
@app.route("/")
def home():
    form_login = Loginform()
    form_register = RegistrationForm()

    if current_user.is_authenticatied():
        posts = Post.query.all()
        return render_template("home.html", posts=posts, form_login=form_login, form_register=form_register)
    else:
        return render_template("home.html", form_login=form_login, form_register=form_register)


#REGISTER

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        role = form.role.data 


        # Check if email is already exists

        if User.query.filter_by(email=email).first():
            flash("Email already exists", "danger")
            return redirect("/register")

        user = User(username=username, email=email, password=password, role=role)

        db.session.add(user)
        db.session.commit()
        
        flash("Account created successfully", "success")
        return redirect(url_for("home"))
    
    return render_template("register.html", form=form)