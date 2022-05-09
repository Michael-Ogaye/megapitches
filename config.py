# this is the configuration module
import os
from  dotenv import load_dotenv
load_dotenv()





class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")




class ProdConfig(Config):
    DATABASE_URL="postgres://zsrkkslissrebb:db4e439bc8352672913c44bb5e2f5baa42603453446e1055b6afc138a19b400e@ec2-52-200-215-149.compute-1.amazonaws.com:5432/dbermpdgukmjpq"


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL")
    DEBUG = True



config_options = {
'development':DevConfig,
'production':ProdConfig
}