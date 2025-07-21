# physics/gravity_slingshot.py

from z3 import Optimize, And, Or, Int, sat

def find_next_coherent_state(universe, logger):
    """
    Motor de física para uma partícula (pedra) sendo desviada por uma massa estática.
    Usa o Princípio da Mínima Ação para encontrar a trajetória ótima.
    """
    # Este motor de física espera uma configuração diferente, com 'bodies' e 'masses'
    # Vamos adaptar para a nova estrutura de 'bodies'
    if len(universe.bodies) < 2:
        logger.error("Slingshot requer 2 corpos: um como 'pedra', outro como 'massa'.")
        return None, None

    opt = Optimize()
    
    # Por convenção, o primeiro corpo é a pedra, o segundo é a massa
    stone = universe.bodies[0]
    mass = universe.bodies[1]
    
    x_curr, y_curr = stone['x'], stone['y']
    mass_x, mass_y = mass['x'], mass['y']

    next_x, next_y = Int(f"next_x_{stone['id']}"), Int(f"next_y_{stone['id']}")

    # --- Restrições Rígidas (Leis) ---
    # 1. Localidade: a pedra só pode se mover para uma célula adjacente.
    opt.add(And(next_x >= 0, next_x < universe.width))
    opt.add(And(next_y >= 0, next_y < universe.height))
    opt.add(And(next_x - x_curr >= -1, next_x - x_curr <= 1))
    opt.add(And(next_y - y_curr >= -1, next_y - y_curr <= 1))
    opt.add(Or(next_x != x_curr, next_y != y_curr)) # Não pode ficar parado
    
    # 2. Exclusão: a pedra não pode ocupar o espaço da massa.
    opt.add(Or(next_x != mass_x, next_y != mass_y))

    # --- Objetivo de Otimização ---
    # Minimizar a distância até a massa.
    dist_sq = (next_x - mass_x)**2 + (next_y - mass_y)**2
    opt.minimize(dist_sq)

    # --- Resolução ---
    if opt.check() == sat:
        model = opt.model()
        new_x = model.evaluate(next_x).as_long()
        new_y = model.evaluate(next_y).as_long()
        logger.info(f"Decisão do Instante: Pedra moveu-se de ({x_curr}, {y_curr}) -> ({new_x}, {new_y})")
        universe.update_body_position(stone['id'], new_x, new_y)
    else:
        logger.warning("Otimizador não encontrou solução. Pedra permanece estática.")

    # A massa permanece fixa neste modelo de física
    return None, None