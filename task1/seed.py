import psycopg2
from faker import Faker

def insert_data():
    fake = Faker()
    conn = None
    try:
        conn = psycopg2.connect(database="yourdbname", user="yourusername", password="yourpassword")
        cur = conn.cursor()
        
        # Insert users
        for _ in range(10):
            cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fake.name(), fake.email()))

        # Insert status
        statuses = ['new', 'in progress', 'completed']
        for status in statuses:
            cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))

        # Insert tasks
        for _ in range(30):
            cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                        (fake.sentence(), fake.text(), fake.random_int(min=1, max=3), fake.random_int(min=1, max=10)))

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_data()