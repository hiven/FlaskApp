from flask import current_app, render_template
from app import db
from . import main_blueprint
from .models import Items

@main_blueprint.route('/')
def index():
    return render_template('main/index.html')
    
@main_blueprint.route('/test', methods=['GET', 'POST'])
def all_items():
    all_user_items = Items.query.filter_by()
    return render_template('main/items.html', items=all_user_items)



