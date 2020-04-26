from . import db


class Users(db.Model):
    """Model for user accounts."""

    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255), index=False, unique=True, nullable=False)

    pwd = db.Column(db.String(255), index=False, unique=False, nullable=False)

    email = db.Column(db.String(255), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Trips(db.Model):
    """Model for user accounts."""

    __tablename__ = 'Trips'

    idt = db.Column(db.Integer, primary_key=True)

    startlocation = db.Column(db.String(255), index=False, unique=False, nullable=False)

    endlocation = db.Column(db.String(255), index=False, unique=False, nullable=False)

    cbfootprint = db.Column(db.Float, index=True, unique=False, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))

    vehicle_id = db.column(db.Integer, db.ForeignKey('Vehicles.vehicle_id'))

    def __repr__(self):
        return '<Trips {}>'.format(self.cbfootprint)


class Vehicles(db.Model):
    """Model for user accounts."""

    __tablename__ = 'Vehicles'

    vehicle_id = db.Column(db.Integer, primary_key=True)

    vehicle_type = db.Column(db.String(255), index=False, unique=False, nullable=False)

    mileage = db.Column(db.Float, index=True, unique=False, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))

    def __repr__(self):
        return '<Vehicles {}>'.format(self.vehicle_type)
