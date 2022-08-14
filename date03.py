#날짜/시간 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

#봄 3 5 여름 6 8 가을 9 11 겨울 12 2
if 3 <= now.month <= 5 :
    print(f"이번달은{now.month}로 봄") 

if 6 <= now.month <=8 : 
    print(f"이번달은{now.month}로 여름")

if 9 <= now.month <= 11 : 
    print(f"이번달은{now.month}로 가을")

if 12 == now.month <=2 : 
    print(f"이번달은{now.month}로 겨울")

