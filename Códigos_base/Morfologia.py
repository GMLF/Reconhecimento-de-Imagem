import cv2

#carregando imagem
img = cv2.imread('../Videos_e_Imagens/piramide.jpg')

#Redimensionando imagem
img = cv2.resize(img,(500,400))

#Filtro Escala Cinza
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#Filtro Bluer (borrar imagem)
imgBlur = cv2.GaussianBlur(imgCinza,(7,7),0)

#Filtro Canny (Achar Contornos Imagens)
imgCanny = cv2.Canny(img,50,100)

#Filtro Dilatação - Expande os pontos da imagem
imgDilat = cv2.dilate(imgCanny,(5,5),iterations=5)

#Filtro Erode - Desfragmenta a imagem
imgErode = cv2.erode(imgCanny,(5,5),iterations=2)

#Opening - Erosão seguido da dilatação (retirar ruído, deixar o objeto da imagem)
imgOpenning = cv2.morphologyEx(imgCanny,cv2.MORPH_OPEN,(5,5))

#Closing - Dilatação seguido da erosão (fechar o objeto, tirar os ruídos do objeto)
imgClosing = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(5,5))

#Exibindo as imagens
cv2.imshow("Imagem Piramide",img)
cv2.imshow("Imagem Cinza",imgCinza)
cv2.imshow("Imagem com BLur",imgBlur)
cv2.imshow("Imagem Canny",imgCanny)
cv2.imshow("Imagem Dilatada",imgDilat)
cv2.imshow("Imagem Erode",imgErode)
cv2.imshow("Imagem Aberta",imgOpenning)
cv2.imshow("Imagem Fechada",imgClosing)


#Delay para imagem não fechar
cv2.waitKey(0)