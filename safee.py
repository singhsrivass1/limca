def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Values cannot be negative")
    return price * quantity


def main():
    price = 100.0
    quantity = 5

    total = calculate_total(price, quantity)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
