from app import db, bcrypt
from app.models.user import User
from flask_jwt_extended import create_access_token

def register_user(username, email, password):
    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return None, "Email already registered"
    if User.query.filter_by(username=username).first():
        return None, "Username already taken"

    # Hash password — never store plain text!
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    return user, None

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return None, None, "User not found"

    # bcrypt checks password against hash
    if not bcrypt.check_password_hash(user.password_hash, password):
        return None, None, "Incorrect password"

    # Create JWT token valid for 24 hours
    token = create_access_token(identity=str(user.id))
    return user, token, None