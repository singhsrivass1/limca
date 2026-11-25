# Define the SQL query with a placeholder for the username.
# The specific placeholder syntax depends on your database driver (e.g., '?' for sqlite3, '%s' for psycopg2).
# For demonstration, we'll use '?' as a common placeholder.
sql_query_template = "SELECT * FROM users WHERE username = ?"

# In a real application, you would execute this query using your database cursor:
# import sqlite3 # Example import for a database driver
# conn = sqlite3.connect(':memory:') # Example connection
# cursor = conn.cursor()
# cursor.execute(sql_query_template, (username,))
# results = cursor.fetchall()

# Since the original code only printed the query string, we will print the template
# and the parameter that would be passed. This clearly separates the SQL structure
# from the user-provided data, demonstrating the secure approach.
print(f"SQL Query Template: {sql_query_template}")
print(f"Parameter to be bound: '{username}'")

# Sensitive data like passwords should not be hardcoded.
# If a password is required for database connection, retrieve it securely
# from environment variables, a secrets manager, or a secure configuration system.
# Example: db_password = os.getenv("DB_PASSWORD")
# The hardcoded password has been removed from the original code, which is a positive change.