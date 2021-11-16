# first class function
"""
일급 함수 조건 및 정의
함수를 변수나 자료구조에 저장할 수 있다.
함수의 매개변수(인자)에 다른 함수를 인수로 전달할 수 있다.
함수의 반환 값(return 값)으로 함수를 전달할 수 있다.

일급 함수가 없다면? a, b, c는 각각 요리하여 가져다 주는 행위의 함수, d는 요리 후의 처리행위의 함수라고 하자.
만약 일급 함수가 없다면 ad, bd, cd를 필요할 때마다 코드를 쳐야 한다.
만약 일급 함수가 있다면 d 인자에 a, b, c를 넣을 수 있으니 d(a), d(b), d(c)로 작성이 가능하여 편리하다.
"""


"""
closure
    1. 해당 함수는 어떤 함수 내의 중첩된 함수여야 한다.
    2. 해당 함수는 자신을 둘러싼(enclose) 함수 내의 상태값을 반드시 참조해야 한다.
    3. 해당 함수를 둘러싼 함수는 이 함수를 반환해야 한다.
"""

# closure
def outer_func():  #1
    message = 'Hi'  #3
    def inner_func():  #4
        print(message)  #6
    return inner_func  #5
my_func = outer_func()  #2

"""
my_func은 outer_func의 반환값인 inner_func을 가리키기 때문에 message값을 기억하지 못해야 한다.
하지만 python에서는 message값 기억을 가능케 하는 기능이 있고 그 기능이 closure다.
"""

print(my_func)  # 7
print((dir(my_func)))  # 8
print(type(my_func.__closure__)) # 9
print(my_func.__closure__) # 10 (<cell at 0x7fda32fa5fd0: str object at 0x7fda32f4a0b0>,)
print(my_func.__closure__[0])  # 11 #
print(dir(my_func.__closure__[0]))  # 12
print(my_func.__closure__[0].cell_contents)  # 13 숨겨둔 값의 위치
