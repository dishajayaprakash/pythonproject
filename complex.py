import math
class ComplexNum:
    def __init__(self):
        self.real=float(input("real: "))
        self.img=float(input("imaginary: "))

    def absolute(self):
        abs=math.sqrt((self.real**2)+(self.img**2))
        return abs
    
    def __add__(self, A):
        return complex(A.real+self.real,A.img+self.img)

    def __mul__(self, A):
        return complex(A.real * self.real - A.img * self.img,A.real * self.img + A.img * self.real)
def main():
    c1=ComplexNum()
    c2=ComplexNum()
    print(c1*c2)
if __name__=="__main__":
    main()