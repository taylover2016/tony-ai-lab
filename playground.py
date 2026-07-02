from dataclasses import dataclass
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

def main() -> None:
    leah = Student(name="Leah", age=24)
    print(f"Student: {leah.name}, Age: {leah.age}")
    print(type(leah.age))

    tony = Student(name="Tony", age=26)
    print(f"Student: {tony.name}, Age: {tony.age}")

    print(tony==leah)
    print(tony==Student(name="Tony", age=26))

    print(tony.model_dump())
    print(type(tony.model_dump()))
    print(Student.model_validate(tony.model_dump()))

    print(tony.model_dump_json())
    print(type(tony.model_dump_json()))
    print(Student.model_validate_json(tony.model_dump_json()))


if __name__ == "__main__":
    main()