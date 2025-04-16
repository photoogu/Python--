# 객체
class Student:
    def __init__(self, name): # 생성자: __init__
        self.name = name
        print("생성자 호출")

    def printInfo(self):
        print("학생정보 출력")
        print(f"이름: {self.name}")

    @staticmethod # 클래스가 정의되는 순간부터 클래스가 static이기 때문에 주소가 필요X
    def printId():
        print("아이디 출력")

    def __str__(self): # toString 역할
        return f"이름: {self.name}__str__"

s1 = Student("김영경") # new 안붙인다
print(s1)
s1.printInfo()
Student.printId()

# self: 객체의 주소
# 파이썬의 모든 객체의 첫번째 매개변수에는 자기 자신의 참조 주소가 생략되어있다(this)
# 생성자에 보통 멤버변수를 정의한다