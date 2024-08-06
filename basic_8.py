#Video GrayScale

import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #แปลงให้เป็น gray color
        cv2.imshow("Output",gray)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break 
    else:
        break

print("End")
cap.release()
cv2.destroyAllWindows()