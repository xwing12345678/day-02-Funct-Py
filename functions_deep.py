from typing import Any
#E1
def make_greeting(name,greeting:str ="Hello", punctuation="!"):
    return f"{greeting} {name}{punctuation}"

print(make_greeting("Dana"))
print(make_greeting("Avi", "Good morning"))
print(make_greeting("Noa", punctuation="?"))

#E2
def average(*numbers:float|int)->float:
    if len(numbers) == 0:
        raise ValueError("need at least one number")
    return sum(numbers) / len(numbers)

print(average(80, 90))
print(average(70, 80, 90, 100))

try:
    average()
except ValueError as error:
    print("error:", error)

#E4
def format_profile(name:str, **details: Any)->str:
    line = name + ":"
    for key, value in details.items():
        line = line + " " + key + "=" + str(value)
    return line

print(format_profile("Dana", age=24, city="Haifa"))
print(format_profile("Avi"))

#E6
products:list[tuple[str,int]] = [("Laptop", 3500), ("Mouse", 80), ("Desk", 900)]

for name, price in sorted(products, key=lambda p: p[1]):
    print(name, price)

most_expensive = max(products, key=lambda p: p[1])
print("Most expensive:", most_expensive[0])

#E7
def add_item(item: Any, cart: list[Any] | None = None) -> list[Any]:
    if cart is None:
        cart = []
    cart.append(item)
    return cart

shopping_cart = add_item(item="Apple")
print(shopping_cart)

print(add_item("milk"))
print(add_item("bread"))