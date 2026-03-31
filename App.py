from flask import Flask, request, jsonify
from database import create_table
from service import insert_value, get_all_values
from auth import require_auth

app = Flask(__name__)

create_table()

@app.route('/', methods=['POST'])
@require_auth
def add_value():
    try:
        data = request.get_json()

        if not data or 'data' not in data:
            return jsonify({"error": "No value provided"}), 400

        value = data['data']

        insert_value(value)

        return jsonify({"message": "Value added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/', methods=['GET'])
@require_auth
def get_values():
    try:
        values = get_all_values()
        return jsonify(values), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)