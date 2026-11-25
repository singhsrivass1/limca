import os

username = input("Enter username: ")

# Define the SQL query with a placeholder for the username.
# Always use parameterized queries to prevent SQL injection.
# The specific placeholder syntax depends on your database driver (e.g., '?' for sqlite3, '%s' for psycopg2).
# For demonstration, we'll use '?' as a common placeholder.
sql_query_template = "SELECT * FROM users WHERE username = ?"

# In a real application, you would execute this query using your database cursor:
# import sqlite3 # Example import for a database driver
# conn = None # Initialize connection to None
# try:
#     conn = sqlite3.connect(':memory:') # Example connection
#     cursor = conn.cursor()
#     cursor.execute(sql_query_template, (username,))
#     results = cursor.fetchall()
#     print(f"Query executed successfully. Results: {results}")
# except Exception as e:
#     print(f"Database error: {e}")
# finally:
#     if conn:
#         conn.close()

# Since the original code only printed the query string, we will print the template
# and the parameter that would be bound. This clearly separates the SQL structure
# from the user-provided data, demonstrating the secure approach without actual DB connection.
print(f"Secure SQL Query Template: {sql_query_template}")
print(f"Parameters to be bound: ('{username}',)") # Represent as a tuple for binding

# If a password is required for database connection, retrieve it securely
# from environment variables, a secrets manager, or a secure configuration system.
# Example: db_password = os.getenv("DB_PASSWORD")
# The hardcoded password has been removed from the original code, which is a positive change.
