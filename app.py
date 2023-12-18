import os
from api import create_app, app
from api.database import db
from flask_migrate import Migrate

config = os.getenv("FLASK_CONFIG", "default")
app = create_app(config)
migrate = Migrate(app, db)
if __name__ == "__main__":
    app.run(debug=True)