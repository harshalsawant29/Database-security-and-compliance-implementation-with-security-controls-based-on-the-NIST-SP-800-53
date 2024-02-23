from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Number of assessments
num_assessments = 60

# Assuming you have 50 courses from the previous script
course_ids = list(range(1, 51))

# Shuffle the course IDs to randomize the assignments
random.shuffle(course_ids)

# Generate unique assessment IDs
assessment_ids = list(range(1, num_assessments + 1))

# Create SQL insert statements
insert_statements = []
for assessment_id in assessment_ids:
    assessment_name = fake.word()
    course_id = course_ids[assessment_id % len(course_ids)]
    max_score = random.randint(50, 100)
    assessment_date = fake.date_between('-30d', 'today')
    
    insert_statements.append(
        f"({assessment_id}, {course_id}, '{assessment_name}', {max_score}, '{assessment_date.strftime('%Y-%m-%d')}')"
    )

# Write SQL script to a file
with open("assessments_insert_script.sql", "w") as sql_file:
    sql_file.write("INSERT INTO Assessments (assessment_id, course_id, assessment_name, max_score, assessment_date) VALUES\n")
    sql_file.write(",\n".join(insert_statements))

print("Assessments SQL script generated successfully.")

