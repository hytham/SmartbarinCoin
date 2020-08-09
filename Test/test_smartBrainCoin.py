from unittest import TestCase

from ConfigurationManager import ConfigurationManager
from smartBrainCoin import smartBrainCoin


class TestsmartBrainCoin(TestCase):
    def test_start(self):
           bcprot = smartBrainCoin(ConfigurationManager())
