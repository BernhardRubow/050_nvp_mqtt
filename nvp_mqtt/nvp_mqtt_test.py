import unittest
from nvp_mqtt import nvp_mqtt as mqtt_client

class nvp_mqtt_unittest(unittest.TestCase):

  def test_can_instantiate(self):
    mqtt = mqtt_client()
    self.assertIsNotNone(mqtt)

  def test_default_values_are_set_properble(self):
    mqtt = mqtt_client()
    self.assertEqual(mqtt.broker_address, '')
    self.assertEqual(mqtt.clientId, '')
    self.assertEqual(mqtt.username, '')
    self.assertEqual(mqtt.password, '')
    self.assertEqual(mqtt.port, 0)
    self.assertEqual(mqtt.last_will_topic, '')


  def test_setting_config_values(self):
    config = {
      'broker_address':'test@test.de',
      'port': 7350,
      'username':'johndoe',
      'password':'1234',
      'last_will_topic': "sensors/sensor_id/state",
      'clientId': "sensor_id"
    }

    mqtt = mqtt_client(**config)

    self.assertEqual(mqtt.broker_address, config['broker_address'])
    self.assertEqual(mqtt.username, config['username'])
    self.assertEqual(mqtt.password, config['password'])
    self.assertEqual(mqtt.last_will_topic, config['last_will_topic'])
    self.assertEqual(mqtt.port, config['port'])
    self.assertEqual(mqtt.clientId, config['clientId'])



if __name__ == "__main__": 
    unittest.main()