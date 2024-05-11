# TaskAPI
hello 
This project is a Task Management System built using Flask, SQLAlchemy, and PostgreSQL. It provides a RESTful API for managing tasks, including creating, reading, updating, and deleting tasks. Each task can have a title, description, completion status, due date, priority, and category.
Prerequisites
Python (3.6 or higher)
Flask
SQLAlchemy
PostgreSQL
Postman (for testing the API)


Installing Dependencies

pip install Flask SQLAlchemy


Setting Up the Database
Install PostgreSQL: PostgreSQL Downloads
Create a PostgreSQL database named Tasks.
create a PostgreSQl table named task.
Set up the database connection URI in app.py

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/Tasks'


Running the Application
python app.py
Running on http://127.0.0.1:5000/task
 
API Endpoints
GET /task: Retrieve all tasks.
POST /task: Create a new task.
GET /task/<task_id>: Retrieve a specific task.
PUT /task/<task_id>: Update a specific task.
DELETE /task/<task_id>: Delete a specific task


Usage
Use Postman to send HTTP requests to the API endpoints.
Ensure proper JSON format for request bodies.
Check the API responses for success or error messages.

make sure in Postman  when using put or post to choose Body tab then raw,and JSON from the drop down
and provide the json you want to add or update
check the screenshot provided  please
