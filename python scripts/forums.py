from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Number of forum posts
num_forum_posts = 80

# Assuming you have 50 courses and 1100 students from previous scripts
course_ids = list(range(1, 51))
student_ids = list(range(1, 1101))

# Shuffle the course and student IDs to randomize the assignments
random.shuffle(course_ids)
random.shuffle(student_ids)

# Generate unique forum IDs
forum_ids = list(range(1, num_forum_posts + 1))

# Create SQL insert statements
insert_statements = []
for forum_id in forum_ids:
    course_id = course_ids[forum_id % len(course_ids)]
    topic = fake.sentence(nb_words=3)
    post_date = fake.date_between('-30d', 'today')
    author_id = student_ids[forum_id % len(student_ids)]
    content = fake.paragraph(nb_sentences=3)
    
    insert_statements.append(
        f"({forum_id}, {course_id}, '{topic}', '{post_date.strftime('%Y-%m-%d %H:%M:%S')}', {author_id}, '{content}')"
    )

# Write SQL script to a file
with open("forums_insert_script.sql", "w") as sql_file:
    sql_file.write("INSERT INTO Forums (forum_id, course_id, topic, post_date, author_id, content) VALUES\n")
    sql_file.write(",\n".join(insert_statements))

print("Forums SQL script generated successfully.")

