#모듈 불러오기

import mod1

from mod1 import add, sub #모듈 이름을 붙이지 않고 사용
from mod1 import * #모듈 내 함수를 모두 불러오기.

import mod1
# print(mod1.__name__)


#클래스나 변수 등을 포함한 모듈 mod2.py 파일로 연습 중

import mod2

# print(mod2.add(mod2.PI, 4.4))

#sys.path.append 사용하기
