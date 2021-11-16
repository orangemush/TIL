"""
plus와 multiple 함수는 inputnum 데코레이터 함수의 execution 함수가 되는거나 마찬가지다. plus -> execution
왜냐하면 inputnum의 반환값은 execution 객체기 때문.
즉 plus 함수의 인자를 넣기 위해서는 excution 함수 인자를 받아야 된다. plus(1, 2, 3) -> execution(1, 2, 3)

복수의 데코레이터를 스택해서 사용하면 아래쪽 데코레이터부터 실행
@a
@b
def c() 일 경우,
1. c는 b의 inner_function이 된다(실행시킨다).
2.b의 inner_function은 a의 inner_function이 된다(실행시킨다.)
"""

# nested function
# 외부 스코프의 변수에 대해 '읽기'가 문제없이 가능하다
# 하지만 nonlocal 영역에 대해 '쓰기'는 제한적이다.
# https://shoark7.github.io/programming/python/closure-in-python
#

from functools import wraps


def inputnum(cal):
    # wraps(cal)을 붙여줌으로써 plus, multiple 함수의 추적 가능
    @wraps(cal)
    def execution():
        nums = input(f"{cal.__name__} 연산 할 숫자들 입력(n1, n2...): ")
        nums = list(map(int, nums.split(', '))) # '1, 2, 3' -> [1, 2, 3]
        return cal(nums)
    return execution

@inputnum
def plus(nums: list) -> int:
    total = 0
    for num in nums:
        total += num
    return total

@inputnum
def multiple(nums: list) -> int:
    total = 1
    for num in nums:
        total *= num
    return total

# print(plus())
# print(multiple())

# @wraps를 붙임으로써 정확한 값 나옴
print(plus.__name__)