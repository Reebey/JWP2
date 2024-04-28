from typing import List
from typing import Optional
from sqlalchemy import *
from sqlalchemy.orm import *

# Stwórz tabelę o nazwie 'students', która zawiera kolumny '
# id' (Integer, Primary Key),
# 'name' (String),
# 'age' (Integer)
# ‘grade’ (Float).
class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]
    grade: Mapped[float]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, age={self.age!r}, grade={self.grade!r})"

engine = create_engine('sqlite:///school.sqlite')
connection = engine.connect()
Base.metadata.create_all(engine)


# Dodaj do tabeli trzech studentów.
with Session(engine) as session:
     students = [ 
        Student(name="Adam Malysz", age=16, grade=5),
        Student(name="Kasia Mostowiak", age=15, grade=3),
        Student(name="Paulina Rydecka", age=15, grade=4.5)
     ]
     session.add_all(students)
     session.commit()

# Napisz zapytanie, które wybiera wszystkich studentów z tabeli i wypisze ich na ekran
students = connection.execute(select(Student)).fetchall()
print(students)