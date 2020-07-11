from unittest import TestCase

from ConfigurationManager import ConfigurationManager


class TestConfigurationManager(TestCase):
    def test_get(self):
        config = ConfigurationManager(config_filepath='../../config.json')
        self.assertIsNotNone(config)
        
        self.assertEqual("127.0.0.1",config.get("p2p")["seed_peers"][0])
