from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Function to generate a random date within a specified range
def random_date(start_date, end_date):
    return fake.date_time_between(start_date, end_date)

# Number of entries
num_entries = 1100

# Generate unique student and course IDs
student_ids = list(range(1, 1101))  # Assuming Students table has 1100 entries
course_ids = list(range(1, 51))  # Assuming Courses table has 50 entries

# Shuffle the IDs to randomize the assignments
random.shuffle(student_ids)
random.shuffle(course_ids)

# Create SQL insert statements
insert_statements = []
for i in range(num_entries):
    student_id = student_ids[i % len(student_ids)]
    course_id = course_ids[i % len(course_ids)]
    enrollment_date = random_date(datetime(2022, 1, 1), datetime(2023, 11, 28))
    insert_statements.append(
        f"({i+1}, {student_id}, {course_id}, '{enrollment_date.strftime('%Y-%m-%d')}')"
    )

# Write SQL script to a file
with open("enrollments_insert_script.sql", "w") as sql_file:
    sql_file.write("INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES\n")
    sql_file.write(",\n".join(insert_statements))

print("Enrollments SQL script generated successfully.")

