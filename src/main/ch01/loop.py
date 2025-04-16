numbers = [1,2,3,4,5]
# java 등에서 사용된 중괄호 -> 파이썬에서는 ':'
# >> 들여쓰기 중요!!      >> "indent rainbow" install 하면 편함
for num in numbers:
    print(num)
print(num) # 위의 반복문에 포함되지 않음!
# 반복문에 조건 추가
print(range(10))
print(list(range(10)))
for n in range(5, 10):
    print(n)

# while
while True:
    selected = input("입력: ")
    if selected in [ 'q', 'Q' ]:
        break

