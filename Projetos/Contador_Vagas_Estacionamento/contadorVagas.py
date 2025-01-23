import cv2
import pickle
import numpy as np

vagas = []

# Carrega as coordenadas das vagas previamente salvas em um arquivo
with open('vagas.pkl', "+rb") as arquivo:
    vagas = pickle.load(arquivo)

# Carrega o vídeo que será usado para monitorar as vagas
video = cv2.VideoCapture('../Contador_Vagas_Estacionamento/dados/video.mp4')

# Verifica se o vídeo foi carregado corretamente
if not video.isOpened():
    print("Erro ao carregar o vídeo!")
    exit()

while True:
    # Lê um frame do vídeo
    check, img = video.read()

    # Converte o frame para escala de cinza
    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplica limiarização adaptativa para destacar áreas de interesse
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    # Aplica filtro de mediana para suavizar a imagem e reduzir ruídos
    imgMedian = cv2.medianBlur(imgTh, 5)

    # Cria um kernel para realizar a operação de dilatação
    Kernel = np.ones((3, 3), np.int8)

    # Aplica a dilatação para aumentar as áreas brancas
    imgDil = cv2.dilate(imgMedian, Kernel)

    vagasAbertas = 0  # Contador de vagas livres


    for x, y, w, h in vagas:
        # Obtém a região de interesse (ROI) da vaga na imagem processada
        vaga = imgDil[y:y + h, x:x + w]

        # Conta os pixels brancos na ROI (indicativo de espaço ocupado)
        count = cv2.countNonZero(vaga)

        # Exibe a contagem de pixels brancos sobre a vaga
        cv2.putText(img, str(count), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Desenha um retângulo azul em torno da vaga
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Determina se a vaga está livre ou ocupada com base no número de pixels brancos
        if count < 770:
            # Vaga livre (retângulo verde)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            vagasAbertas += 1  # Incrementa o contador de vagas livres
        else:
            # Vaga ocupada (retângulo vermelho)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Exibe o número total de vagas livres na tela
        cv2.rectangle(img, (90, 0), (415, 60), (0, 255, 0), -1)  # Fundo verde
        cv2.putText(img, f'Livres: {vagasAbertas}|69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    # Exibe o vídeo com as vagas marcadas e as informações
    cv2.imshow("Video", img)
    cv2.waitKey(10)
