def Collatz(num, count = 0):
    if num <= 1:
        return count
    if num % 2 == 0:
        return Collatz(num / 2, count + 1)
    else:
        return Collatz(num * 3 + 1, count + 1)