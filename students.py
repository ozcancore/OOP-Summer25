# student_details_structure.py

students = [
    {
        "first_name": "Tomy",
        "last_name": "Doe",
        "index_number": 12345,
        "nationality": "Canadian",
        "starting_date": "2023-10-01",
        "courses": ["Mathematics", "Computer Science", "Physics"]
    },
    {
        "first_name": "tomy",
        "last_name": "doee",
        "index_number": 67890,
        "nationality": "American",
        "starting_date": "2023-09-15",
        "courses": ["Biology", "Chemistry", "Statistics"]
    },
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "index_number": 54321,
        "nationality": "British",
        "starting_date": "2023-11-01",
        "courses": ["History", "Literature", "Philosophy"]
    }
]
for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
