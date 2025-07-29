# inheritance with class and instance variables
class P:
    z = "Hello"
    def set_p(self):
        self.x = "Class P"
    def print_p(self):
         print(self.x)
class C(P):
    def set_c(self):
        self.x = "Class C"
    def print_c(self):
        print(self.x)


c = C()
c.set_p()
c.print_p()
c.print_c()
c.set_c()
c.print_c()
c.print_p()

print(f"{c.z=} {C.z=} {P.z=}")
C.z = 'Bonjur'
print(f"{c.z=} {C.z=} {P.z=}")
c.z = 'Ciao'
print(f"{c.z=} {C.z=} {P.z=}")