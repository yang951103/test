class Base:
    def f(self):
        print(0)

class A(Base):
    def f(self):
        print(1)
        super().f()

class B(Base):
    def f(self):
        print(2)
        super().f()

class C(A, B):
    def f(self):
        print(3)
        super().f()

c = C()
c.f()

# 继续顺序是从下到上，从左到右，super也就是沿着这条路走，中间没有super就会调到。
# super好处是公共基类的相同函数只会被调用一次。
