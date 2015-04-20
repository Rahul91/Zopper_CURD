from datetime import datetime

from .. import db


class Blog(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
	
	# pretty self explanotory
    '''title = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text())

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow,
                                          onupdate=datetime.utcnow)
    '''
    id = db.Column(db.Integer, primary_key=True)
    pincode = db.Column(db.String(100), unique=True)
    officename = db.Column(db.String(100))
    districtname = db.Column(db.String(100))
    statename = db.Column(db.String(100))



    def __init__(self, pincode="", officename="", districtname="", statename=""):
        self.pincode = pincode
        self.officename = officename
        self.districtname = districtname
        self.statename = statename
	
    def __repr__(self):
        return '<Blogpost - {}>'.format(self.pincode)