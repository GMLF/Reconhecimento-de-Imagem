import cv2

img = cv2.imread("../Videos_e_Imagens/img01.jpg")

#Imagem com problema de sombra
img2 = cv2.imread("../Videos_e_Imagens/img02.jpg")

#diminuindo a imagem
img = cv2.resize(img,(700,800))
img2 = cv2.resize(img2,(700,800))

#imagem cinza
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgCinza2 = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

#Imagem Binarizada (Importante para transformar imagem em texto)
_,th1 = cv2.threshold(imgCinza,127,255,cv2.THRESH_BINARY)

#Imagem Binarizada Adaptativa
th2 = cv2.adaptiveThreshold(imgCinza2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,16)

#Imagem Binarizada Adaptativa
th3 = cv2.adaptiveThreshold(imgCinza2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,16)

cv2.imshow("Imagem 2 Original",img2)
cv2.imshow("TH1",th1)
cv2.imshow("TH2",th2)
cv2.imshow("TH3",th3)
cv2.imshow("Imagem 1 original",img)
cv2.waitKey(0)