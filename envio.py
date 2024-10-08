class Envio:
    def __init__(self,codigo,dire,tipo_envio,forma_pago):
        self.cp = codigo
        self.direccion = dire
        self.tipo = tipo_envio
        self.forma = forma_pago

    def __str__(self):
        a = "Código postal: " + str(self.cp)
        a += " - Dirección física del destino: " + str(self.direccion)
        a += " - Tipo de envío: " + str(self.tipo)
        a += " - Forma de pago: " + str(self.forma)

        return a

