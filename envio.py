class Envio:
    def __init__(self):
        self.codigo_postal = ""
        self.direccion = ""
        self.tipo_envio = 0
        self.forma_pago = 0

    def mostrar_info(self):
        print(f"{self.codigo_postal} {self.direccion} {
              self.tipo_envio} {self.forma_pago}")
