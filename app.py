# app.py

from flask import Flask, jsonify, request
from models import db, Task
from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_valid_month(month):
    return 1 <= month <= 12

def is_valid_day(year, month, day):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/Tasks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
@app.route('/task', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify([{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'priority': task.priority,
            'category': task.category
        } for task in tasks])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/task', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        if 'due_date' in data:
            due_date_str = data['due_date']
            if not is_valid_date(due_date_str):
                return jsonify({'error': 'Invalid date format. Date must be in YYYY-MM-DD format.'}), 400

            year, month, day = map(int, due_date_str.split('-'))
            if not is_valid_month(month):
                return jsonify({'error': 'Invalid month. Month must be between 1 and 12.'}), 400

            if not is_valid_day(year, month, day):
                return jsonify({'error': 'Invalid day for the given month.'}), 400
        
        category = data.get('category')
        if category not in ['frontend', 'backend', 'fullstack']:
            return jsonify({'error': 'Invalid category. Allowed values: frontend, backend, fullstack'}), 400
        
        new_task = Task(
            title=data['title'],
            description=data['description'],
            completed=data.get('completed', False),
            due_date=data.get('due_date'),
            priority=data.get('priority'),
            category=category
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully!'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key in JSON: {e}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = Task.query.get(task_id)
        if task is None:
            return jsonify({'error': 'Task does not exist.'}), 404
        return jsonify({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'priority': task.priority,
            'category': task.category
        })
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        if 'due_date' in data:
            due_date_str = data['due_date']
            if not is_valid_date(due_date_str):
                return jsonify({'error': 'Invalid date format. Date must be in YYYY-MM-DD format.'}), 400

            year, month, day = map(int, due_date_str.split('-'))
            if not is_valid_month(month):
                return jsonify({'error': 'Invalid month. Month must be between 1 and 12.'}), 400

            if not is_valid_day(year, month, day):
                return jsonify({'error': 'Invalid day for the given month.'}), 400
        
        category = data.get('category')
        if category and category not in ['frontend', 'backend', 'fullstack']:
            return jsonify({'error': 'Invalid category. Allowed values: frontend, backend, fullstack'}), 400
        
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)
        task.due_date = data.get('due_date', task.due_date)
        task.priority = data.get('priority', task.priority)
        task.category = category or task.category
        db.session.commit()
        return jsonify({'message': 'Task updated successfully!'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully!'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)