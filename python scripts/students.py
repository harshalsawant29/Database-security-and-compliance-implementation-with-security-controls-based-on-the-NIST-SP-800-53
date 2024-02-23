from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Function to generate a random date within a specified range
def random_date(start_date, end_date):
    return fake.date_time_between(start_date, end_date)

# Number of entries
num_entries = 1100

# Generate unique email addresses
email_set = set()
while len(email_set) < num_entries:
    email_set.add(fake.email())

# Create SQL insert statements
insert_statements = []
for i, email in enumerate(email_set, start=1):
    student_name = fake.name()
    enrollment_date = random_date(datetime(2022, 1, 1), datetime(2023, 11, 28))
    insert_statements.append(
        f"({i}, '{student_name}', '{email}', '{enrollment_date.strftime('%Y-%m-%d')}')"
    )

# Write SQL script to a file
with open("insert_script.sql", "w") as sql_file:
    sql_file.write("INSERT INTO Students (student_id, student_name, email, enrollment_date) VALUES\n")
    sql_file.write(",\n".join(insert_statements))

print("SQL script generated successfully.")

