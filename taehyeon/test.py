# 현재 시간이 12시 부터 1시 이전이면 점심을 먹고
# 3시부터 4시 이거나 아프면 
# 휴식을 취하고 아니면 일을한다

# time = 12
# seek = True

# if 12 <= time < 1 and not seek:
#     print("점심")
# elif 3 <= time <= 4 or seek:
#     print("휴식을 취한다")
# else:
#     print("일")

# 반복문 while

# guest = 1
# while guest < 10:
#     print(f"손님이 {guest} 명 입니다.")
#     guest = guest + 1
#     if guest == 10:
#     print("손님이 꽉 찾음")

num = 1
while num <= 10:
    if num % 2 == 0:
        print(f"짝수{num}")
    else:
        print(f"홀수여{num}")
    num = num + 1