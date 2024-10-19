from flask import Blueprint, request, jsonify
from controllers.user_controller import get_all_users, create_user, get_user, update_user, delete_user,login_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/get-users', methods=['GET'])
def get_users():
    filters = request.args  # Get filters from query params if any
    return jsonify({
        'message': 'Users retrieved successfully',
        'data':{
            'users': get_all_users(filters),
        }
    })

@user_bp.route('/add-user', methods=['POST'])
def add_user(): 
    user_data = request.json
    return create_user(user_data)

@user_bp.route('/get-user/<int:user_id>', methods=['GET'])
def fetch_user(user_id):
    return jsonify({
        'message': 'Users retrieved successfully',
        'data':{
            'user': get_user(user_id),
        }
    })

@user_bp.route('/update-user/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    user_data = request.json
    return jsonify(update_user(user_id, user_data))

@user_bp.route('/delete-user/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    return jsonify(delete_user(user_id))


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return jsonify(login_user(data))
