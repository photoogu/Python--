from function import add3, add2

if __name__ == "__main__":
    print("시작")
    print(__name__) # 실행된 위치의 파일 이름
    print(add3(10,20,30)) # 참조된 파일 이름 >> 여기선 function 이 된다.
    print(add2(10,20))
# 파이썬에는 main 함수가 따로 없음 >> if __name__ == "__main__" 으로 걸어주면 main 역할이 된다.
# 파이썬은 무조건 위에서부터 순서대로 실행된다
# 즉, import 한 순간 function이 호출되어 실행이 됨

    # try-catch 가 아닌, try-except
    try:
        print("예외처리")
        raise Exception("내가 만든 예외") # 강제 예외 생성(throw)
    except Exception as e:
        print("예외발생")
        print(e)