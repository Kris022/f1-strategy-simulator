class TyreCompound:
    def __init__(self):
        self.k1 = 0. # Curve undinwding - Tyre Life span/Peak performance duration
        self.k2 = 0. # Curve rotation - Speed of the warm up period 
        self.k3 = 0   # Up and down - maximum speed potenital

        self.c = 0

        self.age = 0
    
    def get_degradation(self):
        a = self.age
        #t = self.k1 * a**2 + self.k2 * a + self.k3
        t = self.k1 * (a - self.c)**2 + self.k2 * (a - self.c) + self.k3
        self.age += 1
        
        return t

class Soft(TyreCompound):
    def __init__(self):
        super().__init__()
        self.k1 = 0.01
        self.k2 = -0.41
        self.k3 = 4.2
        self.c = -13.7
        
class Medium(TyreCompound):
    def __init__(self):
        super().__init__()
        self.k1 = 0.005
        self.k2 = -0.1
        self.k3 = 0.5   
        self.c = -1.3

class Hard(TyreCompound):
    def __init__(self):
        super().__init__()
        self.k1 = 0.004
        self.k2 = -0.55 
        self.k3 = 18.9
        self.c = -65
