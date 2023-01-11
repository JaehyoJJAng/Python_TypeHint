# 상수 타입 정의
from typing_extensions import Final

RATE : Final = 300
# RATE = 250 : Error 

People : Final = ['이모씨','김모씨']
People.append('박모씨')
People.extend('개모씨')
# People = Dict() : Error