import cv2

img = cv2.imread("../Videos_e_Imagens/Objetos/objetos.jpg")

#Redimensionando a imagem
img = cv2.resize(img,(600,500))

#Aplicando Filtros
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgCanny = cv2.Canny(imgCinza,30,200)

#Aplicando Morfologia   - Melhora precisao
imgClose = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(7,7))

#Separando os contornos dos objetos
contorno,hierarquia = cv2.findContours(imgClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#Cortando cada objeto da imagem
Obj = 1

for i in contorno:
    #Capturando item por item
    cv2.drawContours(img,i,-1,(255,0,0),2)

    #colocando retangulos nos objetos
    x,y,w,h = cv2.boundingRect(i)           #Pegando as coordenadas dos objetos
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)    #Desenhando o retangulo

    #Fazendo os recortes
    objeto = img[y:y+h,x:x+w]
    cv2.imwrite(f"../Videos_e_Imagens/Objetos/{Obj}.jpg",objeto)

    Obj+=1

#Exibindo imagens
cv2.imshow("Imagem Original",img)
cv2.imshow("Imagem Cinza",imgCinza)
cv2.imshow("Imagem Filtro Canny",imgCanny)

cv2.waitKey(0)