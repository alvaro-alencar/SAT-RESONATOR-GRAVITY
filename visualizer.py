# visualizer.py

import pygame

COLOR_BLACK = (10, 12, 15)
COLOR_GRID = (40, 42, 45)

class Visualizer:
    def __init__(self, universe):
        pygame.init()
        self.universe = universe
        body_config = universe.bodies[0] if universe.bodies else {}
        vis_config = body_config.get('vis_config', {})
        self.cell_size = vis_config.get('cell_size', 20)
        
        self.width = universe.width * self.cell_size
        self.height = universe.height * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.set_caption("Laboratório Cosmológico")
        self.trails = {body['id']: [] for body in self.universe.bodies}

    def set_caption(self, text):
        pygame.display.set_caption(text)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (self.width, y))

    def draw_elements(self):
        for body in self.universe.bodies:
            body_id = body['id']
            pos = (body['x'], body['y'])
            if not self.trails[body_id] or self.trails[body_id][-1] != pos:
                self.trails[body_id].append(pos)

            if len(self.trails[body_id]) > 1:
                pygame.draw.lines(self.screen, tuple(body.get('trail_color', (50,50,50))), False, 
                                  [(x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2) for x, y in self.trails[body_id]], 1)

            center = (pos[0] * self.cell_size + self.cell_size // 2, pos[1] * self.cell_size + self.cell_size // 2)
            color = tuple(body.get('color', (255,255,255)))
            radius = body.get('radius_factor', 0.3) * self.cell_size
            pygame.draw.circle(self.screen, color, center, radius)

    def update_display(self):
        self.screen.fill(COLOR_BLACK)
        self.draw_grid()
        self.draw_elements()
        pygame.display.flip()
    
    def save_final_state(self, path):
        pygame.image.save(self.screen, path)