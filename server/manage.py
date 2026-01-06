from flask.cli import FlaskGroup
from app import app, db
from models import Pet
from flask_migrate import Migrate

# Initialize Migrate
migrate = Migrate(app, db)

# Create CLI group
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
