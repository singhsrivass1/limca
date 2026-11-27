import os

APP_NAME = "OASIS Demo"
DB_USER = os.getenv("DB_USER", "default_user") # Use a non-privileged default if necessary, or raise error
DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")

def connect_database():
    if not DB_PASSWORD:
        raise ValueError("DB_PASSWORD environment variable not set.")
    print(f"Connecting as {DB_USER}")
    print("Database connection established")

def get_api_key():
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set.")
    return API_KEY

def main():
    print(APP_NAME)
    try:
        connect_database()
        print(get_api_key())
    except ValueError as e:
        print(f"Configuration Error: {e}")
        # Optionally, exit or handle the error gracefully

if __name__ == "__main__":
    main()