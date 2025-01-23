import cv2
import pickle
import numpy as np

vagas = []

# Carrega as coordenadas das vagas a partir do arquivo 'vagas.pkl'
with open('vagas.pkl', "+rb") as arquivo:
    vagas = pickle.load(arquivo)

# Carrega o vídeo do estacionamento
video = cv2.VideoCapture('../Contador_Vagas_Estacionamento/dados/video.mp4')


while True:
    # Lê um frame do vídeo
    check, img = video.read()

    # Verifica se o frame foi lido corretamente
    if not check:
        print("Fim do vídeo ou erro na leitura do frame!")
        break

    # Converte o frame para escala de cinza
    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplica limiarização adaptativa para separar objetos do fundo
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    # Aplica um filtro de mediana para reduzir o ruído na imagem
    imgMedian = cv2.medianBlur(imgTh, 5)

    # Cria um kernel 3x3 para a operação de dilatação
    Kernel = np.ones((3, 3), np.int8)

    # Aplica dilatação para ampliar as áreas de interesse
    imgDil = cv2.dilate(imgMedian, Kernel)

    vagasAbertas = 0

    # Loop para verificar as vagas, baseado nas coordenadas salvas
    for x, y, w, h in vagas:
        # Recorta a região correspondente à vaga
        vaga = imgDil[y:y + h, x:x + w]

        # Conta os pixels brancos na imagem da vaga (indicativo de ocupação)
        count = cv2.countNonZero(vaga)

        # Adiciona o valor da contagem na imagem (para visualização)
        cv2.putText(img, str(count), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Desenha um retângulo azul em torno da vaga
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Se a vaga estiver livre (menos de 770 pixels brancos), marca em verde
        if count < 770:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            vagasAbertas += 1
        else:
            # Se a vaga estiver ocupada, marca em vermelho
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Adiciona o número de vagas livres na parte superior da tela
        cv2.rectangle(img, (90, 0), (415, 60), (0, 255, 0), -1)
        cv2.putText(img, f'Livres: {vagasAbertas}|69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    # Exibe a imagem com as marcações sobre o vídeo
    cv2.imshow("Video", img)
    cv2.waitKey(10)
