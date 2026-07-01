from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

def main() -> None:
    leah = Student("Leah", 24)
    print(f"Student: {leah.name}, Age: {leah.age}")

    tony = Student("Tony", 26)
    print(f"Student: {tony.name}, Age: {tony.age}")

    print(tony==leah)
    print(tony==Student("Tony", 26))

if __name__ == "__main__":
    main()