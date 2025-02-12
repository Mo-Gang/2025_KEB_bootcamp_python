# day03 Assignment5
# while 안쪽의 조건문을 줄이세요.

import random

drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]

drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"
drinks.append("데킬라")
snacks.append("소금")

def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {snacks[n]} 입니다')


menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}  '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료 : '

while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks):
        print_menu(menu - 1)
    elif menu == 6:
        random_index = random.randint(0, len(drinks)-1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
    elif menu == 7:
        print(f'다음에 또 오세요')
        break