import ADT

a = ADT.Variable("2")
b = ADT.Variable("10")
c = ADT.Variable("x")

d = ADT.Expression("/",b,c) #d=10*x
e = ADT.Expression("/",d,a) #e=d/2

f = ADT.Equation("=",e,b) #e=10

print(f)