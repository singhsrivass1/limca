def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Invalid input")

    return price * quantity


def main():
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = calculate_total(price, quantity)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
