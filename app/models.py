from . import db


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    pitch = db.Column(db.String)
    description = db.Column(db.String)
    category = db.Column(db.String, nullable=False)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='pitch', lazy='dynamic')
    posted_p = db.Column(db.DateTime,default=datetime.utcnow)
    user_p = db.Column(db.Integer,db.ForeignKey("users.id"),  nullable=False)
    

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.order_by(pitch_id=id).desc().all()
        return pitches
        
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='user', lazy='dynamic')
    
    def __repr__(self):
        return f'User {self.username}'