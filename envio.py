class Envio:
    def __init__(self):
        self.codigo_postal = ""
        self.direccion = ""
        self.tipo_envio = 0
        self.forma_pago = 0

    def mostrar_info(self):
        print(f"{self.codigo_postal} {self.direccion} {
              self.tipo_envio} {self.forma_pago}")

    def obtener_codigo_postal(self, line):
        self.codigo_postal = line[0:8]

    def obtener_direccion(self, line):
        self.direccion = line[9:28]

    def obtener_tipo_envio(self, line):
        self.tipo_envio = line[29]

    def obtener_forma_pago(self, line):
        self.forma_pago = line[30]
