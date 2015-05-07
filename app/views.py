"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
import current_user
import json
from app import app, db
from flask import render_template, request, redirect, url_for, jsonify
from flask.ext.login import login_user, logout_user, login_required
#from .forms import LoginForm
from .models import username


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile', methods =['GET','POST'])
def profile():
#  if request.method == "POST":
#   username = request.form['username']
#    entry=User(username)
#    db.session.add(entry)  
#    db.session.commit() 
#    return render_template("profile.html", username=username)
  #return render_template('.html')
  entry = db.session.query(username).filter(username.username==current_user.curr_user).one()
  #entry.image = entry.image.replace ("./app/","")
  return render_template("profile.html", curr_id = entry.id, curr_image= entry.image, curr_user= entry.username, curr_email= entry.email)
  
  
  
  
  
  
@app.route('/login', methods=['GET', 'POST'])
#@oid.loginhandler
def login():
  if request.method=='POST':
    curr_useremail = request.form['email']
    curr_password = request.form['password']
    curr_user1 = db.session.query(username).filter(username.email==curr_useremail).one()
    if curr_useremail == curr_user1.email and curr_password== curr_user1.password:
      current_user.curr_id = curr_user1.id 
      current_user.curr_image = curr_user1.image
      current_user.curr_user = curr_user1.image
      current_user.curr_email= curr_user1.email
      current_user.curr_password= curr_user1.password
      return redirect("http://robust-kings-landing-82-188867.use1-2.nitrousbox.com:8080/games")
  return render_template("login.html")
  






#@app.route('/signup', methods=)
@app.route('/signup', methods=['GET','POST'])
def contact():
  if request.method == "POST":
    filefolder = './app/static/img'
    image=request.files['image']
    imagename = image.filename
    image.save(os.path.join(filefolder,imagename))
    user_name= request.form['user_name']
    email= request.form['email']
    password =request.form['password']
    entry=username(os.path.join(filefolder,imagename),user_name,email,password)
    db.session.add(entry)
    db.session.commit()
  return render_template('signup.html')

@app.route('/signup/confirm/', methods=['POST','GET'])
def sendemail ():
 ## if request.method==["GET"]: 
   ## return render_template('contact.html')
  ##else: 
    import smtplib
  
    
    fromaddr = request.form['email']
    fropassword= request.form['password']
    toname = 'Jordanne'
    toaddr = 'sweetjordie@hotmail.com'
    
    message = """From: {} <{}>
    To: {} <{}>
    Subject: {}

    {}
    """
    messagetosend = message.format(
                                
                                fromaddr,
                                fropassword,
                                toname,
                                toaddr
                              )

    # Credentials (if needed)
    username = 'jord.vanessa@gmail.com'
    password = 'qcciwbpgniyummve'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddr, messagetosend)
    server.quit()
    return render_template('signup.html')


@app.route('/profiles', methods=["GET"])
def profiles():
    results = db.session.query(username).all()
    profiles = []
    for result in results:
      profiles.append({'UserID' : result.id,
                          'Profile Picture': result.image,
                          'Username':result.username,
                          'email': result.email}) 
    return jsonify(users=profiles)



@app.route('/games', methods=["GET"])
def games():
  return render_template('game.html')

@app.route('/game/2', methods=["GET"])
def spaceinvaders():
    return render_template('spaceinvader.html')
  
@app.route('/game/1',methods=['GET'])
def platformer():
  return render_template('platformer.html')
  
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
