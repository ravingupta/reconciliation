import os
from flask import Flask
from flask_bootstrap import Bootstrap

from controllers.main import main


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

Bootstrap(app)

app.register_blueprint(main, url_prefix='/')


if __name__ == '__main__':
  app.run()