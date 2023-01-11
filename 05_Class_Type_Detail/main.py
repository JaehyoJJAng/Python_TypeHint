# Class Type 보충
from typing import Optional

class Hello:
    def world(self) -> int:
        return 7

class World:
    pass

# Create Instance (1)
hello : Hello = Hello()
world : World = World()

# Create Instance (2)
hello : "Hello" = Hello()
world : "World" = World()

def foo(ins:"Hello")-> int:
    return ins.world()

# Optional["Node"] == Union['Node',None]
# 클래스 안에서 자기 자신 (Node)를 타이핑 할 때
class Node:
    def __init__(self,data:int,node:Optional["Node"]) -> None:
        self.data = data
        self.node = node

node : Node = Node(data=12,node=None)