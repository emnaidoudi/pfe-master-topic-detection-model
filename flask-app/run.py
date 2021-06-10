from app import create_app
from flask_cors import CORS

app = create_app()
cors = CORS(app, resources={r"/word-clouds/*": {"origins": "*"}}) 


if __name__ == "__main__":
    app.run()