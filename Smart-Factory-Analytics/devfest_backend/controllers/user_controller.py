import random
import string 
from models.user import User
from models import db
import jwt
from datetime import datetime

# from werkzeug.security import safe_str_cmp 
SECRET_KEY = 'Hello_From_The_dark_side'

# Function to generate a 16-character alphanumeric password
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def create_token(user):
    payload = {
        'user_id': user.user_id,
        'username': user.username,
        'is_operator': user.is_operator,
        'is_admin': user.is_admin,
        'is_blocked': user.is_blocked,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')



# Create a new user
def create_user(data):
    # Check if all required fields are present
    required_fields = ['last_name', 'first_name' , 'gender']
    if not all(field in data for field in required_fields):
        return {'error': 'Missing required fields'}, 400
    
    # Generate password
    password = generate_password()
    

    # Ensure gender is 'm' or 'f'
    if data['gender'] not in ['m', 'f']:
        return {'error': 'Invalid gender'}, 400
    

    # Create new user instance
    
    duplicate = User.query.filter_by(username=data['first_name']+ ' '+data['last_name']).all()
    if len(duplicate) > 0:
        return {'error' : 'user already exists'}, 400 
    birth_date = data.get('birth_date',None)
    if not birth_date is None :
        birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()

        
    new_user = User(
        last_name=data['last_name'],
        first_name=data['first_name'],
        username=data['first_name']+ ' '+data['last_name'],
        password=password,  # Backend-generated password
        email=data.get('email',None),
        phone_number=data.get('phone_number',None),
        address=data.get('address',None),
        gender=data.get('gender',None),
        birth_date = birth_date,
        study_level=data.get('study_level',None),
        is_operator=data.get('is_operator', False),
        is_admin=data.get('is_admin', False),
        is_sick=data.get('is_sick', False),
        is_blocked=data.get('is_blocked', False),
    )
        
    # Add user to the database
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'User created successfully','user':new_user.serialize()}, 201

# Get all users, or filter by fields
def get_all_users(filters=None):
    query = User.query

    # Apply filters if any are passed
    if filters:
        if 'is_admin' in filters:
            query = query.filter_by(is_admin=filters['is_admin'])
        if 'is_operator' in filters:
            query = query.filter_by(is_operator=filters['is_operator'])
        if 'gender' in filters:
            query = query.filter_by(gender=filters['gender'])
        if 'study_level' in filters:
            query = query.filter_by(study_level=filters['study_level'])
        if 'user_id' in filters:
            query = query.filter_by(user_id=filters['user_id'])

    users = query.all()
    return [user.serialize() for user in users]

# Get a single user by ID
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return {'error': 'User not found'}, 404
    return user.serialize()

# Update an existing user
def update_user(user_id, data):
    user = User.query.get(user_id)
    if user is None:
        return {'error': 'User not found'}, 404

    # Update user fields
    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    first_name = data.get('first_name',None)       
    last_name = data.get('last_name',None)
    username = ''       

    if first_name and last_name:
        username = first_name + ' ' + last_name
    elif first_name and not last_name:
        username = first_name + ' ' + user.last_name
    elif not first_name and last_name:
        username = user.first_name + ' ' + last_name
    
    if first_name or last_name:
        duplicate = User.query.filter_by(username = username).all()
        if len(duplicate) > 0:
            return {'error' : 'this user already exists'}, 400
        else:
            user.username = username
        

    db.session.commit()
    return {'message': 'User updated successfully'}

# Delete a user by ID
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return {'error': 'User not found'}, 404

    db.session.delete(user)
    db.session.commit()
    return {'message': 'User deleted successfully'}



def login_user(data):
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return {'error': 'Username and password are required'}, 400

    # Find the user by username
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and the password matches
    if user and user.password == password:
        # Create a JWT token
        token = create_token(user)

        # Return the token and user information
        return {
            'message': 'Login successful',
            'data':{
                'token':token
            }
            }, 200
    else:
        return {'error': 'Invalid username or password'},401