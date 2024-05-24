from flask import Flask, jsonify, request

# __name__ == '__main__'
app = Flask(__name__) 

users = []


@app.route('/')
def home():
    return jsonify(users)

"""
Vamos a hacer un ejemplo donde vamos a recibir la información 
del usuario pero desde POSTMAN
"""
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    
    users.append(user_data)

    return jsonify({
        "new_user": user_data
    })


if __name__ == '__main__':
    app.run(port=8000, debug=True)
