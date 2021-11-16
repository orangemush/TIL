"""
https://jhnyang.tistory.com/133 (address binding)
https://jhnyang.tistory.com/246?category=815411 (로드 타임 바인딩과 실행 타임 바인딩의 차이점)

absolute code <==> relocatable code
absolute code : 코드가, 이미 정해진 메모리 주소에 로드되는 것을 말한다.

logical address(상대 주소): 프로그램 내부에서 사용하는 주소
Physical address: RAM 내의 물리적 주소

Address Binding 이 일어나는 time
    1) Compile time (컴파일이 진행되는 시점)
        Compile time 때에 메모리 주소를 고정 시켜버리면 RAM에 올라갔었을 때(load),
        해당 주소에 다른 프로그램이나 이미 binding 된 주소라면 에러가 발생한다.
        따라서, 프로그램 내부의 메모리 주소와 physical 주소가 같은 경우일 때에만 사용한다.(ex: 아두이노)

    2) Load time (RAM에 로드되는 시점)
        logical 주소와 physical 주소가 분리되어 있기 때문에
        어디에서나 loading 되어서 수행될 수 있다. (multiprogramming 가능 = 주소 몇 번지에 올라가도 load 가능)
        code segmentation 의 메모리 주소와 관련된 모든 부분들(참조)을 전부 다 변경해줘야 한다.
        따라서, 메모리 로딩할 때 시간이 엄청 오래걸리는 문제 발생하기 때문에 실제로 안 쓰임

    3) Execution(Run) time (ALU가 연산하는 시점)
        명령어를 실행할 때 logical 주소를 physical 주소로 변경을 해준다.
        이 때 이 명령어를 실행하는 hardware는 MMU(memory management unit)이다.
        그래야 주소를 그때그때 변환시켜서 주소를 얻는다.(ALU가 변환연산을 하면 비효율적)

    load time과 execution time을 딱 봤었을 땐, load 타임이 더 효율적이여 보이지만
    하드웨어 성능이 너무 좋아져서(하드웨어 로직이 따로 있음) execution time 때 address binding이 실행되도 성능에 문제가 없다.



"""