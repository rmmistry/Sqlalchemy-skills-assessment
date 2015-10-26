"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "Models"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.SMALLINT, nullable=False)
    brand_name = db.Column(db.String(50), db.ForeignKey("Brands.brand_name"), nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Provide helpful representation when upon print"""

        return "<Model id=%d year=%d brand_name=%s name=%s>" % (self.id, self.year, self.brand_name.encode("utf=8"), self.name)


class Brand(db.Model):

    __tablename__ = "Brands"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    founded = db.Column(db.SMALLINT)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.SMALLINT)

    def __repr__(self):
        """Provide helpful representation when upon print"""

        return "<Brand id=%d name=%s founded=%d>" % (self.id, self.name, self.founded)


# End Part 1
##############################################################################
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
