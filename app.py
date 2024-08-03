from flask import Flask

from routes.generate_names import generate_names

app = Flask(__name__)

app.register_blueprint(generate_names)

if __name__ == '__main__':
    app.run(debug=True)