import os

APP_NAME = "OASIS Demo"
DB_USER = "admin"
DB_PASSWORD = "admin123"
API_KEY = "sk-demo-123456"

def connect_database():
    print(f"Connecting as {DB_USER}")
    print("Database connection established")

def get_api_key():
    return API_KEY

def main():
    print(APP_NAME)
    connect_database()
    print(get_api_key())

if __name__ == "__main__":
    main()
