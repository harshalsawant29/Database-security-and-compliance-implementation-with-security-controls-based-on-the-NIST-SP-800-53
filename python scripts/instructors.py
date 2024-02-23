from faker import Faker
import random

fake = Faker()

# Number of instructors
num_instructors = 40

# Generate unique instructor IDs
instructor_ids = list(range(1, num_instructors + 1))

# Create SQL insert statements
insert_statements = []
for instructor_id in instructor_ids:
    instructor_name = fake.name()
    expertise_area = fake.job()
    insert_statements.append(
        f"({instructor_id}, '{instructor_name}', '{expertise_area}')"
    )

# Write SQL script to a file
with open("instructors_insert_script.sql", "w") as sql_file:
    sql_file.write("INSERT INTO Instructors (instructor_id, instructor_name, expertise_area) VALUES\n")
    sql_file.write(",\n".join(insert_statements))

print("Instructors SQL script generated successfully.")

