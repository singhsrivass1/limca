def greet_user(name):
    name = name.strip()

    if not name:
        return "Hello, Guest!"

    return f"Hello, {name}!"


def main():
    print(greet_user("Shreya"))


if __name__ == "__main__":
    main()
