from flask import Blueprint, render_template

reconcile = Blueprint('reconcile', __name__,
  template_folder='../templates',
  static_folder='../static')


@reconcile.route('/')
def index():
  return render_template('homepage.html')