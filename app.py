import os
from flask import Flask
from flask_bootstrap import Bootstrap

from controllers.main import main
from controllers.reconcile import reconcile


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

Bootstrap(app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(reconcile, url_prefix='/reconcile')


if __name__ == '__main__':
  app.run()