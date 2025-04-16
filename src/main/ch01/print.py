# 파이썬의 철학: 여러가지 문법을 만들지 말자! (println printf 없이 print 하나만)
# print 의 속성이 있음, 줄바꿈 없이 출력하고 싶으면 end 속성 변경!(default: \n)
print("hello python", end=" ")
print("hello python2", end="!!! \n")

# 변수 타입 생략되어있음 (타입 추론형, typeless)
num = 10
name = "김영경"
print(num == 10)
# boolean 타입은 대문자로 시작
isEmpty = False and True #False & True 도 가능, 하지만 가능한 영어로 적는것이 좋음
# 문자열 여러줄 입력 가능
text = """
aaaa
aaa
aaaaa
"""
print(text)
# 리터럴 주소 확인: id
print(id(num), id(10)) # 두 리터럴 주소는 같다

# 표현식
name = "김영경"
age = 26
profile = "이름: {0}, 나이: {1}".format(name, age)
print(profile)
# 파이썬 버전 3 이상부터는 f 를 붙여주면 됨
profile2 = f"이름: {name}, 나이: {age}"
print(profile2)