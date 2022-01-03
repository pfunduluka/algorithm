

class Variable:
    def __init__(self, value:str):
        self.value=value
    def add(self,item):
        a = Expression("+")
        a.lhs=self
        a.rhs=item
        return a

class Expression:
    def __init__(self, operator:str, lhs=None, rhs=None):
        self.lhs=lhs
        self.operator=operator
        self.rhs=rhs
    
    def toString(self):
        view = str()

        if type(self.lhs) == Variable:
            view = self.lhs.value
        elif type(self.lhs) == Expression:
            view = f"({self.lhs.toString()})"
        else:
            return None

        view += self.operator
        
        if type(self.rhs) == Variable:
            view += self.rhs.value
        elif type(self.lhs) == Expression:
            view += f"({self.rhs.toString()})"
        else:
            return None

        return view
    
    def __str__(self):
        return self.toString()

class Equation:
    def __init__(self, asignmentOperator="=", lhs=None, rhs=None):
        self.lhs=lhs
        self.asignmentOperator=asignmentOperator
        self.rhs=rhs
    
    def toString(self):
        view = str()

        if type(self.lhs) == Variable:
            view = self.lhs.value
        elif type(self.lhs) == Expression:
            view = f"{self.lhs.toString()}"
        else:
            return None

        view += self.asignmentOperator
        
        if type(self.rhs) == Variable:
            view += self.rhs.value
        elif type(self.lhs) == Expression:
            view += f"{self.rhs.toString()}"
        else:
            return None

        return view
    
    def __str__(self):
        return self.toString()
