from flask import Flask, request, jsonify
from validation import UserSchema

app = Flask(__name__)
schema = UserSchema()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
     errors = schema.validate(data)

    if errors:
        return jsonify({
            "message": "Invalid input",
            "errors": errors
        }), 400

    return jsonify({
        "message": "Login successful"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
