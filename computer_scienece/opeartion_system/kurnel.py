blog = "https://5equal0.tistory.com/entry/Linux-Kernel-%EC%BB%A4%EB%84%90%EC%9D%98-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%BB%A4%EB%84%90%EC%9D%98-%EA%B5%AC%EC%A1%B0"

"""
리눅스 커널 

단일형 커널(모놀리식 커널)
    유닉스, 리눅스, 솔라리스, BSD, 윈도우 NT
마이크로 커널

커널의 가장 큰 역할은 컴퓨터의 물리적 자원과 추상화 자원을 관리하는 것.
추상화는 물리적 개념을 논리적 개념으로 변환한 개념이라고 보면 된다.
물리적 자원들과 추상화한 자원을 칭하는 용어 간 대응관계 정리

CPU -> 태스크(task)
메모리 -> 페이지(page), 세그먼트(segment)
디스크 -> 파일(file)
네트워크 -> 소켓(socket)

1) 태스크(Task) 관리자
  : 물리적 자원인 CPU를 추상적 자원인 태스크로 제공 

2) 메모리(Memory) 관리자 
  : 물리적 자원인 메모리를 추상적 자원인 페이지나 세그먼트로 제공
  
3) 파일 시스템(File System) 관리자 
  : 물리적 자원인 디스크를 추상적 자원인 파일로 제공

4) 네트워크(Network) 관리자
 : 물리적 자원인 네트워크 장치를 추상적 자원인 소켓으로 제공
 
5) 디바이스 드라이버(Device Driver) 관리자
 : 각종 외부 장치에대한 접근

커널의 구성요소는 여러가지 자원들을 관리하는 관리자(Manager)들이다.

"""