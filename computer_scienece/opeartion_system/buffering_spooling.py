"""
SPOOLing
    디스크에 적재시킨다. (디스크는 전송률이 높고 탐색 시간이 짧아서 액세스가 빠르다는 특징을 가지고 있다.)
    디스크를 하나의 매우 큰 버퍼처럼 사용하며 I/O를 수행한다.
    일반적으로 여러 작업들의 입출력과 cpu 연산 처리를 병행 시킨다.(주목적)

     입력장치가 처리해야 할 데이터를 디스크에 저장하고
     cpu가 디스크에 있는 데이터를 읽고 연산을 한다.

Buffering
    주기억 장치에 적재시킨다.
    I/O device 마다 buffer를 둔다.
    하나의 작업에 대한 입출력과 cpu 연산을 병행시키는 것이 주목적

    이러한 용도로 사용되는 주기억 장치 공간은 버퍼라 한다.
    두 개의 버퍼를 사용하여 입력하는 경우에 CPU가 한 쪽 버퍼의 내용을 처리하는 동안 입력 장치는 다른 쪽 버퍼에 입력

    ex) 유튜브 미리보기

둘 다 시스템 성능 향상에 도움을 준다.
"""