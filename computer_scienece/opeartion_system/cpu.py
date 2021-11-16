"""
CPU, MPU, MCU
한 방에 끝내는 CPU Components
CPU---------------------------------------------------------
    Processor--------------------------------------
        Core---------------------
            ALU
            CU
            Register
        -------------------------
        Cache
        JTAG
        WB
        ...
    ----------------------------------------------------------
    TIMER, ADC, UART, SPI ...
---------------------------------------------------------------
cpu 기본 처리단위: 레코드

bus interface(메모리 <-> CPU, 양방향)
    데이터 버스
    어드레스 버스
    컨트롤 버스

ALU (연산)
Control Unit (제어)
Register Set (기억)
cpu instruction(연산행위를 이야기 함)

http://melonicedlatte.com/computer/2018/11/07/190754.html
register란 flip flop의 집합이며, 이 Flip Flop이라는 것은 각각 1bit의 정보를 저장할 수 있는 것을 의미

(hardware 측면)
register 개수는 32개로 한정되어 있다. (클록 사이클이 길어지기 때문)
register 한 개당 담을 수 있는 bit의 수가 운영체제 bit의 수를 나타낸다.

load-store 방식
main memory(DRAM) -> cache(SRAM) -> register -> main memory(DRAM)
https://ko.gadget-info.com/difference-between-sram (SRAM, DRAM 차이점)

cpu register는 메모리 주소를 기억한다. 이것이 RAM의 메모리에 접근하는 방법이다.
레지스터의 한 bit는 각각 byte로 구성된 메모리를 참조할 수 있다. 32비트 운영체제는 램의 최대 4 gigabytes(2^32) 사용할 수 있다.
실제 한도는 약간 더 적은 약 3.5기가 bytes. 왜냐하면 메모리 주소들을 일시적으로 저장하기 때문이다.

CISC 구조: 하나당 최대한 많은 명령어 실행
RISC 구조: 하나당 하나의 명령어 실행, Load/store 아키텍쳐, 보통 사용하는 구조, 메모리 엑세스가 많지 않고 끊기지 않음

Fetch   : 메모리 상에서 입출력 버스를 통해 Core 안에 있는 레지스터에 들어오게 되는 과정
Decode  : Control Unit이 register에 있는 명령어를 한 줄 한 줄 읽는 과정
Excution: ALU에게 연산을 맡기고 명령에 맞게 실행 시키는 과정

클럭이란 cpu가 1초에 진동하는 횟수(단위 시간당 처리하는 작업량)


"""