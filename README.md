# SAT-RESONATOR-GRAVITY

Um laboratório cosmológico onde a gravidade não é programada em equações diferenciais, mas **em restrições lógicas resolvidas pelo solver Z3**.  
Aqui, o universo não é simulado: ele é **provado** a cada instante.

---

## 🌌 Conceito

O projeto explora a ideia de que **as leis da física podem emergir da coerência lógica**.  
Cada passo no tempo é o resultado de um sistema SAT/SMT decidindo qual é o próximo estado válido do cosmos.  

Isso permite criar mundos onde:

- A **queda livre** de um corpo acontece porque é a **única solução lógica**.  
- A **curvatura do espaço-tempo** é um viés lógico que distorce trajetórias.  
- **Órbitas e ligações** emergem de potenciais lógicos (como Lennard-Jones).  
- A **topologia do universo** (caixa, toro, infinito) muda o destino da simulação.  

---

## ⚙️ Instalação

Clone o repositório e crie um ambiente virtual:

```bash
git clone https://github.com/alvaro-alencar/SAT-RESONATOR-GRAVITY.git
cd SAT-RESONATOR-GRAVITY

python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows

pip install -r requirements.txt


---

🚀 Execução

Execute a simulação com:

python main.py

O sistema:

1. Lê as configurações em config.json.


2. Cria uma pasta em runs/ com os logs e imagens da execução.


3. Abre uma janela com a simulação em tempo real (pygame).


4. Salva o estado final em final_state.png.




---

🗂️ Estrutura do Projeto

SAT-RESONATOR-GRAVITY/
├─ physics/               # Motores de física (gravidade, Lennard-Jones, etc.)
├─ universe.py            # Estado global do cosmos
├─ node.py                # Definição dos corpos/nós
├─ timeline.py            # Avanço do tempo lógico
├─ visualizer.py          # Visualização em pygame
├─ logger.py              # Logs em console e arquivo
├─ main.py                # Orquestração da simulação
├─ config.json            # Configuração de cada run
├─ requirements.txt       # Dependências (z3-solver, pygame)
├─ CRONICAS.md            # Diário filosófico das descobertas
└─ runs/                  # Execuções com logs e imagens


---

🛠️ Configuração

Exemplo de config.json:

{
    "simulation_name": "Fast_Molecular_Dynamics_01",
    "width": 50,
    "height": 40,
    "steps": 300,
    "physics_module": "fast_molecular_dynamics",
    "bodies": [
        {
            "id": 0,
            "x": 10,
            "y": 20,
            "color": [100, 200, 255],
            "trail_color": [100, 200, 255, 100],
            "radius_factor": 0.3,
            "vis_config": {"cell_size": 15}
        },
        {
            "id": 1,
            "x": 40,
            "y": 20,
            "color": [255, 100, 100],
            "trail_color": [255, 100, 100, 100],
            "radius_factor": 0.3
        }
    ],
    "logging_level": "INFO"
}


---

📖 As Crônicas

A cada salto conceitual, escrevemos uma Crônica do Universo Coerente em CRONICAS.md.
Alguns marcos já registrados:

1. O Pulso de Existência → a expansão lógica do ser.


2. A Queda Lógica → um corpo cai porque não há outra solução.


3. A Curvatura → a massa distorce o espaço-tempo lógico.


4. A Dança Cósmica → corpos interagem e buscam equilíbrio.


5. A Natureza do Espaço → topologia define o destino final.


6. A Formação de Ligações → forças opostas geram estabilidade.



Cada crônica corresponde a uma fase do código e um commit histórico.


---

🌠 Roadmap

[ ] Suporte a múltiplos corpos dinâmicos (N > 2)

[ ] Exportação de métricas (energia, distâncias, entropia) em CSV/JSON

[ ] Geração automática de GIFs/MP4 das runs

[ ] Interface web com FastAPI e Canvas

[ ] Paper científico unindo lógica, IA e cosmologia



---

🎨 Potencial

Este repositório não é apenas código: é obra científica e artística.
Pode ser usado como:

Ferramenta educacional (ensino de lógica, física, IA).

Motor de experimentos em computação simbólica.

Base para artigos acadêmicos.

Fonte de arte digital (órbitas, colisões, caos).



---

Autor: Álvaro Alencar
“O universo é um teorema sendo provado a cada instante.”

---

