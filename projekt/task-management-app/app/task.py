from .models import Task
from . import db
from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for, flash, Blueprint, request, jsonify
from flask_login import login_required, current_user
from random import randint
from .forms import TaskForm

task = Blueprint('task', __name__)

@task.route('/tasks/add', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            due_date=form.due_date.data,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        flash('New task added successfully.', 'success')
        return redirect(url_for('task.get_all_tasks'))
    return render_template('add_task.html', form=form)

@task.route('/tasks', methods=['GET'])
@login_required
def get_all_tasks():
    # Fetch tasks for the current user
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    # Generate random colors for notes
    colors = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
              '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D']
    task_notes = []
    for task in user_tasks:
        color = colors[randint(0, len(colors) - 1)]
        task_notes.append({'task': task, 'color': color})
    return render_template('tasks.html', task_notes=task_notes)

@task.route('/tasks/<id>', methods=['GET'])
@login_required
def view_task(id):
    task = Task.query.get_or_404(id)
    return render_template('view_task.html', task=task)

@task.route('/tasks/<int:id>/edit', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        form.populate_obj(task)
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('task.get_all_tasks'))
    return render_template('edit_task.html', form=form, task=task)

@login_required
@task.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200