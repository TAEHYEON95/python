#딕셔너리를 선언 합니다.
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

key = input("접근하고자 하는키 : ")
if key in dictionary:
    print ("있는 키입니다.")
else:
    print ("없는 키입니다,")