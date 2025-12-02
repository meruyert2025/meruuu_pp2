import psycopg2
import csv

# ===== Параметры подключения =====
DB_USER = "postgres"
DB_PASSWORD = "M.m.2019"
DB_HOST = "localhost"
DB_NAME = "phonebook_db"

# ===== 1. Подключаемся к дефолтной базе, чтобы создать phonebook_db =====
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

# ===== 2. Подключаемся к phonebook_db =====
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()

# ===== 3. Создание таблицы =====
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


# ===== 4. Вставка данных из CSV =====
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


# ===== 5. Ввод с консоли =====
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


# ===== 6. UPDATE =====
def update_contact():
    phone = input("Введите номер, который хотите изменить: ")
    new_phone = input("Введите новый номер: ")
    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE phone=%s",
        (new_phone, phone)
    )
    conn.commit()
    print("Телефон обновлён.")


# ===== 7. SEARCH =====
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


# ===== 8. DELETE =====
def delete_contact():
    text = input("Введите имя или номер для удаления: ")
    cur.execute(
        "DELETE FROM phonebook WHERE first_name=%s OR phone=%s",
        (text, text)
    )
    conn.commit()
    print("Контакт удалён.")


# ===== 9. SHOW ALL USERS =====
def show_all():
    cur.execute("SELECT * FROM phonebook ORDER BY user_id")
    rows = cur.fetchall()
    if rows:
        print("\n=== Все пользователи ===")
        for r in rows:
            print(f"ID: {r[0]}, Имя: {r[1]}, Фамилия: {r[2]}, Телефон: {r[3]}")
    else:
        print("Телефонная книга пуста.")


# ===== 10. Меню =====
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
        insert_from_csv("phonebook.csv")
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
