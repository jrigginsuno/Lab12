import pytest
from television import *

class Test:
	def setup_method(self):
		self.tv = Television()

	def teardown_method(self):
		del self.tv

	def test_init(self):
		assert self.tv.get_status() == False
		assert self.tv.get_channel() == Television.MIN_CHANNEL
		assert self.tv.get_volume() == Television.MIN_VOLUME

	def test_power(self):
		self.tv.power()
		assert self.tv.get_status() == True
		self.tv.power()
		assert self.tv.get_status() == False

	def test_mute(self):
		self.tv.power()
		self.tv.volume_up()
		self.tv.mute()
		assert self.tv.get_muted() == True

		self.tv.mute()
		assert self.tv.get_muted() == False


		self.tv.power()
		self.tv.mute()
		assert self.tv.get_muted() == False

		self.tv.power()
		self.tv.mute()
		assert self.tv.get_muted() == True

	def test_channel_up(self):
		self.tv.channel_up()
		assert self.tv.get_channel() == 0

		self.tv.power()
		self.tv.channel_up()
		assert self.tv.get_channel() == 1

		for _ in range(3):
			self.tv.channel_up()
		assert self.tv.get_channel() == 0

	def test_channel_down(self):
		self.tv.channel_down()
		assert self.tv.get_channel() == 0

		self.tv.power()
		self.tv.channel_down()
		assert self.tv.get_channel() == 3

	def test_volume_up(self):
		self.tv.volume_up()
		assert self.tv.get_volume() == 0

		self.tv.power()
		self.tv.volume_up()
		assert self.tv.get_volume() == 1

		self.tv.mute()
		self.tv.volume_up()
		assert self.tv.get_volume() == 2

		self.tv.volume_up()
		assert self.tv.get_volume() == 2

	def test_volume_down(self):
		self.tv.volume_down()
		assert self.tv.get_volume() == 0

		self.tv.power()
		for _ in range(3):
			self.tv.volume_up()
		self.tv.volume_down()
		assert self.tv.get_volume() == 1

		self.tv.mute()
		self.tv.volume_down()
		assert self.tv.get_volume() == 0
