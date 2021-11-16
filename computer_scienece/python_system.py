import sys
import os

"""
https://jins-sw.tistory.com/17?category=858374 sys.path 에 관한 좋은 글
import 할 때, python은 sys.module(dict) -> built-in-module -> sys.path(list) 순서로 검색
import 시, sys.path 첫 번째 값을 기준으로 찾는다. 첫 번째 값은 현재 실행파일의 디렉토리 경로이다.
import 시, 가져오려는 모듈의 코드 전체를 실행한다.
스크립트가 끝날 때까지 모든 import는 처음 실행파일의 디렉토리값(sys.path[0])이 기준이 되어 찾는다.
따라서 python의 설계대로 하려면 main.py가 아니라면 모두 상대경로로 지정해주는 것이 올바르다.(골치 아파지기 때문)
둘 다 가능케 하고싶으면 위 링크로 들어가자.

터미널에서 python -m 옵션은 모듈로써 실행시킨다는 것. 즉, __name__ == __main__으로써 시킨다는 것
"""
#
#
# # 모듈을 import 할 때 모듈을 찾아야할 경로들을 저장해둔 (list)
# print('\n'.join(sys.path))
# print('\n')
#
# # 현재 프로젝트에서 사용하고 있는 모듈과 패키지 (dict)
# print(sys.modules)