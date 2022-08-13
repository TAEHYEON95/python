# 문자열을 숫자로 바꾸기 

#int() 함수 : 문자열을 int 자료형으로 변환 합니다. int는 정수형을 의미 합니다.
#float() 함수 : 문자열을 float 자료형으로 변환합니다. float는 실수형 또는 부동소수점을 의미 합니다.

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료", string_a + string_b)
print("숫자 자료", int_a + int_b) 