from db import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    emp_name = db.Column(db.String(100))
    pass_word = db.Column(db.String(100))

    def __init__(self, user_name, pass_word, emp_name):
        self.user_name = user_name
        self.pass_word = pass_word
        self.emp_name = emp_name

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_user(cls, id):
        return cls.query.with_entities(cls.user_name, cls.emp_name).filter(cls.id == id).first()
