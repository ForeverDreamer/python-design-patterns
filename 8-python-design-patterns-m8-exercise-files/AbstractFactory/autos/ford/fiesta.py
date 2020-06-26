from autos.abs_auto import AbsAuto


class FordFiesta(AbsAuto):

	@staticmethod
	def start():
		print('Ford Fiesta running cheaply.')

	@staticmethod
	def stop():
		print('Ford Fiestashutting down.')
