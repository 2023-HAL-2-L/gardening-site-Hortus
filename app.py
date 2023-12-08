import os
from api import create_app, app

config = os.getenv("FLASK_CONFIG", "default")
app = create_app(config)
if __name__ == "__main__":
    app.run(debug=True)