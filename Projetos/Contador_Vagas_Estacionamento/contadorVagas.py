import cv2
import pickle
import numpy as np

vagas = []

# Carrega as vagas a partir do arquivo
with open('vagas.pkl', "+rb") as arquivo:
    vagas = pickle.load(arquivo)

# Carrega o vídeo
video = cv2.VideoCapture('../Contador_Vagas_Estacionamento/dados/video.mp4')

# Verifica se o vídeo foi carregado corretamente
if not video.isOpened():
    print("Erro ao carregar o vídeo!")
    exit()

while True:
    check, img = video.read()

    # Verifica se o frame foi lido corretamente
    if not check:
        print("Fim do vídeo ou erro na leitura do frame!")
        break

    # Converte a imagem para escala de cinza
    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplica a limiarização adaptativa
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    # Aplica o filtro de mediana
    imgMedian = cv2.medianBlur(imgTh, 5)

    # Cria o kernel para dilatação
    Kernel = np.ones((3, 3), np.int8)

    # Aplica a dilatação
    imgDil = cv2.dilate(imgMedian, Kernel)

    vagasAbertas = 0

    # Loop para verificar as vagas
    for x, y, w, h in vagas:
        vaga = imgDil[y:y + h, x:x + w]

        # Conta os pixels brancos na imagem da vaga
        count = cv2.countNonZero(vaga)
        cv2.putText(img, str(count), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Verifica se a vaga está livre
        if count < 770:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            vagasAbertas += 1
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Exibe o número de vagas livres
        cv2.rectangle(img, (90, 0), (415, 60), (0, 255, 0), -1)
        cv2.putText(img, f'Livres: {vagasAbertas}|69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    # Exibe as imagens
    cv2.imshow("Video", img)
    cv2.waitKey(10)
