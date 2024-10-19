from . import db

class User(db.Model): 
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key = True)
    last_name = db.Column(db.String(100),nullable=False)
    first_name = db.Column(db.String(100),nullable=False)
    username = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(15))
    address = db.Column(db.String(200))
    gender = db.Column(db.String(10))
    birth_date = db.Column(db.Date,default=None)
    study_level = db.Column(db.String(100))
    is_sick = db.Column(db.Boolean,default=False)
    is_admin = db.Column(db.Boolean,default=False)
    is_operator = db.Column(db.Boolean,default=False)
    is_blocked = db.Column(db.Boolean,default=False)

    
    
    
    def serialize(self):
        return {
            'user_id' : self.user_id,
            'last_name' : self.last_name,
            'first_name' : self.first_name,
            'username' : self.username,
            'password' : self.password,
            'email' : self.email,
            'phone_number' : self.phone_number,
            'address' : self.address,
            'gender' : self.gender,
            'birth_date' : self.birth_date,
            'study_level' : self.study_level,
            'is_sick' : self.is_sick,
            'is_admin' : self.is_admin,
            'is_operator' : self.is_operator,
            'is_blocked' : self.is_blocked,
        }