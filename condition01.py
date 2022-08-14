# number = int(input("정수 입력 > "))

# number_a = number%2 


# if number_a == 1 :
#     print("홀수 입니다.")

# if number_a <= 0 :
#     print("짝수 입니다.")

#입력을 받습니다.
number = input("정수 입력")

#마지막 자리 숫자를 추출
last_character = int(number[-1])

if last_character == 0 \
    or last_character == 2 \
    or last_character == 4 \
    or last_character == 6 \
    or last_character == 8:
    print("짝수 입니다.")


if last_character == 1 \
    or last_character == 3 \
    or last_character == 5 \
    or last_character == 7 \
    or last_character == 9:
    print("홀수 입니다.")



