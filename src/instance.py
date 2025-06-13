
class Instance:
    # General
    orders = None
    aisles = None
    wave_size_lb = None
    wave_size_ub = None

    def __init__(self, path):
        self.read_input(path)

    def read_input(self, path):
        with open(path, 'r') as file:
            lines = file.readlines()
            first_line = lines[0].strip().split()
            o, i, a = int(first_line[0]), int(first_line[1]), int(first_line[2])

            # Read orders
            self.orders = []
            for j in range(o):
                order_line = lines[j + 1].strip().split()
                d = int(order_line[0])
                order_map = {int(order_line[2 * k + 1]): int(order_line[2 * k + 2]) for k in range(d)}
                self.orders.append(order_map)

            # Read aisles
            self.aisles = []
            for j in range(a):
                aisle_line = lines[j + o + 1].strip().split()
                d = int(aisle_line[0])
                aisle_map = {int(aisle_line[2 * k + 1]): int(aisle_line[2 * k + 2]) for k in range(d)}
                self.aisles.append(aisle_map)

            # Read wave size bounds
            bounds = lines[o + a + 1].strip().split()
            self.wave_size_lb = int(bounds[0])
            self.wave_size_ub = int(bounds[1])

    def objective_fun(self, selected_orders):

        if not self.waveLimits(selected_orders):
            return 0

        total_order = 0          #Soma total das unidades
        total_aisles = set()     #Indices dos corredores

        for o in selected_orders:
            order = self.orders[o]      #Dicionário item->quantidade
            total_order += sum(order.values())

            for item in order:
                for aisle_index, aisle in enumerate(self.aisles):
                    #PROCURANDO O ITEM NO CORREDOR
                    if item in aisle:
                        total_aisles.add(aisle_index)
                        break

        if not total_aisles: #Evitar divisão por 0
            return 0



        return total_order / len(total_aisles)

    def waveLimits(self, selected_orders): #Restricoes LB e UB
        total_units = 0

        for o in selected_orders:
            order = self.orders[o]  #dicionário {item: quantidade}
            total_units += sum(order.values())

        return self.wave_size_lb <= total_units <= self.wave_size_ub

