# Student Performance API

A RESTful API developed using **Python, FastAPI, and MySQL** to manage student academic performance records. The application supports creating, retrieving, updating, and deleting student information through REST API endpoints.

## Technologies Used

- Python
- FastAPI
- MySQL
- MySQL Connector
- Pydantic
- Python-dotenv
- Uvicorn
- Git and GitHub

## Features

- Retrieve all student records
- Retrieve an individual student using their ID
- Add new student records
- Update existing student details
- Delete student records
- Validate incoming data using Pydantic
- Handle database errors using HTTP exceptions
- Store database credentials in environment variables

## Project Structure

```text
StudentPerformanceAPI/
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── .env              # Local configuration; not uploaded
```

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| POST | `/students` | Add a new student |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## API Request Examples

### 1. Get All Students

**GET** `/students`

Example response:

```json
{
  "total_students": 2,
  "students": [
    {
      "id": 1,
      "name": "Arun",
      "study_hours": 5.0,
      "attendance": 90.0,
      "previous_score": 75.0,
      "final_score": 80.0
    }
  ]
}
```

### 2. Get Student by ID

**GET** `/students/1`

Returns the student record matching the supplied ID.

### 3. Add a Student

**POST** `/students`

Example request body:

```json
{
  "name": "Arun",
  "study_hours": 5.0,
  "attendance": 90.0,
  "previous_score": 75.0,
  "final_score": 80.0
}
```

Example response:

```json
{
  "message": "Student added successfully",
  "student_id": 1
}
```

### 4. Update Student Details

**PUT** `/students/1`

Uses the same request fields as the POST endpoint to update an existing student record.

### 5. Delete a Student

**DELETE** `/students/1`

Deletes the student record matching the supplied ID.

## Data Validation

The API uses Pydantic to validate student input:

- `study_hours` must be greater than or equal to 0.
- `attendance` must be between 0 and 100.
- `previous_score` must be between 0 and 100.
- `final_score` must be between 0 and 100.

## Database Configuration

Database name: `student_db`

Table name: `students`

Expected columns:

| Column | Data type |
|---|---|
| id | INT, Primary Key, Auto Increment |
| name | VARCHAR(50) |
| study_hours | FLOAT |
| attendance | FLOAT |
| previous_score | FLOAT |
| final_score | FLOAT |

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shanmugaprasath05/StudentPerformanceAPI.git
cd StudentPerformanceAPI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create the database and table in MySQL:

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    study_hours FLOAT,
    attendance FLOAT,
    previous_score FLOAT,
    final_score FLOAT
);
```

### 5. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=student_db
```

Replace the placeholder with your own MySQL password. Never upload your actual `.env` file to GitHub.

### 6. Start the FastAPI server

```bash
uvicorn main:app --reload
```

### 7. Open API documentation

Swagger UI:

http://127.0.0.1:8000/docs

Alternative API documentation:

http://127.0.0.1:8000/redoc

## Testing

The five API endpoints were exercised using FastAPI Swagger UI.

- GET all students
- GET student by ID
- POST a student
- PUT student details
- DELETE a student

## Future Improvements

- Integrate the Student Performance Prediction machine learning model.
- Add automated API tests using Pytest.
- Add authentication and authorization.
- Deploy the API to a cloud platform.

## Developer

**B.Sc. Computer Science Graduate**

GitHub: https://github.com/shanmugaprasath05

Project Repository: https://github.com/shanmugaprasath05/StudentPerformanceAPI
