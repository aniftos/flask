import os

# put here all configuration values
# Need to create a class so we can have everything in a new object
class Config:
    #SECRET_KEY = 'ceaa0358f6db721ad45b2e49fce2e7b3' #set environment variables for this
    #SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

