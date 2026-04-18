from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.analytics_service import get_analytics

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/", methods=["GET"])
@jwt_required()
def analytics():
    user_id = int(get_jwt_identity())
    data = get_analytics(user_id)
    return jsonify(data), 200