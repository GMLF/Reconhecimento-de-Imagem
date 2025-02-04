import cv2
from cvzone.PoseModule import PoseDetector
import cvzone

#Abrindo vídeo
video = cv2.VideoCapture('../Detector_Quedas/dados/quedas.mp4')

# Modelo de Detecção com Kill point's
detector = PoseDetector()

while True:
    #Rodando os vídeos
    check,play = video.read()

    #Redimensionando janela
    play = cv2.resize(play,(1280,720))

    resultado = detector.findPose(play)

    pontos,bbox = detector.findPosition(play,draw=False)

    #Se for menor que 1, não tem pessoa identificada no vídeo
    if len(pontos) >=1:

        x,y,w,h = bbox['bbox']

        #Pegando coordenadas cabeça e joelhos, EM pé a posição da cabeça é menor que o joelho, quando queda inverte
        cabeca = pontos[0]  [1]
        joelho = pontos[26] [1]

        queda = joelho - cabeca

        #Se for negativa, houve queda detectada
        if queda <= 0:
            cvzone.putTextRect(play,"A queda foi detectada",(x,y-80),scale=3,thickness=3,colorR=(0,0,255))


    cv2.imshow("Video",play)
    cv2.waitKey(1)
