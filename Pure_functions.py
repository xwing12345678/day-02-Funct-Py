from typing import Sequence
#E1
def square(n): #pure,
    return n * n

def log_square(n): # impure, it outputs a print to the screen
    print("squaring", n)
    return n * n

def add_item(cart, item): # Impure, Mutates the list it was given because it uses a object method list.append
    cart.append(item)
    return cart

def with_item(cart, item): # Pure, unlike the previous one + plus is a inbuilt function that creates a new list
    return cart + [item]

#E2
def add_price(total:int|float, price:int|float):
    return total + price

total = 0
total = add_price(total, 10)
total = add_price(total, 10)
print(total)
print(add_price(0, 10))
print(add_price(0, 10))
#E3
TAX = 1.17
def apply_tax(prices:Sequence[int|float])->list[int]:
    result:list[int] = [round(price*TAX) for price in prices]
    return result

prices = [100, 50]
with_tax = apply_tax(prices)
print(prices)
print(with_tax)
print(prices)