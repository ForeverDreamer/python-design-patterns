from factories import loader

for factory_name in 'chevy_factory', 'jeep_factory', 'ford_factory', 'tesla_factory':

    factorys = loader.load_factory(factory_name)
    for factory in factorys:
        car = factory.create_auto()
        car.start()
        car.stop()
