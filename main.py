from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="Jamila Karim", grade=3),
    Student(id=2, name= "Ali Sami", grade=2),
    Student(id=3, name= "Said Rami", grade=4),
    Student(id=4, name= "Fatma Adil", grade=3)
]

@app.get("/students")
async def fetch_students():
    return students

@app.post("/students")
async def register_student(newStudent: Student):
    students.append(newStudent)
    return {"id": newStudent.id}

@app.put("/students/{student_id}")
async def update_student(student: Student, student_id: int):
    for index, existing_student in enumerate(students):
        if existing_student.id == student_id:
            students[index] = student
            return student
    raise HTTPException(
        status_code=404,
        detail=f"Student with id: {student_id} does not exist"
    )

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for index, existing_student in enumerate(students):
        if existing_student.id == student_id:
            del students[index]
            return {"message": "User deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"Student with id: {student_id} does not exist"
    )