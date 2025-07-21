# physics/toroidal_repulsion.py

from z3 import Optimize, And, Or, Int, sat

def find_next_coherent_state(universe, logger):
    """Motor de física para um universo repulsivo em uma topologia toroidal (sem bordas)."""
    if len(universe.bodies) < 2:
        logger.error("Este módulo de física requer pelo menos 2 corpos.")
        return

    opt = Optimize()
    body1 = universe.bodies[0]
    body2 = universe.bodies[1]

    next_x1, next_y1 = Int(f"next_x_{body1['id']}"), Int(f"next_y_{body1['id']}")
    next_x2, next_y2 = Int(f"next_x_{body2['id']}"), Int(f"next_y_{body2['id']}")

    # --- Restrições Rígidas (Leis) ---
    for x_curr, y_curr, next_x, next_y in [(body1['x'], body1['y'], next_x1, next_y1),
                                           (body2['x'], body2['y'], next_x2, next_y2)]:
        possible_moves = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0: continue
                px = (x_curr + dx) % universe.width
                py = (y_curr + dy) % universe.height
                possible_moves.append(And(next_x == px, next_y == py))
        opt.add(Or(possible_moves))

    opt.add(Or(next_x1 != next_x2, next_y1 != next_y2))

    # --- Objetivo de Otimização (Simplificado para o Z3) ---
    dist_sq = (next_x1 - next_x2)**2 + (next_y1 - next_y2)**2
    opt.maximize(dist_sq)

    # --- Resolução ---
    if opt.check() == sat:
        model = opt.model()
        universe.update_body_position(body1['id'], model.evaluate(next_x1).as_long(), model.evaluate(next_y1).as_long())
        universe.update_body_position(body2['id'], model.evaluate(next_x2).as_long(), model.evaluate(next_y2).as_long())
    else:
        logger.warning("Otimizador não encontrou solução. Corpos permanecem estáticos.")

    return None, None