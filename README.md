# SAT-RESONATOR-GRAVITY

![Made with
Z3](https://img.shields.io/badge/Made%20with-Z3--Solver-blue?logo=python&logoColor=white)
![Powered by Pygame](https://img.shields.io/badge/Powered%20by-Pygame-green?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Universe-Expanding-purple?style=flat-square)

Um laboratório cosmológico onde a gravidade não é programada em equações diferenciais, mas **em restrições lógicas resolvidas pelo solver Z3**.  
Aqui, o universo não é simulado: ele é **provado** a cada instante.

---

## 🌐 Demo Online
[Abra a página de demo](https://alvaro-alencar.github.io/SAT-RESONATOR-GRAVITY/)

## 🌌 Demo

<p align="center">
  <img src="docs/demo.gif" alt="Simulação SAT-Resonator-Gravity em ação" width="500"/>
</p>

> *O GIF acima mostra duas massas dançando até alcançar um estado de equilíbrio lógico.*  
> O arquivo pode ser gerado automaticamente em cada run e colocado na pasta `docs/`.

---

## ⚙️ Instalação

```bash
git clone https://github.com/alvaro-alencar/SAT-RESONATOR-GRAVITY.git
cd SAT-RESONATOR-GRAVITY

python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows

pip install -r requirements.txt


---

🚀 Execução

python main.py

O sistema:

1. Lê as configurações em config.json.


2. Cria uma pasta em runs/ com logs e imagens.


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
├─ requirements.txt       # Dependências
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
        {"id":0,"x":10,"y":20,"color":[100,200,255]},
        {"id":1,"x":40,"y":20,"color":[255,100,100]}
    ],
    "logging_level": "INFO"
}


---

📖 As Crônicas

O projeto também é uma narrativa: cada salto é descrito em CRONICAS.md.
Exemplos:

O Pulso de Existência → expansão lógica do ser.

A Queda Lógica → queda livre como consequência da coerência.

A Curvatura → massas distorcem trajetórias.

A Dança Cósmica → corpos orbitam até equilíbrio.

A Formação de Ligações → estabilidade via forças opostas.



---

🌠 Roadmap

[ ] N corpos dinâmicos (N > 2)

[ ] Exportação de métricas (energia, distâncias, entropia) em CSV/JSON

[ ] Geração automática de GIFs/MP4 das runs

[ ] Interface web com FastAPI e Canvas

[ ] Paper científico unindo lógica, IA e cosmologia



---

🎨 Potencial

Educação → lógica, física e IA em sala de aula.

Pesquisa → base para artigos acadêmicos.

Arte digital → prints, vídeos, NFTs de órbitas e caos.

Produto → workshops e consultorias de simulações lógicas.



---

Autor: Álvaro Alencar
“O universo é um teorema sendo provado a cada instante.”

---

👉 O GIF (`docs/demo.gif`) pode ser gerado assim:

```bash
# grava 300 frames no Visualizer
python main.py

# converte imagens em vídeo
ffmpeg -framerate 30 -i runs/2025*/frame_%04d.png docs/demo.gif

