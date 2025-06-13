from random import sample

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

    def construcao_inicial(self, max_tentativas=1000):
        num_pedidos = len(self.I.orders)
        lb = min(self.lb, num_pedidos)
        ub = min(self.ub, num_pedidos)

        for _ in range(max_tentativas):
            self.x = [0] * len(self.I.orders)
            self.y = [0] * len(self.I.aisles)

            wave_size = sample(range(lb, ub + 1), 1)[0]
            select_orders = sample(range(num_pedidos), wave_size)

            for o in select_orders:
                self.x[o] = 1
                for a in self.I.order_aisles[o]:
                    self.y[a] = 1

            if self.solucao_viavel() and self.aisles_storage():
                return

        raise Exception("Não foi possível construir uma solução viável após várias tentativas.")

    def calculate_ofv(self):
        numerador = 0
        denominador = sum(self.y)

        for a in range(len(self.I.aisles)):
            if self.y[a] == 1:
                for o in range(len(self.I.orders)):
                   if self.x[o] ==  1 and a in self.I.order_aisles[o]:
                       numerador += self.I.u[a][o]

        return numerador / denominador

    def solucao_viavel(self):
        total = 0
        for a in range(len(self.I.aisles)):
            if self.y[a] == 1:
                for o in range(len(self.I.orders)):
                    if self.x[o] == 1 and a in self.I.order_aisles[o]:
                        total += self.I.u[a][o]

        return self.lb <= total <= self.ub

    def aisles_storage(self):
        for o in range(len(self.I.orders)):
            if self.x[o] == 1:
                demanda_total = 0
                total_disponivel = 0
                for a in self.I.order_aisles[o]:
                    if self.y[a] == 1:
                        demanda_total += self.I.u[a][o]

                for a in range(len(self.I.aisles)):
                    if self.y[a] == 1:
                        total_disponivel += self.I.u[a][o]
                if demanda_total > total_disponivel:
                    return False
        return True

