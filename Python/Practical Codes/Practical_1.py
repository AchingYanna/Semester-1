#PRACTICAL 1:- PROGRAM TO FIND ROOT OF QUADRATIC EQUATIONS

import math

def sqrt_root(a,b,c):
    cal = b*b-4*a*c
    sqrt = math.sqrt(abs(cal))

    if sqrt > 0:
        print("Real and distinct roots")
        print((-b+ sqrt)/(2*a))



    if sqrt == 0 :
        print("Real and same roots")
        print(-b/(2*a))

    else:
        print("Complex roots")
        print(-b / (2*a),  sqrt / (2*a))
        print(-b / (2*a),  sqrt / (2*a))

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

c = float(input("Enter the value of c: "))


if a == 0:
    print("Enter correct quadratic equation")

else:
    sqrt_root(a,b,c)

