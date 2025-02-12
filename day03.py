# day03 Assignment2
# 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정하시오.
import random
drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]

drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[1]}에 어울리는 안주는 {snacks[1]} 입니다')
    elif menu == '3':
        print(f'{drinks[2]}에 어울리는 안주는 {snacks[2]} 입니다')
    elif menu == '4':
        print(f'{drinks[3]}에 어울리는 안주는 {snacks[3]} 입니다')
    elif menu == '5':
        print(f'{drinks[4]}에 어울리는 안주는 {snacks[4]} 입니다')
    elif menu == '6':
        random_index = random.randint(0, len(drinks)-1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break