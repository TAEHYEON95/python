#리스트에 요소 추가하기: append(), insert()
#리스트를 선언합니다.
list_a= [1,2,3]

#리스트뒤에 요소 추가하기
print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)

#리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기 ")
list_a.insert(1,10)
print(list_a)

list_a.extend([4,5,6])
print(list_a)