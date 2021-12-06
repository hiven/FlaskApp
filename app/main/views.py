from flask import current_app, render_template
from app import db
from . import main_blueprint
from .models import Items
from .forms import ItemsForm

   
@main_blueprint.route('/', methods=['GET', 'POST'])
def all_items():
    all_user_items = Items.query.filter_by()
    return render_template('main/items.html', items=all_user_items)
    

@main_blueprint.route('/add', methods=['GET', 'POST'])
def add_item():
    form = ItemsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_item = Items(form.name.data, form.notes.data)
                db.session.add(new_item)
                db.session.commit()
                flash('Item added', 'success')
                return redirect(url_for('all_items'))
            except:
                db.session.rollback()
                flash('Something went wrong', 'danger')
    return render_template('main/add.html', form=form)
    

@main_blueprint.route('/test')
def index():
    return render_template('main/index.html')



