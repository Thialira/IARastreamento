# Rastreando a quantidade de mãos

import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(1)
rastreador = HandDetector(detectionCon=0.8, maxHands=4)

while True:
    sucesso, imagem = webcam.read()
    coordenadas, imagem_maos = rastreador.findHands(imagem)

    # print(coordenadas)

    cv2.imshow("Projeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()
