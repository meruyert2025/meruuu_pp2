import psycopg2
import csv
import json

DB_USER = "postgres"
DB_PASSWORD = "M.m.2019"
DB_HOST = "localhost"
DB_NAME = "phonebook_db"

conn = psycopg2.connect(
    host=DB_HOST,
    database="postgres",
    user=DB_USER,
    password=DB_PASSWORD
)
conn.autocommit = True
cur = conn.cursor()

cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (DB_NAME,))
exists = cur.fetchone()
if not exists:
    cur.execute(f"CREATE DATABASE {DB_NAME};")
    print(f"База данных '{DB_NAME}' создана.")
else:
    print(f"База данных '{DB_NAME}' уже существует.")

cur.close()
conn.close()

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    phone VARCHAR(20) NOT NULL UNIQUE
)
""")
conn.commit()
print("Таблица 'phonebook' готова.")

def search_phonebook(pattern):
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_or_update_user(first_name, last_name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s, %s);", (first_name, last_name, phone))
    conn.commit()
    print("User inserted or updated.")

def insert_multiple_users(users_list):
    users_json = json.dumps(users_list)
    cur.execute("CALL insert_multiple_users(%s);", (users_json,))
    conn.commit()
    print("Multiple users inserted.")

def get_phonebook_page(limit_count, offset_count):
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit_count, offset_count))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user_by_name_or_phone(username_or_phone):
    cur.execute("CALL delete_user_by_name_or_phone(%s);", (username_or_phone,))
    conn.commit()
    print("User deleted.")

def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
                (row['first_name'], row['last_name'], row['phone'])
            )
    conn.commit()
    print("Данные из CSV вставлены.")

def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
        (first_name, last_name, phone)
    )
    conn.commit()
    print("Данные вставлены.")

def update_contact():
    phone = input("Введите номер, который хотите изменить: ")
    new_phone = input("Введите новый номер: ")
    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE phone=%s",
        (new_phone, phone)
    )
    conn.commit()
    print("Телефон обновлён.")

def search():
    text = input("Введите имя или телефон для поиска: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name=%s OR phone=%s",
        (text, text)
    )
    rows = cur.fetchall()
    if rows:
        for r in rows:
            print(r)
    else:
        print("Ничего не найдено.")

def delete_contact():
    text = input("Введите имя или номер для удаления: ")
    cur.execute(
        "DELETE FROM phonebook WHERE first_name=%s OR phone=%s",
        (text, text)
    )
    conn.commit()
    print("Контакт удалён.")

def show_all():
    cur.execute("SELECT * FROM phonebook ORDER BY user_id")
    rows = cur.fetchall()
    if rows:
        print("\n=== Все пользователи ===")
        for r in rows:
            print(f"ID: {r[0]}, Имя: {r[1]}, Фамилия: {r[2]}, Телефон: {r[3]}")
    else:
        print("Телефонная книга пуста.")

while True:
    print("\nMenu:")
    print("1) CSV Insert")
    print("2) Console Insert")
    print("3) Update contact")
    print("4) Search")
    print("5) Delete")
    print("6) Show all users")
    print("7) Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_from_csv("/Users/meruert/Desktop/python/meruuu_pp2/lab100/phonebook.csv")
    elif choice == "2":
        insert_from_console()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        search()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        show_all()
    elif choice == "7":
        break
    else:
        print("Invalid choice")

cur.close()
conn.close()
