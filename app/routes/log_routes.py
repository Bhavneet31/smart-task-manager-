from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.log_service import get_user_logs

log_bp = Blueprint("logs", __name__)

@log_bp.route("/", methods=["GET"])
@jwt_required()
def logs():
    user_id = int(get_jwt_identity())
    logs = get_user_logs(user_id)
    return jsonify({"logs": [l.to_dict() for l in logs]}), 200