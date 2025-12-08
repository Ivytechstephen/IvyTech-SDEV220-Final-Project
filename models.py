from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


""" SQLAlchemy database models """
# User model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)


# List model
class List_Obj(db.Model):
    __tablename__ = 'list_obj'   

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_template = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    items = db.relationship('Item_Obj', backref='parent_list',
                            cascade="all, delete-orphan", lazy=True)


# Item model
class Item_Obj(db.Model):
    __tablename__ = 'item_obj'   

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    is_completed = db.Column(db.Boolean, default=False)

    # Foreign key must match List_Obj.__tablename__
    list_id = db.Column(db.Integer, db.ForeignKey('list_obj.id'), nullable=False)


# Profanity model
class Profanity(db.Model):
    __tablename__ = 'profanity'

    word = db.Column(db.String, primary_key=True, nullable=False)
    canonical_form_1 = db.Column(db.String)
    canonical_form_2 = db.Column(db.String)
    canonical_form_3 = db.Column(db.String)

