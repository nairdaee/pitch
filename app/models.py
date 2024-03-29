from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted_c = db.Column(db.DateTime,default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"), nullable=False)
    user_c = db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(pitch_id=id).all()
        return comments



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default= None)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_upvotes(cls, id):
        upvote_pitch = Upvote(user=current_user, pitch_id=id)
        upvote_pitch.save_upvotes()

    @classmethod
    def get_upvotes(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls, pitch_id):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'


class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default= None)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_downvotes(cls, id):
        downvote_pitch = Downvote(user=current_user, pitch_id=id)
        downvote_pitch.save_downvotes()

    @classmethod
    def get_downvotes(cls, id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls, pitch_id):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
