"""
퍼스트 클래스
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
    

"""



"""
iterator 
    iterator class는 __iter__, __next__ 또는 __getitem__ 메서드를 구현해야 한다.
    
"""
a = [1, 2, 3]
a_iter = iter(a) # <class 'list_iterator'>

b = {1, 2, 3}
b_iter = b.__iter__()
b_iter.__next__()


""" 
generator 
    이터레이터를 생성해주는 함수입니다.
    아래 generator 함수는 __iter__, __next__ 메서드가 생깁니다.
    
"""
# lazy evaluation

def generator():
    yield 1
    yield 2
    yield 3

