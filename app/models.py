from app import db

class username(db.Model):     
    id = db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(200))
    username = db.Column(db.String(80),unique = True)     
    email = db.Column(db.String(80),unique = True)     
    password = db.Column(db.String(80))   
    
    def  __init__(self, image, username,email,password):
      self.image = image
      self.username = username
      self.email = email
      self.password = password


  #  def is_authenticated(self):
  #      return True

   # def is_active(self):
    #    return True

   # def is_anonymous(self):
    #    return False

    #def get_id(self):
     #   try:
      #      return unicode(self.id)  # python 2 support
      #  except NameError:
       #     return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)