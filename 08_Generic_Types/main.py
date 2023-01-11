"""
* 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술 
"""
from typing import Union,Optional,TypeVar,Generic

# TypeVar 지정
ARM  = TypeVar('ARM' ,int,float,str)
HEAD = TypeVar('HEAD',int,float,str)

class Robot(Generic[ARM,HEAD]):
    def __init__(self,arm: ARM , head: HEAD) -> None:
        self.arm  : ARM  = arm
        self.head : HEAD = head

    def decode(self):
        # 임호를 해독하는 코드
        # .. ~
        # bbb : Optional[ARM] = None 
        pass        
            
robot1 : Robot = Robot[int,int](arm=213123,head=2343243221)
robot2 : Robot = Robot[str,int](arm="5435431",head=4234234132)
robot3 : Robot = Robot[float,str](arm=2.13123124,head="523404023")