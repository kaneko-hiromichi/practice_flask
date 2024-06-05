import os
from app import app, db

print(f"Current working directory: {os.getcwd()}")
print(f"Database file should be created at: {app.config['SQLALCHEMY_DATABASE_URI']}")

with app.app_context():
    db.create_all()
    print("Database created successfully")
