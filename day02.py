# 구구단
# for dan in range (2, 10, 1): #2부터 10앞(9)까지 1씩 증가
#     for i in range (1, 10, 1):
#         print(f"{dan} * {i} = {dan*i}") #파이썬엔 중괄호 같은 거 없음; 들여쓰기

# 구구단(입력)
# dan = int(input("Input dan :")) #JAVA와 다르게, 자동형변환이 안 된다
# for i in range(1, 10, 1):
#     print(f"{dan} * {i} = {dan * i}")




# 소수 판단
# n = int(input("Input number : "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#          count = count + 1
#
# if count == 2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is NOT prime number!")


# 속도를 올리려면,
# 루트를 활용.

# JAVA의 경우, (핵심만 정리)
# for(int i=2; i<=Math.sqrt(num)l i++){
#     if(num % i ==0){
#         return false;
#     }
#     System.out.print(i + "")
#     }
# return true;
# }
# }

# Python, By Professor
n = int(input("Input number : "))
is_prime = True
if n >= 2:
    #for i in range(2, n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False  #count = count + 1
            break
        print(i, end=' ')
else:
    is_prime = False

#if count == 0:
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")
