import ADT

a = ADT.Variable("2")
b = ADT.Variable("x")
e = ADT.Variable("5")

c = ADT.Expression("/",e,b)
d = ADT.Expression("*",c,a)
d = ADT.Expression("/",a,d)

e = ADT.Expression("*",e,a)
f = ADT.Equation("=",d,e)

print(f)