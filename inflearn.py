#파이썬 자료형 
# a = 10
# print(type(a))

#이스케이프 문자
# \n : 줄바꿈
# \t : 탭
# \\ : '\'(역슬래쉬)
# \' : '(따옴표)
# \" : "(쌍따옴표)

# a = 30
# b = 5.5
# print(f"나는 {a}살이고 100미터 달리기는 {b} 입니다.")
# print("나는 {}살이고 100미터 달리기는 {}초 입니다".format(a,b))


#파이썬 문자열 메서드 
# test = "abcd 가나다라마바사 하하하"
#문자 찾기 메서드 find,index
# print(test.find("가"))
# print(test.index("가"))
# #오류 반환 값이 틀림 
# print(test.find("zzz"))
# print(test.index("zzz"))

# #오른쪽 부터 찾기 rfind
# path = "c:\\test\\abcd\\abcd.jpg"
# print(path[path.rfind("\\") + 1:])

# # 짜르기 split
# print(path.split("\\")) 

# # 문자 치환 replace
# print(path.replace("c:\\test\\abcd\\abcd.jpg","hi"))

# #앞 뒤 공백지우기 strip
# a = "     test     "
# print(a.strip())

# # 대문자 upper() 변환 소문자 lower() 변환
# b = "aaAAbbBBccCC"
# print(b.upper())
# print(b.lower())

# # 문자 수 세기
# c = "aaabbbcccddddd"
# print(c.count("a") , c.count("ccc"))

# # 문자열의 총 길이 len
# print(len(c))

# # 문자열이 영어인지 확인하는 함수 isalpha()
# d = "aa"
# e = "12"
# print (d.isalpha(), e.isalpha())

# dir(str)
# print(dir(str))

#2
#파이썬 데이터 구조 
#리스트 함수
# append() 리스트 추가
# insert() 리스트 삽입
# del 인덱스 삭제
# remove(요소) 삭제
# pop(인덱스) 삭제 및 값 리턴
# extend() 리스트 확장
# sort() 정렬
# reverse() 역정렬

# print(dir(dict))

# casting
a = "10"
b = int(a)
print(type(b), type(a))
