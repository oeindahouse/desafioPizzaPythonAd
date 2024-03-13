from pizza import Pizza


print("ingredientes disponibles para su pizza:")
print("ingredientes proteina:", Pizza.ingredientes_carne)
print("ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("tipos de masa:", Pizza.tipos_masa)


print("¿'salsa de tomate' está presente en la lista?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))


pizza_instancia = Pizza()
pizza_instancia.realizar_pedido()


print("\n el pedido de su pizza es el siguiente:")
print("ingredientes vegetales:", pizza_instancia.ingrediente_vegetal_1, ",", pizza_instancia.ingrediente_vegetal_2)
print("ingrediente proteico:", pizza_instancia.ingrediente_proteico)
print("tipo de masa:", pizza_instancia.tipo_masa)
print("¿es una pizza válida?", pizza_instancia.es_valida)
print("recuerde que su pizza es formato tradicional, con un valor de $10000")


print("\n¿Es la clase Pizza válida?", Pizza.es_valida)