import cv2

#Lendo a imagem
img = cv2.imread('../Videos_e_Imagens/farol.jpg')

#Extraindo as dimensões das imagens em pixel's e canais
print(img.shape)

#Descobrindo os pixel's para recortar imagem
dim = cv2.selectROI('Selecione a area de corte',img,False)

#Fechando a janela após obter as coordenadas
cv2.destroyWindow('Selecione a area de corte')
print(dim)

#Dim é um array e estou organizando para conseguir utilizar a imagem recortada
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

recorte = img[v2:v2+v4,v1:v1+v3]
caminho ='../Videos_e_Imagens/Recortes/'
nome_arquivo = input("Nome que deseja salvar a imagem: ")

#Salvando imagem recortada
cv2.imwrite(f'{caminho}{nome_arquivo}.jpg',recorte)
print("Imagem Salva com Sucesso")

#Travando a tela para não abrir e fechar
cv2.waitKey(0)