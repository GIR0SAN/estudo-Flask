from app import db

class user(db.Model):
    tablename = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.unique =(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True) 

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

        def __rep__(self):
            return"<User %r>" % self.username
        
class Post(db.Model):
    __tablename__ = "posts" 

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    id user =db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = contentself.user_id = user_id
        
    def __rep__(self):
        return "<Post %r>" % self.id

class Follow(db.Model):
    tablename = "follow"
    
    id = db.Column(db.Integer, primary_key=True)
    user id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower id = db.Column(db.Integer, db.ForeingKey('user.id'))

    user = db.relationship('User', foreign_keys=id.user)
    follower = db.relationship('User', foreign_keys=follower_id)
    