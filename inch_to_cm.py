#숫자를 입력 받습니다
raw_input = input("inch 단위의 숫자를 입력해주세요: ")

#입력받은 데이터를 숫자 자료형으로변경하고, cm 단위로 변경합니다.
inch = int(raw_input)
cm = inch * 2.54

#출력합니다.
print(inch, "int_number는 cm 단위로", cm,"cm입니다")

#원의 반지름을 입력 받아 원의 둘레의 넓이를 구하는 코드 
str_input = input("원의 반지름 입력>")
num_input = float(str_input)
print()
print("반지름:",num_input)
print("둘레:", 2 * 3.14 * num_input)
print("넓이:", 3.14 * num_input ** 2 )


#변수 swap 
a = input("문자열 입력 > ")
b = input("문자열 입력 > ")

print (a + b)

temp = a
a = b
b = temp

print (a + b)