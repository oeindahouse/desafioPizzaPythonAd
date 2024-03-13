class Pizza:
    ingredientes_carne = ['pollo', 'vacuno', 'carne vegetal']
    ingredientes_vegetales = ['tomate', 'aceitunas', 'champignon']
    tipos_masa = ['tradicional', 'delgada']

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_masa = None
        self.es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def realizar_pedido(self):
        self.ingrediente_proteico = str(input("ingresar el ingrediente proteico (pollo, vacuno, carne vegetal): "))
        self.ingrediente_vegetal_1 = str(input("ingresar el primer ingrediente vegetal (tomate, aceitunas, champignon): "))
        self.ingrediente_vegetal_2 = str(input("ingresar el segundo ingrediente vegetal (tomate, aceitunas, champignon): "))
        self.tipo_masa = str(input("ingresar el tipo de masa (tradicional, delgada): "))

        # Validar los ingredientes
        if (self.validar_elemento(self.ingrediente_proteico, self.ingredientes_carne) and
            
            self.validar_elemento(self.ingrediente_vegetal_1, self.ingredientes_vegetales) and
            self.validar_elemento(self.ingrediente_vegetal_2, self.ingredientes_vegetales) and
            self.validar_elemento(self.tipo_masa, self.tipos_masa)):
            self.es_valida = True