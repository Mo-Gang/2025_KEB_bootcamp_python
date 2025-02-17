# # 피보나치 수 계산함수


# 재귀함수 ver
def fibonacci_recursion(n) -> int:
    """
    피보나치 수 계산함수
    :param n:
    :return: 피보나치 계산 결과 값
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

# 반복문 ver
def fibonacci_loop(n) -> int:
    """
    피보나치 수 계산함수
    :param n:
    :return: 피보나치 계산 결과 값
    """
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]

n = int(input())
print(fibonacci_loop(n))
print(fibonacci_recursion(n))