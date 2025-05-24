import unittest
from Sistema_riego import SensorHumedad, SensorNivelAgua, BombaAgua, SistemaRiego
class PruebasSistemaRiego(unittest.TestCase):
    def test_integracion_no_activar_bomba_por_humedad_alta(self):
        sensor_humedad = SensorHumedad(40)
        sensor_nivel = SensorNivelAgua(True)
        bomba = BombaAgua()
        sistema = SistemaRiego(sensor_humedad, sensor_nivel, bomba)
        sistema.evaluar_y_regar()
        self.assertFalse(bomba.esta_activa())

    def test_integracion_no_activar_bomba_por_falta_de_agua(self):
        sensor_humedad = SensorHumedad(20)
        sensor_nivel = SensorNivelAgua(False)
        bomba = BombaAgua()
        sistema = SistemaRiego(sensor_humedad, sensor_nivel, bomba)
        sistema.evaluar_y_regar()
        self.assertFalse(bomba.esta_activa())
        
if __name__ == "__main__":
    unittest.main() 