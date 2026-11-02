from typing import Callable, Optional
#E1.1 inner variable it disappears unless we save it
#E1.2
def welcome(name:str)->str:
    message = "Welcome " + name
    return message
result = welcome("Dana")
print(result)
print(result)

#E2 only the first is local because a local var was locally defined
# the others just did a reference without assignment
x = "global"

def first():
    x = "local in first"
    print("1:", x)

def second():
    print("2:", x)

first()
second()
print("3:", x)
#E3 a local_unbound_error because of the equal sign which references a local variable
# but then the assignment references  the uncreated variable
def add_one(count:int|float)->int|float:
    return count + 1

count = 0
count = add_one(count)
print(count)

#E4 builtin function overridden by local
items:list[int] = [1, 2, 3]
numbers:list[int] = list(range(5))
print(items, numbers)

#E5
def add(cart:list[int|float], price:int|float)->list[int|float]:
    cart.append(price)
    return cart

def cart_total(cart):
    return sum(cart)
cart = []
print(cart, cart_total(cart))
cart = add(cart, 100)
print(cart, cart_total(cart))
cart = add(cart, 50)
print(cart, cart_total(cart))