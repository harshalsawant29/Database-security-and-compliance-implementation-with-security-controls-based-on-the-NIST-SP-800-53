from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Number of courses
num_courses = 50

# Generate unique course IDs
course_ids = list(range(1, num_courses + 1))

# Assuming you have 40 instructors from the previous script
instructor_ids = list(range(1, 41))

# Shuffle the instructor IDs to randomize the assignments
random.shuffle(instructor_ids)

# Create SQL insert statements
insert_statements = []
for course_id in course_ids:
    course_name = fake.catch_phrase()
    instructor_id = instructor_ids[course_id % len(instructor_ids)]
    start_date = fake.date_between('-30d', 'today')
    end_date = start_date + timedelta(days=random.randint(30, 90))
    description = fake.text()
    
    insert_statements.append(
        f"({course_id}, '{course_name}', {instructor_id}, '{start_date.strftime('%Y-%m-%d')}', "
        f"'{end_date.strftime('%Y-%m-%d')}', '{description}')"
    )

# Write SQL script to a file
with open("courses_insert_script.sql", "w") as sql_file:
    sql_file.write("INSERT INTO Courses (course_id, course_name, instructor_id, start_date, end_date, description) VALUES\n")
    sql_file.write(",\n".join(insert_statements))

print("Courses SQL script generated successfully.")

