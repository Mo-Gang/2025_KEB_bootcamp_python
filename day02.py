# 구구단
# for dan in range (2, 10, 1): #2부터 10앞(9)까지 1씩 증가
#     for i in range (1, 10, 1):
#         print(f"{dan} * {i} = {dan*i}") #파이썬엔 중괄호 같은 거 없음; 들여쓰기

# 구구단(입력)
dan = int(input("Input dan :")) #JAVA와 다르게, 자동형변환이 안 된다
for i in range(1, 10, 1):
    print(f"{dan} * {i} = {dan * i}")


