import cv2
import pickle

img = cv2.imread('../Contador_Vagas_Estacionamento/dados/estacionamento.png')

vagas = []

for x in range(69):
    #Selecionando a vaga a cada vez que rodar
    vaga = cv2.selectROI('vagas',img,False)

    #Fechando a janela
    cv2.destroyWindow('vagas')

    #Coletando as vagas
    vagas.append((vaga))

    for x,y,w,h in vagas:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

with open('vagas.pkl','wb') as arquivo:
    pickle.dump(vagas,arquivo)
cv2.waitKey(0)
