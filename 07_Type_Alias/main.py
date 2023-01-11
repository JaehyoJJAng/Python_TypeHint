# Type Alias

from typing import Union,List,Dict
from typing_extensions import TypedDict

# * type alias
Value = Union[int,bool,List[Union[str,int]],Dict[str,Union[List[str],str]]] 
value : Value  = 17


# * dict alias
# TypedDict
ddd: Dict[str,Union[str,int]] = {"Hello":"World","World":"Hello","Bye":100}

class Point(TypedDict):
    x:int
    y:float
    z:str
point : Point = {'x':8,'y':1.5,'z':'string'}