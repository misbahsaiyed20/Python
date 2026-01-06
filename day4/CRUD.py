from flask import Flask, request, jsonify
from model import db, Activity

app = Flask(__name__)

@app.route('/')
def home():
    return "DAY4 FLASK APP IS RUNNING"


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/activity_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/activities', methods=['POST'])
def create_activity():
    data = request.json

    activity = Activity(
        name=data['name'],
        description=data.get('description')
    )

    db.session.add(activity)
    db.session.commit()

    return jsonify(activity.to_dict()), 201

@app.route('/activities', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    return jsonify([activity.to_dict() for activity in activities])

@app.route('/activities/<int:id>', methods=['GET'])
def get_activity(id):
    activity = Activity.query.get(id)

    if not activity:
        return jsonify({
            "error": "Activity not found"
            }), 404

    return jsonify(activity.to_dict())


@app.route('/activities/<int:id>', methods=['PUT'])
def update_activity(id):
    activity = Activity.query.get(id)

    if not activity:
        return jsonify({
            "error": "Activity not found"
            }), 404

    data = request.json
    activity.name = data.get('name', activity.name)
    activity.description = data.get('description', activity.description)

    db.session.commit()
    return jsonify(activity.to_dict())

@app.route('/activities/<int:id>', methods=['DELETE'])
def delete_activity(id):
    activity = Activity.query.get(id)

    if not activity:
        return jsonify({
            "error": "Activity not found"
            }), 404

    db.session.delete(activity)
    db.session.commit()

    return jsonify({
        "message": "Activity deleted successfully"
        })


if __name__ == '__main__':
    app.run(debug=True)
