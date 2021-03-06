__author__ = 'yuanchun'
import unittest
from droidbot.droidbot import DroidBot


class TestDroidBot(unittest.TestCase):
    def setUp(self):
        self.droidbot = DroidBot(device_serial="emulator-5554")

    def test_init(self):
        self.assertIsNotNone(self.droidbot.app)
        self.assertIsNotNone(self.droidbot.device)
        self.assertIsNotNone(self.droidbot.env_manager)
        self.assertIsNotNone(self.droidbot.event_manager)

    def test_start(self):
        self.droidbot.start()
        self.assertTrue(self.droidbot.device.is_connected())
        self.assertIsNotNone(self.droidbot.app)
