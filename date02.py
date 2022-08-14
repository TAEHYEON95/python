#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

#오전 구분 
if now.hour < 12:
    print(f"현재 시간은 {now.hour}시로 오전입니다")

if now.hour >= 12:
    print(f"현재 시간은 {now.hour}시로 오후입니다.")