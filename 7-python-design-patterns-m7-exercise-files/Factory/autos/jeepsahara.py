from .abs_auto import AbsAuto


class JeepSahara(AbsAuto):

	def start(self):
		print('%s running ruggedly.' % self.name)

	def stop(self):
		print('%s shutting down.' % self.name)