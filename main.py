import ADT

a = ADT.Variable("2")
b = ADT.Variable("x")

c = ADT.Expression("+",a,b)
d = ADT.Expression("/",c,a)

e = ADT.Variable("5")
f = ADT.Equation("=",d,e)

print(f)