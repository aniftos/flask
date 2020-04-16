import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
from threading import Thread

def save_picture(form_picture): #save the uplodated picture to our file system
    #randomise the image name so its unique
    random_hex = secrets.token_hex(8)
    #save in the same extention the user uploaded
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    #app.root_path will give all the root up to the app package directory
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path) #save image to filesystem

    return picture_fn #return picture filename


def send_reset_email(user): #function to send an email!
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
                    sender = 'noreply@demo.com', 
                    recipients=[user.email])
    #external=true will give you an absolute url instead of relative url
    # if message too big use jinja2 to write the msg                
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token',token=token, _external = True)}
If you did not make this request then simply ignore this email and no changes will be made
'''
    #mail.send(msg) #send the mail
    Thread(target=send_async_email, args=(current_app,msg)).start()

def send_async_email(app, msg):
    with app.app_context(): #when running a thread need to give the application context to know that the mail
        mail.send(msg)       #servel will take the values from the app.config file. It can now see the parameters
