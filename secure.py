import os

APP_NAME = "OASIS Demo"

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")

def connect_database():
    if DB_USER and DB_PASSWORD:
        print("Database configuration loaded securely.")
    else:
        print("Database configuration is incomplete.")

def main():
    print(APP_NAME)
    connect_database()

    if API_KEY:
        print("API key loaded securely.")
    else:
        print("API key is not configured.")

if __name__ == "__main__":
    main()
