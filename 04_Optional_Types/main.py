# Optional Type : Union Type이 Optional Type 대체 가능함
# Optional Type : 있을 수도 있고 , 없을 수도 있는 타입에다가 명시
from typing import Union,Optional


xxx : Union[str,None] = 'JaehyoJJAng'
xxx = None

xx  : Optional[str] = 'JaehyoJJAng'
xx = None

def foo(name:str)-> Optional[str]:
    if name == 'JaehyoJJAng':
        return None
    else :
        return name

foo(name='JaehyoJJAng')