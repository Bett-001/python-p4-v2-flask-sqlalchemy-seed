#!/usr/bin/env python3
#server/seed.py

#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet

with app.app_context():

    # Delete all existing rows to avoid duplicates
    Pet.query.delete()

    # List of pets to insert
    pets = [
        Pet(name="Fido", species="Dog"),
        Pet(name="Whiskers", species="Cat"),
        Pet(name="Hermie", species="Hamster"),
        Pet(name="Slither", species="Snake"),
        Pet(name="Bella", species="Dog"),
        Pet(name="Luna", species="Cat"),
        Pet(name="Charlie", species="Hamster"),
        Pet(name="Max", species="Dog"),
        Pet(name="Coco", species="Turtle"),
        Pet(name="Milo", species="Cat"),
    ]

    # Add pets to the session
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()

    print("Seeded 10 pets successfully!")
