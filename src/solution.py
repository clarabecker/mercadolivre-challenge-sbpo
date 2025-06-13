from random import shuffle, random

class Solution:
    # Representation
    x = None  #lista que armazena quais pedidos são escolhidos
    y = None #lista que armazena quais corredores são escolhidos
    lb = None
    ub = None

    #Auxiliary structures --> Nao tem

    def __init__(self, I, S = None):
        self.I = I

        if S is not None:
            self.x = S.x.copy()
            self.y = S.y.copy()
            self.lb = S.lb.copy()
            self.ub = S.ub.copy()
        else:
            self.x = [0] * len(I.orders)
            self.y = [0] * len(I.aisles)
            self.lb = I.wave_size_lb
            self.ub = I.wave_size_ub

