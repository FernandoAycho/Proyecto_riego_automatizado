# Simulación de sensores y actuadores del sistema de riego
class SensorHumedad:
    def __init__(self, valor):
        self.valor = valor

    def leer_humedad(self):
        return self.valor

class SensorNivelAgua:
    def __init__(self, hay_agua):
        self.hay_agua = hay_agua

    def nivel_suficiente(self):
        return self.hay_agua

class BombaAgua:
    def __init__(self):
        self.estado = False

    def activar(self):
        self.estado = True

    def desactivar(self):
        self.estado = False

    def esta_activa(self):
        return self.estado

class SistemaRiego:
    def __init__(self, sensor_humedad, sensor_nivel, bomba, umbral_humedad=30):
        self.sensor_humedad = sensor_humedad
        self.sensor_nivel = sensor_nivel
        self.bomba = bomba
        self.umbral_humedad = umbral_humedad
    #Se agrego la funcionalidad requerida para su personalizacion
    def evaluar_y_regar(self):
        humedad = self.sensor_humedad.leer_humedad()
        if humedad < self.umbral_humedad and self.sensor_nivel.nivel_suficiente():
            self.bomba.activar()
        else:
            self.bomba.desactivar()
