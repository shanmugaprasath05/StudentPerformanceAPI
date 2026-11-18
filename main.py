
import os

import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

# Load environment variables
load_dotenv()

# Create FastAPI application
app = FastAPI()

# GET API: Retrieve all students
@app.get("/students")
def get_students():

    connection = None
    cursor = None

    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        # Create cursor
        cursor = connection.cursor(dictionary=True)

        # Execute SQL query
        query = """
        SELECT id, name, study_hours, attendance,
               previous_score, final_score
        FROM students
        """

        cursor.execute(query)

        # Retrieve all records
        students = cursor.fetchall()

        return {
            "total_students": len(students),
            "students": students
        }



    except mysql.connector.Error as e:

        print("MYSQL ERROR:", e)

        raise HTTPException(

            status_code=500,

            detail="Database connection or query failed"

        )


    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

# GET API: Retrieve one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):

    connection = None
    cursor = None

    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        # Create cursor
        cursor = connection.cursor(dictionary=True)

        # SQL query with parameter
        query = """
        SELECT id, name, study_hours, attendance,
               previous_score, final_score
        FROM students
        WHERE id = %s
        """

        # Execute query
        cursor.execute(query, (student_id,))

        # Retrieve one student
        student = cursor.fetchone()

        # Check whether student exists
        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student

    except mysql.connector.Error as e:
        print("MYSQL ERROR:", e)
        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
from pydantic import BaseModel, Field
class StudentCreate(BaseModel):

    name: str

    study_hours: float = Field(ge=0)

    attendance: float = Field(ge=0, le=100)

    previous_score: float = Field(ge=0, le=100)

    final_score: float = Field(ge=0, le=100)


@app.post("/students", status_code=201)
def add_student(student: StudentCreate):

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()

        query = """
        INSERT INTO students
        (name, study_hours, attendance, previous_score, final_score)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            student.name,
            student.study_hours,
            student.attendance,
            student.previous_score,
            student.final_score
        )

        cursor.execute(query, values)

        connection.commit()

        return {
            "message": "Student added successfully",
            "student_id": cursor.lastrowid
        }

    except mysql.connector.Error as e:
        print("MYSQL ERROR:", e)

        if connection:
            connection.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


# PUT API: Update student details

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()

        # Check whether student exists
        cursor.execute(
            "SELECT id FROM students WHERE id = %s",
            (student_id,)
        )

        existing_student = cursor.fetchone()

        if existing_student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        # Update student details
        query = """
        UPDATE students
        SET name = %s,
            study_hours = %s,
            attendance = %s,
            previous_score = %s,
            final_score = %s
        WHERE id = %s
        """

        values = (
            student.name,
            student.study_hours,
            student.attendance,
            student.previous_score,
            student.final_score,
            student_id
        )

        cursor.execute(query, values)
        connection.commit()

        return {
            "message": "Student updated successfully",
            "student_id": student_id
        }

    except mysql.connector.Error as e:
        print("MYSQL ERROR:", e)

        if connection:
            connection.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


# DELETE API: Delete a student by ID

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()

        # Check whether student exists
        cursor.execute(
            "SELECT id FROM students WHERE id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        # Delete student
        query = "DELETE FROM students WHERE id = %s"

        cursor.execute(query, (student_id,))

        connection.commit()

        return {
            "message": "Student deleted successfully",
            "student_id": student_id
        }

    except mysql.connector.Error as e:
        print("MYSQL ERROR:", e)

        if connection:
            connection.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
    
