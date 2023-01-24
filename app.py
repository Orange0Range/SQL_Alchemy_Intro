"""Blogly application."""

from flask import Flask, session, request, render_template, jsonify, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """Display All Users"""
    users = User.query.all()
    return render_template('home.html', users = users)

@app.route('/users/new')
def create_user():
    """Display All Users"""
    return render_template('add_user.html')

@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show info on a single pet."""

    user_info = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user_info)

@app.route('/users/<int:user_id>/edit')
def edit_user_options(user_id):
    """Display All Users"""
    user_info = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user_info)

@app.route('/users/<int:user_id>/edit', methods = ['POST'])
def edit_user(user_id):
    """Display All Users"""
    user_info = User.query.get_or_404(user_id)
    user_info.first_name = request.form['First Name']
    user_info.last_name = request.form['Last Name']
    user_info.image_url = request.form['image URL']
    db.session.commit()
    return redirect('/')

@app.route("/user/new", methods=["POST"])
def add_user():
    """Add user and redirect to list."""
    first = request.form['First Name']
    last = request.form['Last Name']
    img = request.form['image URL']
    user = User(first_name=first, last_name=last, image_url=img)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """Delete user"""
    user_info = User.query.filter(User.id == user_id).delete()
    db.session.commit()
    return redirect('/')
