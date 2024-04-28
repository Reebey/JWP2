from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Inicjalizacja bazy danych SQLAlchemy
engine = create_engine('sqlite:///school.sqlite')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Definicja modelu Student
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    grade = Column(Float)

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)

# CRUD Operations

# Dodanie nowego studenta
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    grade = data.get('grade')
    if name and age and grade:
        session = Session()
        new_student = Student(name=name, age=age, grade=grade)
        session.add(new_student)
        session.commit()
        session.close()
        return jsonify({'message': 'Student added successfully'}), 201
    else:
        return jsonify({'error': 'Missing data in request'}), 400

# Pobieranie danych studenta po ID
@app.route('/get_student/<int:id>', methods=['GET'])
def get_student(id):
    session = Session()
    student = session.query(Student).filter_by(id=id).first()
    session.close()
    if student:
        return jsonify(student.__dict__), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

# Aktualizacja danych studenta po ID
@app.route('/update_student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    name = data.get('name')
    age = data.get('age')
    grade = data.get('grade')
    session = Session()
    student = session.query(Student).filter_by(id=id).first()
    if student:
        if name:
            student.name = name
        if age:
            student.age = age
        if grade:
            student.grade = grade
        session.commit()
        session.close()
        return jsonify({'message': 'Student updated successfully'}), 200
    else:
        session.close()
        return jsonify({'error': 'Student not found'}), 404

# Usunięcie studenta po ID
@app.route('/delete_student/<int:id>', methods=['DELETE'])
def delete_student(id):
    session = Session()
    student = session.query(Student).filter_by(id=id).first()
    if student:
        session.delete(student)
        session.commit()
        session.close()
        return jsonify({'message': 'Student deleted successfully'}), 200
    else:
        session.close()
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
