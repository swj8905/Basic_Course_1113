# 함수 정의 : 함수를 만듦
def add(a, b): # a, b : 매개 변수
    c = a + b
    return c # c : 반환값

def minus(a, b):
    c = a - b
    return c

def calculator(a, b):
    result = [a + b, a - b, a * b, a / b]
    return result

# 함수 호출 : 함수를 사용함
# result = add(10, 20) # 10, 20 : 인자(인수)
result = calculator(10, 20)
print(result)