from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

venue_genres = db.Table('venue_genres',
                        db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
                        db.Column('genre_id', db.Integer, db.ForeignKey('Genre.id'), primary_key=True)
                        )

artist_genres = db.Table('artist_genres',
                         db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'), primary_key=True),
                         db.Column('genre_id', db.Integer, db.ForeignKey('Genre.id'), primary_key=True)
                         )


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(500), nullable=True)
    # genres = db.relationship('Genre', secondary=venue_genres, backref=db.backref('venues', lazy=True))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
        return f"<Venue {self.id}, {self.name}, {self.state} {self.city}>"

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


class Genre(db.Model):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120), nullable=True)
    # genres = db.relationship('Genre', secondary=artist_genres, backref=db.backref('artists', lazy=True))
    genres = db.Column(db.ARRAY(db.String()))
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)
    looking_for_venue = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f"<Artist {self.id}, {self.name}, {self.state} {self.city}>"

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id', ondelete='SET NULL'))
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id', ondelete='SET NULL'))
    start_time = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Show artist_id: {self.artist_id} venue_id: {self.venue_id}" \
               f"starting_date_time: {self.start_time} venue: {self.venue.name}>"