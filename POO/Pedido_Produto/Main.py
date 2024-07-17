from Produto import Produto
from Pedido import Pedido
from Item_pedido import itemPedido

note = Produto(15,5000,"note ultrafino")
cadeira = Produto(25,22,"cadeira home office")

p1 = Pedido()
item = itemPedido(note,3)
p1.adicionar_item(item)
print(p1.obter_total())


p2 = Pedido()
item2 = itemPedido(cadeira,3)
p2.adicionar_item(item2)
print(p2.obter_total())

