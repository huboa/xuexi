#coding:utf-8
#单继承
# class A:
#     def f1(self):
#         print('A.f1')
#
#     def f2(self):
#         print('A.f2')
#         self.f1() #b.f1()
#
# class B(A):
#     def f1(self):
#         print('B.f2')
#
#
# b=B()
# # b.f2=111111
# b.f2()

#多继承
class J:
    def test(self):
        print('J')
class A(J):
    # def test(self):
    #     print('A')
    pass
class E(J):
    def test(self):
        print('E')
    pass
class H(J):
    def test(self):
        print('H')

class G(H):
    def test(self):
        print('G')
    pass
class B(A):
    # def test(self):
    #     print('B')
    pass
class D(E):
    def test(self):
        print('D')
    pass
class F(G):
    def test(self):
        print('F')
    pass
class C(B,D,F):
    # def test(self):
    #     print('C')
    pass

c=C()
# c.test=1111
# c.test()

#MRO列表
print(C.mro())



#C B A D E F G H J object








