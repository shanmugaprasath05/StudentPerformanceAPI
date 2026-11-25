# Student Performance API

A RESTful API built using Python, FastAPI, and MySQL to manage student academic performance records.

## Technologies Used

- Python
- FastAPI
- MySQL
- MySQL Connector
- Pydantic
- Uvicorn
- Git and GitHub

## Features

- Retrieve all student records
- Retrieve an individual student by ID
- Add new student records
- Update existing student records
- Delete student records
- Validate incoming student data
- Handle database errors
- Store database credentials using environment variables

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| POST | `/students` | Add a new student |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/shanmugaprasath05/StudentPerformanceAPI.git
cd StudentPerformanceAPI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project directory:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=student_db
```

Never upload your `.env` file to GitHub.

### 5. Run the application

```bash
uvicorn main:app --reload
```

### 6. Open API documentation

Visit:

http://127.0.0.1:8000/docs

Use Swagger UI to test the API endpoints.

## Database

Database: `student_db`

Table: `students`

Expected columns:

- id
- name
- study_hours
- attendance
- previous_score
- final_score

## Developer

B.Sc. Data Science Graduate

GitHub: https://github.com/shanmugaprasath05
