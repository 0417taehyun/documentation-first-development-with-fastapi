from flask import Flask
from flasgger import Swagger

from src.router import router


app = Flask(__name__)
app.register_blueprint(blueprint=router)

Swagger(app=app)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
