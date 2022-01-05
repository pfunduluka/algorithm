

class Variable:
    def __init__(self, value:str):
        self.value=value
    
    def evaluation(self):
        try:
            a = float(self.value)
        except Exception as e:
            print(e)
            return None
        else:
            return a
    
    def multiply(self,item):
        a = Expression("*",self,item)
        return a
    
    def divide(self,item):
        a = Expression("/",self,item)
        return a
    
    def subtract(self,item):
        a = Expression("-",self,item)
        return a
        
    def add(self,item):
        a = Expression("+")
        a.lhs=self
        a.rhs=item
        return a

    def __str__(self):
        return self.value

class Expression:
    def __init__(self, operator:str, lhs=None, rhs=None):
        self.lhs=lhs
        self.operator=operator
        self.rhs=rhs
    
    def _operation(self, lhs, rhs):
        if lhs != None and rhs != None:
            if self.operator == "+":
                return lhs+rhs
            elif self.operator == "-":
                return lhs-rhs
            elif self.operator == "*":
                return lhs*rhs
            elif self.operator == "/":
                return lhs/rhs
            else:
                return None
        else:
            return None
    
    def evaluation(self):
        a = self.lhs.evaluation()
        b = self.rhs.evaluation()
        #"""
        if self.operator == "*":
            if a != None and b == None:
                if type(self.rhs) == Expression:
                    a1 = self.rhs.lhs.evaluation()
                    b1 = self.rhs.rhs.evaluation()
                    if self.rhs.operator == "*":
                        if a1 != None:
                            new1 = Expression("*",self.lhs,self.rhs.lhs)
                            self.lhs = new1
                            self.rhs = self.rhs.rhs
                            self.evaluation()
                        elif b1 != None:
                            new1 = Expression("*",self.lhs,self.rhs.rhs)
                            self.lhs = self.rhs.lhs
                            self.rhs = new1
                            self.evaluation()
                    if self.rhs.operator == "/":
                        if a1 != None:
                            new1 = Expression("*",self.lhs,self.rhs.lhs)
                            self.lhs = new1
                            self.rhs = self.rhs.rhs
                            self.operator = "/"
                        elif b1 != None:
                            new1 = Expression("/",self.lhs,self.rhs.rhs)
                            self.lhs = self.rhs.lhs
                            self.rhs = new1
                            self.evaluation()
            elif a == None and b != None:
                if type(self.lhs) == Expression:
                    a1 = self.lhs.lhs.evaluation()
                    b1 = self.lhs.rhs.evaluation()
                    if self.lhs.operator == "*":
                        if a1 != None:
                            c = self.lhs.rhs
                            new1 = Expression("*",self.lhs.lhs,self.rhs)
                            self.lhs = new1
                            self.rhs = c
                            self.evaluation()
                        elif b1 != None:
                            new1 = Expression("*",self.lhs.rhs,self.rhs)
                            self.lhs = self.lhs.lhs
                            self.rhs = new1
                            self.evaluation()
                    elif self.lhs.operator == "/":
                        if a1 != None:
                            c = self.lhs.rhs
                            new1 = Expression("*",self.lhs.lhs,self.rhs)
                            self.lhs = new1
                            self.rhs = c
                            self.operator = "/"
                            self.evaluation()
                        elif b1 != None:
                            new1 = Expression("/",self.rhs,self.lhs.rhs)
                            self.lhs = self.lhs.lhs
                            self.rhs = new1
                            self.evaluation()
        elif self.operator == "/":
            if a != None and b == None:
                pass
            elif a == None and b != None:
                pass
        #"""
        return self._operation(a,b)
    
    def toString(self):
        view = str()

        if self.evaluation() == None:
            if type(self.lhs) == Variable:
                view = self.lhs.value
            elif type(self.lhs) == Expression:
                view = f"({self.lhs.toString()})"
            else:
                return None

            view += self.operator
            
            if type(self.rhs) == Variable:
                view += self.rhs.value
            elif type(self.rhs) == Expression:
                view += f"({self.rhs.toString()})"
            else:
                return None
        else:
            view = str(self.evaluation())

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
