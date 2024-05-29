from flask import Flask, jsonify, request
from utils import encrypt_password
from config import Config
from extensions import db, migrate

# __name__ == '__main__'
app = Flask(__name__) 
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def home():
    return jsonify([])

"""
Vamos a hacer un ejemplo donde vamos a recibir la información 
del usuario pero desde POSTMAN
"""
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        user_data['password'] = encrypt_password(user_data.get('password')).decode("utf-8")

        return jsonify({
            "new_user": user_data
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        })


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8000, debug=True)
