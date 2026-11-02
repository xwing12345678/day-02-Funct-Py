info = {"title":"MR.","age":25,"city":"haifa"}
#E1
def make_greeting(name,greeting:str ="hello", punctuation="!"):

    return f"{greeting} {name}{punctuation}"

print(make_greeting("Dana"))
print(make_greeting("Avi", "Good morning"))
print(make_greeting("Noa", punctuation="?"))

prices = [20,75,120,90,45]
expensive = list(filter(lambda price : price>100 ,prices))

