"""
24 game
given 4 numbers
output: all possible ways to use these 4 numbers to get the number 24
allowed operations: +,-,*,/
"""
from itertools import permutations
from itertools import product

#permutations of numbers
def permutate_nums(nums):
    perm_num = permutations(nums)
    return list(perm_num)

#cartesian product of operations
def permutate_ops():
    ops = ['+', '-', '*', '/']
    perm_ops = product(ops, repeat=3)
    return list(perm_ops)


def main():
    numbers = input().split()
    expressions = []
    solutions = []
    list_ops = permutate_ops()
    list_nums = permutate_nums(numbers)

    #list of all possible expressions
    for item in list_ops:
        for perm in list_nums:
            expr = (str(perm[0]) + item[0] + str(perm[1]) + item[1] + str(perm[2]) + item[2] + str(perm[3]))
            expressions.append(expr)

    #evaluates all expressions
    for value in expressions:
        if eval(value) == 24:
            solutions.append(value)
    if solutions == []:
        print('yeah... as it may suck, there is no way to shuffle these numbers and mathematical operations to get the number 24')
    for solution in solutions:
        print(solution)

#still not one hundred percent sure, why is this used, but it is, so...
if __name__ == '__main__':
    main()

