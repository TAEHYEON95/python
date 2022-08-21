#리스트에 요소 제거하기
#인덱스로 제거하기 , 값으로 제거하기 

#인덱스로 제거하기 : del 키워드, pop()
# del 리스트명[인덱스]
# 리스트명.pop(인덱스)

list_a = [0,1,2,3,4,5]
print("#리스트의 요소 하나 제거하기")
#제거 방법[1] - del 키워드
del list_a[1]
print("del list_a[1]:", list_a)

# 제거 방법[2] - pop()
list_a.pop(2)
print("pop(2):", list_a)

list_a.pop()
print("pop():", list_a)


#리스트 슬라이싱
# 리스트[시작_인덱스:끝_인덱스:단계]
num = [3,7,0,9,7,8,3,4,5]
num[2:7:2]
print(num[2:7:2])

#값으로 제거하기
# 리스트.remove(값)
list_c = [1,2,1,2] #리스트 선언
list_c.remove(2)
print(list_c)

#모두 제거하기: clear()
# 리스트.clear()
list_d = [0,1,2,3,4,5]
list_d.clear()
print(list_d)

#리스트 정렬하기: sort()
#리스트.sort()
list_e = [52,273,103,32,275,1,7]
list_e.sort() # 오름차순 정렬
print(list_e)
list_e.sort(reverse=True) # 내림차순 정렬  
print(list_e)

#리스트 내부에 있는지 확인하기 : in/not in 연산자
# 값 in 리스트

list_a = [273,32,103,57,52]
print(273 in list_a)
print(99 in list_a)
print(52 in list_a)
print(273 not in list_a)
print(99 not in list_a)
print(52 not in list_a)



