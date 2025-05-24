# Pruebas TTD
import unittest
from Sistema_riego_v2 import SensorHumedad, SensorNivelAgua, BombaAgua, SistemaRiego

class PruebasSistemaRiego(unittest.TestCase):
    def test_sensor_humedad(self):
        sensor = SensorHumedad(45)
        self.assertEqual(sensor.leer_humedad(), 45)

    def test_sensor_nivel_agua(self):
        sensor = SensorNivelAgua(True)
        self.assertTrue(sensor.nivel_suficiente())

    def test_bomba_agua(self):
        bomba = BombaAgua()
        bomba.activar()
        self.assertTrue(bomba.esta_activa())
        bomba.desactivar()
        self.assertFalse(bomba.esta_activa())

    def test_integracion_activar_bomba(self):
        sensor_humedad = SensorHumedad(20)
        sensor_nivel = SensorNivelAgua(True)
        bomba = BombaAgua()
        sistema = SistemaRiego(sensor_humedad, sensor_nivel, bomba)
        sistema.evaluar_y_regar()
        self.assertTrue(bomba.esta_activa())

    
    def test_activar_bomba_con_umbral_personalizado(self):
        sensor_humedad = SensorHumedad(32)
        sensor_nivel = SensorNivelAgua(True)
        bomba = BombaAgua()
        sistema = SistemaRiego(sensor_humedad, sensor_nivel, bomba, umbral_humedad=40)  # umbral cambiado
        sistema.evaluar_y_regar()
        self.assertTrue(bomba.esta_activa())

if __name__ == "__main__":
    unittest.main() 