# main.py

import json
import importlib
import os
import datetime
import pygame
import threading # Importamos a biblioteca de threading
import time
from universe import Universe
from timeline import Timeline
from visualizer import Visualizer
from logger import setup_logger

# --- Variáveis Globais para comunicação entre Threads ---
simulation_state = {
    "universe": None,
    "is_calculating": False,
    "new_state_ready": False,
    "step_count": 0
}

def worker_thread_logic(timeline, steps, logger):
    """
    Esta função é o "cérebro". Ela roda em uma thread separada.
    """
    for i in range(steps):
        simulation_state["is_calculating"] = True
        logger.info(f"--- [CÉREBRO] Calculando Instante {i + 1} ---")
        
        timeline.step() # O cálculo pesado acontece aqui
        
        simulation_state["step_count"] = i + 1
        simulation_state["is_calculating"] = False
        simulation_state["new_state_ready"] = True
        
        # Espera até que a thread principal processe o resultado
        while simulation_state["new_state_ready"]:
            time.sleep(0.01)

    logger.info("--- [CÉREBRO] Todos os passos calculados. Encerrando a thread. ---")
    simulation_state["is_calculating"] = 'done'


def main():
    config = load_config()
    run_path = setup_run_directory(name=config['simulation_name'])
    log_file_path = os.path.join(run_path, "simulation.log")
    logger = setup_logger(config.get("logging_level", "INFO"), log_file_path)

    logger.info(f"--- [PRINCIPAL] Iniciando Simulação: {config['simulation_name']} ---")
    
    # --- Setup ---
    try:
        physics_module_name = f"physics.{config['physics_module']}"
        physics_engine = importlib.import_module(physics_module_name)
        logger.info(f"Módulo de física '{physics_module_name}' carregado.")
    except ImportError as e:
        logger.error(f"Não foi possível carregar o módulo de física: {e}")
        return
        
    u = Universe(config, logger)
    t = Timeline(u, physics_engine, logger)
    v = Visualizer(u)
    
    simulation_state["universe"] = u
    
    # --- Inicia a Thread do Cérebro ---
    worker = threading.Thread(target=worker_thread_logic, args=(t, config['steps'], logger))
    worker.start()

    # --- Loop Principal (O "Corpo") ---
    running = True
    while running:
        if not v.process_events():
            running = False
            break

        # Se o cérebro terminou de calcular, atualizamos o visual
        if simulation_state["new_state_ready"]:
            v.update_display()
            simulation_state["new_state_ready"] = False

        # Atualiza o título da janela para dar feedback
        if simulation_state["is_calculating"] == True:
            v.set_caption(f"Calculando Instante {simulation_state['step_count'] + 1}...")
        elif simulation_state["is_calculating"] == 'done':
             v.set_caption("Simulação Completa!")
        else:
            v.set_caption("Laboratório Cosmológico (Aguardando próximo cálculo)")
        
        # Mesmo que o cérebro esteja pensando, o corpo continua se atualizando
        v.update_display()

        if not worker.is_alive() and simulation_state["is_calculating"] != 'done':
            # Se a thread morreu inesperadamente
            logger.error("A thread de cálculo parou de funcionar.")
            running = False
    
    # --- Finalização ---
    if worker.is_alive():
        # Idealmente, teríamos um mecanismo para parar a thread graciosamente
        logger.info("Aguardando a finalização da thread de cálculo...")
    
    final_image_path = os.path.join(run_path, "final_state.png")
    v.save_final_state(final_image_path)
    logger.info(f"Imagem final salva em: {final_image_path}")

    pygame.quit()
    logger.info(f"--- Simulação Terminada ---")


def load_config(path="config.json"):
    with open(path, 'r') as f:
        return json.load(f)

def setup_run_directory(base_dir="runs", name=""):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_name = f"{timestamp}_{name}"
    run_path = os.path.join(base_dir, run_name)
    os.makedirs(run_path, exist_ok=True)
    return run_path

if __name__ == "__main__":
    main()