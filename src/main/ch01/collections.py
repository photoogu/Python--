# list
numberList = []
numberList = list() # list 생성(위와 같음)
numberList.append(10)
numberList.append("가")
numberList.append([1,2,3,True])
print(numberList)

# map (python 에서는 dictionary 라고 한다)
nameDict = {}
nameDict = dict() # dictionary 생성(위와 같음)
nameDict["name1"] = "김영경"
nameDict = {"name1": "김영경", "name2": "김양갱"}
print(nameDict)
# 특정 값 가져오기
print(nameDict["name1"])
print(nameDict.get("name2"))
print(nameDict.keys()) # key만 가져오기
print(nameDict.values()) # value만 가져오기
print(nameDict.items()) # entry >> list 안에 괄호로 key value가 묶여있음

# 파이썬에서는 tuple 이라는 자료형이 있다.
# tuple: 불변 리스트, 값을 추가할 수도, 뺄 수도 없다
nameList = ["김영경", "김양갱"]
nameTuple = ("김영경", "김양갱")
for name in nameList:
    print(name)
for name in nameTuple:
    print(name)
# tuple을 변경하고싶다? -> list로 만들면 됨!
nameList = list(nameTuple)
nameList.append("밤양갱")
print(nameList)
# list 두개를 합칠 수 있음. 대신 새로운 list로 생성이 됨 >> 주소가 다르다
nameList2 = nameList + list(nameTuple)
print(nameList2)
nameList3 = nameList.extend(list(nameTuple))
print(nameList3)