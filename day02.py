#Ex2) while 구문으로 구간 소수를 출력하는 프로그램을 작성

def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while i < (int(num ** 0.5) + 1):
        #for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

# main
#help(abs)
#help(is_prime)
numbers = input("Input number : ").split()  # 900 1000
n1 = int(numbers[0])
n2 = int(numbers[1])

# if n1 > n2:
#     temp = n1
#     n1 = n2
#     n2 = temp

if n1 > n2:
    n1, n2 = n2, n1

j = n1
while j <= n2:
    if is_prime(j):
        print(j, end=' ')
    j = j + 1