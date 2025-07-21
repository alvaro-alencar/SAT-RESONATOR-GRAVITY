# timeline.py

class Timeline:
    def __init__(self, universe, physics_engine, logger):
        self.universe = universe
        self.physics_engine = physics_engine
        self.logger = logger

    def step(self):
        self.physics_engine.find_next_coherent_state(self.universe, self.logger)