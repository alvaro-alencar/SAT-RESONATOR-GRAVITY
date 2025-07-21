# physics/molecular_dynamics.py

from z3 import Optimize, And, Or, Int, sat, Real, ToReal, RealVal

def find_next_coherent_state(universe, logger):
    """
    Motor de física que simula uma dinâmica molecular simplificada (Potencial de Lennard-Jones).
    Os corpos se repelem a curta distância e se atraem a média distância. (Versão lenta)
    """
    if len(universe.bodies) < 2:
        logger.error("Este módulo de física requer pelo menos 2 corpos.")
        return

    opt = Optimize()
    body1 = universe.bodies[0]
    body2 = universe.bodies[1]

    next_x1, next_y1 = Int(f"next_x_{body1['id']}"), Int(f"next_y_{body1['id']}")
    next_x2, next_y2 = Int(f"next_x_{body2['id']}"), Int(f"next_y_{body2['id']}")

    # --- Restrições Rígidas ---
    for x_curr, y_curr, next_x, next_y in [(body1['x'], body1['y'], next_x1, next_y1),
                                           (body2['x'], body2['y'], next_x2, next_y2)]:
        opt.add(And(next_x >= 0, next_x < universe.width))
        opt.add(And(next_y >= 0, next_y < universe.height))
        opt.add(And(next_x - x_curr >= -1, next_x - x_curr <= 1))
        opt.add(And(next_y - y_curr >= -1, next_y - y_curr <= 1))

    opt.add(Or(next_x1 != next_x2, next_y1 != next_y2))

    # --- Objetivo de Otimização ---
    r_next_x1, r_next_y1 = ToReal(next_x1), ToReal(next_y1)
    r_next_x2, r_next_y2 = ToReal(next_x2), ToReal(next_y2)

    dist_sq_real = (r_next_x1 - r_next_x2)**2 + (r_next_y1 - r_next_y2)**2

    repulsion_factor = RealVal("100000.0")
    attraction_factor = RealVal("-1000.0")
    epsilon = RealVal("0.001")

    repulsion = repulsion_factor / (dist_sq_real * dist_sq_real + epsilon)
    attraction = attraction_factor / (dist_sq_real + epsilon)
    
    potential_energy = attraction + repulsion
    
    opt.minimize(potential_energy)
    
    # --- Resolução ---
    if opt.check() == sat:
        model = opt.model()
        universe.update_body_position(body1['id'], model.evaluate(next_x1).as_long(), model.evaluate(next_y1).as_long())
        universe.update_body_position(body2['id'], model.evaluate(next_x2).as_long(), model.evaluate(next_y2).as_long())
    else:
        logger.warning("Otimizador não encontrou solução. Corpos em equilíbrio ou presos.")

    return None, None