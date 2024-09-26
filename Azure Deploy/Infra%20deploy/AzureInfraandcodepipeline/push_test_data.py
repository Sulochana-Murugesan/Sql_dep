import mysql.connector
import os
import random
import string
from datetime import datetime, timedelta

def generate_random_data(num_records):
    data = []
    job_titles = ["Engineer", "Manager", "Analyst", "Clerk", "Technician"]
    for _ in range(num_records):
        first_name = ''.join(random.choices(string.ascii_letters, k=7))
        last_name = ''.join(random.choices(string.ascii_letters, k=10))
        job_title = random.choice(job_titles)
        hire_date = datetime.now() - timedelta(days=random.randint(1, 3650))
        salary = round(random.uniform(30000, 120000), 2)
        data.append((first_name, last_name, job_title, hire_date, salary))
    return data

def push_test_data():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_SERVER'),
        database=os.getenv('MYSQL_DATABASE'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD')
    )

    cursor = connection.cursor()
    test_data = generate_random_data(1000)

    cursor.executemany("""
        INSERT INTO Employee (FirstName, LastName, JobTitle, HireDate, Salary)
        VALUES (%s, %s, %s, %s, %s)
    """, test_data)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    push_test_data()
