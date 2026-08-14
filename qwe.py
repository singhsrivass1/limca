username = input("Enter username: ")

# Vulnerable to SQL injection
query = "SELECT * FROM users WHERE username = '" + username + "'"

print(query)
