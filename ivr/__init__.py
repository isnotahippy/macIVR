from flask import Flask, Blueprint
from flask.ext.mongoengine import MongoEngine
from ivr import settings

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'db': settings.MONGODB_DBNAME, 'host': settings.MONGODB_HOST}
app.config["SERVER_NAME"] = settings.SERVER_NAME

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

blueprint = Blueprint('ivr', __name__, template_folder='templates')

def register_blueprints(app):
    # Prevents circular imports
    app.register_blueprint(blueprint)

from ivr import views

register_blueprints(app)
