from typing import Callable

#E1

def apply_to_all(numbers:list[int|float], action:Callable)->list[int|float]:
    result:list[int|float] = []
    for n in numbers:
        result.append(action(n))
    return result


def double(n:int|float)->int|float:
    return n * 2


print(apply_to_all([1, 2, 3], double))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], round))

#E2
prices:list[int|float] = [20, 75, 120, 45, 90]

expensive = list(filter(lambda p: p > 50, prices))
inflated = list(map(lambda p: p + 10, expensive))
print(expensive)
print(inflated)

#E3
words:list[str] = ["banana", "fig", "cherry", "kiwi"]
students:list[tuple[str,int|float]] = [("Dana", 92), ("Avi", 78), ("Noa", 85)]

print(sorted(words, key=len))
print(max(words, key=len))

for name, grade in sorted(students, key=lambda s: s[1], reverse=True):
    print(name)
