import json
from flask import request
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    data = {
        "message": "This is my first Flask Server"
    }
    return (
        json.dumps(data, indent=4, sort_keys=True),
        200,
        {'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    app.run(debug=True)