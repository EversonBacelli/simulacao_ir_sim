from PIL import Image
import numpy as np

# Caminho da imagem enviada
img_path = "./image.png"

# Carregar imagem em tons de cinza (RGB para detectar verde)
img = Image.open(img_path).convert("RGB")
w, h = img.size

# Converter para numpy array
data = np.array(img)

# Criar matriz binária: 1 = parede (preto), 0 = caminho (branco)
maze_matrix = np.zeros((h, w), dtype=int)
for y in range(h):
    for x in range(w):
        r, g, b = data[y, x]
        if (r, g, b) == (0, 255, 0):  # Verde -> caminho (ignorar)
            maze_matrix[y, x] = 0
        elif r < 50 and g < 50 and b < 50:  # Preto -> parede
            maze_matrix[y, x] = 1
        else:
            maze_matrix[y, x] = 0

# Montar conteúdo YAML (world + robot fixos)
yaml_content = """# labirinto_imagem.yaml
world:
  height: 51
  width: 51
  step_time: 0.1
  sample_time: 0.1
  offset: [0, 0]
  control_mode: 'acker'
  collision_mode: 'rvo'
  plot:
    show-title: True
    title: 'Robot World'
    show-axis: True
    x-label: 'X'
    y-label: 'Y'

robot:
  - number: 1
    kinematics: {name: 'omni'}
    shape: {name: 'circle', radius: 0.4}
    state: [1, 1, 0]
    goal: [23, 23, 0]
    behavior: {name: 'rvo'}
    color: 'g'
    sensors:
        - name: 'lidar2d'
          range_min: 1.0
          range_max: 5
          angle_range: 6.0
          number: 50
          noise: True
          alpha: 0.2

  - number: 1
    kinematics: {name: 'omni'}
    shape: {name: 'circle', radius: 0.4}
    state: [20, 1, 0]
    goal: [2, 23, 0]
    behavior: {name: 'rvo'}
    color: 'blue'
    sensors:
        - name: 'lidar2d'
          range_min: 0
          range_max: 10
          angle_range: 7.14
          number: 100
          noise: True
          alpha: 0.3

obstacle:
"""

# Adicionar obstáculos para cada pixel preto (1 na matriz)
for y in range(h):
    for x in range(w):
        if maze_matrix[y, x] == 1:
            yaml_content += f"  - shape: {{name: 'rectangle', length: 1.0, width: 1.0}}\n"
            yaml_content += f"    state: [{x}, {y}, 0]\n"
            yaml_content += f"    unobstructed: False\n"
            yaml_content += f"    plot: {{color: 'black'}}\n"

# Salvar YAML em arquivo
yaml_path = "/mnt/data/labirinto_imagem.yaml"
with open(yaml_path, "w") as f:
    f.write(yaml_content)

yaml_path
