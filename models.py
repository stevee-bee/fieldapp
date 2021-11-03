from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from flask_app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(32))
    land_loc = db.Column(db.String(32))
    comment = db.Column(db.String(255))
    seeds = db.relationship('Seed', backref='field', lazy='dynamic')
    chemicals = db.relationship('Chemical', backref='field', lazy='dynamic')

    def __repr__(self):
        return '<Field {} "{}">'.format(self.number, self.name)


class Seed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    date_seeded = db.Column(db.Date, index=True)
    date_harvested = db.Column(db.Date, index=True)
    bu_yield = db.Column(db.Numeric(4,1))
    comment = db.Column(db.String(255))
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'))

    def __repr__(self):
        return '<Seed.id={} .name={} .date_seeded={} .date_harvested={} .bu_yield={} .comment={} .field_id={}>'.format(self.id, self.name, self.date_seeded, self.date_harvested, self.bu_yield, self.comment, self.field_id)


class Chemical(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, db.ForeignKey('chemical_type.id'))
    name = db.Column(db.String(25))
    date_applied = db.Column(db.Date, index=True)
    rate = db.Column(db.String(16))
    wind_dir = db.Column(db.String(10))
    comment = db.Column(db.String(255))
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'))

    def __repr__(self):
        return '<Chemical.id={} .type={} .name={} .date_applied={} .rate={} .wind_dir={} .comment={} .field_id={}>'.format(self.id, self.type, self.name, self.date_applied, self.rate, self.wind_dir, self.comment, self.field_id)


class ChemicalType(db.Model):

    __tablename__ = "chemical_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    chemicals = db.relationship('Chemical', backref='chemical_type', lazy='dynamic')
