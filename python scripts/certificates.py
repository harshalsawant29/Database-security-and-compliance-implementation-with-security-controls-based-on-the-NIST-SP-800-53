from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Number of certificates
num_certificates = 70

# Assuming you have 1100 students and 50 courses from previous scripts
student_ids = list(range(1, 1101))
course_ids = list(range(1, 51))

# Shuffle the student and course IDs to randomize the assignments
random.shuffle(student_ids)
random.shuffle(course_ids)

# Generate unique certificate IDs
certificate_ids = list(range(1, num_certificates + 1))

# Create SQL insert statements
insert_statements = []
for certificate_id in certificate_ids:
    student_id = student_ids[certificate_id % len(student_ids)]
    course_id = course_ids[certificate_id % len(course_ids)]
    issue_date = fake.date_between('-365d', 'today')
    
    insert_statements.append(
        f"({certificate_id}, {student_id}, {course_id}, '{issue_date.strftime('%Y-%m-%d')}')"
    )

# Write SQL script to a file
with open("certificates_insert_script.sql", "w") as sql_file:
    sql_file.write("INSERT INTO Certificates (certificate_id, student_id, course_id, issue_date) VALUES\n")
    sql_file.write(",\n".join(insert_statements))

print("Certificates SQL script generated successfully.")

