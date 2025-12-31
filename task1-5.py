from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ayaan", "email": "ayaan@gmail.com"},
    {"id": 2, "name": "Sara", "email": "sara@gmail.com"}
]

#task-1 set up
@app.route('/')
def home():
    return jsonify({
        "message": "API is working"
        }), 200

#get users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": "success",
        "users": users
    }), 200

#user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user), 200

    return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if not data:
        return jsonify({
            "error": "JSON body required"
            }), 400

    name = data.get("name")
    email = data.get("email")
    if not name or name.strip() == "":
        return jsonify({
            "error": "Name is required"
            }), 400

    if not email:
        return jsonify({
            "error": "Email is required"
            }), 400

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email
    }
    users.append(new_user)

    return jsonify({
        "message": "User added successfully",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
