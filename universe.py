# universe.py

class Universe:
    def __init__(self, config, logger):
        self.width = config['width']
        self.height = config['height']
        self.logger = logger
        
        self.bodies = config.get('bodies', [])
        for i, body in enumerate(self.bodies):
            body['id'] = i

        self.history = []
        self.logger.info(f"Universo inicializado com {len(self.bodies)} corpos.")

    def get_body(self, body_id):
        for body in self.bodies:
            if body['id'] == body_id:
                return body
        return None

    def update_body_position(self, body_id, new_x, new_y):
        body = self.get_body(body_id)
        if body:
            body['x'] = new_x
            body['y'] = new_y
        else:
            self.logger.warning(f"Tentativa de atualizar a posição do corpo com ID inexistente: {body_id}")