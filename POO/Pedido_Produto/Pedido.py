class Pedido:
    def __init__(self,valor = 0.0) :
        self._valor_total = valor
        self._item = []

    def adicionar_item(self, item):
        self._item.append(item)

    def obter_total(self):
        total = 0.0
        for item in self._item:
            total += (item._produto._valor * item._quantidade)
        return total
        