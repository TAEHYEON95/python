#다양한 형태의 부동소수점 출력하기
#15칸 만들기
#15칸에 부호 추가하기 
#15칸에 부호 추가하고 0으로 채우기 

output_a = "{:15f}".format(23.1231)
output_b = "{:+15f}".format(23.123)
output_c = "{:+015f}".format(23.123)

print(output_a)
print(output_b)
print(output_c)