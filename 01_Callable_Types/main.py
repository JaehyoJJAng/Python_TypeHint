# Callable Types
from typing import Callable,Dict,Union

# 리턴 값이 숫자형인 경우 
def add(a:int,b:int)-> int:
    return a + b

# 리턴 값이 없는 경우 
def say_hello(text:str)-> None:
    print(text)

# 리턴 값이 문자열인 경우
def say_return(text:str)-> str:
    return text

# 리턴 값이 리스트인 경우
def say_list(lst:list)-> list:
    return lst

# 리턴 값이 딕셔너리인 경우
def say_dic(dic:dict)-> dict:
    return dic

"""
함수 자체를 인자로 받는 경우 : Callable Type 사용
Callable[[인자값]],리턴값]
""" 

def return_my_info(name:str,age:int)-> Dict[str,int]:
    dic : Dict[str,Union[str,int]] = dict()
    dic['name'] = name
    dic['age']  = age
    return dic

def print_func(func:Callable[[str,int],Dict[str,int]])-> None:
    print(func)

print_func(func=return_my_info(name='Lee jae hyo',age=26))