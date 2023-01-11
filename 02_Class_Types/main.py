# Class Types

class Hello:
    # Instance Method
    def world(self)-> int:
        return 7

# 클래스에 대한 인스턴스를 타이핑 해줄 때 해당 클래스명을 써주면 됨
hello : Hello = Hello()

def foo(instance:Hello)-> int:
    return instance.world()

print(foo(instance=hello))