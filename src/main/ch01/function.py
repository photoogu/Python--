# 파이썬에서는 함수를 정의할 때 def 를 적는다
def add(num1, num2):
    return num1 + num2, num1, num2
# # return에 쉼표로 여러개를 넣을 경우, tuple로 감싸진다
# print(add(10, 20))
# n1, n2, n3 = add(10, 20) # 비구조할당
# print(n1, n2, n3)

# 파이썬에서는 오버로딩이 안됨! 오버로딩처럼 사용하고싶다면 default 값을 넣어줘야함
# default 는 앞에 붙여주면 그로부터 뒤에 있는 애들도 다 잡아줘야함 >> default는 뒤에서부터 넣어준다(num1 의 default 값이 있을 경우, num2와 num3에도 default가 있어야한다)
def add(num1:str="0", num2 = 0, num3 = 0):
    return num1, num2, num3

# print(add([10], 20)) # 첫번째 매개변수의 자료형은 str 자료형으로 명시되어있지만, 강제성을 부여하진 않는다.

# *을 앞에 붙여주면 여러개의 값을 tuple로 받을 수 있다
def add2(*a):
    print(a)
    result = 0
    for n in a:
        result += n
    return result

# print(add2(1,2,3,4,5))

def add3(*b):
    print(__name__) # 여기서 실행하면 __main__ 이 된다.
    return sum(b)

# print(add3(1,2,3,4,5))


if __name__ == "__main__":
    print(add(10, 20))
    n1, n2, n3 = add(10, 20) # 비구조할당
    print(n1, n2, n3)
    print(add([10], 20))
    print(add2(1, 2, 3, 4, 5))
    print(add3(1, 2, 3, 4, 5))