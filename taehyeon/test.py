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

# num = 1
# jjak = 0
# hol = 0

# while num <= 10:
#     if num % 2 == 0:
#         print(f"짝 {num}")
#         jjak += num
#     else:
#         print(f"홀 {num}")
#         hol += num
#     num = num + 1

# print (f"짝{jjak} 합", f"홀{hol} 합")

# num = 1
# hap = 0
# while num <= 100:
#     hap += num
#     num += 1
# print(hap)

# 반복문 for

# a = [ [1,2,3,4,5], ["a","b","c","d"], [11,12,13,14] ]
# for i in a:
#     print (i)
    # for j in i:
        # print (j)
        # for k in j:
        #     print (k)

# student = [{"홍길동":100},{"가제트":200},{"가가멜": 300}]

# for s, i in enumerate(student):
#     data = (list(i.items())[0])
#     name = data[0]
#     value = data[1]
#     print (f"{s+1}. 이름은 {name} 이고 점수는 {value} 이다")
# enumerate 요소 앞에 카운팅 부여 가능 

#예시
# msg = "python programming"
# for s, i in enumerate(msg, start=1 ):
#     print (s,i)

# #구구단
# for i in range(2,10):
#     for j in range(1,10):
#         val = i * j
#         print (f"{i} x {j} = {val}")

# #구구단 컴프리핸션
# gugudan = [f"{i} x {j} = {i*j}" for i in range(2,10) for j in range(1,10)]
# print (gugudan)

# 반복문 while, for
# num = 0
# while True:
#     print(num)
#     num += 1 
#     if num == 10:
#         break

# num = 0
# while num < 10:
#     num += 1 
#     if num == 5:
#         continue
#     print(num)

# user = input("사용자이름 입력>:")
# print(user)

# num1 = int(input("숫자1"))
# num2 = int(input("숫자2"))
# print(num1 + num2)

# langs = ["한국어", "Enlgish"]
# for i, l in enumerate(langs, start=1):
#     print(f"{i}.{l}")

# while True:
#     sel = (input("언어를 입력하세요 : "))
    
#     if not sel.isnumeric():
#         continue
#     sel = int(sel)
#     if 0 < sel < 3:
#         break
# print(f"사용자가 선택한 언어는 {langs[sel-1]}")


# 입력한 숫자가 소수인지
'''
while True:
    num = input("2 이상의 숫자를 입력 하세요> ")
    if not num.isnumeric(): # num 이 입력 받은 값이 숫자가 아니라면 
        continue # 돌아간다 
    num = int(num) # num에 입력 받은 값을 문자열이 아닌 숫자형으로 캐스팅한다.
    if num < 2: # num 의 값이 2 보다 작으면
        continue # 돌아간다
    break # 빠져나옴 

isprime = True
for n in range(2, num): # n에 2부터 num 입력 받은 값 까지 
    if num % n == 0: # ex) num 값에 10을 입력했을 때 2,3,4,5,6,7,8,9 의 숫자가 각각 10을 나눠본다
        isprime = False # 위 조건문을 판단하기 위한 변수
        break

if isprime:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")
'''

while True:
    num = input("2 이상의 숫자를 입력 하세요> ")
    if not num.isnumeric(): # num 이 입력 받은 값이 숫자가 아니라면 
        continue # 돌아간다 
    num = int(num) # num에 입력 받은 값을 문자열이 아닌 숫자형으로 캐스팅한다.
    if num < 2: # num 의 값이 2 보다 작으면
        continue # 돌아간다
    break # 빠져나옴 

prime_list = [False,False] + [True] * (num -1) 
# num이 5라면 F:F:T:T:T:T
prims = []

for i in range(2, num + 1): #num이 5라면 2 ~ 6
    if prime_list[i]: #F:F:T:T:T:T
        for j in range(2 * i, num + 1, i):
            prime_list[j] = False

prims = [i for i in range(2, num+1) if prime_list[i] == True]
print(prims)

if num in prims:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")

