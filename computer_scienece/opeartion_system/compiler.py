"""
좁은 의미의 컴파일러: 소스코드를 기계어로 번역하는 것
넓은 의미의 컴파일러: 하나의 언어 코드를 다른 언어로 변환하는 것
"""

"""
컴파일러 언어
    모든 줄을 한 번에 번역하여 실행파일을 만든다.
    실행파일만을 실행시키기 때문에 실행시간이 빠르다.
    코드 전체를 읽고나서 컴파일 하기 때문에 목적 파일 생성 O
인터프리터 언어
    byte 코드로 컴파일을 실행한다.
    한 줄씩 번역하고 실행한다.
    번역 시간은 짧으나 실행시간이 느리다.
    코드 한 줄씩 읽고 진행하기 때문에 목적 파일 생성 X
    
    compile time에 link 되지 않는다. 하지만 로딩 과정은 존재한다.
"""

"""
바이트 코드와 바이너리 코드 차이점
Byte Code
    바이트코드는 가상 컴퓨터에서 돌아가는 실행 프로그램을 위한 이진 표현법
    가장 기계어와 유사한 레벨의 코드지만 완전한 기계어는 아니다.
    "가상 머신이 이해할 수 있는 이진 코드"
Binary Code
    "컴퓨터가 이해할 수 있는 이진 코드"
    하지만 모든 바이너리 코드가 cpu가 이해할 수 있는 기계어는 아니다.
Assembly Code
    기계어와 일대일 대응이 되는 저급 언어이다.
"""

"""
링커와 로더 https://jess2.tistory.com/72

링커(프로그램 내에서 참조하는 함수나 라이브러리들을 하나로 묶는 작업을 함) + 실행파일(바이너리 코드로 구성) 생성

동적 링크 라이브러리(Dynamic-lnk Library, DLL)를 사용하여 실행파일과 분리시킬 수 있다. DLL 또한 컴파일러에 의해 컴파일 된다.
런타임시에 함수가 실행파일에 연결된다. 실행파일에는 호출할 함수의 정보만 가지고 있기 때문에 실행 파일의 크기가 줄어든다.
1. DLL을 사용하는 프로그램이 여러개 있어도, 한 번만 메모리에 적재하고 DLL을 공유한다.
2. 라이브러리 내용이 수정되어도 실행 파일을 다시 컴파일 할 필요가 없다.
3. 실행 파일의 크기가 줄어든다.

로더는 컴퓨터 내부로 정보를 들여오거나 로드 모듈을 디스크 등의 보조기억장치로부터 주기억장치에 적재하는 시스템 소프트웨어이다.
로더는 기본적으로 다음과 같은 기능을 차례로 수행하지만, 로더의 각 기능을 언어 번역 프로그램 또는 링커 등의 시스템 소프트웨어가 수행할 수도 있다.
    할당(Allocation): 실행 프로그램을 실행시키기 위해 기억장치 내에 옮겨놓을 공간을 확보하는 기능
    연결(Linking): 부 프로그램 호출 시 그 부 프로그램이 할당된 기억장소의 시작주소를 호출한 부분에 등록하여 연결하는 기능
    재배치(Relocation): 디스크 등의 보조기억장치에 저장된 프로그램이 사용하는 각 주소들을 할당된 기억장소의 실제 주소로 배치시키는 기능
    적재(Loading): 실행 프로그램을 할당된 기억공간에 실제로 옮기는 기능
    
"""

"""
파이썬 컴파일 과정
소스 코드를 Parse Tree 로 변환합니다
Parse Tree 를 AST(Abstract Syntax Tree) 로 다시 한 번 변환 합니다
AST를 제어 흐름 그래프(Control FlowGraph)로 변환 합니다
제어 흐름 그래프를 Byte code로 변환 합니다.
"""