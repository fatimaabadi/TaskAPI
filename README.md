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

pip install Flask SQLAlchemy  psycopg2


Setting Up the Database
Install PostgreSQL: PostgreSQL Downloads
Create a PostgreSQL database named Tasks.
create a PostgreSQl table named task.
CREATE TABLE task (
	id SERIAL PRIMARY KEY,
	title VARCHAR(250),
    description VARCHAR(250),
	completed BOOLEAN,
	due_date DATE,
    priority INTEGER,
    category TEXT;
	
);
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

this is an example of the json we are passing to the  post method with clicking raw and choosing JSON
{
    "category": "frontend",
    "completed": false,
    "description": "testing purpose only",
    "due_date": "2024-01-04",
    "priority": 2,
    "title": "testing"
}


Error Handling
General Error Responses
400 Bad Request: This error response indicates that the server cannot process the request due to client error (e.g., invalid JSON, missing parameters). The response body will include details about the error.

404 Not Found: This error response indicates that the requested resource could not be found on the server. For example, when attempting to retrieve or update a task with an invalid ID.

500 Internal Server Error: This error response indicates that the server encountered an unexpected condition that prevented it from fulfilling the request. This could occur due to issues with the database or server-side logic. The response body will include details about the error.

Specific Error Handling
Invalid Date Format: When creating or updating a task, if the provided date is not in the YYYY-MM-DD format, the server will respond with a 400 Bad Request error and provide details about the expected date format.

Invalid Month or Day: If the provided date contains an invalid month or day (e.g., month greater than 12, day out of range for the given month), the server will respond with a 400 Bad Request error and provide details about the issue.

Invalid Category: When creating or updating a task, if the provided category is not one of the allowed values ('frontend', 'backend', 'fullstack'), the server will respond with a 400 Bad Request error and provide details about the allowed categories.

Task Not Found: When attempting to retrieve, update, or delete a task with an invalid ID (i.e., a task that does not exist), the server will respond with a 404 Not Found error and inform the client that the task does ot exist.
Cannot Update ID: When attempting to update a task and including the id field in the request payload, the server will respond with a 400 Bad Request error and inform the client that the task ID cannot be updated.

Cannot Specify ID: When attempting to create a new task and including the id field in the request payload, the server will respond with a 400 Bad Request error and inform the client that the ID cannot be specified during task creation.
