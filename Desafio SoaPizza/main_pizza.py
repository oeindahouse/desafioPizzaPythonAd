from pizza import Pizza

if __name__ == "__main__":
    pizza = Pizza()
    pizza.realizar_pedido()
    if pizza.es_valida:
        print("pedido valido")
        
    else:
        print("pedido invalido")