username = input("Enter username: ")

# Using parameterized query approach to prevent SQL injection (OWASP A03:2021-Injection, CWE-89).
# In a real application, the query template and parameters would be passed to a database driver's execute method.
# Example: cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
# For the purpose of demonstrating the secure query construction while maintaining the original
# intent of printing a string, we represent the parameterized query.
query_template = "SELECT * FROM users WHERE username = %s"
query_parameters = (username,)

# This string representation demonstrates the secure query structure.
# It is NOT the final SQL string that would be sent to the database,
# but rather how the query and its parameters would be handled separately.
query_output_string = f"Secure Query Template: '{query_template}', Parameters: {query_parameters}"

print(query_output_string)