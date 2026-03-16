from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
import schema
import model

app = FastAPI()

def get_db():
    db = database.session()
    try:
        yield db
    finally:
        db.close()


# Add Student
@app.post('/add_student', response_model=model.StudentCreate)
def add_student(student: model.StudentCreate, db: Session = Depends(get_db)):
    db_student = schema.Student(**student.model_dump())
    if db.query(schema.Student).filter(schema.Student.email == db_student.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    if db.query(schema.Student).filter(schema.Student.name == db_student.name).first():
        raise HTTPException(status_code=400, detail="Name already exists")
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
    
# View Students
@app.get('/view_students', response_model=list[model.Student])
def view_students(db:Session=Depends(get_db)):
    if not db.query(schema.Student).first():
        raise HTTPException(status_code=404, detail="No students found")
    return db.query(schema.Student).all()

@app.get('/view_students/filter/{student_id}', response_model=list[model.Student])
def view_student_by_id(student_id: int, db:Session=Depends(get_db)):
    db_student = db.query(schema.Student).filter(schema.Student.id==student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return db_student

# Update Student Grade
@app.put('/update_student_grade/{student_id}', response_model=model.Student)
def update_student_grade(new_grade: str, student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(schema.Student).filter(schema.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.grade = new_grade
    db.commit()
    db.refresh(db_student)
    return db_student


# Delete Student
@app.delete('/delete_student/{student_id}')
def delete_student(student_id:int, db:Session=Depends(get_db)):
    db_student = db.query(schema.Student).filter(schema.Student.id==student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="No students found")
    db.delete(db_student)
    db.commit()
    return "Student Deleted"