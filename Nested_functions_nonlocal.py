from typing import Callable
#E1
def format_receipt(items:list[tuple[str,int|float]])->str:    
    def line(name:str, price:int|float):
        return name.ljust(10) + str(price)

    lines:list = []
    for name, price in items:
        lines.append(line(name, price))
    return "\n".join(lines)

print((format_receipt([("Milk", 6), ("Bread", 9)])))

#E2
def make_greeter(greeting:str)->Callable:
    def greet(name:str):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
shalom = make_greeter("Shalom")
print(hello("Dana"))
print(shalom("Avi"))

#E3
def outer():
    message = "outer"

    def show():
        print("show:", message)

    def change():
        nonlocal message #changes the outer scope
        message = "changed"

    show()# message prints outer the first time
    change() # changes message to "change"
    show() #prints the changed message

outer()