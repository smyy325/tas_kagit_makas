import os
import time
from random import randint
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

# TensorFlow log seviyesini ayarla (yalnızca hata mesajlarını göster)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Kamera kurulumu
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)
timer = 0
stateResult = False
startGame = False
scores = [0, 0]
player_move = None

# Oyunun ana döngüsü
while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # El tespiti
    hands, img = detector.findHands(imgScaled, draw=True, flipType=True)

    if startGame:
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0

                if hands:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        player_move = 1
                    elif fingers == [1, 1, 1, 1, 1]:
                        player_move = 2
                    elif fingers == [0, 1, 1, 0, 0]:
                        player_move = 3

                    random_number = randint(1, 3)
                    imgAI = cv2.imread(f'Resources/{random_number}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # Kazananı belirleme
                    if (player_move == 1 and random_number == 3) or \
                            (player_move == 2 and random_number == 1) or \
                            (player_move == 3 and random_number == 2):
                        scores[1] += 1
                    elif (player_move == 3 and random_number == 1) or \
                            (player_move == 1 and random_number == 2) or \
                            (player_move == 2 and random_number == 3):
                        scores[0] += 1

    # Talimatları ekrana yazdırma
    cv2.putText(imgBG, "T - Tas, K - Kagit, M - Makas", (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    cv2.putText(imgBG, "Oynamak icin S'ye basin", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    imgBG[234:654, 795:1195] = imgScaled

    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("BG", imgBG)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False

    # Kullanıcı seçimi
    if key == ord('t'):
        player_move = 1
    elif key == ord('k'):
        player_move = 2
    elif key == ord('m'):
        player_move = 3

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
