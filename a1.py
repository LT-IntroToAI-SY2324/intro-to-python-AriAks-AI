"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    if (n<0):
        n = n*-1
    return n
    raise NotImplementedError("absolute")


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    x = n
    while n > 2:
        x = x*(n-1)
        
        n = n - 1
    print(x)
    return(x)
    raise NotImplementedError("factorial")


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    return lst[::2]

     
    raise NotImplementedError("every_other")


def sum_list(lst: List[int]) -> int:
    """
    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    total = 0
    for num in lst:
        total += num
    return total

    raise NotImplementedError("sum_list")


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    total = 0
    for num in lst:
        total += num

    print(total / len(lst))
    return(total / len(lst))


    raise NotImplementedError("mean")


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    lst.sort()
    n = len(lst)
    if n % 2 == 1:
        # If odd, return the middle element
        return lst[n // 2]
    else:
        # If even, return the average of the two middle elements
        middle1 = lst[(n // 2) - 1]
        middle2 = lst[n // 2]
        return (middle1 + middle2) / 2

    raise NotImplementedError("median")


def duck_duck_goose(lst: List[str]) -> List[str]:
    #BERGS ANSWER...
    i = 0 
    current = "duck1"
    while len(lst) >= 2:
        if current == "duck1":
            current == "duck2"
            i += 1
        elif current == "duck2":
            current = "goose"
            i += 1
        else:
            current = "duck1"
            lst.pop(i)

    #wrap back around
        i %= len(lst)
    return(lst)

# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")