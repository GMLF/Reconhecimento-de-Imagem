# Importa bibliotecas
import cv2
import pickle

# Carrega a imagem
img = cv2.imread('../Contador_Vagas_Estacionamento/dados/estacionamento.png')

# Cria lista para armazenar as vagas
vagas = []

# Laço para selecionar 69 vagas
for x in range(69):

    # Permite ao usuário selecionar uma vaga (ROI)
    vaga = cv2.selectROI('vagas', img, False)

    # Fecha a janela de seleção
    cv2.destroyWindow('vagas')

    # Armazena a coordenada da vaga
    vagas.append((vaga))

    # Desenha retângulo em torno da vaga selecionada
    for x, y, w, h in vagas:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Salva as coordenadas das vagas em um arquivo
with open('vagas.pkl', 'wb') as arquivo:
    pickle.dump(vagas, arquivo)


