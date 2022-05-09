from app import db,create_app
# from flask_migrate import migrate
app=create_app('production')
db.init_app(app)

with app.app_context():
    db.create_all()


