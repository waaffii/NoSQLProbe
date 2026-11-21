import re
from flask import Flask, jsonify, request

app = Flask(__name__)

FAKE_USERS = [
    {"username": "alice", "password": "secret", "role": "user"},
    {"username": "admin_lab", "password": "lab_password", "role": "admin"},
]


def matches_query(actual: str, expected) -> bool:
    if isinstance(expected, dict):
        if "$ne" in expected:
            return actual != expected["$ne"]
        if "$gt" in expected:
            return str(actual) > str(expected["$gt"])
        if "$regex" in expected:
            return re.search(expected["$regex"], str(actual)) is not None
        if "$where" in expected:
            return "true" in str(expected["$where"]).lower()
        return False
    return actual == expected


@app.post("/vuln-login")
def vuln_login():
    data = request.get_json(silent=True) or {}
    u_q = data.get("username")
    p_q = data.get("password")

    for user in FAKE_USERS:
        if matches_query(user["username"], u_q) and matches_query(user["password"], p_q):
            return jsonify({"authenticated": True, "user": user["username"], "role": user["role"]}), 200

    return jsonify({"authenticated": False, "message": "Invalid credentials"}), 401


@app.post("/safe-login")
def safe_login():
    data = request.get_json(silent=True) or {}
    u_q = data.get("username")
    p_q = data.get("password")

    # Strict input typing: only accept plain strings
    if not isinstance(u_q, str) or not isinstance(p_q, str):
        return jsonify({"authenticated": False, "message": "Invalid input type"}), 400

    for user in FAKE_USERS:
        if user["username"] == u_q and user["password"] == p_q:
            return jsonify({"authenticated": True, "user": user["username"], "role": user["role"]}), 200

    return jsonify({"authenticated": False, "message": "Invalid credentials"}), 401


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)