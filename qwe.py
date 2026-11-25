import os

username = input("Enter username: ")

# To prevent SQL injection, always use parameterized queries with your database driver.
# Manual escaping, as shown below, is error-prone and should only be used if
# parameterized queries are absolutely not an option (e.g., for logging/debugging a *safe* string).
# For actual database interaction, use placeholders like '?' or '%s' and pass parameters separately.
sanitized_username = username.replace("'", "''")
query = "SELECT * FROM users WHERE username = '" + sanitized_username + "'"

# Sensitive data like passwords should not be hardcoded.
# Load from environment variables, a secrets manager, or a secure configuration system.
# Example: password = os.getenv("DB_PASSWORD")
# The hardcoded password has been removed.

print(query)