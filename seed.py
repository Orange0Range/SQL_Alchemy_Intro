"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

# If table isn't empty, empty it
with app.app_context():
    User.query.delete()

# Add pets
tom = User(first_name='tom', last_name = 'tommy', image_url="google.com")
jon = User(first_name='jon', last_name = 'jonny', image_url="nfl.com")
bob = User(first_name='bob', last_name = 'bobby', image_url="nba.com")

# Add new objects to session, so they'll persist
with app.app_context():
    db.session.add(tom)
    db.session.add(jon)
    db.session.add(bob)

# Commit--otherwise, this never gets saved!
with app.app_context():    
    db.session.commit()