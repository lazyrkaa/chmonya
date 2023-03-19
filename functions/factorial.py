# Написать программу поиска наименьшего положительного числа n,
# факториал которого не делится нацело на сумму цифр самого факториала. На-
# пример, 6 не является таким числом, потому что 6! = 720, а 720 нацело делится
# на 7 + 2 + 0 = 9.
def factorial (n):
    """factorial of n"""
    if n == 1:
        return 1
    return n*factorial(n-1)
def condition (k):
    a=0
    for i in str(factorial(k)):
        a+= int(i)
    if factorial(k) % a == 0:
        a=0
        condition(k+1)
    else:
        print('We won! the number is {}'.format(k))
condition(1)
