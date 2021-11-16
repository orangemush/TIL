# 파이썬 프로그램 실행과정

"""
compiled language(C 언어) 실행 과정 (각 컴파일 과정은 compiler.py 파일 확인)

전처리기 -> 컴파일러 -> 어셈블러 -> 링커(실행파일 생성) -> 로더(메모리 load) -> 입/출력 버스(Fetch) ->
cpu(bus interface) -> cpu(registers) -> cpu(control unit)(decode) -> cpu(ALU)(execution)
"""

"""
파이썬은 소스 코드를 바이트코드로 컴파일 한 다음, 이 바이트코드를 해석기(interpreter)가 돌려주는 방식으로 실행한다.
이 때 말하는 바이트코드는 해석기가 사용하는 명령어 세트로 처리된 코드로 가상 머신을 위한 어셈블리 코드 정도로 이해하면 된다.

(.py: source code file, .pyc: bytes code file)
1. .py 파일을 바이트 코드로 컴파일 한다.
2. 그러면 바이트 코드의 .pyc 파일이 생성 되고 PVM에 넘긴다.
...
https://www.youtube.com/watch?v=AisW8ZhqUuc (Python Program Execution Process youtube)

"""
