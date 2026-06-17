class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

class C(A):
    def __init__(self):
        super().__init__()
        print("C init")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")

d = D()
# Output:
# A init
# C init
# B init
# D init




# class A:
#     def __init__(self, a, **kwargs):
#         super().__init__(**kwargs)
#         self.a = a
#         print(f"A init: a={a}")

# class B(A):
#     def __init__(self, b, **kwargs):
#         super().__init__(**kwargs)
#         self.b = b
#         print(f"B init: b={b}")

# class C(A):
#     def __init__(self, c, **kwargs):
#         super().__init__(**kwargs)
#         self.c = c
#         print(f"C init: c={c}")

# class D(B, C):
#     def __init__(self, a, b, c):
#         super().__init__(a=a, b=b, c=c)
#         print("D init")

# d = D(a=1, b=2, c=3)