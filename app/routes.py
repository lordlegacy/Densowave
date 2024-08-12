from app.config import PASSKEY
from flask import Blueprint, request, jsonify
from app.models import User,BusinessInfo
from app.extensions import db, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.stk_push import send_stk_push

business_bp = Blueprint('business', __name__)
auth_bp = Blueprint('auth', __name__)
stk_bp = Blueprint('stk', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "User registered successfully!"}), 200


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200




@business_bp.route('/register', methods=['POST'])
@jwt_required()
def create_business_info():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity['username']).first()
    
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    data = request.get_json()

    business_info = BusinessInfo(
        user_id=user.id,
        business_name=data['business_name'],
        business_number=data['business_number'],
        paybill=data['paybill']
    )
    
    db.session.add(business_info)
    db.session.commit()
    return jsonify({"message": "Business information created successfully"}), 201

@business_bp.route('/view', methods=['GET'])
@jwt_required()
def get_business_info():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity['username']).first()
    
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    business_info = BusinessInfo.query.filter_by(user_id=user.id).first()

    if not business_info:
        return jsonify({"message": "No business information found"}), 404

    return jsonify({
        "business_name": business_info.business_name,
        "business_number": business_info.business_number,
        "paybill": business_info.paybill
    }), 200

@business_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_business_info():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity['username']).first()
    
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    data = request.get_json()
    business_info = BusinessInfo.query.filter_by(user_id=user.id).first()

    if not business_info:
        return jsonify({"message": "No business information found"}), 404
    
    business_info.business_name = data['business_name']
    business_info.business_number = data['business_number']
    business_info.paybill = data['paybill']
    
    db.session.commit()

    return jsonify({"message": "Business information updated successfully"}), 200

@stk_bp.route('/stk', methods=['POST'])
@jwt_required()
def handle_stk_push():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity['username']).first()
    data = request.get_json()

    

    amount = data['amount']
    phone_number = data['phone_number']
    transaction_desc = data['transaction_desc']

    # Assuming you store the business info in the BusinessInfo table
    business_info = BusinessInfo.query.filter_by(user_id=user.id).first()
    if not business_info:
        return jsonify({"message": "No business information found"}), 404

    shortcode = business_info.business_number
    callback_url = "https://mydomain.com/pat"  # Replace with your actual callback URL

    response = send_stk_push(shortcode, PASSKEY, amount, phone_number, phone_number, transaction_desc, callback_url)
    return jsonify(response), 200
