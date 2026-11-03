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



