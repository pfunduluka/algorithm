import ADT

a = ADT.Variable("2")
b = ADT.Variable("4")

c = ADT.Expression("+",a,b)
d = ADT.Expression("/",c,a)

e = ADT.Variable("x")
f = ADT.Equation("=",d,e)

print(f)