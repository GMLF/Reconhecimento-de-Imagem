import cv2

#Lendo a imagem
img = cv2.imread('../Videos_e_Imagens/farol.jpg')

#Convertendo a imagem de RGB para 2 canais (cinza)
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#Extraindo as dimensões das imagens em pixel's e canais
print(img.shape)
print(imgCinza.shape)

#Exibe a imagem na tela (renderiza)
cv2.imshow('Imagem',img)
cv2.imshow('Imagem Cinza',imgCinza)

#Travando a tela para não abrir e fechar
cv2.waitKey(0)