import cv2

# Carrega o vídeo
video = cv2.VideoCapture('../Videos_e_Imagens/runners.mp4')

# Laço infinito para exibir os frames do vídeo até que o usuário feche a janela
while True:
    # Lê o próximo frame do vídeo e armazena a imagem na variável 'img'
    check, img = video.read()

    # Imprime as dimensões do frame atual (altura, largura, canais de cor)
    print(img.shape)

    # Redimensiona o frame para o tamanho de 640x420 pixels
    imgRedim = cv2.resize(img, (640, 420))

    # Exibe o frame redimensionado em uma janela chamada 'video'
    cv2.imshow('video', imgRedim)

    # Aguarda 10 milissegundos pela pressionamento de uma tecla
    cv2.waitKey(10)
