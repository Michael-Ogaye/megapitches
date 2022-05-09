from app import db,create_app
from flask_migrate import migrate
app=create_app('production')


db.create_all()