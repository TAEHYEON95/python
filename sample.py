# print ("3 + 4 = " + str(3+4))

# print ("3 + 4 = {}".format(3+4))

# print ("{}".format(10))

# print(f'{10}')

# print(f"3+4 ={3+4}")

# print("{},{}".format(52,type(273)))

# a = "hello"

# print(a.upper())

#a = int(input("> 1번째 숫자: "))
#b = input("> 2번째 숫자: ")
#print()


# z,j,a = map(int,input().split())
# print(z[0])
# for i in z:
#     print(i)
#1print("{} + {} = {}".format(a,b,int(a)+int(b)))

#print("{} + {} = {}".format(a,b,int(a+b)))

# a = int(input("> 1번째 숫자: "))
# b = int(input("> 2번째 숫자: "))

# if a > b:
#     print(f"처음에 입력햇던 {a}가 {b} 보다 큽니다")

# if b > a :
#     print(f"두번째로 입력햇던 {b}가 {a}보다 더 큽니다")

# x = 10
# y = 2
# if x>4:
#     if y>2:
#         print(x*y)
# else:
#     print(x+y)

# x = 15
# if 10 < x < 20:
#     print("조건에 맞다")
# else:
#     print("조건 꺼져")

# print(1992 % 12)




# str_input = input("태어난 해를 입력해 주세요>")
# birth_year = int(str_input) % 12


# if 0 == birth_year:
#     print("원숭이 띠입니다")
# elif 1 == birth_year:
#     print("닭 띠입니다.")
# elif 2 == birth_year:
#     print("개 띠입니다.")
# elif 3 == birth_year:
#     print("돼지 띠입니다.")
# elif 4 == birth_year:
#     print("쥐 띠입니다.")
# elif 5 == birth_year:
#     print("소 띠입니다.")
# elif 6 == birth_year:
#     print("범 띠입니다.")
# elif 7 == birth_year:
#     print("토끼 띠입니다.")
# elif 8 == birth_year:
#     print("용 띠입니다.")
# elif 9 == birth_year:
#     print("뱀 띠입니다.")
# elif 10 == birth_year:
#     print("말 띠입니다.")
# elif 11 == birth_year:
#     print("양 띠입니다.")


# import datetime

#현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()

# hello = input("입력 : ")

# if hello in "안녕":
#     print("안녕하세요")
# elif hello in "안녕하세요":
#     print("안녕하세요")
# elif hello in "지금 몇 시야?":
#     print(now.hour,"입니다.")
# else:
#     print(hello)

# input_num = int(input("정수를 입력 하세여 : "))

# if input_num % 2 == 0:
#     print("나누어 떨어짐")
# else:
#     print(input_num,"은 2로 나누어 떨어지는 숫자가 아닙니다.")

# list_a = [0,1,2,3,4,5,6,7]
# list_a.extend(list_a)
# list_a.append(10)
# list_a.insert(3,0)
# list_a.remove(3)
# list_a.pop(3)
# list_a.clear()
# print(list_a)

# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# for number in numbers:
#     if 100 < number:
#         print("- 100 이상의 수:", number)

# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# print(len(str(numbers[0])))
# print(len(numbers))

# for number in numbers:
#     if number % 2 == 0:
#         print (number,"짝수 입니다.")
#     else:
#         print (number,"홀수 입니다.")

# for number in numbers:
#     if len(str(number)) == 1:
#         print (number,"는 1 자릿수 입니다.")
#     elif len(str(number)) == 2:
#         print (number,"는 2 자릿수 입니다.")
#     else:
#         print (number,"는 3 자릿수 입니다.")

# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]

# for number in numbers:
#     output[(number+2)% 3].append(number)
# print(output)

# numbers = [1,2,3,4,5,6,7,8,9]

# for i in range(0, len(numbers) // 2):
#     j = i * 2 + 1
#     print (f"i = {i},j = {j}")
#     numbers[j] = numbers[j] ** 2

# print(numbers)

# dict_a = {}

# print (dict_a)
# dict_a["name"] = "구름"
# print(dict_a)

# del dict_a["name"]

# print(dict_a)

# pets = [
#     {"name": "구름", "age": 5},
#     {"name": "초코", "age": 3},
#     {"name": "아지", "age": 1},
#     {"name": "호랑이", "age": 1}
# ]
# print("#우리 동네 애완 동물들")
# for key in pets:
#     print(key["name"], str(key["age"]) + "살")

#다음 빈칸을 채워서 numbers 내부에 들어 있는 숫자가 몇번 등장하는지를 출력 하시요 
# numbers = [1,3,4,2,4,5,8,5,3,2,5,6,8,9,6,4,3,1,3,3,4,5,6]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1
# print (counter)

character = {
    "name":"기사",
    "level":12,
    "items":{"sword":"불꽃의 검", "armor":"풀플레이트"},
    "skill":["베기","세게 베기", "아주 세게 베기"]
}
for key in character:


















# for key in character:
#     if type(character[key]) is dict:
#         for k in character[key] :
#             print("{} : {}".format(k,character[key][k]))
#             print(f"{k} : {character[key][k]}")
#     elif type(character[key]) is list:
#         for i in character[key] :
#             print(f"{key} : {i}")
#     else:
#         print(key,":",character[key])
