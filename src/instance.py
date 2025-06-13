
class Instance:
    # General
    orders = None
    aisles = None
    wave_size_lb = None
    wave_size_ub = None

    def __init__(self, path):
        self.read_input(path)
        self.criar_order_aisles()
        self.criar_matriz_u()


    def read_input(self, path):
        # só lê pedidos, corredores e limites, sem criar estruturas auxiliares
        with open(path, 'r') as file:
            lines = file.readlines()
            first_line = lines[0].strip().split()
            o, i, a = int(first_line[0]), int(first_line[1]), int(first_line[2])

            self.orders = []
            for j in range(o):
                order_line = lines[j + 1].strip().split()
                d = int(order_line[0])
                order_map = {int(order_line[2 * k + 1]): int(order_line[2 * k + 2]) for k in range(d)}
                self.orders.append(order_map)

            self.aisles = []
            for j in range(a):
                aisle_line = lines[j + o + 1].strip().split()
                d = int(aisle_line[0])
                aisle_map = {int(aisle_line[2 * k + 1]): int(aisle_line[2 * k + 2]) for k in range(d)}
                self.aisles.append(aisle_map)

            bounds = lines[o + a + 1].strip().split()
            self.wave_size_lb = int(bounds[0])
            self.wave_size_ub = int(bounds[1])

    def criar_order_aisles(self):
        self.order_aisles = []
        for order in self.orders:
            aisles_for_order = set()
            for item in order:
                for aisle_index, aisle in enumerate(self.aisles):
                    if item in aisle:
                        aisles_for_order.add(aisle_index)
                        break
            self.order_aisles.append(list(aisles_for_order))

    def criar_matriz_u(self):
        num_aisles = len(self.aisles)
        num_orders = len(self.orders)
        u = [[0] * num_orders for _ in range(num_aisles)]

        for o_idx, order in enumerate(self.orders):
            for a_idx, aisle in enumerate(self.aisles):
                total = 0
                for item, qty in order.items():
                    if item in aisle:
                        total += qty
                u[a_idx][o_idx] = total

        self.u = u

