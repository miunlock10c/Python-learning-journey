def calculate_total(price: int, quantity: int, has_discount: bool):
    total = price * quantity

    if has_discount:
        total -= 10
    return total


print(calculate_total(price=15, quantity=2, has_discount=True))

name: str = "kirill"

