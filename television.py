class Television:
	'''
	A class representing details for a television object.
	'''
	MIN_VOLUME: int = 0
	MAX_VOLUME: int = 2
	MIN_CHANNEL: int = 0
	MAX_CHANNEL: int  = 3

	def __init__(self):
		'''
		Sets default values
		'''
		self.__status: bool = False
		self.__muted: bool = False
		self.__volume: int = self.MIN_VOLUME
		self.__saved_volume: int = self.MIN_VOLUME
		self.__channel: int = self.MIN_CHANNEL

	def power(self):
		'''
		Turns the power on
		'''
		self.__status = not self.__status

	def mute(self):
		'''
		Mutes the volume
		'''
		if self.__status:
			if self.__muted:
				self.__volume = self.__saved_volume
			if not self.__muted:
				self.__saved_volume = self.__volume
				self.__volume = self.MIN_VOLUME
			self.__muted = not self.__muted

	def channel_up(self):
		'''
		Increases the channel
		'''
		if self.__status:
			if self.__muted:
				self.__volume = self.__saved_volume
				self.__muted = False
			elif self.__channel == self.MAX_CHANNEL:
				self.__channel = self.MIN_CHANNEL
			else:
				self.__channel += 1

	def channel_down(self):
		'''
		Decreases the channel
		'''
		if self.__status:
			if self.__channel == self.MIN_CHANNEL:
				self.__channel = self.MAX_CHANNEL
			else:
				self.__channel -= 1

	def volume_up(self):
		'''
		Increases the volume
		'''
		if self.__status:
			if self.__muted:
				self.__muted = not self.__muted
				self.__volume = self.__saved_volume
			if self.__volume != self.MAX_VOLUME:
				self.__volume += 1

	def volume_down(self):
		'''
		Decreases  the volume
		'''
		if self.__status:
			if self.__muted:
				self.__muted = not self.__muted
				self.__volume = self.__saved_volume
			if self.__volume != self.MIN_VOLUME:
				self.__volume -= 1

	def get_volume(self):
		if self.__muted:
			return 0
		else:
			return self.__volume

	def __str__(self):
		return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
