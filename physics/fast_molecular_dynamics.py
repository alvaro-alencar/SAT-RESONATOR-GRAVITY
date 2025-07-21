# physics/fast_molecular_dynamics.py

from z3 import Optimize, And, Or, Int, sat, unknown

def find_next_coherent_state(universe, logger):
    """
    Uma versão otimizada da dinâmica molecular, com um timeout para garantir a responsividade.
    """
    if len(universe.bodies) < 2:
        return

    opt = Optimize()
    
    # NOVA LEI: TIMEOUT DE 5 SEGUNDOS (5000 ms)
    # Se o solver não encontrar uma solução neste tempo, ele irá parar.
    opt.set("timeout", 5000)

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
    
    dist_sq = (next_x1 - next_x2)**2 + (next_y1 - next_y2)**2
    
    equilibrium_dist_sq = 100
    potential_energy = (dist_sq - equilibrium_dist_sq)**2

    opt.minimize(potential_energy)
    
    # --- Resolução ---
    check_result = opt.check()

    if check_result == sat:
        model = opt.model()
        final_energy = model.evaluate(potential_energy).as_long()
        logger.info(f"Energia potencial do sistema resolvida para: {final_energy}")
        universe.update_body_position(body1['id'], model.evaluate(next_x1).as_long(), model.evaluate(next_y1).as_long())
        universe.update_body_position(body2['id'], model.evaluate(next_x2).as_long(), model.evaluate(next_y2).as_long())
    elif check_result == unknown:
        logger.warning("TIMEOUT! O cálculo foi muito complexo. Corpos permanecem estáticos neste instante.")
        # Não faz nada, os corpos ficam parados.
    else:
        logger.warning("Otimizador não encontrou solução. Corpos em equilíbrio ou presos.")

    return None, None