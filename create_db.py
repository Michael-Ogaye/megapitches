from app import db,create_app
from flask_migrate import migrate
app=create_app('production')
db.init_app(app)


db.create_all()