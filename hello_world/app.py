import json
from flask import request
from flask_lambda import FlaskLambda

flaskapp = FlaskLambda(__name__)


@flaskapp.route('/hello', methods=['GET', 'POST'])
def index():
    data = {
        "message": "This is my first Flask Server"
    }
    return (
        json.dumps(data),
        200,
        {'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    flaskapp.run(debug=True)