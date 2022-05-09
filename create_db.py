from app import db,create_app
# from flask_migrate import migrate
app=create_app('production')
# app.config['DATABASE_URL']='postgresql://zsrkkslissrebb:db4e439bc8352672913c44bb5e2f5baa42603453446e1055b6afc138a19b400e@ec2-52-200-215-149.compute-1.amazonaws.com:5432/dbermpdgukmjpq'
db.init_app(app)

with app.app_context():
    db.create_all()


