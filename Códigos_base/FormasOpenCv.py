import cv2

img = cv2.imread('../videos_e_Imagens/piramide.jpg')

#Video
video = cv2.VideoCapture('../videos_e_Imagens/runners.mp4')

while True:

    check,corrida = video.read()

    #Criando objeto retangulo na imagem (image, pixel que começa, pixel que termina, código de cor e espessura
    cv2.rectangle(img,(50,50),(200,200),(255,0,0),4)

    #circulo (imagem) (inicio do circulo) (raio) (cor) (espessura)
    cv2.circle(img,(300,300),50,(0,0,255),3)

    #Linha (imagem) (inicio) (termino) (cor) (espessura)
    cv2.line(img,(400,400),(500,400),(0,255,0),3)

    #inserindo texto
    cv2.putText(img,"Piramide do Egito",(200,200),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)

    # inserindo texto
    cv2.putText(corrida, "Corrida", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

    cv2.imshow("Piramide",img)
    cv2.imshow("Corrida", corrida)

    cv2.waitKey(1)