# Union Types [합집합 개념]
# Union[올 수 있는 타입]
# Union[str,int,dict] = 스트링 또는 숫자형 또는 딕셔너리 자료형이 올 수도 있음
from typing import Union,Dict,List

xxx : Union[str,int] = 3
xxx = '17'

def foo(x:Union[int,str])-> None:
    print(x)

foo(x=xxx)

a : Dict[str,Union[str,int,List[str]]] = {'hi':"hello"}
def fetch(a:Dict[str,Union[str,int,List[str]]])-> None:
    print(a)
fetch(a=a)