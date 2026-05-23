# MATRIZ DEL INVENTARIO

inventario = [
    [101, "Teclado", 3, 10],
    [102, "Mouse", 15, 10],
    [103, "Monitor", 2, 5],
    [104, "Impresora", 8, 8],
    [105, "USB", 1, 6]
]

# FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR

def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        pedido = stock_minimo - stock_actual
    else:
        pedido = 0

    return pedido

# RECORRER LA MATRIZ Y MOSTRAR RESULTADOS

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("-----------------------------")
    