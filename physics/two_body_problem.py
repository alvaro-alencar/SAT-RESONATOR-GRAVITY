# physics/two_body_problem.py

from z3 import Solver, And, Or, Int, sat

def find_next_coherent_state(universe, logger):
    """Motor de física para o problema de dois corpos, baseado na busca por um estado de menor energia."""
    if len(universe.bodies) < 2:
        logger.error("O 'two_body_problem' requer pelo menos 2 corpos definidos no config.")
        return

    s = Solver()
    body1 = universe.bodies[0]
    body2 = universe.bodies[1]

    next_x1, next_y1 = Int(f"next_x_{body1['id']}"), Int(f"next_y_{body1['id']}")
    next_x2, next_y2 = Int(f"next_x_{body2['id']}"), Int(f"next_y_{body2['id']}")

    # --- Restrições Rígidas (Leis) ---
    for x_curr, y_curr, next_x, next_y in [(body1['x'], body1['y'], next_x1, next_y1),
                                           (body2['x'], body2['y'], next_x2, next_y2)]:
        s.add(And(next_x - x_curr >= -1, next_x - x_curr <= 1))
        s.add(And(next_y - y_curr >= -1, next_y - y_curr <= 1))

    s.add(Or(next_x1 != next_x2, next_y1 != next_y2))

    dist_sq_curr = (body1['x'] - body2['x'])**2 + (body1['y'] - body2['y'])**2
    dist_sq_next = (next_x1 - next_x2)**2 + (next_y1 - next_y2)**2
    
    if dist_sq_curr > 2:
        s.add(dist_sq_next < dist_sq_curr)

    # --- Resolução ---
    if s.check() == sat:
        model = s.model()
        universe.update_body_position(body1['id'], model.evaluate(next_x1).as_long(), model.evaluate(next_y1).as_long())
        universe.update_body_position(body2['id'], model.evaluate(next_x2).as_long(), model.evaluate(next_y2).as_long())
    else:
        logger.warning("Não foi encontrado um estado melhor. Corpos entram em equilíbrio.")

    return None, None