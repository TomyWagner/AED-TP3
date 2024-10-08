class Envio:
    def __init__(self):
        self.codigo_postal = ""
        self.direccion = ""
        self.tipo_envio = 0
        self.forma_pago = 0

    def mostrar_info(self):
        print(f"| código postal: {self.codigo_postal} | dirección: {self.direccion} | tipo de envío: {
              self.tipo_envio} | forma de pago: {self.forma_pago} |")
