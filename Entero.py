class entero:
    def __init__(self, ent):
        self.entero = ent

    def Primo(self):
        if self.entero < 2:
            return False
        for i in range(2, self.entero):
            if self.entero % i == 0:
                return False
        return True

    def Fibonacci(self):
        a=0
        b=1
        t=0
        while t<self.entero :
            t=a+b
            a=b
            b=t
        if t == self.entero:
            return True
        else:
            return False
    
    def Par(self):
        if self.entero % 2 == 0:
            return True
        else:
            return False
    
    def Impar(self):
        if self.entero % 2 != 0:
            return True
        else:
            return False