from flask import current_app, render_template, request, redirect, flash, url_for
from app import db
from . import main_blueprint
from .models import Items
from .forms import ItemsForm, EditItemsForm

   
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
                return redirect(url_for('main.all_items'))
            except:
                db.session.rollback()
                flash('Something went wrong', 'danger')
    return render_template('main/add.html', form=form)
    
@main_blueprint.route('/edit_item/<items_id>', methods=['GET', 'POST'])
def edit_item(items_id):
    form = EditItemsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                item = Items.query.get(items_id)
                item.name = form.name.data
                item.notes = form.notes.data
                db.session.commit()
                flash('Item edited successfully!', 'success')
                return redirect(url_for('main.all_items'))
            except:
                db.session.rollback()
                flash('Unable to edit item', 'danger')
        return render_template('edit_item.html', item=item, form=form)
    else:
        flash('Something went wrong', 'danger')
    return redirect(url_for('main.all_items'))


@main_blueprint.route('/delete_item/<items_id>')
def delete_item(items_id):
    item = Items.query.filter_by(id=items_id).first_or_404()
    db.session.delete(item)
    db.session.commit()
    flash('{} was deleted.'.format(item.name), 'success')
    return redirect(url_for('main.all_items'))
